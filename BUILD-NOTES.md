# Build notes

The bounty asks for a program that writes exactly one word describing an ex
to the entry file, between 1 and 111 characters, with nothing else attached.
A judge model then compares words head to head and picks the funnier one,
weighing first whether the word reads instantly as a verdict on a former
partner, then comic punch, surprise, craft, and recognition.

The word chosen is unsubscribed. The reasoning behind it: the obvious
insults were avoided on purpose, since the judge brief says a plain insult
is not a joke. Unsubscribed treats the ex as a subscription that got
cancelled, which is a precise modern absurdity rather than a label. It
arrives without a caption, it is spelled plainly with no punctuation tricks,
and anyone who has ever unsubscribed from something that kept showing up
uninvited recognises the feeling at once. It is also a less common pick
than the expired or blocked style answers, which helps it stand out in a
pairwise comparison.

The program itself is deliberately tiny. It holds the word as a constant,
checks it against the gate before writing (one word, no whitespace, within
the length limit), creates the output directory if needed, and writes the
word with no trailing newline so the file holds exactly the word and nothing
else. The entry was run locally and verified by counting characters and by
comparing hashes of the file with and without a trailing newline, so the
exact bytes the grader will see are known.

The repository carries the three linked makefun badges in the readme, an MIT
license file with the SPDX identifier line, and the owner file naming the
payout wallet.
