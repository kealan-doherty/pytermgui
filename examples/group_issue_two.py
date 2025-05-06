import pytermgui as ptg
from pytermgui import ansi_interface, tim
from pytermgui import inverse_color_parser
colors_list = ['red', 'greenyellow', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black']

user_input = input("to see terminal inline markup format enter 1 for gui window version press 2: ")

if user_input == '1':
    inverse_color_parser.tim_color_parser(colors_list)
    for color in colors_list:
        tim.print(color)
elif user_input == '2':
    inverse_color_parser.window_color_parser(colors_list)
    window = ptg.Window()
    for color in colors_list:

        ptg.Button.set_char("delimiter", [""] * 2 )
        my_Button = ptg.Button(color).set_style("label", color).set_style("highlight", color)

        window.__add__(my_Button)
    with ptg.WindowManager() as manager:
        manager.layout.add_slot("Body")
        manager.add(
            window
        )

