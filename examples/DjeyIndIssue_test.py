import pytermgui as ptg

container = ptg.Container(overflow=ptg.Overflow.SCROLL)

# Add more widgets than the terminal can show
for i in range(50):
    container.lazy_add(ptg.Button(f"Button {i+1}"))

# Set window height smaller than the terminal
window = ptg.Window(container, box="DOUBLE")
window.height = ptg.terminal.height - 5

with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(window)

