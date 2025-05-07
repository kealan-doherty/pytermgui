import pytermgui as ptg
from pytermgui import trans_button


"""
this is my solution for individual issue for project 2 which showcases ten normal buttons then the transparent
button to show the user the difference implemented in trans_button.py under pytermgui folder
"""

hi = trans_button.trans_button("Hello there",5)
container = ptg.Container()
for i in range(10):
    container.lazy_add(ptg.Button("BUTTON"))



container.lazy_add(hi)
window=ptg.Window(container)


with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(window)
