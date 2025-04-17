#!/bin/python
import pytermgui as gui

with gui.WindowManager() as manager:
    manager.layout.add_slot("body")
    manager.add(
        gui.Window(
            gui.Container(
                "Test Container",
                gui.InputField("Waku waku", multiline=True, width=30),
                overflow=gui.Overflow.SCROLL,
                width=40,
                height=10,
            )
        )
    )
