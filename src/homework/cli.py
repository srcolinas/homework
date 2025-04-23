import argparse
import pathlib

from . import prepare


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=pathlib.Path)
    parser.add_argument("-e", "--extensions", default=None, type=pathlib.Path | None, help="")
    args = parser.parse_args()

    homework_dir = prepare.prepare(args.source_dir, extensions=args.extensions)
    print(f"Homework created from {args.source_dir} in {homework_dir}")
