import pytermgui as ptg
from pytermgui import ansi_interface, tim
from pytermgui import markup


def split_style(_: int, item: str, template: str) -> str:
    if "<SPLIT>" not in item:
        return item

    first, second = item.split("<SPLIT>")
    return tim.parse(template.format(first=first, second=second))

colors_list = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'black']

new_color_list = []
for i in range(len(colors_list)):
    match colors_list[i]:
        case 'red':
            colors_list[i] = "[@red][green][inverse]"
        case 'green':
            colors_list[i] = "[@green][red][inverse]green"
        case 'blue':
            colors_list[i] = "[@blue][orange][inverse]blue"
        case 'orange':
            colors_list[i] = "[@orange][blue][inverse]orange"
        case 'yellow':
            colors_list[i] = "[@yellow][purple][inverse]yellow"
        case 'purple':
            colors_list[i] = "[@purple][yellow][inverse]purple"
        case 'magenta':
            colors_list[i] = "[@magenta][green][inverse]magenta"
        case 'cyan':
            colors_list[i] = "[@cyan][red][inverse]cyan"
        case 'white':
            colors_list[i] = "[@white][black][inverse]white"
        case 'black':
            colors_list[i] = "[@black][white][inverse]black"
    print(colors_list[i])






window = ptg.Window()
"""
for color in colors_list:
    label = ptg.Label("red", "blue inverse")
    window.__add__(label )
"""
template = "[@red]green [@green]red"

ptg.Button.styles.label = split_style
ptg.Button.set_char("delimiter", [""] * 2 )
my_Button = ptg.Button("red").set_style("label", template)

window.__add__(my_Button)
with ptg.WindowManager() as manager:
    manager.layout.add_slot("Body")
    manager.add(
        window
    )

