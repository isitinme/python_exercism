"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        v = current_cart.get(item)
        if v is not None:
            current_cart[item] = v + 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    cart = dict()
    for note in notes:
        cart.setdefault(note, 1)
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for key, value in recipe_updates:
        ideas[key] = value
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fullfilment_dict = dict()
    res = dict()

    for key, value in aisle_mapping.items():
        if cart.get(key) is not None:
            fullfilment = [cart[key]] + value
            fullfilment_dict[key] = fullfilment

    for item in reversed(sorted(fullfilment_dict.keys())):
        res[item] = fullfilment_dict[item]

    return res

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key, value in fulfillment_cart.items():
        if store_inventory.get(key) is not None:
            store_fulfillment = store_inventory[key]
            amount = max(0, store_fulfillment[0] - value[0])
            new_value = amount if amount > 0 else 'Out of Stock'
            store_inventory[key] = [new_value] + value[1:]
    return store_inventory