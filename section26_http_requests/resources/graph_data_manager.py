class GraphDataManager():
    
    def __init__(self):
        self.graph_config = {}
        
    def determine_graph_config_value(self, graph_config_keys_list, choice):
        for key in graph_config_keys_list:
            if choice == '1':
                self.graph_config[key] = input(f"Type your graph {key}: ")
            elif choice == '4':
                self.graph_config[key] = input(f"Type your new graph {key}: ")

    def asking_user_for_editing_choice(self, graph_body_editing_choice):
        while True:
            try:
                asking_editing_title_quote = f"""
Please choose your title that you want to editing choice.
Your choice is {graph_body_editing_choice}.
please choose your choice (hint:if you want to editing more that one title please make the space between each title.): """

                edited_choice = input(asking_editing_title_quote).split(" ")
            
                for title in edited_choice:
                    if title not in graph_body_editing_choice:
                        raise ValueError()

            except:
                print("Invalid choice!!!, please try again!!!.")

            else:
                return edited_choice