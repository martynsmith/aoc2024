#!/usr/bin/env python

import sys
import os
import httpx
from datetime import date
from bs4 import BeautifulSoup
from pathlib import Path

YEAR = "2024"

# DAY_NUMBER
# YEAR

if len(sys.argv) > 1:
    day = int(sys.argv[1])
else:
    day = date.today().day

input_file = Path(f"input{day:02}.txt")
sample_file = Path(f"sample{day:02}.txt")
solution_file = Path(f"day{day:02}.py")
template_file = Path("fetch.template.py")

print(f"fetching for {day:02} December")

if not solution_file.exists():
    print(f"creating:", solution_file)

    contents = template_file.read_text()
    contents = contents.replace('DAY_NUMBER', f"{day:02}")
    contents = contents.replace('YEAR', YEAR)
    solution_file.write_text(contents)
    solution_file.chmod(0o755)

if not input_file.exists():
    print(f"fetching input:", input_file)
    response = httpx.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        cookies=dict(session=os.environ['AOC_SESSION'])
    )
    response.raise_for_status()
    input_file.write_bytes(response.content)

if not sample_file.exists():
    print(f"fetching sample:", sample_file)
    response = httpx.get(f"https://adventofcode.com/{YEAR}/day/{day}")
    response.raise_for_status()
    soup = BeautifulSoup(response.text, features="html.parser")
    for c in soup.select('code'):
        if len(c.text.splitlines()) < 3:
            continue
        sample_file.write_text(c.text)
        break

print(f"\nYou might want this:\n\nwatchexec --timings --clear=clear uv run day{day:02}.py")
