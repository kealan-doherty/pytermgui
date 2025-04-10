import pytermgui as ptg
import time

# Define a dynamic time macro
def macro_time(fmt: str) -> str:
    return time.strftime(fmt)

ptg.tim.define("!time", macro_time)

# Customize the selection style
ptg.styles.define("highlight", "on #008080")  # Teal background for selection

# Create a window manager
with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")

    # Create a container with selectable buttons
    container = ptg.Container(
        ptg.Button("ONE"),
        ptg.Button("TWO"),
        ptg.Button("THREE"),
        ptg.Button("FOUR"),
        ptg.Button("FIVE"),
        ptg.Collapsible("drop",
            ptg.Button("Six"),
            ptg.Button("Seven"),
            *[ptg.Button(f"Button {i}") for i in range(8, 30)]
        )
    )

    # Apply the custom highlight style to the buttons
    for widget in container:
        if isinstance(widget, ptg.Button):
            widget.styles.highlight = ptg.styles.get("highlight")

    #Create a window and add the container
    window = ptg.Window(container, box="DOUBLE")
    manager.add(window)
