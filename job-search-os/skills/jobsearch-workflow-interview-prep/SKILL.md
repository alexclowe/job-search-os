---
name: jobsearch-workflow-interview-prep
description: Prep for an interview for the Job Search AI Operating System. Invoke when a job seeker says "prep me for an interview", "I have a recruiter screen Tuesday", "hiring manager round tomorrow", "panel loop next week", "final round with the VP", "prep me for [company]", or names an upcoming interview and asks how to prepare. Starts with a sourced company brief, then builds a stage-specific prep brief — likely questions, the person's Story Bank mapped to the interviewers' concerns, answers to the hard questions, questions to ask back — files it for the company, and offers a practice round, one question at a time. Never invents stories.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.
> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

A recruiter screen, a hiring-manager round, a panel loop, and a final round are four
different interviews. This job preps the one that's actually next — company brief
first, then the person's own stories — and then lets them practice it out loud.

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
pasted in this chat. Present → use current role, target roles, minimum pay,
what a hiring manager might question, wins, and voice samples; don't re-ask. Absent →
say setup takes about two minutes; if declined, continue from what they paste and say
so in the close.

Older profiles use other labels for the same fields: `Minimum salary:` or `Salary floor:`
mean minimum pay (annual salary unless the value says otherwise), **Shipped artifacts**
means wins, `Positioning challenges:` means things a hiring manager might question,
and `Target level:` means career stage. Read them the same way.

**Profession archetype (read, don't ask).** If the profile or the posting names a
profession, read the matching archetype — `./archetypes/<profession>.md` in this
Project first, then the `archetypes/` folder that ships with the Tailor & apply job
(`jobsearch-workflow-tailor-apply/archetypes/`). Find the file through `archetypes/index.md` first (it ships in the same folder): match the profession against its Name and Also called columns and open only that one file. If more than one row fits ("nurse" could be a registered nurse, an LPN, a nurse practitioner, or a nursing assistant), ask one short question with those rows as options before opening anything. Use its **How interviews usually run**
section to shape the brief for this round (for example a nursing panel with
scenario and behavioral questions, a teaching demo lesson, a bookkeeping skills test,
a loan officer's pipeline and compliance questions) and its **Story types that land**
to pick which stories to lead with. It never supplies a story, a claim, or a number the
person's own record doesn't support; if no archetype matches, say nothing about it.

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
build it now from your wins (run the story-bank method inline: for each
artifact — situation, what the person did, what changed, which questions it answers)
and save it as the **Story Bank** artifact before writing the brief. Ask for at most
one missing detail per story; the rest is `[confirm]`.

Before tool writes, say once: "As I work, Claude may ask you to approve actions — about
[N] (the company brief, the prep brief file, the Story Bank, and the Application
Board). **Allow for this task** covers the rest of this run; tracker updates always
take a quick confirm."

## Company brief first (before any questions or answers)

Look in this Project for **"Company brief — [Company].md"**. Under 30 days old → use it
and add a short section for this round. Older or missing → build it now with the
company-brief method (`jobsearch-company-brief`), inline:
- **Sources or nothing.** With web search: the company's own pages (about, careers, the
  posting, news or press, annual report if public; for hospitals and districts, board
  minutes, strategic plans, published salary schedules) and recent reputable news.
  Every fact gets a source and a date. Without web search in this conversation, say so
  in one line and ask the person to paste the posting or the about page — never fill
  the gap from memory. Review sites are opinion, quoted as "people on [site] say".
- **One page:** what they do (two lines) · recent news, three items at most, dated ·
  the team and why this role is likely open · what they say they value (quoted, with
  the link) · two or three of the person's wins that line up · five questions the
  website doesn't answer · sources.
- Save as "Company brief — [Company].md" in this Project (and in the company's Drive
  folder when connected).

**For a recruiter screen, the brief comes before the screen questions** and feeds both
sides: the "why this role / why us" answer is built from what they value and the wins
that line up, and the questions to ask back start from the brief's open questions.
Later rounds reuse the same brief and add to it.

## Produce

**Prep brief (.docx, 2–4 pages)** for the named round only:

1. **This round in one paragraph** — what it decides, who decides it, and what a
   strong outcome looks like.
2. **Their likely worries** — three to five, inferred from the posting, the round, and
   what a hiring manager might question (e.g. "will a former manager be happy back in the
   weeds?"). Each with the story that answers it.
3. **Questions to expect** — for the round:
   - *Recruiter screen:* the five or six that always come up — walk me through your
     background, why this role and why us (from the company brief), why you're looking
     (the approved line only), what you want next, pay expectations, timeline and
     other processes, remote and location.
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
   for their range first; if pushed, state your minimum pay as the lowest you'd take, not a target; never
   give salary history.
5. **Getting ahead of what a hiring manager might question** — one prepared paragraph that
   addresses it before they ask, plus the one-line version.
6. **Questions to ask back** — five, specific to this company and round, none
   answerable from the website, starting from the company brief's open questions.
7. **The 2026 question** — "How do you use AI in your work?" — a concrete, honest
   answer from the person's real practice (what they use it for, what they don't trust
   it with, an example), never a boast.
8. **Day-of card** (half a page): logistics, names, three stories to lead with, the
   one thing to avoid, the close.

## Compliance pass (inline — do not hand off)

- **No invented stories:** every answer names its Story Bank entry or the resume line
  it comes from. A question with no matching story gets "no story yet — pick one of
  these three from your record" rather than a fabricated one.
- **Every claim holds up:** every claim survives a follow-up question ("what exactly did you
  do?"); soften anything the person didn't personally do.
- **Nothing undersold:** the same record, the other direction — a stronger honest win
  that answers one of their worries isn't left out of the answers.
- **Company facts are sourced:** every fact about the employer comes from the company
  brief's sources; nothing about them is guessed.
- **Minimum pay:** the compensation answer holds to your minimum pay and gives no history.
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
the **Story Bank** with any story refined during prep (columns: Story · Win ·
Situation · What I did · What changed · Answers these questions · Used with). Update
the **Application Board** row (columns as in Tailor & apply): stage; the round's date
in **Screen on** (recruiter screen), **Interview on** (add the date — one per round,
separated by semicolons), or **Final on** (final or executive round); interviewers in
Contact; Next action "thank-you note" with Due = interview date. An older board
without these columns gets them added, blank where unknown.

## Practice it with me (offer once, after the brief)

Offer as clickable options: **Practice this round now** · **Later**. On "now", run a
mock interview inline (the `jobsearch-mock-interview` method):
- The format for this round and profession — behavioral for everyone; clinical
  scenario and prioritization practice for nurses; a demo-lesson plan and panel
  questions for teachers; a sell-me-this role-play for sales and lending (common, not
  guaranteed); technical plus behavioral for tech; the five or six screen questions
  plus the pay answer for a recruiter screen.
- **One question at a time**, then wait. After each answer, five lines at most: what
  worked · structure (situation, what you did, what changed) · does it hold up ·
  anything undersold from their own record · length and register. Offer "try that
  one again" or "next question".
- Clinical scenarios are practice only — feedback on structure and communication, not
  clinical correctness; say once to check clinical content against their training and
  facility policy.
- **Debrief:** per-question read (strong · solid · needs a story · needs a shorter
  version), three fixes with the exact line to practice, and any new story the person
  told — offered for the Story Bank, only what they actually said. Saved as "Practice —
  [Company] — [round] — [date].md".

## Close

Never narrate your own tooling in the close: nothing about files you could not open, workbooks you could not recalculate, pages you did not open, or what the sandbox lacks. State what was produced, what needs confirming, and where it landed.

The three stories to lead with in one line each, the company brief's most useful
finding, what was saved and where, the `[confirm]` list, then "What's next?" — offer the command center, and name **Follow up
& negotiate** for the day after the interview.
