from data import etherscan
from data import infura
import dearpygui.dearpygui as dpg
import utils as util
import dearpygui.demo as demo
import datetime as dt



# TODO: Fix this function
def add_transactions(transaction, parent):

    util.clear_item_children(parent)
    add_transaction_window()
    dpg.set_value("ethereum-transaction-input", transaction["hash"])

    # Parent will pass this child_window to the "Primary Window" tag (main viewport in gui.py)
    with dpg.child_window(parent=parent, autosize_x=True, height=85):
        with dpg.group(horizontal=True):
            dpg.add_text(f"Hash: {transaction['hash']}")
            dpg.add_text(f"Value: {util.wei_to_eth(int(transaction['value'], 16))}")
        dpg.add_button(label=f"From: {transaction['from']}", callback=lambda: etherscan.get_wallet_transactions(transaction['from'], save_to_file=False, parent="output"))
        # TODO: Add callback, to search this address. It should remove children from "parent" param, and fill it with the transactions in "transactions["to"]"
        dpg.add_button(label=f"To: {transaction['to']}", callback=lambda: etherscan.get_wallet_transactions(transaction['to'], save_to_file=False, parent="output"))
    


def add_block(block_data, parent):

    util.clear_item_children(parent)

    def add_block_data(block):
        with dpg.group(horizontal=True, parent=parent):
            dpg.add_text(f"Block: {block['number']}")
            dpg.add_text(f"Timestamp: {dt.datetime.fromtimestamp(int(block['timestamp'], 16))}") # convert to datetime

        dpg.add_text("Transctions:", parent=parent)
        for transaction in block_data['transactions']:
            dpg.add_button(label=f"{transaction}", tag=f"{transaction}", parent=parent, callback=infura.search_transaction, user_data=parent)

    
    add_block_data(block_data)


def add_menu_bar():
    """_summary_
    """
    # ETHEREUM WALLET LOOKUP
    with dpg.menu_bar():
        with dpg.menu(label="Ethereum"):
            dpg.add_menu_item(label="Address Lookup", callback=add_wallet_window)
            dpg.add_menu_item(label="Block Lookup", callback=add_block_window)
            dpg.add_menu_item(label="Transaction Lookup", callback=add_transaction_window)


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
    if dpg.does_alias_exist("main-frame"):
        util.clear_item_children("main-frame")

    with dpg.group(horizontal=True, parent="main-frame"):
        wallet = dpg.add_input_text(label="Ethereum Address")
        dpg.add_button(label="Search", tag="ethereum-address-input", callback=lambda: etherscan.get_wallet_transactions(dpg.get_value(wallet), save_to_file=False, parent="output"))

    dpg.add_child_window(tag="output", parent="main-frame")


def add_block_window():
    """_summary_
    """
    if dpg.does_alias_exist("main-frame"):
        util.clear_item_children("main-frame")

    with dpg.group(horizontal=True, parent="main-frame"):
        block = dpg.add_input_text(label="Ethereum Block")
        dpg.add_button(label="Search", tag="ethereum-block-input", callback=lambda: infura.fetch_latest_block(save_to_file=False, parent="output"))

    dpg.add_child_window(tag="output", parent="main-frame")


def add_transaction_window():
    """_summary_
    """
    if dpg.does_alias_exist("main-frame"):
        util.clear_item_children("main-frame")

    with dpg.group(horizontal=True, parent="main-frame"):
        block = dpg.add_input_text(label="Ethereum Transaction")
        dpg.add_button(label="Search", tag="ethereum-transaction-input", callback=lambda: infura.fetch_latest_block(save_to_file=False, parent="output"))

    dpg.add_child_window(tag="output", parent="main-frame")