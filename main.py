import func

Main_Menu_Msg = """
Which operation on tree you want to perform
A. Array Representation options
T. Output Traversal
E. Exit
"""
my_tree = func.binary_tree()
my_tree.take_input_lvl_wise()
my_tree.arr_rep_print()
while True:
    choice = input(Main_Menu_Msg)
    choice = choice.capitalize()
    match choice:
        case 'A':
            arr_rep_msg = """
What operation you want to perform in array representation
O. Print array
C. Print childs of a node
P. Print parent of a node
D. Find and print Depth or total levels
E. Exit
"""
            while True:
                arr_user_choice = input(arr_rep_msg)
                arr_user_choice = arr_user_choice.capitalize()
                match arr_user_choice:
                    case 'O':
                        print("Your tree in array format is : ")
                        my_tree.arr_rep_print()
                    case 'C':
                        try:
                            my_tree.find_child_nodes()
                        except:
                            print("Child not found")
                    case 'P':
                        try:
                            my_tree.find_parent_node()
                        except:
                            print("Parent not found")
                    case 'D':
                        print("___Finding Depth___")
                        my_tree.find_depth()
                    case 'E':
                        break
        case 'T':
            trav_msg = """
In which order you want to traverse your tree
P. PreOrder Traversal
I. InOrder Traversal
O. PostOrder Traversal
E. Exit
"""
            while True:
                trav_choice = input(trav_msg)
                trav_choice = trav_choice.capitalize()
                match trav_choice:
                    case 'P':
                        try:
                            print("Your tree in Preorder is : ")
                            my_tree.print_preorder_traversal()
                        except:
                            print("")
                    case 'I':
                        try:
                            print("Your tree in Inorder is : ")
                            my_tree.inorder_myalgo()
                        except:
                            print("")

                    case 'O':
                        try:
                            print("Your tree in Postorder is : ")
                            my_tree.print_postorder_alg_rem()
                        except:
                            print("")
                    case 'E':
                        break

        case 'E':
            break
        case _:
            print("Please Enter a correct Value both upper and lowercase are allowed")
