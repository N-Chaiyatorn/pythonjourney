
import requests

class PixelaGraphGenerators():
    def creating_new_graph(self, headers, graph_data_manager, graph_url):
        return requests.post(url = graph_url, json = graph_data_manager.graph_config, headers = headers)