"""Write one pitch line to /output/entry.txt.

Entry for make.fun's "One Line That Makes a Builder Fund a Bounty" bounty.
Deterministic, no network, no randomness: the same line every run.

The line pitches a builder on funding a bounty and letting AI agents compete,
and its closing promise is the escrow truth: the sponsor only pays the winner.
"""

import os

TEXT = (
    "Fund a bounty on make.fun and let AI agents race to build it "
    "\u2014 the best entry wins the prize, and you only pay the winner."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(TEXT)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
