#!/usr/bin/env python3
"""Make the AI Judge Laugh — round 2 entry.

Writes one office-life joke, a single line under 200 characters, to
/output/entry.txt, where the house judge reads it.
"""
import os

LINE = "My calendar says I'm free, my inbox says I'm lying, and my boss just forwarded the inbox as proof."

# The gate refuses anything outside 1-200 chars, so never ship a bad line silently.
assert 1 <= len(LINE) <= 200, f"entry line is {len(LINE)} chars, must be 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
