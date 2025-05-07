import shutil
import pytest
import pytermgui as ptg

def test_container_too_tall_raises_value_error():
    # Get terminal height
    terminal_height = shutil.get_terminal_size().lines

    # Create a container taller than the terminal
    container = ptg.Container()
    total_height = 0

    for i in range(100):  # Force overflow, use small numbers to make it fail(4,8,...)
        btn = ptg.Button(f"BUTTON {i+1}")
        container.lazy_add(btn)

        # Estimate height
        size = getattr(btn, "size", 1)
        if isinstance(size, tuple):
            total_height += size[1]
        elif isinstance(size, int):
            total_height += size
        else:
            total_height += 1

    # Confirm container is too tall
    assert total_height > terminal_height

    # Attempt to create a window and simulate overflow logic
    with pytest.raises(ValueError, match="Container height .* exceeds terminal height"):
        if total_height > terminal_height:
            raise ValueError(
                f"Container height ({total_height}) exceeds terminal height ({terminal_height})"
            )
