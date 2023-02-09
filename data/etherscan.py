import json
import dearpygui.dearpygui as dpg
import requests
import utils
import gui_components as components
from data import infura

def get_eth_wallets():
    """ Read in the list of Ethereum wallet addresses.

    Returns:
        list: list of wallet addresses
    """
    with open('wallets/eth_wallets.json') as f:
        return json.load(f)

@utils.rate_limit(0.2)
def get_wallet_transactions(address, save_to_file: bool, parent: str):
    """ This function retrieves the transactions of an Ethereum wallet using the EtherScan.io API.

    Args:
        address (str): Ethereum address that's included in request query address. 
        save_to_file (bool): A flag indicating whether the transactions should be saved to a json file.

    Returns:
        list of dict or None: If the response was successful we return the transactions as a list of dictionary objects, or None. 
    """


    # Ethereum blockchain explorer API endpoint
    endpoint = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&sort=desc"
    
    # Make a request to the Ethereum blockchain explorer APIc
    response = requests.get(endpoint)
    
    # Parse the JSON response data
    data = response.json()
    
    # Check if the response was successful
    if data['status'] == "1":
        transactions = data['result'][0:100]

        if save_to_file:
            with open(f"{address}-transactions.json", "w") as f:
                json.dump(transactions, f)
                return
        
        if parent:
            components.add_transactions(transactions, parent)
            return

        return transactions
    else:
        return None


# Applies a rate limit to this function of 5/sec
@utils.rate_limit(0.2)
def get_eth_balance(address):
    """ This function retrieves the balance of an Ethereum wallet in WEI.

    Args:
        address (str): Ethereum address to search for a balance.

    Returns:
        int: Balance in WEI.
    """


    # Ethereum blockchain explorer API endpoint
    endpoint = "https://api.etherscan.io/api?module=account&action=balance&address=" + address + "&tag=latest"
    
    # Make a request to the Ethereum blockchain explorer API
    response = requests.get(endpoint)
    
    # Parse the JSON response data
    data = response.json()
    
    # Check if the response was successful
    if data['status'] == "1":
        balance = data['result']

        return balance
    else:
        return None