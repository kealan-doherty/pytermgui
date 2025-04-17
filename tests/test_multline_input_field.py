import pytest
from pytermgui.widgets.containers import Container
from pytermgui.widgets.input_field import InputField
from pytermgui.enums import Overflow

def test_container_initialization():
    """Test that a Container initializes correctly with widgets."""
    input_field = InputField("Test Input", multiline=True, width=20)
    container = Container(input_field, width=30, height=10, overflow=Overflow.SCROLL)

    assert container.width == 30
    assert container.height == 10
    assert len(container) == 1
    assert container.overflow == Overflow.SCROLL

def test_input_field_initialization():
    """Test that an InputField initializes correctly."""
    input_field = InputField("Hello, world!", multiline=False, width=20)

    assert input_field.value == "Hello, world!"
    assert input_field.width == 20
    assert not input_field.multiline

def test_container_overflow_handling():
    """Test that a Container handles overflow correctly."""
    input_field = InputField("Line 1\nLine 2\nLine 3", multiline=True, width=20)
    container = Container(input_field, width=30, height=2, overflow=Overflow.SCROLL)

    lines = container.get_lines()
    assert len(lines) == 2  # Should only show 2 lines due to height limit

def test_input_field_text_insertion():
    """Test that text can be inserted into an InputField."""
    input_field = InputField("Hello", width=20)
    input_field.insert_text(", world!")

    assert input_field.value == "Hello, world!"

def test_input_field_cursor_movement():
    """Test cursor movement in an InputField."""
    input_field = InputField("Hello", width=20)
    input_field.move_cursor((0, -2))  # Move cursor 2 steps left

    assert input_field.cursor.col == 3

def test_container_widget_addition():
    """Test adding widgets to a Container."""
    container = Container(width=30, height=10)
    input_field = InputField("Test", width=20)

    container += input_field
    assert input_field in container
    assert len(container) == 1
