import pytermgui as ptg
from pytermgui import ansi_interface, tim
from pytermgui import markup


def split_style(_: int, item: str, template: str) -> str:
    if "<SPLIT>" not in item:
        return item

    first, second = item.split("<SPLIT>")
    return tim.parse(template.format(first=first, second=second))


def tim_color_parser(colors_list: list[str]) ->list[str]:
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
            case _:
                raise ValueError(f"Invalid color: {colors_list[i]} is not supported")
    return colors_list


def window_color_parser(colors_list: list[str]) ->list[str]:
    for i in range(len(colors_list)):
        match colors_list[i]:
            case 'red':
                colors_list[i] = "[@red]green[@green]red"
            case 'green':
                colors_list[i] = "[@green]red[@red]green"
            case 'blue':
                colors_list[i] = "[@blue]orange[@orange]blue"
            case 'orange':
                colors_list[i] = "[@orange]blue[@blue]orange"
            case 'yellow':
                colors_list[i] = "[@yellow]purple[@purple]yellow"
            case 'purple':
                colors_list[i] = "[@purple]yellow[@yellow]purple"
            case 'magenta':
                colors_list[i] = "[@magenta]green[@green]magenta"
            case 'cyan':
                colors_list[i] = "[@cyan]red[@red]cyan"
            case 'white':
                colors_list[i] = "[@white]black[@black]white"
            case 'black':
                colors_list[i] = "[@black]white[@white]black"
            case _:
                raise ValueError(F"color {colors_list[i]} is not supported")
    return colors_list