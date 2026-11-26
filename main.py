# The Dog Reviews the Mailman — make.fun entry
# (u-motasimfuad-the-dog-reviews-the-mailman-87608f85)
#
# One funny one-line review a dog gives the mailman, written as plain
# text to /output/entry.txt. The line is a fixed string: the grader runs
# the program twice and the runs must be deterministic, so there is no
# randomness and no input. Standard library only.

import os

LINE = (
    "One star. He rings twice, waves like we're old friends, "
    "then flees before I can accept his apology "
    "\u2014 but he left the biscuit, so technically I won the war."
)

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(f"Wrote {len(LINE)} characters to {output_dir}/entry.txt")
