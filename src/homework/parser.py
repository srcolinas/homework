from typing import Iterable


def parse(source: str) -> str:
    """
    Produces a homework by replacing implementations
    with the hints provided within speciall delimited
    sections.
    """
    output = []
    lines = iter(source.splitlines())
    for line in lines:
        if line.endswith("## homework:replace:on"):
            buffer = _group_task(line, lines)
            for b in buffer:
                output.append(b)
            continue
        output.append(line)
    if source.endswith("\n"):
        output.append("")
    return "\n".join(output)


def _group_task(first: str, lines: Iterable[str]) -> list[str]:
    indentation = first.split("## homework")[0]
    buffer = [indentation + "## homework:start"]
    for line in lines:
        if line.endswith("## homework:replace:off"):
            buffer.append(indentation + "## homework:end")
            return buffer
        if line.lstrip().startswith("#."):
            buffer.append(indentation + line.split("#.")[-1])
    raise ValueError
