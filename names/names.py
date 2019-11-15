import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        # >= go right
        if value < self.value:
            if not self.left:
                # valye less than least, instantiate as child
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                # value greater than max, instantiate as child
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # first compare key with the root, if key is present return root. if key is greater than root's key, recur right subtree of root node, otherwise recur for left subtree
        if self.value == target:
            return True
        
        if target < self.value:
            if not self.left:
                return False
                # recur for right subtree
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
                # recur for left subtree
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you can go right no further
        if not self.right:
            # get current value if no child on right
            return self.value
        else:
            # recur there if child on right
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # visit every not exactly one time each
        # go left until you can't anymore, then go back and go right
        # recursive
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        return cb(self.value)

duplicates = []
binary_search = BinarySearchTree(names_1[0])

for name1 in names_1:
    binary_search.insert(name1)

for name2 in names_2:
    if binary_search.contains(name2):
        duplicates.append(name2)

# original O(n2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")