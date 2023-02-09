from data import etherscan
import dearpygui.dearpygui as dpg
import utils as util
import dearpygui.demo as demo
import datetime as dt

""" This file impliments all GUI components that may appear on the main_menu. """
# TODO: Add documentation for all these functions.

# TODO: Fix this function
def add_transactions(transactions, parent):
    """_summary_

    Args:
        wallets (_type_): _description_
        parent (_type_): _description_
    """
    util.clear_item_children(parent)

    # Function within draw_transaction to add each transaction window to the primary viewport window
    def add_transaction(transaction):
        # Parent will pass this child_window to the "Primary Window" tag (main viewport in gui.py)
        with dpg.child_window(parent=parent, autosize_x=True, height=85):
            with dpg.group(horizontal=True):
                dpg.add_text(f"Timestamp: {dt.datetime.fromtimestamp(int(transaction['timeStamp']))}") # convert to datetime
                dpg.add_text(f"Block: {transaction['blockNumber']}")
                dpg.add_text(f"Value: {util.wei_to_eth(transaction['value'])}")
            dpg.add_button(label=f"From: {transaction['from']}", enabled=False)
            # TODO: Add callback, to search this address. It should remove children from "parent" param, and fill it with the transactions in "transactions["to"]"
            dpg.add_button(label=f"To: {transaction['to']}")
    
    # For every transaction push a child window containing its information
    for transaction in transactions:
        add_transaction(transaction)


def add_menu_bar():
    """_summary_
    """
    # ETHEREUM WALLET LOOKUP
    with dpg.menu_bar():
        with dpg.menu(label="Ethereum"):
            dpg.add_menu_item(label="Address Lookup", callback=add_wallet_window)



        # DEARPYGUI DEBUGGING TOOL MENU
        with dpg.menu(label="Tools"):
            dpg.add_menu_item(label="Demo", callback=lambda: demo.show_demo())
            dpg.add_menu_item(label="Show About", callback=lambda:dpg.show_tool(dpg.mvTool_About))
            dpg.add_menu_item(label="Show Metrics", callback=lambda:dpg.show_tool(dpg.mvTool_Metrics))
            dpg.add_menu_item(label="Show Documentation", callback=lambda:dpg.show_tool(dpg.mvTool_Doc))
            dpg.add_menu_item(label="Show Debug", callback=lambda:dpg.show_tool(dpg.mvTool_Debug))
            dpg.add_menu_item(label="Show Style Editor", callback=lambda:dpg.show_tool(dpg.mvTool_Style))
            dpg.add_menu_item(label="Show Font Manager", callback=lambda:dpg.show_tool(dpg.mvTool_Font))
            dpg.add_menu_item(label="Show Item Registry", callback=lambda:dpg.show_tool(dpg.mvTool_ItemRegistry))


def add_wallet_window():
    """_summary_
    """
    if not dpg.does_alias_exist("output"):
        with dpg.group(horizontal=True, parent="main-frame"):
            wallet = dpg.add_input_text(label="Address")
            dpg.add_button(label="Search", callback=lambda: etherscan.get_wallet_transactions(dpg.get_value(wallet), save_to_file=False, parent="output"))

        dpg.add_child_window(tag="output", parent="main-frame")