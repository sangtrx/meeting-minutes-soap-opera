from __future__ import annotations

import argparse
import random

from .core import dramaticize, extract_action_items, pick_cliffhanger, split_lines, summarize
from .data import STYLES
from .io import load_text


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Turn meeting notes into a soap opera recap.")
    parser.add_argument("--file", help="Input file with meeting notes")
    parser.add_argument("--seed", type=int, help="Random seed for repeatability")
    parser.add_argument(
        "--mode",
        choices=("recap", "summary", "actions", "full"),
        default="recap",
        help="Output mode",
    )
    parser.add_argument(
        "--style",
        choices=sorted(STYLES.keys()),
        default="dramatic",
        help="Tone style",
    )
    parser.add_argument(
        "--max-items",
        type=int,
        default=5,
        help="Max items for summaries and action items",
    )
    return parser


def print_section(title: str, items: list[str], empty_label: str = "(none)") -> None:
    print(title)
    if not items:
        print(f"- {empty_label}")
        return
    for item in items:
        print(f"- {item}")


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    rng = random.Random(args.seed)

    text = load_text(args.file)
    lines = split_lines(text)

    if args.mode in {"recap", "full"}:
        recap_lines = dramaticize(text, rng, style=args.style)
        print_section("Previously on: The Meeting Minutes…", recap_lines, "(no notes provided)")

    if args.mode in {"summary", "full"}:
        summary_lines = summarize(lines, max_items=args.max_items)
        print_section("\nSummary:", summary_lines, "(no summary items)")

    if args.mode in {"actions", "full"}:
        action_items = extract_action_items(lines, max_items=args.max_items)
        print_section("\nAction items:", action_items, "(no action items detected)")

    if args.mode in {"recap", "full"}:
        print("\nNext time:")
        print(pick_cliffhanger(rng, style=args.style))
