from typing import Iterable


def parse(source: str, hint_marker: str, block_marker: str) -> str:
    """
    Produces a homework by replacing implementations
    with the hints provided within speciall delimited
    sections.
    """
    output = []
    lines = iter(source.splitlines())
    for line in lines:
        markers = _get_markers(line, block_marker=block_marker)
        if markers is None:
            output.append(line)
            continue
        last, header, footer = markers
        buffer = _group(
            lines,
            first=line,
            last=last,
            header=header,
            footer=footer,
            hint_marker=hint_marker,
            block_marker=block_marker,
        )
        output.extend(buffer)
    if source.endswith("\n"):
        output.append("")
    return "\n".join(output)


def _get_markers(
    line: str, block_marker: str
) -> tuple[str, str | None, str | None] | None:
    if line.endswith(f"{block_marker}homework:replace:on"):
        return (
            f"{block_marker}homework:replace:off",
            f"{block_marker}homework:start",
            f"{block_marker}homework:end",
        )
    if line.endswith(f"{block_marker}homework:delete:on"):
        return f"{block_marker}homework:delete:off", None, None


def _group(
    lines: Iterable[str],
    *,
    first: str,
    last: str,
    header: str | None,
    footer: str | None,
    hint_marker: str,
    block_marker: str,
) -> list[str]:
    indentation = first.split(f"{block_marker}homework")[0]
    buffer = [""]
    if header is not None:
        buffer[0] += indentation + header
    for line in lines:
        if line.endswith(last):
            buffer.append("")
            if footer is not None:
                buffer[-1] += indentation + footer
            return buffer
        if line.lstrip().startswith(hint_marker):
            buffer.append(indentation + line.split(hint_marker)[-1])
    raise ValueError
