import pathlib

from homework import prepare


def test_produces_assignment(tmp_path: pathlib.Path):
    (tmp_path / "source.py").write_text("""## homework:replace:on
#.dw =
#.w =
dw = compute_gradients()
w = w - alpha * dw
## homework:replace:off""")
    homework_dir = prepare.prepare(tmp_path, r".*source\.py$")
    assert (
        (homework_dir / "source.py").read_text()
        == """## homework:start
dw =
w =
## homework:end"""
    )


def test_handles_pattern_from_source_dir(tmp_path: pathlib.Path):
    (tmp_path / "main.py").touch()
    (tmp_path / "first.rs").touch()
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "module.py").touch()
    (subdir / "data.json").touch()

    homework_dir = prepare.prepare(tmp_path, r".*\.(py|json)$")
    assert (homework_dir / "main.py").exists()
    assert (homework_dir / "subdir" / "module.py").exists()
    assert (homework_dir / "subdir" / "data.json").exists()
    assert not (homework_dir / "first.rs").exists()
