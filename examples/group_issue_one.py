import pytermgui as ptg



def button_press(manager: ptg.WindowManager) -> None:
    modal = container.select(7)



container = ptg.Container()
for i in range(70):
    container.lazy_add(ptg.Button("BUTTON"))
window=ptg.Window(container)
ptg.overflow_preventer(container.height, window.height)
with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(window)
    #if(container.height > window.height):
        #raise ValueError("container size is too big and has overflown Window please reconfigure Container size")





