import json
import os
from unidecode import unidecode
from treelib import Tree

def json_dict_from_file():
    local_path = os.path.dirname(os.path.abspath("/workspaces/Python-OOP-Project/exercices/03.class_tree/json_data.json"))
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))
    json_str = json.dumps(json_data)
    json_data = (unidecode(json_str))
    json_dict = json.loads(json_data)

    return json_dict

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            create_tree_from_dict(tree, new_node_id, value)


def main():
    my_tree = Tree()
    my_tree.create_node(tag="Racine", identifier="racine")
    json_dict = json_dict_from_file()
    create_tree_from_dict(my_tree, "racine", json_dict)
    my_tree.show()

if __name__ == '__main__':
    main()