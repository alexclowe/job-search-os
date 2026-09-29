---
name: decline-offer-letter
description: Write a gracious, specific note declining an offer or withdrawing from a process — sincere enough to mean it, short enough to send, and clear about the one thing that would have changed the answer, so the door stays open. Activates on "help me decline" / "withdraw from this process" / "turn down the offer" / "say no nicely".
disable-model-invocation: true
---

> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

Declining well is a networking move. Keep it short, true, and warm.

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block. Continue with
pasted material if none.

Older profiles use other labels for the same fields: `Minimum salary:` or `Salary floor:`
mean minimum pay (annual salary unless the value says otherwise), **Shipped artifacts**
means wins, `Positioning challenges:` means things a hiring manager might question,
and `Target level:` means career stage. Read them the same way.

<!-- shared:board-check:start — edit products/job-search-os/shared-instructions/board-check.md, then run scripts/job-search-os/sync-shared-instructions.py -->
## Board check — moves saved on the board (always first)

Run this before anything else in this job reads, counts, summarizes, or changes the
**Application Board**. It is not optional and it is not silent: it ends with one line
that says what you found. Never report what moved, what's stale, stage counts, or
"nothing moved" until this check has run in this conversation.

The person can move a card on the board themselves. A board built from the template
saves each move in the board artifact's storage: one document per row in its `moves`
collection, holding the row id, the new stage, and when it was saved.

1. **Find the board.** List this Project's artifacts, including ones from earlier
   conversations, and open the one named **Application Board** (never one named
   "SAMPLE — …" unless this is a sample run).
2. **Read the saved moves.** Use the tool that reads an artifact's stored data to list
   every document in the board's `moves` collection. Do this every time; don't assume
   there are none because the data block looks current or because an earlier reply
   said so.
3. **Apply each saved move whose row is still on the board.** These are the person's
   own edits: apply them without asking "apply it?". A saved move is the person's
   latest word on that row's stage.
   - Set that row's **Stage** in the board's data block to the saved stage.
   - If the date for the new stage is blank, fill it with the date the move was saved
     (Applied → Applied on, Screening → Screen on, Interviewing → Interview on,
     Onsite → Final on, Offer → Offer on, Closed → Closed on) and mark it
     `[confirm date]`.
   - A row moved to Closed with no Closed why: leave it blank and ask for the reason
     at the end of this job, as clickable choices.
4. **Save it once.** Republish the board, update the CSV backup, then delete exactly
   the saved-move documents you applied (and any for rows no longer on the board). If
   Claude asks permission to write the board or its backup, that request covers this
   step — ask in this same turn and carry on with the job; don't stop and wait for a
   separate "apply it".
5. **Say what you found, in one line, then continue:**
   - "Board check: applied 2 moves you made on the board — Northwind → Interviewing,
     Harbor → Closed."
   - "Board check: no moves saved on the board since last time."
   - If the moves were read but the board couldn't be written (permission declined or
     the file is locked): "Board check: you moved Northwind → Interviewing on the board;
     I'm using that here, and it will be saved to the board next time." Use the moved
     stages for everything in this job anyway.
   - If this board has no storage, or the stored-data tool isn't available here:
     "Board check: I can't read moves saved on the board here, so I'm using the board
     as it was last published — tell me if you moved anything."

From here on, use the board with the saved moves applied.
<!-- shared:board-check:end -->

## Inputs

Company, role, who to write to (recruiter, hiring manager, or both), where in the
process it is (offer in hand or mid-process), the real reason (clickable: accepted
elsewhere · pay below my minimum · level or scope · remote or location · timing ·
other), and whether the person wants to name the reason.

## Output

Two notes, 60–110 words each, the person's voice:
- **To the hiring manager:** thanks for something specific from the conversations,
  the decision in one plain sentence, the reason only if the person chose to name it
  (comp and level stated factually, never as a complaint), the door left open
  ("if the level or the range changes, I'd want to hear about it").
- **To the recruiter:** the decision, the thanks, and the same one-line reason.

If the person is **mid-process** (withdrawing): the same shape, sent as soon as they
know — with an offer to introduce someone else if they have a name.

## Constraints

- Never negotiate inside a decline; if the person still wants to negotiate, route to
  `salary-negotiation-script` first.
- No invented reasons; no reason at all if they'd rather not.
- Drafts only (Gmail drafts when connected). Nothing sends.

## After

"Want me to move the row to Closed on your Application Board (Closed why: offer declined, or withdrew)? Say 'close it'."

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
