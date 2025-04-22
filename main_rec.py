from pprint import pprint

root = 2
height = 6
tree = {}

count = 0

def build_tree(node, height, current_height=0):
    if current_height >= height:
        return {}
    
    left_child = node * 3  
    right_child = node + 4 

    return {
        node: {
            "left": build_tree(left_child, height, current_height + 1),  
            "right": build_tree(right_child, height, current_height + 1) 
        }
    }

tree = build_tree(root, height)
pprint(tree)
