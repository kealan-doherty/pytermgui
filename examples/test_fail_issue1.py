from pytermgui import Container, Button, terminal
from pytermgui.enums import Overflow


def test_select_does_not_scroll_if_not_fixed():
    """Simulate the pre-fix behavior: selection doesn't trigger scroll."""

    # Create a tall container and limit its height
    container = Container(overflow=Overflow.SCROLL)
    container.height = 10  # Limit container display height

    # Add 30 buttons (more than visible height)
    for i in range(30):
        container.lazy_add(Button(f"Item {i+1}"))

    container.get_lines()  # Initialize positions

    # Select the last button
    container.select(29)

    # Get the selected widget
    selected_widget = container.selected

    # Fail if the selected widget's position is still outside the visible area
    if selected_widget.pos[1] < container._scroll_offset:
        raise AssertionError("Selected widget is above visible scroll area — container did not scroll")

    elif selected_widget.pos[1] >= container._scroll_offset + container.height:
        raise AssertionError("Selected widget is below visible scroll area — container did not scroll")
