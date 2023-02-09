import dearpygui.dearpygui as dpg
import gui_components as components

def draw_gui():
    """ Responsible for drawing main window within viewport that will contains every other GUI component. """
    with dpg.window(tag="Primary Window", label="On-Chain Tracker"):
        # DearPyGUI Demo
        components.add_menu_bar()
        
        # This child window is a staging frame for any output there may be. It can be used to push other components (dearpygui items) to
        # such as the transactions within a ethereum address. 
        dpg.add_child_window(tag="main-frame")