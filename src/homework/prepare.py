import pathlib
import re
from typing import Callable

from . import parser


def prepare(
    source_dir: pathlib.Path, pattern: str, cipher: Callable[[str], str] = lambda x: x
) -> tuple[pathlib.Path, pathlib.Path]:
    homework_dir = _create_derived_directory(source_dir, "_homework")
    solution_dir = _create_derived_directory(source_dir, "_solution")

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

        teacher_content = cipher(source_content)
        solution = solution_dir / relative_path
        solution.parent.mkdir(exist_ok=True)
        solution.write_text(teacher_content)
    return homework_dir, solution_dir


def _create_derived_directory(source_dir: pathlib.Path, suffix: str) -> pathlib.Path:
    dir = source_dir.with_name(source_dir.stem + suffix)
    dir.mkdir(parents=False)
    return dir
