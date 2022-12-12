# Question 1
# Python code to Check for 
# balanced parentheses in an expression
open_list = ["[","{","("]
close_list = ["]","}",")"]

# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"
  
  
# Driver code
string = "([[y+t]*(j+9v)*{ww+yy})"
print(string,"-", check(string))

# Question 3
class Students():
    def _init_(self):
        self.size = 100
        self.array = [[] for i in range(self.size)]

    def get_hash(self, key):    # hash function
        h = 0
        for char in key:
            h += ord(char)
        return h% self.size

    def _setitem_(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.array[h]):  # Loop through iteration of array
            if len(element) == 2 and element[0] == key:  # Checks for key collisions using Linear Probing
                self.array[h][index] = (key, value)
                found = True
                break
        if not found:
            self.array[h].append((key, value))

    def _getitem_(self, key):
        h = self.get_hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]


students = Students()
students._setitem_("Paul", 38)
students._setitem_("Ben", 12)
students._setitem_("Chole", 5)
students._setitem_("Bob", 10)
students._setitem_("Alex", 20)
students._setitem_("Jane", 23)
students._setitem_("Den", 45)
students._setitem_("Mike", 90)
students._setitem_("Amos", 25)
students._setitem_("Mag", 47)
    
# Question 4.2
# Python program to demonstrate
# insert operation in binary search tree

# A utility class that represents
# an individual node in a BST


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

# A utility function to insert
# a new node with the given key


def insert(root, key):
	if root is None:
		return Node(key)
	else:
		if root.val == key:
			return root
		elif root.val < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

# A utility function to do inorder tree traversal


def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)


# Driver program to test the above functions
# Let us create the following BST
# 18
# /	 \
# 5	 21
# / \ / \
# 2 10 19 24
#          \
#          128

r = Node(18)
r = insert(r, 5)
r = insert(r, 21)
r = insert(r, 2)
r = insert(r, 10)
r = insert(r, 19)
r = insert(r, 24)
r = insert(r, 128)

# Print inoder traversal of the BST
inorder(r)

# Calculation of the division of the max and min values
def MinNode(self):
    cur = self
    while cur.left:
        cur = cur.left


def MaxNode(self):
    cur = self
    while cur.right:
        cur = cur.right


Div = root.MaxNode() / root.MinNode()
print("The division = ", Div)

# Question 5.1
# Import libraries
from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray

text = "aaaaaaaayyyyyyyuuuuuuuuuuuuukkkkkkkkkkzzzllggggqqqqqxxxxxx"

freq_lib = defaultdict(int)  # generate a default library
for char in text:  # count each letter and record into the frequency library
    freq_lib[char] += 1


# Huffmann Tree
heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]
heapify(heap)

while len(heap) > 1:
    right = heappop(heap)  # Pop and return the smallest item from the heap
    left = heappop(heap)

    for pair in right[1:]:
        pair[1] = '0' + pair[1]   # add zero to all the right note
    for pair in left[1:]:
        pair[1] = '1' + pair[1]   # add one to all the left note
    heappush(heap, [right[0] + left[0]] + right[1:] + left[1:])  # add values onto the heap

huffman_list = right[1:] + left[1:]
huffman_dict = {a[0]:bitarray(str(a[1])) for a in huffman_list}

encoded_text = bitarray()
encoded_text.encode(huffman_dict, text)
print(encoded_text)

padding = 8 - (len(encoded_text) % 8)  # Add padding since data is stored in bytes which contain 8 bits
with open('compressed_file.bin', 'wb') as w:
    encoded_text.tofile(w)  # Save encoded text as binary file


# Decoding
decoded_text = bitarray()

with open('compressed_file.bin', 'rb') as r:
    decoded_text.fromfile(r)

decoded_text = decoded_text[:-padding]  # remove padding

decoded_text = decoded_text.decode(huffman_dict)
decoded_text = ''.join(decoded_text)

print(decoded_text)

# Question 5.2
import math
import sys
global probabilities
probabilities = []


class HuffmanCode:
    def _init_(self, probability):
        self.probability = probability

    def position(self, value, index):
        for j in range(len(self.probability)):
            if value >= self.probability[j]:
                return j
        return index-1

    def characteristics_huffman_code(self, code):
        length_of_code = [len(k) for k in code]

        mean_length = sum([a*b for a, b in zip(length_of_code, self.probability)])

        print("Average length of the code: %f" % mean_length)

# Question 5.3
# characters from the huffman tree
chars = ['a', 'y', 'u', 'k', 'z', 'l', 'g', 'x']

# frequency of characters
freq = [8, 7, 13, 11, 3, 2, 9 , 6]

# list containing the unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for i in range(len(chars)):
    nodes.append(node(freq[i], chars[i]))

code_length = len(nodes)
print("The code length is: ", code_length)