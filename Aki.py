# Define a class for a tree node
class TreeNode:
    def __init__(self, data, question):
        self.data = data
        self.question = question
        self.left = None
        self.right = None
# Define the Quiz class
class Quiz:
    def __init__(self):
        self.root = None
    # Method to insert a new node into the tree
    def insert(self, data, question):
        self.root = self._insert_rec(self.root, data, question)
    # Recursive helper method for inserting a new node
    def _insert_rec(self, root, data, question):
        if root is None:
            return TreeNode(data, question)
        if data < root.data:
            root.left = self._insert_rec(root.left, data, question)
        elif data > root.data:
            root.right = self._insert_rec(root.right, data, question)
        return root
    # Method to query the tree and play the quiz
    def query_tree(self):
        current_node = self.root
        while current_node.left or current_node.right:
            self.print_question(current_node)
            user_input = self.get_user_input().strip().lower()
            if (user_input == "y" or user_input == "yes") and current_node.left:
                current_node = current_node.left
            elif (user_input == "n" or user_input == "no") and current_node.right:
                current_node = current_node.right
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        return f"Final Answer: {current_node.question}"
    # Method to read input from a file and build the tree
    def read_input_from_file(self, file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[2:]:
                data, question = line.strip().split(' ', 1)
                self.insert(int(data), question)
    # Method to display tree traversal options
    def display_tree(self):
        while True:
            print("Tree Traversal Options:")
            print("1 - In-order Traversal")
            print("2 - Pre-order Traversal")
            print("3 - Post-order Traversal")
            print("4 - Return to Main Menu")
            choice = self.get_user_input()
            traversal_functions = {
                "1": self.in_order_traversal,
                "2": self.pre_order_traversal,
                "3": self.post_order_traversal,
            }
            if choice in traversal_functions:
                print(f"{traversal_functions[choice].__name__} Traversal:")
                traversal_functions[choice](self.root)
            elif choice == "4":
                return
            else:
                print("Invalid choice")
    # Method for in-order tree traversal
    def in_order_traversal(self, node):
        if node is None:
            return
        self.in_order_traversal(node.left)
        self.print_node_data(node)
        self.in_order_traversal(node.right)
    # Method for pre-order tree traversal
    def pre_order_traversal(self, node):
        if node is None:
            return
        self.print_node_data(node)
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)
    # Method for post-order tree traversal
    def post_order_traversal(self, node):
        if node is None:
            return
        self.post_order_traversal(node.left)
        self.post_order_traversal(node.right)
        self.print_node_data(node)
    # Method to print a question from a tree node
    def print_question(self, node):
        print(node.question)
    # Method to print data from a tree node
    def print_node_data(self, node):
        print(node.data, node.question)
    # Method to get user input
    def get_user_input(self):
        return input("Enter your choice: ").strip().lower()
# Main execution block
if __name__ == "__main__":
    # Create an instance of the Quiz class
    bt = Quiz()
    file_name = "akifood.txt"
    bt.read_input_from_file(file_name)
    # Main menu loop
    while True:
        print("Menu:")
        print("P - Play Quiz")
        print("L - Load Game File")
        print("D - Display Tree")
        print("H - Help")
        print("X - Quit")
        choice = bt.get_user_input()
        if choice == "p":
            final_answer = bt.query_tree()
            print(final_answer)
        elif choice == "l":
            print("Enter file path or name")
            file_name = bt.get_user_input().strip()
            bt.read_input_from_file(file_name)
        elif choice == "d":
            bt.display_tree()
        elif choice == "h":
            with open(file_name, 'r') as file:
                print(file.readline().strip())
                print(file.readline().strip())
        elif choice == "x":
            break
        else:
            print("Invalid choice")