from blockchain import BlockChain
from heapify import Heapify, HeapType
from sorting import Sorting
from matrix import Matrix
from binary_search_tree import BinarySearchTree, TreeTraversalType

# ------------------BST----------------------------#

# tree = BinarySearchTree()
# tree.insert_node(5)
# tree.insert_node(3)
# tree.insert_node(6)
# tree.insert_node(4)
# tree.insert_node(9)
# tree.insert_node(1)
# tree.print_tree(tree.root, TreeTraversalType.ReverseInorder)
# print(tree.array_of_tree)

# -----------------Matrix------------------------#

m = Matrix(3, 4)
m.create_matrix()
print(m.grid)

# -----------------QuickSort------------------------#

# elements = [40, 8, 17, 12, 55, 19, 6, 37]
# sort = Sorting(elements)
# sort.quicksort(0, len(elements) - 1)
# print(sort.arr)

# ----------------Heapify---------------------------#

# heap = Heapify()
# elements = [10, 50, 20, 30, 15]
# print(elements[2: len(elements)])
# for element in elements:
#     heap.do_heapify(element, HeapType.min)
# print(heap.arr)

# -----------------BlockChain Sample---------------#

# bc = BlockChain()
# bc.add_block("Achin gave $100 to Ram")
# block_id = bc.add_block("Ram gave $100 to Raju")
# bc.add_block("raju gave $10 to Sanju")
# print(bc.blockchain)
# bc.update_blockchain(block_id, "Ram gave $150 to Raju")
# print(bc.blockchain)
# print(bc.proof_of_work())
