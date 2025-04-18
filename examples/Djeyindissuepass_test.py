

from pytermgui import Container, Button, terminal
from pytermgui.enums import Overflow


def test_scroll_is_triggered_when_widgets_overflow_terminal():
    """Test that scroll is used when widgets overflow container height."""

    container = Container(overflow=Overflow.SCROLL)
    container.height = 10  # Simulate small visible space

    # Add 40 buttons — clearly more than visible space
    for i in range(40):
        container.lazy_add(Button(f"Item {i+1}"))

    container.get_lines()  # Layout and position widgets

    # Scroll to the last item by selecting it
    container.select(39)

    selected = container.selected

    # Now test: is the selected item in view?
    assert selected is not None, " No widget selected"

    assert container._scroll_offset <= selected.pos[1] < container._scroll_offset + container.height, (
        " Selected item is not visible — container failed to scroll"
    )


