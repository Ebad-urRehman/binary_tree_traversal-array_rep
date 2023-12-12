import numpy as np

class Node:
    def __init__(self, data):
        self.node_data = data
        self.left = None
        self.right = None
        self.root = None

class binary_tree:
    def __init__(self):
        self.my_list = []

    def print_preorder_traversal(self):
        temp_stack = []
        root = self.root
        while root is not None:
            print(root.node_data)
            if root.right is not None:
                temp_stack.append(root.right)
            if root.left is not None:
                root = root.left
            else:
                back_trav = temp_stack.pop()
                root = back_trav

    def inorder_myalgo(self):
        temp_stack = []
        root = self.root
        while root is not None:
            if root.left is not None:
                temp_stack.append(root)
                root = root.left
            else:
                print(root.node_data, end=", ")
                if root.right is not None:
                    temp_stack.append(root.right)
                poped_ele = temp_stack.pop()
                print(poped_ele.node_data, end=", ")
                if poped_ele.right is not None:
                    root = poped_ele.right
                else:
                    if len(temp_stack) >= 1:
                        poped_ele = temp_stack.pop()
                        root = poped_ele
                    else:
                        root = None

    def print_postorder_alg_rem(self):
        # this list will later converted into a stack
        root = self.root
        keys_stack = []
        dict = {}
        while True:
            while root is not None:
                # storing root value in stack
                # stack to keep track of all values
                keys_stack.insert(0, root.node_data)

                # dictionary to find address of coresponding value
                dict[root.node_data] = root

                if root.right is not None:
                    negative_flag = -root.right.node_data
                    # appending right nodedata to temp_stack with -ive sign
                    keys_stack.insert(0, negative_flag)
                    dict[negative_flag] = root.right
                root = root.left

            for i in range(len(keys_stack)):
                if keys_stack[0] >= 0:
                    print(keys_stack[0])
                    # deleting poped values
                    del dict[keys_stack[0]]
                    keys_stack.pop(0)
                else:
                    right_node = dict[keys_stack[0]]
                    root = right_node
                    # deleting poped values
                    del dict[keys_stack[0]]
                    keys_stack.pop(0)
                    break
    def is_instance_node(self, address):
        return isinstance(address, Node)

    def take_input_lvl_wise(self):
        total_levels = int(input("Enter total levels of complete binary tree"))
        total_nodes = (2 ** total_levels) - 1
        print(f"Total Nodes : {total_nodes}")
        my_queue = []
        root_data = int(input("Enter data for root Node"))
        root = Node(root_data)
        self.root = root
        my_queue.insert(0, root)
        self.my_list.append(root)
        nodes_processed = 1
        while nodes_processed != total_nodes:
            poped_ele = my_queue.pop(0)
            current = poped_ele
            if current:
                if current.left is None:
                    data_left = int(input("Enter data for nodes in level order"))
                    new_node_left = Node(data_left)
                    current.left = new_node_left
                    my_queue.append(new_node_left)
                    self.my_list.append(new_node_left)
                    nodes_processed += 1
                if current.right is None:
                    data_right = int(input("Enter data for nodes in level order"))
                    new_node_right = Node(data_right)
                    my_queue.append(new_node_right)
                    current.right = new_node_right
                    self.my_list.append(new_node_right)
                    nodes_processed += 1


    def arr_rep_print(self):
        for address in self.my_list:
            print(address.node_data)

    def find_parent_node(self):
        child_node_pos = int(input("Enter the position of child node to find its parent"))
        if 0 < child_node_pos <= len(self.my_list):
            parent_node_pos = child_node_pos // 2
            print(parent_node_pos)
            print(f"The value at parent Position {parent_node_pos} is : {self.my_list[parent_node_pos - 1].node_data}")
        elif child_node_pos == 0:
            print("The index you entered is of root node")
        else:
            print("Child does not exists")

    def find_child_nodes(self):
        parent_node_pos = int(input("Enter the position of parent node to find its left and right child"))
        parent_node_index = parent_node_pos - 1
        print(f"The value at parent Position {parent_node_pos} is : {self.my_list[parent_node_index].node_data}")
        left_child_index = (2 * parent_node_index) + 1
        right_child_index = (2 * parent_node_index) + 2
        print(f"Left Child Data at Position {left_child_index + 1} is {self.my_list[left_child_index].node_data}")
        print(f"Right Child Data at Position {right_child_index + 1} is {self.my_list[right_child_index].node_data}")

    def find_depth(self):
        total_levels = np.log2(len(self.my_list) + 1)
        print(int(total_levels))

"""
               1
             /  \
            2    3
           / \   / \
          4  5  6   7
"""
if __name__ == "__main__":
    my_tree = binary_tree()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    stack = []
    my_tree.print_postorder_alg_rem(root)


# def print_postorder_alg1(self, root, temp_stack):
#     dict = {}
#     while root is not None:
#         temp_stack.append(root.node_data)
#         dict[root.node_data] = root
#         print(f"{root} apended to stack")
#         print(f"stack status{temp_stack}")
#         if root.right is not None:
#             print(f"root.data appended right encourted {root.right.node_data}")
#             root.right.node_data = -root.right.node_data
#             temp_stack.append(int(root.right.node_data))
#             dict[root.right.node_data] = root
#             print(temp_stack)
#             print(f"Dictionary Status : {dict}")
#         root = root.left
#         if root is None:
#             print("root become none")
#             poped_ele = temp_stack.pop()
#             # if +ive elements are poped meaning roots are poped
#             print("isinstance")
#             print(f" is instance ? {poped_ele}", isinstance(poped_ele, int))
#             if isinstance(poped_ele, int):
#                 poped_ele = -poped_ele
#                 root = Node(poped_ele)
#                 print(f"an int object encountered{root}")
#                 if not temp_stack:
#                     break
#             else:
#                 print(poped_ele.node_data)
#                 poped_ele = temp_stack.pop()
#                 root = poped_ele
#                 print(f"an adress encounted{root}")
#                 if not temp_stack:
#                     break


# def print_preorder(self, root):
    #     temp_stack = []
    #     # printing first ever node
    #     print(root.node_data)
    #     while True:
    #         while root.left is not None:
    #             if root.right is not None:
    #                 print(temp_stack)
    #                 temp_stack.append(root.right)
    #                 print(temp_stack)
    #
    #             # traversing through left of root
    #             root = root.left
    #             print(root.node_data)
    #         if root.left is None:
    #             if root.right is not None:
    #                 root = root.right
    #             elif root.right is None:
    #                 print(temp_stack)
    #                 back_trav = temp_stack.pop()
    #                 print(temp_stack)
    #                 print(back_trav.node_data)
    #                 root = back_trav
    #                 break

    # def print_inorder(self):
    #     if self.root is None:
    #         print("BST is empty.")
    #         return
    #
    #     temp_stack = []
    #     current = self.root
    #
    #     while current is not None or temp_stack:
    #         while current is not None:
    #             temp_stack.append(current)
    #             current = current.left
    #
    #         current = temp_stack.pop()
    #         print(current.node_data, end=", ")
    #         current = current.right