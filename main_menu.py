import dearpygui.dearpygui as dpg
import gui_components as gui

def draw_gui():
    """ Responsible for drawing main window within viewport which contains every thing else. """
    with dpg.window(tag="Primary Window", label="On-Chain Tracker"):
        # DearPyGUI Demo
        gui.add_menu_bar()
        
        with dpg.child_window(tag="main-frame"):
            pass
            # add_wallet_section()