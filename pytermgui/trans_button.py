import sys

import pytermgui as ptg


def trans_button( label: str, hover_color: int) -> ptg.Button:
    os = sys.platform
    if os == 'win32':
        button = ptg.Button(label).set_style("label", "#000000").set_style("highlight", f"@{hover_color}")
        return button
    elif os == 'darwin':
        button = ptg.Button(label).set_style("label", "#000000").set_style("highlight", f"@{hover_color}")
        return button
    elif os == 'linux':
        button = ptg.Button(label).set_style("label", "#000000").set_style("highlight", f"@{hover_color}")
        return button
    elif hover_color < 0 or hover_color > 255:
        raise ValueError("hover_color must be between 0 and 255")
    else:
        raise OSError( "your current OS is not supported for this functionality ")


