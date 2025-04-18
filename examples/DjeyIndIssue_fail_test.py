from pytermgui import Container, Button
from pytermgui.enums import Overflow


def test_scroll_does_not_trigger_when_scroll_is_missing():
    """Simulates the broken behavior before scrolling was fixed."""

    # Container without scrolling
    container = Container(overflow=Overflow.HIDE)
    container.height = 10

    # Add more buttons than can fit on screen
    for i in range(40):
        container.lazy_add(Button(f"Item {i+1}"))

    container.get_lines()

    # Try selecting the last button
    container.select(39)

    selected = container.selected

    # This SHOULD fail — the button is not visible, but no scroll happened
    assert container._scroll_offset <= selected.pos[1] < container._scroll_offset + container.height, (
        "Broken: Selected item is offscreen — container did NOT scroll (expected before-fix behavior)."
    )
