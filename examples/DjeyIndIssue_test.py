import pytermgui as ptg
import shutil

# Get terminal height
terminal_height = shutil.get_terminal_size().lines
print("Terminal height:", terminal_height)

# Create a scrollable container and set height smaller than terminal
container = ptg.Container(overflow=ptg.Overflow.SCROLL)
container.height = terminal_height - 5  # Force scrolling

# Add all buttons with the same dark blue color
for i in range(35):
    label = "[bold 18]Button {}".format(i + 1)
    container.lazy_add(ptg.Button(label))

# Debug print
container_height = len(container._widgets)
print("Container widget count:", container_height)

# Wrap in a window
window = ptg.Window(container, box="DOUBLE")

try:
    with ptg.WindowManager() as manager:
        manager.layout.add_slot("Body")
        manager.add(window)
except Exception as e:
    print("Exception occurred:", e)
