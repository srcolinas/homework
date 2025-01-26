import argparse
import pathlib

from . import prepare


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=pathlib.Path)
    parser.add_argument("-p", "--pattern", default=".*\.(py|json|csv|yaml|yml)")
    args = parser.parse_args()


    homework_dir = prepare.prepare(args.source_dir, pattern=args.pattern)
    print(f"Homework created from {args.source_dir} in {homework_dir}")
