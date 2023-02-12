import json
import requests
import pandas as pd
import dearpygui.dearpygui as dpg
import gui_components as components



""" File under construction. Not being used elsewhere atm. """

def get_current_block():
    """ Infura request to get the latest ethereum block number.

    Args:
        next_block (bool, optional): Option to get the next block returned. Defaults to False.

    Returns:
        int: Current block number or block after. 
    """
    url = "https://mainnet.infura.io/v3/45cf63ab61664628a400aca8c1af4b71"
    headers = {'Content-Type': 'application/json'}
    data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'

    response = requests.post(url, headers=headers, data=data)

    response = response.json()
    return response['result']



def fetch_latest_block(save_to_file, parent):
    """ This will search a particular block for a list of wallets and return a list of ones that do.
    This means these wallets have just confirmed a blockchain purchase and we can search their wallets for the transactions made.

    Args:
        block_number (int): A ethereum block to search.
        wallets (list): A list of wallets to be searched
    """

    url = "https://mainnet.infura.io/v3/45cf63ab61664628a400aca8c1af4b71"
    headers = {'Content-Type': 'application/json'}
    data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params": ["latest",false],"id":1}'

    response = requests.post(url, headers=headers, data=data)

    block_data = response.json()['result']

    if save_to_file:
        with open(f"{block_data['number']}.json", "w") as f:
            json.dump(block_data, f)

    if parent:
        dpg.set_value("ethereum-block-input", block_data['number'])
        components.add_block(block_data, parent)
        return
    
    return response


def search_transaction(s, a, u):
    url = "https://mainnet.infura.io/v3/45cf63ab61664628a400aca8c1af4b71"
    headers = {'Content-Type': 'application/json'}
    data = {"jsonrpc":"2.0","method":"eth_getTransactionByHash","params": [s],"id":1}

    response = requests.post(url, headers=headers, json=data)

    transaction = response.json()['result']

    if u:
        components.add_transactions(transaction, u)
        return