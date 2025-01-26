import pathlib
import re

from . import parser


def prepare(
    source_dir: pathlib.Path, pattern: str
) -> pathlib.Path:
    homework_dir = source_dir.with_name(source_dir.stem + "_homework")
    homework_dir.mkdir(parents=False)

    expresion = re.compile(pattern)

    for source in source_dir.rglob("*"):
        if source.is_dir():
            continue

        if expresion.match(str(source)) is None:
            continue

        relative_path = source.relative_to(source_dir)

        source_content = source.read_text()
        student_content = parser.parse(source_content)
        homework = homework_dir / relative_path
        homework.parent.mkdir(exist_ok=True)
        homework.write_text(student_content)
    return homework_dir

