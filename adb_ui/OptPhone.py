#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from dearpygui.core import *
from dearpygui.simple import *

#add_additional_font('三极中柔宋.ttf', 18, glyph_ranges='chinese_simplified_common')

def print_me(sender, data):
    log_debug(f"菜单项: {sender}")

#show_logger()

with window("Tutorial"):
    with menu_bar("Main Menu Bar"):
        with menu("file"):
            add_menu_item("save", callback=print_me)
            add_menu_item("save other", callback=print_me)

            with menu("seting"):
                add_menu_item("seting 1", callback=print_me)
                add_menu_item("seting 2", callback=print_me)

        add_menu_item("help", callback=print_me)

        with menu("contor"):
            add_checkbox("sel", callback=print_me)
            add_button("click", callback=print_me)
            add_color_picker4("color", callback=print_me)

start_dearpygui()
