import dearpygui.dearpygui as dpg
import gui_components as components
import utils as util


class GUI:

    def __init__(self):
        self.draw_gui()


    def draw_gui(self):
        """ Responsible for drawing main DPG window viewport that will contain every other GUI component. """
        with dpg.window(tag="Primary Window", label="On-Chain Tracker"):
            # Add the navigation bar at the top of the window
            components.add_menu_bar()
            
            # This child window is a staging frame for any output there may be. It can be used to push other components (dearpygui items) to
            # such as the transactions within a ethereum address. 
            dpg.add_child_window(tag="main-frame")


    def push_to_main_frame(self, items):
        util.clear_item_children("main-frame")