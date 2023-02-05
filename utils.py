import time
from screeninfo import get_monitors
import dearpygui.dearpygui as dpg


def monitors():
    monitors = [s for s in get_monitors()]
    for monitor in monitors:
        if monitor.is_primary:
            return monitor, monitor.x, monitor.y, monitor.width, monitor.height
            

def rate_limit(wait_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            results = func(*args, **kwargs)
            end_time = time.time()

            if end_time - start_time < wait_time:
                time.sleep(wait_time - (end_time - start_time))
            
            return results
        return wrapper
    return decorator


def wei_to_eth(wei):
    # 1 ETH = 10^18 WEI
    return int(wei) / 10**18


def eth_to_wei(eth):
    # 1 ETH = 10^18 WEI
    return int(eth * 10**18)


def clear_item_children(item):
    dpg.delete_item(item, children_only=True)