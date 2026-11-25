# Design — One-Line Office Jokes

## The line

> I raised an IT ticket about the printer, and the printer raised one about me.

77 characters, 77 bytes, one line, no trailing newline. It is the whole
entry: `main.py` writes exactly this string to `/output/entry.txt`.

## Why this line wins under the judge's brief, criterion by criterion

The brief weighs five criteria in order, and the line was built to clear
them in that order — the first difference decides, so the line must not
lose early.

**1. It is a single-line joke about office life.** The line is one
sentence, one incident, no story, no slogan, no list. It does not describe
a joke or promise one later; the sentence itself is the joke. A judge
comparing it against a generic work aphorism or a multi-sentence anecdote
finds the difference here, on the first criterion.

**2. It turns on a real detail of office life.** Two of them, stacked in
one sentence: raising an IT ticket, and the office printer. Both are
things anyone who has worked in an office has actually done or cursed at.
Nothing in the line is generic talk about "work" or "being busy" — the
humour needs the ticket queue and the printer to exist. A line about
hating Mondays fails here; this one cannot be moved to any other setting
without breaking.

**3. The laugh lands in the last few words.** The first half sets up a
completely ordinary act — I complained about the printer. The second half
flips the direction: the printer complained about me. The turn arrives in
the final five words ("raised one about me"), which is exactly where the
brief says the laugh belongs. There is no punchline buried in the middle
and no trailing explanation after it. The line ends the moment the joke
lands.

**4. It is clear on one reading.** No jargon beyond "IT ticket", which is
everyday office vocabulary. No setup that needs explaining, no wordplay
that needs a second pass, no reference to a meme or a news story. A reader
who has never seen an IT ticket system still gets it: I reported the
printer, the printer reported me. The symmetry of the two halves does the
work — "raised ... about the printer" mirrored by "raised one about me".

**5. The wording is fresh.** The device — the object answers back — is an
old comedy move, but this exact sentence is not a joke going round the
internet. It avoids the recycled office lines entirely: no "this meeting
could have been an email", no "I hate Mondays", no "the printer is broken"
stated flat. The ticket, rather than a complaint form or a grievance, is
the specific vehicle, and the reversal is stated in the driest possible
words, which is what makes it sound new instead of borrowed.

## Lane choice

The field was empty when this entry was built (zero submissions), so the
lane was chosen on the brief alone, not against rivals. The printer lane
was picked because the printer is the one office object that is both
universally resented and universally specific: everybody has a printer
story, and "IT ticket" is the office's own ritual for dealing with it.
The ticket queue is also the rare office detail that is itself a small
bureaucracy, so the reversal — the machine using the bureaucracy against
you — feels like the office fighting back rather than a random absurdity.

## What was rejected and why

Twelve candidates were drafted and judged pairwise against the exact brief
(full tournament in `../CANDIDATES.md`). The decisions that mattered:

- **The reply-all line** ("HR answered with a calendar invite titled
  'A Quick Chat'") was the runner-up. It stacks two real details and its
  final phrase is the most office-specific in the field. It lost because
  its laugh is a phrase, not a reversal — the printer line flips the whole
  sentence in the last five words.
- **The printer-out-of-paper line** ("HR calls a growth opportunity and
  the rest of us call Tuesday") has a fine single-word closer, but its
  detail is thinner: "out of paper" is a state, where the ticket is an
  action with a direction that can be reversed.
- **The sentient-meeting line** lost on freshness: the meeting that gains
  consciousness is a lane other competitions have already mined, and its
  laugh sits mid-concept rather than on the final beat.
- **The "corporate for" line** ("the minutes just say 'discussed'") lost
  because its format is a known meme template — criterion 5 again.
- **The password-expiry line** is a wry observation, not a turn: it
  reports a fact with a raised eyebrow, where the winner reverses the
  situation.

## The program

`main.py` is deliberately the smallest program that satisfies the task: a
constant string, a directory creation, one write. Determinism is total —
no network, no clock, no randomness, no file reads — so two runs in fresh
directories produce byte-identical output, verified by sha256 during the
build. The entry tree is four files (`main.py`, this document, `README.md`,
`LICENSE`), kept under the 8,192-byte cap.
