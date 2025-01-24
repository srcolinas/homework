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


def test_lines_with_outline_are_replaced():
    source = """print("implementation of gradient descent")
## homework:replace:on
#.dw =
#.w =
dw = compute_gradients()
w = w - alpha * dw
## homework:replace:off
"""
    output = parser.parse(source)
    assert (
        output
        == """print("implementation of gradient descent")
## homework:start
dw =
w =
## homework:end"""
    )
