import argparse
import pathlib

from . import prepare


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_dir", type=pathlib.Path)
    parser.add_argument("-e", "--extensions", default=None, type=pathlib.Path, help="")
    parser.add_argument("-c", "--copy-unnafected", default=False, action="store_true")
    parser.add_argument(
        "-i",
        "--ignore",
        nargs="*",
        help="Patterns to ignore",
        default=[".git", "__pycache__", "*.pyc"],
    )
    args = parser.parse_args()

    homework_dir = prepare.prepare(
        args.source_dir,
        extensions=args.extensions,
        copy_unaffected_files=args.copy_unnafected,
        ignore_patterns=args.ignore,
    )
    print(f"Homework created from {args.source_dir} in {homework_dir}")
