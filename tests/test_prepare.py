import json
import pathlib

from homework import prepare


def test_produces_assignment(tmp_path: pathlib.Path):
    (tmp_path / "source.py").write_text("""## homework:replace:on
#.dw =
#.w =
dw = compute_gradients()
w = w - alpha * dw
## homework:replace:off""")
    homework_dir = prepare.prepare(tmp_path, extensions={".py": ("#.", "## ")})
    assert (
        (homework_dir / "source.py").read_text()
        == """## homework:start
dw =
w =
## homework:end"""
    )


def test_it_uses_default_extensions(tmp_path: pathlib.Path):
    (tmp_path / "source.py").write_text("""## homework:replace:on
#.dw =
#.w =
dw = compute_gradients()
w = w - alpha * dw
## homework:replace:off""")
    homework_dir = prepare.prepare(tmp_path)
    assert (
        (homework_dir / "source.py").read_text()
        == """## homework:start
dw =
w =
## homework:end"""
    )


def test_handles_files_with_extensions_from_source_dir(tmp_path: pathlib.Path):
    (tmp_path / "main.py").touch()
    (tmp_path / "first.rs").touch()
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "module.py").touch()
    (subdir / "data.json").touch()

    homework_dir = prepare.prepare(
        tmp_path, extensions={".py": ("", ""), ".json": ("", "")}
    )
    assert (homework_dir / "main.py").exists()
    assert (homework_dir / "subdir" / "module.py").exists()
    assert (homework_dir / "subdir" / "data.json").exists()
    assert not (homework_dir / "first.rs").exists()


def test_handles_extensions_in_file(tmp_path: pathlib.Path):
    (tmp_path / "source.py").write_text("""## homework:replace:on
#.dw =
#.w =
dw = compute_gradients()
w = w - alpha * dw
## homework:replace:off""")

    extensions = tmp_path / "extensions.json"
    extensions.write_text(json.dumps({".py": ("#.", "## ")}))
    homework_dir = prepare.prepare(tmp_path, extensions=extensions)
    assert (
        (homework_dir / "source.py").read_text()
        == """## homework:start
dw =
w =
## homework:end"""
    )


def test_copies_unaffected_files_when_flag_is_given(tmp_path: pathlib.Path):
    (tmp_path / "main.py").touch()
    (tmp_path / "first.rs").touch()
    subdir = tmp_path / "subdir"
    subdir.mkdir()
    (subdir / "module.py").touch()
    (subdir / "data.json").touch()

    homework_dir = prepare.prepare(
        tmp_path,
        extensions={".py": ("", ""), ".json": ("", "")},
        copy_unaffected_files=True,
    )
    assert (homework_dir / "main.py").exists()
    assert (homework_dir / "subdir" / "module.py").exists()
    assert (homework_dir / "subdir" / "data.json").exists()
    assert (homework_dir / "first.rs").exists()
