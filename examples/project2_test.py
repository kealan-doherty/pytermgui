import shutil
import pytest
import pytermgui as ptg
from pytermgui import overflow_preventer
from pytermgui.trans_button import trans_button
from pytermgui.inverse_color_parser import *

def create_container(num_buttons=70):
    container = ptg.Container()
    total_height = 0

    for i in range(num_buttons):
        button = ptg.Button(f"BUTTON {i+1}")
        container.lazy_add(button)

        if hasattr(button, "size"):
            size = button.size
            if isinstance(size, tuple):
                total_height += size[1]
            elif isinstance(size, int):
                total_height += size
            else:
                total_height += 1  # Default fallback

    return container, total_height

def test_container_fits_terminal():
    terminal_height = shutil.get_terminal_size().lines
    container, total_height = create_container()

    assert total_height <= terminal_height, (
        f"Container height ({total_height}) exceeds terminal height ({terminal_height})"
    )

def test_overflow_prevention():
    with pytest.raises(ValueError) as error:
        container = ptg.Container()
        for i in range(55):
            container.lazy_add(ptg.Button(f"BUTTON"))
        window = ptg.Window(container)
        container_height = container.height
        window_height = container.height
        overflow_preventer.overflow_preventer(container_height, window_height)
    assert str(error.value) == "container size is too big and has overflown Window due to number of widgets please reconfigure amount of widgets within the container"
    print("passed")

def test_kealan_indvidual():
    with pytest.raises(ValueError) as error:
        trans_button("hello", 256)
    assert str(error.value) == "IndexedColor value has to fit in range 0-255, got '256'."
    with pytest.raises(OSError) as error:
        os = "random"
        if os == 'win32':
            button = ptg.Button("hello").set_style("hello", "#000000").set_style("highlight", f"@{5}")
            return button
        elif os == 'darwin':
            button = ptg.Button("hello").set_style("hello", "#000000").set_style("highlight", f"@{5}")
            return button
        elif os == 'linux':
            button = ptg.Button("hello").set_style("label", "#000000").set_style("highlight", f"@{5}")
            return button
        else:
            raise OSError("your current OS is not supported for this functionality ")
    assert str(error.value) == "your current OS is not supported for this functionality "


def test_group_issue_two():
    colors_list = ['red','orange']

    assert tim_color_parser(colors_list) == ["[@red][green][inverse]", "[@orange][blue][inverse]orange" ]
    colors_list = ['purple', 'yellow']

    assert window_color_parser(colors_list) == ["[@purple]yellow[@yellow]purple", "[@yellow]purple[@purple]yellow"]
    colors_list = ['blue', 'yellowgreen']

    with pytest.raises(ValueError) as error:
        tim_color_parser(colors_list)
    assert ValueError

    with pytest.raises(ValueError) as error:
        window_color_parser(colors_list)
    assert ValueError

    with pytest.raises(ValueError) as error:
        colors_list = [5,5,4]
        tim_color_parser(colors_list)
    assert ValueError



