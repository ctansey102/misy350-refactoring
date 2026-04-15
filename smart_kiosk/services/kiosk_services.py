import uuid








def place_order(inventory_items : list, item_id : str, quantity : int):
    #find item 
    item = find_inventory_item_by_item_id(inventory_items, item_id)
    #check the existing inventory for the item.
    if item:
        if item['quantity'] >= quantity:
            orders.append(
                {
                    "order_id": str(uuid.uuid4())
                }
            )
        #if we have enough inventory, then reduce the inventory
        #then place the order

def find_orders_by_item():
    pass

def count_orders_by_item_id():
    pass

def find_inventory_item_by_item_id(inventory_list: list, item_id : str):
    for item in inventory_list:
        if item['id'] == item_id:
            return item
    return None
    

def update_inventory_item():
    pass