
import pytermgui as ptg
from pytermgui import overflow_preventer
"""
this contains the file to showcase group issue one with the overflow container and allow user 
option to test when an overflow occurs or when it doesn't 
"""
user_input = input("Enter 1 to show a proper container or Enter two to show how an overflow is handled:  ")
container = ptg.Container()
if user_input == "1":
    for i in range(10):
        container.lazy_add(ptg.Button("see it works"))

elif user_input == "2":
    for i in range(55):
        container.lazy_add(ptg.Button("see it doesn't work"))


window=ptg.Window(container)

container_height = container.height
window_height = window.height
overflow_preventer.overflow_preventer(container_height, window_height)


with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(window)
