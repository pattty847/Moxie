from data import etherscan
import dearpygui.dearpygui as dpg
import utils as util
import dearpygui.demo as demo

""" This file impliments all GUI components that may appear on the main_menu. """


def draw_transactions(wallets, parent):
    util.clear_item_children(parent)

    def add_transaction(transaction):
        with dpg.child_window(parent=parent, autosize_x=True, no_scrollbar=True):
            with dpg.group(horizontal=True):
                dpg.add_text(f"Timestamp: {transaction['timeStamp']}") # convert to datetime
                dpg.add_text(f"Block: {transaction['blockNumber']}")
                dpg.add_text(f"Value: {util.wei_to_eth(transaction['value'])}")
            dpg.add_text(f"From: {transaction['from']}")
            dpg.add_text(f"To: {transaction['to']}")
    
    for wallet in wallets:
        for transaction in wallet.transactions:
            add_transaction(transaction)


def add_menu_bar():
    with dpg.menu_bar():
        with dpg.menu(label="Wallets"):
            dpg.add_menu_item(label="Transactions", callback=add_wallet_window)

        add_tools_menu()


def add_tools_menu():
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
    if not dpg.does_alias_exist("output"):
        with dpg.group(horizontal=True, parent="main-frame"):
            wallet = dpg.add_input_text(label="Address")
            dpg.add_button(label="Search", callback=lambda: etherscan.get_wallet_transactions(dpg.get_value(wallet), save_to_file=False, parent="output"))

        dpg.add_child_window(tag="output", parent="main-frame")