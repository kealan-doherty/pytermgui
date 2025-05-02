import pytermgui as ptg
from pytermgui import trans_button


def button_press(manager: ptg.WindowManager) -> None:
    modal = container.select(7)


hi = trans_button.trans_button("Hello there",5)
container = ptg.Container()
for i in range(10):
    container.lazy_add(ptg.Button("BUTTON"))



container.lazy_add(hi)
window=ptg.Window(container)


with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(window)
