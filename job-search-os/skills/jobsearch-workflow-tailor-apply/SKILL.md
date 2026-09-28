---
name: jobsearch-workflow-tailor-apply
description: Tailor and apply for the Job Search AI Operating System. Invoke when a job seeker says "tailor and apply", "tailor my resume to this posting", "apply to this job", "here's a posting", "write my cover letter for this role", or pastes a job description and asks for a resume or application. Runs a salary check on the posting first, decodes the real requirements, produces a tailored resume and cover letter that lead with real results and trace every claim to the person's own record, and files the application on the Application Board.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

One posting, start to finish: is it worth your hour, what they actually want, a resume
and letter built from what you did and what came of it, and a row on the board so it doesn't vanish.

## How this job delivers its outputs

- **Anything that leaves your hands** — submitted, attached, or edited in Word (resume,
  cover letter, a one-page addendum) — is a real file: .docx or .pdf, saved in this
  Project (and in the Drive folder when Drive is connected).
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
  saved as a .txt file). Nothing is ever sent or submitted.
- In the close, name the one output to look at first.

## Pre-flight 1 — Profile

Look for the career profile where every skill in this pack looks: the Project file
`./job-search-os-profile.md`, then this Project's instructions, then a profile block
pasted in this chat. Accept any block with the profile fields, whatever its heading says.
- **Present:** use current role, years, target roles, career stage, pay type and
  minimum pay, things a hiring manager might question, wins, location and remote
  preference, and voice samples. Don't re-ask. (Older profiles say `Minimum salary:` or
  `Salary floor:` for minimum pay, **Shipped artifacts** for wins, and `Positioning
  challenges:` for things a hiring manager might question — read them the same way.)
- **Absent:** say the profile isn't set up and that "run the setup wizard" takes about
  two minutes. If they decline, continue with what they paste, mark the salary check
  "no minimum pay on file", and say so in the close.

## Pre-flight 2 — Connections

Read `./jobsearch-connections.md`.
- **Present:** note which of gmail / calendar / drive are connected and the
  `drive-root-folder`.
- **Absent:** say once: "I'm not connected to your tools yet — say 'connect my tools'
  anytime. For now everything comes out paste-ready." Continue.

Check which connector tools actually exist in this session; never assume a tool name.

## Intake

Trackers named "SAMPLE — …" are from the demo. Never read from or write to them except
during a sample run.

**Read first, ask last.** If the person pasted or pointed to anything (the posting, a
link, their resume, a referral's message), pull every answer you can from it first.
Then ask only what's still missing — at most 3 questions in one card of clickable
choices — and produce a first draft. Anything still unknown goes in the draft as
`[confirm]`, not another question.

**Missing profile detail?** If this job needs something the profile doesn't have
(minimum pay, remote preference, the current resume), ask for it once here, use it,
then save it into the matching section of the profile with one line: "Saved to your
profile so I won't ask again — say 'undo' to remove it." Never block the job on it.

1. **The posting** — pasted text, a link (fetch it if you have web access; otherwise
   ask for the text), or a message from a recruiter or referrer. Note company, title,
   location and remote terms, the schedule (shift, hours, days), and the pay exactly
   as posted — an hourly range, an annual range, base plus commission, or a
   salary-schedule placement.
2. **The resume** — the current resume in this Project, a file they point to, or
   pasted text. If none exists anywhere, ask for it; never write a resume from the
   profile alone.
3. **How they're applying** (clickable): company site or ATS · through a recruiter ·
   through a referral (name) · by email to a hiring manager.
4. **Anything to get ahead of for this one** — a gap, a title mismatch, a location
   question — beyond what a hiring manager might question already on file.

**Profession archetype (read, don't ask).** If the profile or the posting names a
profession, look for a matching archetype file — first `./archetypes/<profession>.md`
in this Project, then the `archetypes/` folder that ships next to this skill (for
example `archetypes/nurse.md`, `archetypes/teacher.md`, `archetypes/bookkeeper.md`).
An archetype is a short, hedged brief: the titles that hiring teams use for the role,
where the postings tend to live, what a recruiter screens for first, the story types
that land, the red flags in postings, how pay is usually structured, and what's
usually negotiable. Use it to sharpen the posting decode and the
resume's ordering; it never supplies a claim, a number, or a keyword the person's own
record doesn't support. If no archetype matches, continue without one and say nothing
about it. Anyone can add one — see `archetypes/_template.md`.

## Salary check — before any materials (non-negotiable)

Compare the posting against the minimum pay on file, **like with like** (the salary
guard's rules):
- **Hourly:** the top of the posted hourly range against the hourly minimum.
  Differentials, overtime, and sign-on bonuses are noted separately, never added to
  the base. If one side is annual and the other hourly, convert with a stated hours
  assumption ("at 36 hours a week [confirm hours/week]").
- **Annual salary:** the top of the posted range against the annual minimum.
- **Commission or commission plus base:** the base (or draw) against any base minimum,
  and the realistic expected total the posting or recruiter states against the
  expected-total minimum. "Up to" and "top producers earn" figures don't count.
- **Salary schedule:** the step and lane the posting or district would likely place
  you at, and that step's figure on the published schedule, against the minimum.
No pay posted → look in the recruiter's message; if none, mark "pay unknown — ask on
the first call" and continue.
- **At or below your minimum pay:** stop and say it plainly, before drafting anything:
  "This role posts at [pay as posted], and your minimum is [minimum pay]. Flagging it
  now, not after three rounds. Want to (a) skip it, (b) apply anyway and raise pay on
  the first call, or (c) apply and mark it as a fallback?" Continue only on (b) or (c),
  and record the choice on the board.
- **Above your minimum pay or unknown:** one line, then move on. For hourly and
  commission roles, add the one pay question worth asking on the first call (for
  example guaranteed hours and the differential schedule, or the split, draw, and ramp).

Before any tool writes, say once: "As I work, Claude may ask you to approve actions —
this run involves about [N] (the resume file, the cover letter, one folder, and the
Application Board). Choosing **Allow for this task** covers the rest of this run, and
tracker updates always take a quick confirm."

## Produce

1. **Posting decoded** (in chat, short) — must-haves vs. nice-to-haves in their own
   words; the three things the hiring manager is most likely worried about; keywords an
   applicant-tracking system will match on; anything ambiguous to ask about; red flags
   (a "wishlist of six jobs", a range far below market for the title, "fast-paced" as a
   euphemism) named once, without drama.
2. **Tailored resume (.docx)** — the person's real resume, reordered and rewritten for
   this posting:
   - Summary (3 lines max) that names the target role and leads with the two wins most relevant to their worries — **what was done and its result before
     any title**.
   - Each bullet: action, scope, result, in the posting's vocabulary where the person's
     record honestly supports it. Quantify only with figures the person supplied; a
     bullet with no figure says what changed, not a made-up percentage.
   - Whatever a hiring manager might question is handled in the text, not in a
     disclaimer: a manager returning to hands-on work leads with the hands-on work from
     the management years; a career changer leads with the results that carry over, in
     the new field's words; someone returning to work gets a one-line, factual entry
     for the gap; a license from another state names its status plainly.
   - Same page count as the original unless they asked to cut. Plain formatting an
     ATS can parse: no tables, no columns, no graphics.
   - A **change log** at the end of the chat message: what moved, what was reworded,
     what was cut, and any claim the person should double-check.
3. **Cover letter (.docx, 250–350 words)** in the person's voice: a specific opening
   about this company or problem (never "I am excited to apply"), two short paragraphs
   pairing their two strongest wins with the posting's top worries, one line that
   gets ahead of what a hiring manager might question, a plain close. No adjectives about
   themselves ("results-driven", "passionate"), no mention of pay.
4. **Application note** (only for referral or email applications) — 60–120 words to
   the referrer or hiring manager, in their voice, attaching or naming the two files.

## Compliance pass (inline — do not hand off)

Screen every file in this turn:
- **Traceability:** every metric, title, date, employer, and accomplishment traces to
  the resume or profile the person supplied. Anything else is cut or replaced with
  `[confirm]`. Never round a number up.
- **Every claim holds up:** for each claim, could the person back it with a specific example
  in an interview? Flag any that reads stronger than the record ("led" where they
  "contributed to"; "owned" where they "worked on").
- **AI-register tells:** remove "leverage", "synergy", "results-driven", "passionate",
  "spearheaded", "dynamic", stacked adjectives, and any sentence that could open any
  cover letter. Read the letter aloud in your head; if it doesn't sound like the voice
  samples, rewrite it.
- **Privacy:** no home street address, no date of birth, no photo, no current-employer
  confidential figures (name the scale in relative terms if the profile marks it
  confidential), no salary history.
- **Minimum pay:** the salary-check result is recorded on the board; the letter never names
  a number.
Append one short **Before you submit** checklist with only the checks that fired.

## Route outputs

- **Drive connected:** create `[drive-root-folder]/[Company] — [Role]/` and save the
  resume as "[First Last] — Resume — [Company].docx" and the letter as "[First Last]
  — Cover letter — [Company].docx". Never overwrite the master resume.
- **Gmail connected:** the application note as a draft, To: filled only if the address
  is known. **Never send.** Never draft into an employer's inbox for them.
- **Calendar connected:** one reminder titled "Follow up — [Company]" only if the
  person gives a follow-up date; never invent one.
- **Otherwise:** both files saved to this Project's folder, the note paste-ready.

## Application Board (living tracker)

List this Project's artifacts first, including ones from earlier conversations. If an
**"Application Board"** artifact exists, add this application; create it only if
absent. Columns: Company · Role · Stage (Interested → Applied → Screening →
Interviewing → Onsite → Offer → Closed) · Posted range · Salary check (above / below,
applying anyway / unknown) · Source · Applied on · Last touch · Next action · Due ·
Contact · Notes. Board views: by stage, plus a "Due this week" list at the top. Sample
rows sit under "Samples" and never count.

## Close

Never narrate your own tooling in the close: nothing about files you could not open, workbooks you could not recalculate, pages you did not open, or what the sandbox lacks. State what was produced, what needs confirming, and where it landed.

List what was made and where (resume / letter / note / folder / board row), the
`[confirm]` list, the salary check verdict in one line, then "What's next?" — offer the
command center. If a Story Bank exists and a strong story surfaced during tailoring
that isn't on it, offer to add it.
