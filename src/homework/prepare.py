import json
import pathlib

from . import parser


def prepare(
    source_dir: pathlib.Path, extensions: dict[str, str] | pathlib.Path | None = None
) -> pathlib.Path:
    if isinstance(extensions, pathlib.Path):
        extensions = json.loads(extensions.read_text())
    if extensions is None:
        extensions = default_extensions()

    homework_dir = source_dir.with_name(source_dir.stem + "_homework")
    homework_dir.mkdir(parents=False)

    for source in source_dir.rglob("*"):
        if source.suffix not in extensions:
            continue

        relative_path = source.relative_to(source_dir)

        source_content = source.read_text()

        hint_marker, block_marker = extensions[source.suffix]
        student_content = parser.parse(
            source_content, hint_marker=hint_marker, block_marker=block_marker
        )
        homework = homework_dir / relative_path
        homework.parent.mkdir(exist_ok=True)
        homework.write_text(student_content)
    return homework_dir


def default_extensions() -> dict[str, tuple[str, str]]:
    """
    Returns a mapping from extension to a tuple of (hint marker, block marker)
    """
    return {".py": ("#.", "## "), ".tf": ("# ", "## ")}
