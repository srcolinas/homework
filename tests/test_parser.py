import pathlib

import pytest

from homework import parser


def test_ValueError_if_task_never_closes():
    with pytest.raises(ValueError):
        parser.parse("""## homework:replace:on
#.dw =
#.w = 
dw = compute_gradients()
w -= alpha * dw
""")


def test_reference_files(test_files: list[tuple[pathlib.Path, pathlib.Path]]):
    for source, expected_file in test_files:
        result = parser.parse(source.read_text())
        expected = expected_file.read_text()
        assert result == expected


@pytest.fixture
def test_files(
    request: pytest.FixtureRequest,
) -> list[tuple[pathlib.Path, pathlib.Path]]:
    data_dir = pathlib.Path(request.module.__file__).parent / "data"

    files = []
    for source in data_dir.rglob("*"):
        if source.is_dir():
            continue

        if "_homework" not in source.name:
            files.append(
                (source, source.with_name(source.stem + f"_homework{source.suffix}"))
            )

    return files
