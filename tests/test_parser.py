import pathlib
from typing import Iterator

import pytest

from homework import parser, prepare


def test_ValueError_if_task_never_closes():
    with pytest.raises(ValueError):
        parser.parse(
            """## homework:replace:on
#.dw =
#.w = 
dw = compute_gradients()
w -= alpha * dw
""",
            hint_marker="#.",
            block_marker="## "
        )


def test_reference_files(test_files: tuple[pathlib.Path, pathlib.Path]):
    source, target = test_files
    extensions = prepare.default_extensions()
    hint_marker, block_marker = extensions[source.suffix]

    result = parser.parse(
        source.read_text(), hint_marker=hint_marker, block_marker=block_marker
    )
    expected = target.read_text()
    assert result == expected


@pytest.fixture(params=["sample_0.py", "sample_1.py", "sample_2.py", "sample_3.tf"])
def test_files(
    request: pytest.FixtureRequest,
) -> Iterator[tuple[pathlib.Path, pathlib.Path]]:
    data_dir = pathlib.Path(request.module.__file__).parent / "data"
    name: str = request.param
    source = data_dir / name
    target = source.with_name(source.stem + f"_homework{source.suffix}")
    yield source, target
