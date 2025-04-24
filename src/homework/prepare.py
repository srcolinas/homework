import fnmatch
import json
import pathlib
import shutil
from typing import cast

from . import parser


def prepare(
    source_dir: pathlib.Path,
    *,
    extensions: dict[str, tuple[str, str]] | pathlib.Path | None = None,
    copy_unaffected_files: bool = False,
    ignore_patterns: list[str] | None = None,
) -> pathlib.Path:
    print(ignore_patterns)
    if isinstance(extensions, pathlib.Path):
        extensions = json.loads(extensions.read_text())
    if extensions is None:
        extensions = default_extensions()
    extensions = cast(dict[str, tuple[str, str]], extensions)

    if ignore_patterns is None:
        ignore_patterns = []

    # ignore_patterns = [os.path.join(source_dir, p) for p in ignore_patterns]

    homework_dir = source_dir.with_name(source_dir.stem + "_homework")
    homework_dir.mkdir(parents=False)

    for source in source_dir.rglob("*"):
        if _should_be_ignored(
            source, ignore_patterns, extensions, copy_unaffected_files
        ):
            continue

        relative_path = source.relative_to(source_dir)
        homework = homework_dir / relative_path
        homework.parent.mkdir(exist_ok=True)
        if source.suffix in extensions:
            homework.parent.mkdir(exist_ok=True)
            source_content = source.read_text()
            hint_marker, block_marker = extensions[source.suffix]
            student_content = parser.parse(
                source_content, hint_marker=hint_marker, block_marker=block_marker
            )
            homework.write_text(student_content)
        else:
            shutil.copyfile(source, homework)
    return homework_dir


def _should_be_ignored(
    source: pathlib.Path,
    ignore_patterns: list[str],
    extensions: dict[str, tuple[str, str]],
    copy_unnaffected_files: bool,
) -> bool:
    if source.is_dir():
        return True
    if source.suffix not in extensions and not copy_unnaffected_files:
        return True
    for pattern in ignore_patterns:
        for part in source.parts:
            if fnmatch.fnmatch(part, pattern):
                return True
    return False


def default_extensions() -> dict[str, tuple[str, str]]:
    """
    Returns a mapping from extension to a tuple of (hint marker, block marker)
    """
    return {".py": ("#.", "## "), ".tf": ("# ", "## ")}
