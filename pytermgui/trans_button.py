import sys

import pytermgui as ptg


def trans_button( label: str, hover_color: int) -> ptg.Button:

    if sys.platform == 'win32':
        button = ptg.Button(label).set_style("label", "#000000").set_style("highlight", f"@{hover_color}")
        return button
    elif sys.platform == 'darwin':
        button = ptg.Button(label).set_style("label", "#000000").set_style("highlight", f"@{hover_color}")
        return button
    elif sys.platform == 'linux':
        button = ptg.Button(label).set_style("label", "#000000").set_style("highlight", f"@{hover_color}")
        return button
    else:
        raise OSError( "your current OS is not supported for this functionality ")


