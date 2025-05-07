import shutil
import pytest
import pytermgui as ptg

def create_test_container(num_buttons=18):
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
    container, total_height = create_test_container()

    assert total_height <= terminal_height, (
        f"Container height ({total_height}) exceeds terminal height ({terminal_height})"
    )


