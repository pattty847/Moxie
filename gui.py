import dearpygui.dearpygui as dpg
import gui_components as components

def draw_gui():
    """ Responsible for drawing main window within viewport which contains every thing else. """
    with dpg.window(tag="Primary Window", label="On-Chain Tracker"):
        # DearPyGUI Demo
        components.add_menu_bar()
        components.add_tab_menu()
        
        with dpg.child_window(tag="main-frame"):
            pass
            # add_wallet_section()