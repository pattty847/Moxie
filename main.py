import dearpygui.dearpygui as dpg
import utils as util
import main_menu

# ==================================== DPG & VIEWPORT SETUP ====================================
dpg.create_context()

# Draw main gui
main_menu.draw_gui()

# Primary Monitor info
monitor, x, y, width, height = util.monitors() 

# Viewport size vars
width_ = 1200
height_ = 700

dpg.create_viewport(
    title='Custom Title', 
    x_pos=x+int(width/2-(width_/2)),    # Center window's x_pos
    y_pos=y+int(height/2-(height_/2)),  # Center window's y_pos
    width=width_, height=height_
)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
# ==================================== DPG & VIEWPORT SETUP ====================================


# Random Test Bitcoin Wallet
# 34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo