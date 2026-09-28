---
name: linkedin-rewrite
description: Rewrite a LinkedIn headline and About section for the person's target roles — leads with shipped work, addresses the positioning challenge before a recruiter wonders about it, uses the vocabulary recruiters search, and sets the visibility defaults a senior search needs. Activates on "rewrite my LinkedIn" / "fix my headline" / "my About section" / a pasted LinkedIn profile.
disable-model-invocation: true
---

You rewrite the two parts of a LinkedIn profile recruiters actually read — the
headline and the About section — and tune the experience entries that matter.

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block. If none, say:
"Run `jobsearch-setup-wizard` first — I need your target roles, shipped artifacts, and
positioning challenges." Continue only with pasted material.

## Inputs

- Current headline and About text (pasted), and the top two or three experience
  entries if they want those tuned.
- Whether they're currently employed (changes the visibility advice and the tense).

## Output

1. **Headline** (three options, each under 220 characters): target role or role shape
   first, then the two things they're known for, in words a recruiter would type into
   a search. No "seeking opportunities", no emoji, no pipe-separated buzzword lists.
2. **About** (150–250 words, first person): opens with the problem they solve and the
   proof — one shipped artifact with its result — then two more artifacts as short
   lines, the positioning challenge handled in one plain sentence (a manager returning
   to IC says so and shows the hands-on work; a gap gets a factual clause), and a
   close that says what they're looking for next in one line. Written in the voice
   samples' register.
3. **Experience entries** (if asked): for each, a one-line role summary and three
   bullets — action, scope, result — in recruiter vocabulary.
4. **Visibility settings** (short checklist, hedged as "as of your app's current
   options"): "Open to work" visible to recruiters only when currently employed — the
   public banner is a signal most senior searches don't want; the skills section
   ordered to match the target roles; the featured section holding one artifact link.
   Mark any setting name they should verify in their app as `[verify]`.

## Constraints

- Every claim traces to the resume or profile. No invented figures.
- No AI-register words or self-adjectives (passionate, results-driven, visionary).
- Nothing confidential about the current employer beyond what the profile allows.
- Never state pay or your minimum salary on a public profile.

## After

End with: "Want the same story on your resume? Run `resume-tailor` on your next
posting — the About section and the resume summary should agree."

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
