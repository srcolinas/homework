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
        markers = _get_markers(line)
        if markers is None:
            output.append(line)
            continue
        last, header, footer = markers
        buffer = _group(lines, first=line, last=last, header=header, footer=footer)
        output.extend(buffer)
    if source.endswith("\n"):
        output.append("")
    return "\n".join(output)


def _get_markers(line: str) -> tuple[str, str | None, str | None] | None:
    if line.endswith("## homework:replace:on"):
        return "## homework:replace:off", "## homework:start", "## homework:end"
    if line.endswith("## homework:delete:on"):
        return "## homework:delete:off", None, None


def _group(
    lines: Iterable[str],
    *,
    first: str,
    last: str,
    header: str | None,
    footer: str | None,
) -> list[str]:
    indentation = first.split("## homework")[0]
    buffer = [""]
    if header is not None:
        buffer[0] += indentation + header
    for line in lines:
        if line.endswith(last):
            buffer.append("")
            if footer is not None:
                buffer[-1] += indentation + footer
            return buffer
        if line.lstrip().startswith("#."):
            buffer.append(indentation + line.split("#.")[-1])
    raise ValueError
