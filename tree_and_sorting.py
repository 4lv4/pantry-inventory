import json

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
class Tree:
    def __init__(self, dictonary = None, json_path = None) -> None:
        self.path = json_path
        self.dict = dictonary
        self.root = None
        if self.dict:
            print("In the if")
            for key in self.dict.keys():
               self.root = self.insert(self.root, key)

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key <self.root.key:
               root.left = self.insert(root.left, key)
            else:
               root.right = self.insert(root.right, key)
        return root

    def search(self, key):
        if self.root is None or self.root.key[0] == key[0]:
            return self.root.key
        if key <self.root.key:
            return self.search(self.root.left, key)
        return self.search(self.root.right, key)
    
    def key_list(self, root):
        result = []
        if root:
            result = self.key_list(root.left)
            result.append(root.key)
            result += self.key_list(root.right)
        return result

    def search_incomplete(self ,root, letter ):
        result = []
        if not (root is  None):
            if self.root.key.startswith(letter):
                result.append(root.key)
            if letter < self.root.key[len(letter)]:
                result += self.search_incomplete(root.left, letter)
            result += self.search_incomplete(root.right, letter)
        return result


d = {
    "Äpple":
    {
        "type" : "Fruit", 
        "unit" : "St" , 
        "amount": 5 ,
        "pantry_location" : "Frige",
        "best_befor" : None,
        "always_stock" : False,
        "limit" : 2,
        "Ready_to_eat": True,
        "prep_time" : None ,
        "tags" : ["snack", "sweet"],
        "nutrition": { "kcal" : 55,
                        "carbs" : 11,
                        "fat" : 0,
                        "protein" : 0
         }
    },

    "Klementin":
    {
        "type" : "Fruit", 
        "unit" : "St" , 
        "amount": 5 ,
        "pantry_location" : "Frige",
        "best_befor" : None,
        "always_stock" : False,
        "limit" : 2,
        "Ready_to_eat": True,
        "prep_time" : None ,
        "tags" : ["snack", "sweet"],
        "nutrition": { "kcal" : 47,
                        "carbs" : 12,
                        "fat" : 0,
                        "protein" : 0
         }
    },

    "Paprika":
    {
        "type" : "Vegetabl", 
        "unit" : "St" , 
        "amount": 5 ,
        "pantry_location" : "Frige",
        "best_befor" : None,
        "always_stock" : False,
        "limit" : 2,
        "Ready_to_eat": True,
        "prep_time" : None ,
        "tags" : ["snack", "sweet"],
        "nutrition": { "kcal" : 20,
                        "carbs" : 4.5,
                        "fat" : 0,
                        "protein" : 0
         }
    }
}


tree = Tree(d)
print(tree.search_incomplete(tree.root,"Ä"))
print(tree.key_list(tree.root))
print(tree.search("Äpple"))




