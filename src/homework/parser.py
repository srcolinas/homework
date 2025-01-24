from typing import Iterable


def parse(source: str) -> str:
    """
    Produces a homework by replacing implementations
    with the hints provided within speciall delimited
    sections.
    """
    output = ""
    lines = iter(source.splitlines())
    for line in lines:
        if line.endswith("## homework:replace:on"):
            output += "\n".join(_group_task(line, lines))
            continue
        output += line + "\n"
    return output


def _group_task(first: str, lines: Iterable[str]) -> list[str]:
    indentation = first.split("## homework")[0]
    buffer = [indentation + "## homework:start"]
    for line in lines:
        if line.endswith("## homework:replace:off"):
            buffer.append("## homework:end")
            return buffer
        if line.lstrip().startswith("#."):
            buffer.append(indentation + line.split("#.")[-1])
    raise ValueError
