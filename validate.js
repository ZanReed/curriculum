/* =============================================================================
 * validate.js — thread validation, shared between builder.html and CI
 * -----------------------------------------------------------------------------
 * One implementation of the thread checks. The builder loads this via
 * <script src="validate.js"> and formats the plain-text messages as HTML;
 * CI runs `node validate.js thread-01-rate-of-change.json` and fails the
 * build on any error-level finding.
 *
 * validateThread(data) -> [{ level: 'error'|'warn'|'note', message: string }]
 * Messages are plain text; ids are wrapped in `backticks` for the builder
 * to render as <code>. This function never mutates `data`.
 * ============================================================================= */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.validateThread = factory();
})(typeof self !== 'undefined' ? self : this, function () {

  function validateThread(D) {
    var out = [];
    function push(level, message) { out.push({ level: level, message: message }); }

    var skills = D.skills || [];
    var activities = D.activities || [];
    var chains = (D.chunking_plan && D.chunking_plan.chains) || [];

    /* ---- lookups (all derived, none mutating) ---- */
    var s = {}; skills.forEach(function (x) { s[x.id] = x; });
    var known = {}; skills.forEach(function (x) { known[x.id] = 1; });
    (D.external_prereqs || []).forEach(function (e) { known[e.id] = 1; });
    var mis = {}; (D.misconceptions || []).forEach(function (m) { mis[m.id] = 1; });
    var caps = {}; (D.capabilities || []).forEach(function (c) { caps[c.id] = c; });
    var chainList = chains.map(function (c) { return c.chain_id; });
    var cids = {}; chainList.forEach(function (c) { cids[c] = 1; });

    var P = {}; // in-graph prerequisites per skill
    skills.forEach(function (x) {
      P[x.id] = (x.prereqs || []).filter(function (p) { return !!s[p]; });
    });

    function depths() {
      var d = {}, stack = {};
      function go(n) {
        if (d[n] !== undefined) return d[n];
        if (stack[n]) return 0;
        stack[n] = 1;
        var m = 0;
        (P[n] || []).forEach(function (p) { m = Math.max(m, go(p) + 1); });
        stack[n] = 0; d[n] = m; return m;
      }
      skills.forEach(function (x) { go(x.id); });
      return d;
    }
    function ancOf(n) {
      var seen = {};
      (function go(x) {
        (P[x] || []).forEach(function (p) { if (!seen[p]) { seen[p] = 1; go(p); } });
      })(n);
      return seen;
    }
    function stat(a) { return a.status === 'approved' ? 'approved' : 'draft'; }
    // Non-mutating view of an activity's components (handles the legacy
    // phases/review_slice shape the builder's migrate() rewrites in place).
    function componentsOf(a) {
      if (a.components) return a.components;
      var ph = a.phases || {}, rs = a.review_slice || {};
      return {
        review: { mode: rs.mode || 'prereq_targeted', target_skills: rs.target_skills || [], items: rs.items || 3, note: rs.note || '' },
        lesson: { worked: ph.worked_example || {}, faded: ph.faded_example || {}, independent: ph.independent || {} },
        dol: { locale: 'us-teks', items: (ph.exit_check || {}).items || [] }
      };
    }
    // What an activity's DoL actually yields, from the capabilities it declares.
    function dolSignal(a) {
      var items = ((componentsOf(a).dol) || {}).items || [];
      var hasAuto = false, hasRubric = false, hasDistractor = false;
      items.forEach(function (it) {
        if (it.distractor_map && Object.keys(it.distractor_map).length) hasDistractor = true;
      });
      (a.uses_capabilities || []).forEach(function (c) {
        var g = (caps[c] || {}).grading || {};
        if (g.scoring === 'auto') hasAuto = true;
        if (g.scoring === 'rubric') hasRubric = true;
      });
      return {
        hasAuto: hasAuto, hasRubric: hasRubric, hasDistractor: hasDistractor,
        distractorOnRubric: hasDistractor && !hasAuto
      };
    }

    /* ---- skill checks ---- */
    var seen = {};
    skills.forEach(function (x) {
      if (seen[x.id]) push('error', 'Two skills share the id `' + x.id + '`.');
      seen[x.id] = 1;
      if (!x.label || !x.label.trim()) push('error', '`' + x.id + '` has no label.');
      (x.prereqs || []).forEach(function (p) {
        if (!known[p]) push('error', '`' + x.id + '` lists a prerequisite that does not exist: `' + p + '`.');
      });
      (x.misconceptions || []).forEach(function (m) {
        if (!mis[m]) push('error', '`' + x.id + '` references an unknown misconception `' + m + '`.');
      });
    });

    /* ---- cycles ---- */
    var color = {};
    function dfs(n, path) {
      color[n] = 'g';
      (P[n] || []).forEach(function (m) {
        if (color[m] === 'g') push('error', 'Circular dependency: `' + path.concat([n, m]).join(' → ') + '`. A skill cannot require itself, however indirectly.');
        else if (!color[m]) dfs(m, path.concat([n]));
      });
      color[n] = 'b';
    }
    skills.forEach(function (x) { if (!color[x.id]) dfs(x.id, []); });

    /* ---- chain membership ---- */
    var planned = {};
    chains.forEach(function (c) { (c.skills || []).forEach(function (k) { planned[k] = 1; }); });
    skills.forEach(function (x) {
      if (!planned[x.id]) push('warn', '`' + x.id + '` is in no chain, so nothing will ever be authored for it.');
    });
    chains.forEach(function (c) {
      (c.skills || []).forEach(function (k) {
        if (!s[k]) push('error', 'Chain `' + c.chain_id + '` lists a skill that does not exist: `' + k + '`.');
      });
    });

    /* ---- activity references ---- */
    activities.forEach(function (a) {
      if (!s[a.primary_skill]) push('error', 'Activity `' + a.id + '` targets a skill that does not exist: `' + a.primary_skill + '`.');
      if (!cids[a.chain_id]) push('error', 'Activity `' + a.id + '` is in an unknown chain `' + a.chain_id + '`.');
      (((componentsOf(a)).review || {}).target_skills || []).forEach(function (t) {
        if (!s[t]) push('error', 'Activity `' + a.id + '` reviews a skill that does not exist: `' + t + '`.');
      });
    });

    /* ---- chain-level contracts ---- */
    chains.forEach(function (c) {
      var have = (c.hooks || []).length;
      var authoredN = activities.filter(function (a) { return a.chain_id === c.chain_id && a.status === 'approved'; }).length;
      if (authoredN > 0 && have < Math.ceil(authoredN / 2))
        push('warn', 'Chain `' + c.chain_id + '` has ' + authoredN + ' approved activit' + (authoredN === 1 ? 'y' : 'ies') + ' but only ' + have + ' hook' + (have === 1 ? '' : 's') + '. The contract is at least 1 hook per 2 activities — a teacher mid-chain will have nothing to open a day with.');
    });
    chains.forEach(function (c) {
      var acts = activities.filter(function (a) { return a.chain_id === c.chain_id; });
      if (acts.length >= 2 && acts.every(function (a) { var g = dolSignal(a); return g.hasRubric && !g.hasAuto; }))
        push('note', 'Every DoL in chain `' + c.chain_id + '` is teacher-graded. Pedagogically fine for a justification locale, but it yields no automatic misconception data and concentrates hand-marking. Consider at least one auto-scored check in the chain.');
    });
    var cc = {};
    activities.forEach(function (a) {
      var q = cc[a.chain_id] = cc[a.chain_id] || { draft: 0, approved: 0 };
      q[stat(a)]++;
    });
    chains.forEach(function (c) {
      var q = cc[c.chain_id] || { draft: 0, approved: 0 };
      var n = q.draft + q.approved;
      if (n > c.activities) push('warn', 'Chain `' + c.chain_id + '` has ' + n + ' activities but projected ' + c.activities + '. Revise the projection.');
    });

    /* ---- per-activity checks ---- */
    activities.filter(function (a) { return stat(a) === 'draft'; }).forEach(function (a) {
      push('note', 'Activity `' + a.id + '` is still a draft. It does not count until you approve it.');
    });
    var dep = depths();
    activities.forEach(function (a) {
      var C = componentsOf(a);
      if (!(C.lesson && C.lesson.faded && C.lesson.faded.prompt))
        push('error', 'Activity `' + a.id + '` has no faded example. It jumps from demonstration to independent practice.');
      if (!(C.dol && (C.dol.items || []).length))
        push('warn', 'Activity `' + a.id + '` has no DoL items — nothing checks whether it landed.');
      if (C.dol && !C.dol.locale)
        push('warn', 'Activity `' + a.id + '` has no assessment locale on its DoL.');
      var sig = dolSignal(a);
      if (sig.distractorOnRubric)
        push('warn', 'Activity `' + a.id + '` has a distractor map but no auto-scored capability to render it. On a teacher-graded item the misconception mapping produces no aggregate signal until a human grades — put diagnostic items on mc, graph, or fill-in-the-blank.');
      (a.uses_capabilities || []).forEach(function (c) {
        if (!caps[c]) push('error', 'Activity `' + a.id + '` uses an unknown capability `' + c + '`.');
        else if (caps[c].status === 'proposed' && stat(a) === 'approved') push('error', 'Activity `' + a.id + '` is approved but needs `' + c + '`, which is not built. Approval requires it work on shipped capabilities today.');
        else if (caps[c].status === 'proposed') push('note', 'Activity `' + a.id + '` wishes for `' + c + '` — capped at draft until it ships.');
      });
      var A = ancOf(a.primary_skill), ts = ((C.review || {}).target_skills) || [];
      if (C.review && C.review.mode === 'prereq_targeted' && ts.length) {
        var far = 0;
        ts.forEach(function (t) { if (A[t]) far = Math.max(far, dep[a.primary_skill] - dep[t]); });
        if (far < 2) push('note', 'Activity `' + a.id + '` only reviews skills one row back. Reach further — that is what the graph is for.');
        var chd = chains.filter(function (c) { return c.chain_id === a.chain_id; })[0];
        var chainAnc = {};
        if (chd) (chd.skills || []).forEach(function (cs) {
          var CA = ancOf(cs);
          Object.keys(CA).forEach(function (k) { chainAnc[k] = cs; });
        });
        ts.forEach(function (t) {
          if (A[t] || !s[t]) return;
          if (chainAnc[t]) push('note', 'Activity `' + a.id + '` reviews `' + t + '` as planting — it is upstream of `' + chainAnc[t] + '` later in this chain. Legal under the planting rule.');
          else push('warn', 'Activity `' + a.id + '` reviews `' + t + '`, which is upstream of neither its target nor anything in its chain. Students may not have met it.');
        });
      }
    });

    return out;
  }

  return validateThread;
});

/* ---- headless CLI: node validate.js <thread.json> ---- */
if (typeof require !== 'undefined' && typeof module !== 'undefined' && require.main === module) {
  var fs = require('fs');
  var file = process.argv[2];
  if (!file) {
    console.error('usage: node validate.js <thread.json>');
    process.exit(2);
  }
  var data;
  try {
    data = JSON.parse(fs.readFileSync(file, 'utf8'));
  } catch (e) {
    console.error('could not read ' + file + ': ' + e.message);
    process.exit(2);
  }
  var findings = module.exports(data);
  var order = { error: 0, warn: 1, note: 2 };
  findings.sort(function (a, b) { return order[a.level] - order[b.level]; });
  findings.forEach(function (f) {
    console.log((f.level === 'error' ? 'ERROR' : f.level === 'warn' ? 'WARN ' : 'note ') + ' ' + f.message);
  });
  var errors = findings.filter(function (f) { return f.level === 'error'; }).length;
  var warns = findings.filter(function (f) { return f.level === 'warn'; }).length;
  console.log(findings.length
    ? errors + ' error(s), ' + warns + ' warning(s), ' + (findings.length - errors - warns) + ' note(s).'
    : 'Nothing wrong. The graph is acyclic, every reference resolves, and every skill sits in a chain.');
  process.exit(errors ? 1 : 0);
}
