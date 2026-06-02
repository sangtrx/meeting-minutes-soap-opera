from __future__ import annotations

import argparse
import random

from .core import dramaticize
from .data import CLIFFHANGERS
from .io import load_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Turn meeting notes into a soap opera recap.")
    parser.add_argument("--file", help="Input file with meeting notes")
    parser.add_argument("--seed", type=int, help="Random seed for repeatability")
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    rng = random.Random(args.seed)

    text = load_text(args.file)
    recap_lines = dramaticize(text, rng)

    print("Previously on: The Meeting Minutes…")
    for line in recap_lines:
        print(f"- {line}")
    print("\nNext time:")
    print(rng.choice(CLIFFHANGERS))
