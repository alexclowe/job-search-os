---
name: jobsearch-workflow-follow-up-negotiate
description: Follow up and negotiate for the Job Search AI Operating System. Invoke when a job seeker says "follow up and negotiate", "write my thank-you note", "I haven't heard back", "I got an offer", "help me counter", "negotiate this offer", "should I take it", or pastes offer terms or an interview recap and asks what to send next. Drafts thank-you and follow-up notes on a cadence, reads an offer against the minimum pay and market notes, builds a counter with the exact words, and keeps the Offer Tracker current. Never accepts or declines on its own.
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

Everything after the interview: the note the same day, the nudge that isn't needy, and
the counter that holds to your minimum pay without burning the offer.

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
pasted in this chat. Present → use pay type, minimum pay, target pay, what else
matters (the `Also matters:` line), target roles, location and remote preference,
career stage, and voice samples; don't re-ask. (Older profiles say `Minimum salary:`
or `Salary floor:` for minimum pay, annual unless the value says otherwise, and
`Total-comp target:` for target pay.) Absent → say setup takes about two minutes;
without a minimum pay, negotiation drafts are marked "no minimum pay on file" and the
person supplies the number.

**Profession archetype (read, don't ask).** If the profile or the offer names a
profession, read the matching archetype — `./archetypes/<profession>.md` in this
Project first, then the `archetypes/` folder that ships with the Tailor & apply job
(`jobsearch-workflow-tailor-apply/archetypes/`). Use its **How pay is usually structured**
and **What's usually negotiable** sections to shape the questions to ask and the
counter. It never supplies a figure; if no archetype matches, say nothing about it.

## Pre-flight 2 — Connections

Read `./jobsearch-connections.md`. Present → route to connected tools. Absent → say
once: "I'm not connected to your tools yet — say 'connect my tools' anytime. For now
everything comes out paste-ready." Check which connector tools exist; never assume a
tool name.

## Intake

Trackers named "SAMPLE — …" are from the demo. Never read from or write to them except
during a sample run.

**Read first, ask last.** Pull the company, round, date, interviewer names, and any
offer terms from the Application Board, the Offer Tracker, the calendar (if connected,
offer to read yesterday's interview event), or what the person pasted. Then ask only
what's still missing — at most 3 questions in one card of clickable choices — and
produce a first draft. Unknowns go in the draft as `[confirm]`.

1. **Which application** — picked from the board.
2. **What happened** (clickable): just interviewed · waiting, no word for [n] days ·
   got an offer · got a competing offer · they asked for references.
3. **For an offer** — the written terms (paste or file), read by pay type:
   - **Hourly:** base rate, shift and weekend/night differentials, overtime rules,
     guaranteed hours per week or pay period, on-call and call-back pay, schedule
     (shift length, days, rotation), sign-on and its repayment terms.
   - **Annual salary:** base, bonus target and basis, equity only if the offer includes
     it (type, amount or value, vesting, strike or price if given), sign-on.
   - **Commission or commission plus base:** base or draw (and whether a draw is
     recoverable), commission split or rate, ramp period and any guarantee during it,
     caps, clawbacks, territory or lead source, expected first-year total as stated.
   - **Salary schedule:** step and lane placement, years of prior experience credited,
     stipends (coaching, extra duties, advanced degree), pension or retirement plan,
     contract days.
   Plus, for every type: start date, title, location and remote terms, benefits that
   matter, license or certification support, the decision deadline. What the person
   wants most (clickable, pick two) — offer the options that fit the pay type: hourly →
   base rate · differentials · schedule · guaranteed hours · sign-on; salary → base ·
   bonus · equity (only if offered) · title · start date · remote terms; commission →
   base or draw · split · ramp guarantee · lead source · territory; schedule → step
   placement · years credited · stipends · start date.
4. **For a follow-up** — days since last contact and what they were told about timing.

Before tool writes, say once: "As I work, Claude may ask you to approve actions — about
[N] (one draft per note, the offer worksheet, the Offer Tracker, and the Application
Board). **Allow for this task** covers the rest of this run; tracker updates always
take a quick confirm."

## Produce

**After an interview**
1. **Thank-you notes** — one per interviewer, 60–100 words each, sent the same day:
   one specific thing from *that* conversation, one line that reinforces the story
   that mattered most to them, one line that adds something they asked about and the
   person didn't fully answer. No two notes alike; no "I remain very excited".
2. **Follow-up cadence** — the next two touches with dates: a check-in at the timing
   they were given plus two business days, then one more a week later; each 40–80
   words, one new piece of information each time (a link to the person's work, a
   certificate or reference they mentioned, an answer they owe). Never a third nudge — after that the board row goes
   to "parked".

**Offer in hand**
3. **Offer worksheet (.xlsx)** — each component as the company stated it, in its own
   unit, with the annual value computed by formula only where the person supplied the
   inputs (never estimates). Rows follow the pay type:
   - **Hourly:** base rate × hours per week × 52 (hours as stated, or
     `[confirm hours/week]`), each differential × the hours it applies to, overtime at
     the stated rule, sign-on (with any repayment clause noted).
   - **Annual salary:** base, bonus at target, equity per year only from the company's
     own numbers, sign-on.
   - **Commission:** base or draw, commission at the stated expected level, ramp
     guarantee, and a "low / expected" pair of totals only when the company gave both.
   - **Salary schedule:** the placement's figure, stipends, and a note on the pension
     or retirement contribution as stated.
   Then total first-year and steady-state, any competing offer side by side, and the
   salary check like with like: base rate vs. your minimum pay in the same unit, total
   vs. the target pay on file. Any market figure the person pastes goes in a "notes"
   column with its source; the worksheet never invents a market rate.
4. **Counter script** — the exact words for the call and a matching email (120–200
   words): open with genuine interest, name the two priorities, anchor the ask on a
   specific number with a reason drawn from the role's scope, the person's wins, or a
   competing offer (only if real), leave the other components alone, and close with a
   date. Fit the ask to the pay type: hourly → the base rate, a differential, a
   guaranteed schedule or hours, sign-on; commission → the split, a ramp guarantee or
   non-recoverable draw, the lead source; schedule → step placement and years credited
   (often the one lever a published scale leaves), stipends; salary → base, bonus,
   equity only if it's on the table, title, start date. If the offer is **below your
   minimum pay**, say so plainly to the person first and give two scripts: the counter
   that would bring it to your minimum pay, and the walk-away that keeps the door open.
   Include the questions to ask before countering, for the pay type (for example:
   guaranteed hours and how differentials are paid; how the draw is recovered and what
   a typical first-year rep earns; how prior years are credited; level calibration,
   bonus history, and remote terms in writing).
5. **Decision memo** (in chat, short) — the offer against the person's must-haves,
   what's negotiable in the company's usual practice, what to get in writing, and the
   one thing they should sleep on. The decision stays theirs.
6. **Decline note** (only if they choose it) — gracious, specific, door open.

## Compliance pass (inline — do not hand off)

- **Minimum pay:** an offer at or below your minimum pay is called that in the first line of the
  memo; no draft soft-pedals it or asks for less than your minimum pay.
- **No commitments:** no draft accepts, declines, resigns, or gives notice. Acceptance
  wording is produced only when the person says "write my acceptance".
- **No invented figures:** market ranges appear only when the person supplies them
  with a source; equity value only from inputs the company gave; commission totals
  only as the company stated them, never "up to" figures presented as expected. Pay-transparency
  rules vary by state and country — note "[verify your state's pay-range disclosure
  rule]" when relevant; never state one as fact.
- **Every claim holds up:** every reason in a counter is true and specific.
- **Privacy:** never share a competing offer's letter or exact terms unless the person
  chose to; no salary history.
- **Professional advice:** equity taxation, sign-on repayment clauses, draw
  recovery terms, pension vesting, union contract questions, separation timing against
  a current employer's bonus or vesting, and any non-compete get a "worth a
  professional's eyes" line (or "ask your union representative", where there is one),
  not an answer.
Append one short **Before you send** checklist with only the checks that fired.

## Route outputs

- **Gmail connected:** each note as a draft, in the interview thread when possible,
  To: the interviewer only if the address is known. **Never send.**
- **Drive connected:** the worksheet in `[drive-root-folder]/[Company] — [Role]/` as
  "Offer — [Company].xlsx"; the counter email saved alongside as .docx.
- **Calendar connected:** the follow-up touches as reminders on their dates; the offer
  deadline as an all-day event "Decide — [Company]". Only dates the person confirmed.
- **Otherwise:** notes paste-ready in this Project, the worksheet saved here.

## Trackers (living)

List this Project's artifacts first, including ones from earlier conversations. Update
the **Application Board** row: Last touch, Next action, Due. Update the **Offer
Tracker** (create only if absent): Company · Role · Pay type · Base (in its unit, e.g.
$46/hour or $92,000/year or step 6) · Variable (differentials, bonus, or commission as
stated) · Other (sign-on, equity, stipends, pension) · Est. first-year total · Salary
check · Deadline · Status (Received → Countered → Accepted / Declined) · Counter ·
Next. An existing tracker with the older columns (Base · Bonus · Equity · Other) keeps
working — add the Pay type column and put hourly or commission details under Other
and Variable rather than rebuilding it. When an offer is accepted, offer to move every other open row to
Closed with a decline note each.

## Close

Never narrate your own tooling in the close: nothing about files you could not open, workbooks you could not recalculate, pages you did not open, or what the sandbox lacks. State what was produced, what needs confirming, and where it landed.

What was drafted and where, your minimum pay verdict on any offer in one line, the
`[confirm]` list, then "What's next?" — offer the command center. If they accepted,
name `/thirty-sixty-ninety-plan` as the next thing to run.
