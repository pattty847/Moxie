import json
import dearpygui.dearpygui as dpg
import requests
import utils
import gui_components as gui



@utils.rate_limit(0.2)
def get_wallet_transactions(address, save_to_file: bool, parent: str):
    """ This function retrieves the transactions of an Ethereum wallet.

    Args:
        address (str): Ethereum address to search for transactions. 
        save_to_file (bool): A flag indicating whether the transactions should be saved to a json file.

    Returns:
        list of dict or None: If the response was successful we return the transactions as a list of dictionary objects, or None. 
    """


    # Ethereum blockchain explorer API endpoint
    endpoint = "https://api.etherscan.io/api?module=account&action=txlist&address=" + address + "&sort=desc"
    
    # Make a request to the Ethereum blockchain explorer API
    response = requests.get(endpoint)
    
    # Parse the JSON response data
    data = response.json()
    
    # Check if the response was successful
    if data['status'] == "1":
        transactions = data['result'][0:100]

        if save_to_file:
            with open(f"{address}.json", "w") as f:
                json.dump(transactions, f)
                return
        
        if parent:
            gui.draw_transactions(transactions, parent)
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


def get_next_block():
    endpoint = "https://api.etherscan.io/api?module=block&action=getblockcountdown&blockno=16564000"

    # Make a request to the Ethereum blockchain explorer API
    response = requests.get(endpoint)
    
    # Parse the JSON response data
    data = response.json()
    
    return data


print(get_next_block())