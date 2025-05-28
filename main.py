from linkedlist import LinkedList
def main():
    linked_list=LinkedList()
    linked_list.instert_at_front(9)
    linked_list.instert_at_front(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(6)
    linked_list.instert_at_front(11)
    Node=linked_list.get_node(3)
    if Node is not None:
        print('Found Node with data 3')
    else:
        print('Node with data 3 not found') 
    first_node=linked_list.get_first_node()
    if first_node is not None:
        print(f"First Node {first_node.data}")
    last_node=linked_list.get_last_node()
    if last_node is not None:
        print(f"Last Node {last_node.data}")  
    linked_list.print_list()
    linked_list.delete_node(9)
    print('After delete Node 9')
    linked_list.print_list()

    
if __name__=="__main__":
    main()    