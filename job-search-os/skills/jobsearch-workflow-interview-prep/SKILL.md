---
name: jobsearch-workflow-interview-prep
description: Prep for an interview for the Job Search AI Operating System. Invoke when a job seeker says "prep me for an interview", "I have a recruiter screen Tuesday", "hiring manager round tomorrow", "panel loop next week", "final round with the VP", "prep me for [company]", or names an upcoming interview and asks how to prepare. Builds a stage-specific prep brief — likely questions, the person's Story Bank mapped to the interviewers' concerns, answers to the hard questions, questions to ask back — and files it for the company. Never invents stories.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

A recruiter screen, a hiring-manager round, a panel loop, and a final round are four
different interviews. This job preps the one that's actually next, from the person's
own stories.

## How this job delivers its outputs

- **Anything that leaves your hands** — submitted, attached, or edited in Word — is a
  real file: .docx or .pdf, saved in this Project (and in the Drive folder when Drive is
  connected).
- **Anything you come back to** — the Application Board, the Story Bank, the Offer
  Tracker, the Weekly Search Log — **must be published or updated as a live artifact**
  in your Artifacts sidebar on every run (a CSV alone is not enough when artifacts are
  available), with its data stored in the artifact so you can edit rows and stages in
  place. Before creating one, look for an existing artifact with the same name
  (including from earlier conversations) and update it instead of making a duplicate.
  Keep a CSV copy of a tracker's rows in the Project as a backup and keep it in sync.
  Sample-run items go in a separate "Samples" section and never count toward totals.
  If artifacts aren't available in this environment, use the CSV alone and say so once.
- **Emails** are Gmail drafts when Gmail is connected, otherwise paste-ready text (also
  saved as a .txt file). Nothing is ever sent.
- In the close, name the one output to look at first.

## Pre-flight 1 — Profile

Look for the career profile where every skill in this pack looks: the Project file
`./job-search-os-profile.md`, then this Project's instructions, then a profile block
pasted in this chat. Present → use current role, target roles, salary floor,
positioning challenges, shipped artifacts, and voice samples; don't re-ask. Absent →
say setup takes about two minutes; if declined, continue from what they paste and say
so in the close.

## Pre-flight 2 — Connections

Read `./jobsearch-connections.md`. Present → route to connected tools. Absent → say
once: "I'm not connected to your tools yet — say 'connect my tools' anytime. For now
everything comes out paste-ready." Check which connector tools exist; never assume a
tool name.

## Intake

Trackers named "SAMPLE — …" are from the demo. Never read from or write to them except
during a sample run.

**Read first, ask last.** Pull the company, role, posting, stage, date, and interviewer
names from the Application Board, this Project's files, the calendar (if connected,
offer to read the event), or what the person pasted. Then ask only what's still
missing — at most 3 questions in one card of clickable choices — and produce a first
draft. Unknowns go in the brief as `[confirm]`.

1. **Which application** — picked from the Application Board rows at Screening,
   Interviewing, or Onsite; or a new one.
2. **Which round** (clickable): recruiter screen · hiring-manager round · panel or
   loop (several interviewers) · final or executive round · technical or case
   exercise (say what kind).
3. **Who** — names and titles if known; if the person has interviewer names and web
   access, offer a two-line public-profile read per interviewer (role, tenure, what
   they've written or built — nothing personal).
4. **What worries you about this one** — one free-text line.

**Missing profile detail?** If the Story Bank is empty or has fewer than five stories,
build it now from the shipped artifacts (run the story-bank method inline: for each
artifact — situation, what the person did, what changed, which questions it answers)
and save it as the **Story Bank** artifact before writing the brief. Ask for at most
one missing detail per story; the rest is `[confirm]`.

Before tool writes, say once: "As I work, Claude may ask you to approve actions — about
[N] (the prep brief file, the Story Bank, and the Application Board). **Allow for this
task** covers the rest of this run; tracker updates always take a quick confirm."

## Produce

**Prep brief (.docx, 2–4 pages)** for the named round only:

1. **This round in one paragraph** — what it decides, who decides it, and what a
   strong outcome looks like.
2. **Their likely worries** — three to five, inferred from the posting, the round, and
   the positioning challenges (e.g. "will a former manager be happy back in the
   weeds?"). Each with the story that answers it.
3. **Questions to expect** — for the round:
   - *Recruiter screen:* why this role, walk me through your background, compensation
     expectations, timeline, other processes, remote and location.
   - *Hiring manager:* the top three things the posting is worried about, a "tell me
     about a time" for each, how you'd approach their known problem, working style.
   - *Panel or loop:* per-interviewer angle (peer, cross-functional partner, skip-level),
     consistency of your story across rounds, the collaboration and conflict
     questions, a plan for energy across a long day.
   - *Final or executive:* why this company and why now, strategy and judgment, how you
     handle ambiguity and a bad quarter, what you'd do in the first ninety days, how
     you close.
   - *Technical or case:* the format, the two or three areas the posting implies, how
     to think aloud, what to do when stuck.
4. **Your answers** — for each expected question, a tight answer in the person's voice
   (60–120 words), built from a named Story Bank entry: situation, what you did, what
   changed, in that order. The **compensation answer** for the recruiter screen: ask
   for their range first; if pushed, state the floor as a floor, not a target; never
   give salary history.
5. **Getting ahead of the positioning challenge** — one prepared paragraph that
   addresses it before they ask, plus the one-line version.
6. **Questions to ask back** — five, specific to this company and round, none
   answerable from the website.
7. **The 2026 question** — "How do you use AI in your work?" — a concrete, honest
   answer from the person's real practice (what they use it for, what they don't trust
   it with, an example), never a boast.
8. **Day-of card** (half a page): logistics, names, three stories to lead with, the
   one thing to avoid, the close.

## Compliance pass (inline — do not hand off)

- **No invented stories:** every answer names its Story Bank entry or the resume line
  it comes from. A question with no matching story gets "no story yet — pick one of
  these three from your record" rather than a fabricated one.
- **Defensibility:** every claim survives a follow-up question ("what exactly did you
  do?"); soften anything the person didn't personally do.
- **Floor:** the compensation answer protects the floor and gives no history.
- **AI-register tells** removed; answers sound like the voice samples, spoken.
- **Privacy:** nothing confidential about the current employer; competitors' names and
  figures only from public sources.
Append one short **Before you walk in** checklist with only the checks that fired.

## Route outputs

- **Drive connected:** save the brief in `[drive-root-folder]/[Company] — [Role]/` as
  "Prep — [Round] — [date].docx".
- **Calendar connected:** if no prep hold exists, offer one 45-minute "Prep — [Company]"
  block the day before at a time they pick.
- **Gmail connected:** nothing to draft in this job unless the person asks for a
  scheduling reply.
- **Otherwise:** the brief saved to this Project's folder.

## Trackers (living)

List this Project's artifacts first, including ones from earlier conversations. Update
the **Story Bank** with any story refined during prep (columns: Story · Artifact ·
Situation · What I did · What changed · Answers these questions · Used with). Update
the **Application Board** row: stage, interview date, interviewers in Contact, Next
action "thank-you note" with Due = interview date.

## Close

The three stories to lead with in one line each, what was saved and where, the
`[confirm]` list, then "What's next?" — offer the command center, and name **Follow up
& negotiate** for the day after the interview.
