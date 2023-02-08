import requests

def get_current_block(next_block = False):
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
    return int(response['result'], 16) if not next_block else int(response['result'], 16) + 1



def search_block_for_wallets(block_number: int, wallets: list):
    """ This will search a particular block for a list of wallets and return a list of ones that do.
    This means these wallets have just confirmed a blockchain purchase and we can search their wallets for the transactions made.

    Args:
        block_number (int): A ethereum block to search.
        wallets (list): A list of wallets to be searched
    """
    pass