'''
Code used fir the 'create an array' class.

Array type classMethods:
    1.Length
    2.String representation
    3.Membership
    4.Index
    5.Replacement
'''

class Array(object):
    'represents an array'
    def __init__(self, capacity, fill_value = None):
        """
        Args:
            capacity (int): static size of the array.
            fill_value (any, optional): value at each position. Defaults to None.
        """
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        'returns capacity of the array'
        return len(self.items)

    def __str__(self):
        'returns a string representation of the array'
        return str(self.items)

    def __iter__(self):
        'supports traversal with a for loop'
        return iter(self.items)

    def __getitem__(self, index):
        'subscript operator for access at index'
        return self.items[index]

    def __setitem__(self, index, new_item):
        'subscript operator for replacement at index'
        self.items[index] = new_item


"""
Code used in the shell to create an array
instance and methods.
"""















