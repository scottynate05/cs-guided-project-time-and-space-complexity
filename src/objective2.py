# Constant Time O(1)
# Only checking item @ index [0], does not care what the length of items is.
def print_one_item(items):
    print(items[0]) # O(1)

def print_one_item_twice(items): # O(1) + O(1) = O(2) => O(1)
    print(items[0]) # O(1)
    print(items[0]) # O(1)


# Linear Time o(n)
# Every NESTED loop adds?
def print_all_items(items): # O(1) * O(n) => O(1 * n) = O(n)
    for item in items: # O(n)
        print(item) # O(1)

def print_all_items_twice(items): # O(1) * O(n) + O(1) * O(n) => O(2 * 2 * n) => O(n) * O(2) => O(n)
    for item in items: # O(n)
        print(item) # O(1)
    for item in items: # O(n)
        print(item) # O(1)


# Quadratic Time O(n^2)

def print_all_items_twice2(items): # O(n^2) <= ?
    for item in items: # O(n)
        print(item) # O(1)
        for item in items: # O(n)
            print(item) # O(1)


# What about constants?
# If not NESTED it's always O(n) <= ?
def do_a_bunch_of_stuff(items): # O(0.5 * n) + O(2007.5) => O(n) + O(1) => O(n)
    last_idx = len(items) - 1 # O(1)
    print (items[lastidx]) # Get the item at an idex of a list O(1) Print the result of that O(1)

    middle_idx = len(items) / 2 # O(1)
    idx = 0 # O(1)
    while idx < middle_idx: # O(0.5 * n)
        print(items[idx]) # Get the item at an idex of a list O(1) Print the result of that O(1)
        idx = idx + 1 # O(1)

    for num in range(2000): # O(2000) => O(1)
        print(num) # O(1)


# Most significant term
def do_different_things(items):
    for item in items: # O(n)
        print(items)

    for item_one in items: # O()
        for item_two in items:
            print(item_one, item_two)


# Big O is the worst case
def search_for_thing(items, thing): # O(n)
    for item in items:
        if item == thing:
            return True
    
    return False