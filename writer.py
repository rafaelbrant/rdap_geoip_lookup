import json


class ResponseWriter:
    def __init__(self, response):
        self.response = response

    def save_services_to_json(self):
        for service_name in self.response:
            with open(f'{service_name}_response.json', 'w') as json_file:
                json.dump(self.response.get(service_name), json_file)
            print(f'File {service_name}_response.json saved')
