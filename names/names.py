import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        new_node = BSTNode(value)

        if value < self.value:
            if self.left is None:
                self.left = new_node
            else:
                self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = new_node
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True

        elif self.value > target:
            if self.left is None:
                return False
            else:
                found = self.left.contains(target)

        elif self.value < target:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    def get_max(self):
        current = self

        while(current.right is not None):
            current = current.right
        return current.value

    def for_each(self, fn):
        if(self.left):
            self.left.for_each(fn)
        fn(self.value)
        if(self.right):
            self.right.for_each(fn)

duplicates = []  # Return the list of duplicates in this data structure


tree = None

# Replace the nested for loops below with your improvements
for name in names_1:
    if tree is None:
        tree = BSTNode(name)
        tree.insert(name)

for name in names_2:
    if tree.contains(name):
        duplicates.append(name)
        
        
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.