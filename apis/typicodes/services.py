import requests, json


class Service:

    def get_data_typicode(self):
        return Service.get_data_typicode_first_five_items(
                requests.get("https://jsonplaceholder.typicode.com/todos")
            )

    def get_data_typicode_first_five_items(data_typicode_list):
        return Service.format_data_typicode(
            json.loads(data_typicode_list.content)[:5]
            )

    @staticmethod
    def format_data_typicode(data_typicode_list):
        for data_typicode in data_typicode_list:
            for key in data_typicode.copy():
                if key not in ['title', 'id']:
                    data_typicode.pop(key)
        return data_typicode_list
