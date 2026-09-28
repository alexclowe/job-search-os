---
name: jobsearch-workflow-inbox
description: Work my inbox for the Job Search AI Operating System. Invoke when a job seeker says "work my inbox", "check my inbox for recruiters", "reply to this recruiter", "they want to schedule a call", "I got a rejection", "here's what came in this week", or pastes recruiter messages, scheduling requests, or rejections and asks what to do. Sorts what came in, drafts replies in the person's voice with the salary floor protected, puts interviews on the calendar, and moves each application to its new stage on the Application Board. Can run on a schedule.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

The inbox is where searches quietly stall: an unanswered recruiter, a scheduling thread
lost under newsletters, a rejection nobody learned from. This job clears it in one pass
and keeps the board honest.

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
pasted in this chat. Present → use target roles, salary floor, remote and location
preference, search stage, and voice samples; don't re-ask. Absent → say setup takes
about two minutes; if declined, continue with neutral defaults and no floor check, and
say so in the close.

## Pre-flight 2 — Connections

Read `./jobsearch-connections.md`. Present → route to connected tools. Absent → say
once: "I'm not connected to your tools yet — say 'connect my tools' anytime. For now
everything comes out paste-ready." Check which connector tools exist; never assume a
tool name. Never read or write an employer's mailbox.

## Intake

Trackers named "SAMPLE — …" are from the demo. Never read from or write to them except
during a sample run.

**Read first, ask last.** If the person pasted messages, pull every answer from them
first. Then ask only what's still missing — at most 3 questions in one card of
clickable choices — and produce a first draft. Unknowns go in the draft as `[confirm]`.

1. **The messages** — pasted, or (Gmail connected) "check my inbox": search the last
   [window] for messages from recruiters, hiring teams, scheduling tools, and anyone on
   the Application Board's Contact column. List what was found by sender, subject, and
   date, grouped as **recruiter outreach · scheduling · next-round news · rejection ·
   offer · other**, and confirm the list before using it. Skip newsletters and job
   alerts unless asked.
2. **Window** (clickable): since my last inbox run · last 7 days · last 14 days.
3. **For inbound recruiter outreach** — reply, decline politely, or ignore (clickable,
   per message). Any role the person hasn't seen: run the floor check on whatever
   range the message gives.
4. **For scheduling requests** — if Calendar is connected, offer to read the days they
   proposed and list open slots; the person picks. Never propose a time you haven't
   checked.

Before tool writes, say once: "As I work, Claude may ask you to approve actions — about
[N] (one draft per reply, any interview holds, and the Application Board). **Allow for
this task** covers the rest of this run; tracker updates always take a quick confirm."

## Produce

One reply per message the person chose, 40–150 words, in their voice, no "Thank you
for reaching out!" opener:
- **Recruiter outreach, interested:** two lines on fit that lead with a shipped
  artifact, then the three qualifying questions before a call — the compensation range
  for the level, remote terms, and where the role sits (team, manager, why it's open).
  State the floor only if the person's profile says "share my floor up front";
  otherwise ask for their range first.
- **Recruiter outreach, declining:** specific, kind, door open — name the one thing
  that would change the answer (level, comp, location).
- **Scheduling:** confirm the slot the person picked, the format, and who they'll meet;
  ask for the interviewer names if missing.
- **Next-round news:** confirm, ask what the round covers and who's on it, and note
  "Prep for an interview" as the next job.
- **Rejection:** a two-line gracious reply that asks one specific question about what
  would have made the difference — only if the rejection came from a human. Automated
  rejections get no reply; they get a note on the board.
- **Offer:** acknowledge, thank, ask for the full written terms and the decision date,
  commit to nothing. Then route to **Follow up & negotiate**.

**Rejection read** (in chat, per human rejection): one line on the most likely cause
from the record — stage it died at, whether the keyword match was thin, whether the
positioning challenge showed — and one thing to change. No spirals, no guessing beyond
the evidence.

## Compliance pass (inline — do not hand off)

- **Floor:** every new role is compared to the floor before a reply is drafted; below
  the floor gets the plain flag, not a softened one.
- **No commitments:** no reply accepts, declines, or promises a start date, references,
  or a number the person hasn't decided.
- **Traceability:** claims in replies come from the profile and resume only.
- **AI-register tells** removed; the voice matches the samples.
- **Privacy:** no salary history, no current-employer confidential detail, no reason
  for leaving beyond the profile's one approved line.
- **Employer systems:** never draft into, read from, or forward through a current
  employer's mail.
Append one short **Before you send** checklist with only the checks that apply.

## Route outputs

- **Gmail connected:** each reply as a draft in the original thread when the connector
  supports replying to a thread, otherwise a new draft with the same subject; To: the
  original sender. **Never send.**
- **Calendar connected:** one event per confirmed interview — title "Interview —
  [Company] · [Round]", the format and names in the description, plus a 30-minute
  "Prep — [Company]" hold the day before if the person wants it. Only for times they
  confirmed.
- **Otherwise:** replies paste-ready, separated by message, saved as one .txt in this
  Project.

## Application Board (living tracker)

List this Project's artifacts first, including ones from earlier conversations. Update
the **"Application Board"** if it exists; create it only if absent (columns as in Tailor
& apply). For each message: move the stage, set Last touch to today, set Next action
and Due, add the contact. New inbound roles get a row at Interested with the floor
check filled in. Rejections move to Closed with the read in Notes. Offers get a row on
the **Offer Tracker** too (created if absent: Company · Role · Base · Bonus · Equity ·
Other · Total · Floor check · Deadline · Status (Received → Countered → Accepted /
Declined) · Counter · Next).

## Make it automatic

Offer once: "Want this every [Tuesday and Friday]? Say **'schedule this'** and pick the
time." A scheduled run works from messages saved in this Project, prepares replies as
files here, and updates the board — it **does not** read your inbox, draft into Gmail,
or touch your calendar on its own. You review, then say 'move these to Gmail'.

## Close

What came in by group, what was drafted and where, stage moves on the board, the
`[confirm]` list, then "What's next?" — offer the command center, and name **Prep for
an interview** if any interview was confirmed.
