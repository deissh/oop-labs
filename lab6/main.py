from time import sleep

import dearpygui.dearpygui as dpg
import random


def on_btn_click_regenerate(tag_name: str):
    def callback():
        dpg.set_item_label(tag_name, f'{random.randint(1, 10)}')

    return callback


def on_btn_click(tag_name: str):
    def callback():
        for i in range(11):
            el = f'btn__{i}'
            dpg.set_item_callback(el, on_btn_click_regenerate(tag_name))

        anim(tag_name)

    return callback


def anim(tag_name: str):
    for _ in range(3):
        h = dpg.get_item_height(tag_name)
        for i in range(10):
            sleep(.2)
            dpg.set_item_height(tag_name, h + i * 10)

        h = dpg.get_item_height(tag_name)
        for i in range(10):
            sleep(.2)
            dpg.set_item_height(tag_name, h - i * 10)


def window_content():
    dpg.add_spacing(count=6)

    with dpg.group(horizontal=True):
        for i in range(11):
            tag_name = f'btn__{i}'
            dpg.add_button(label=f'{i}', id=tag_name, callback=on_btn_click(tag_name))


with dpg.window(autosize=True, no_close=True, no_title_bar=True):
    window_content()


dpg.start_dearpygui()
