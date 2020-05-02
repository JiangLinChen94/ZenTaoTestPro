import os
import yaml
from common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
yaml_path = os.path.join(current_path, '..', local_config.yaml_path)


class ElementYamlUtils:
    def __init__(self):
        with open(yaml_path, 'r', encoding='utf-8') as file:
            self.data = yaml.load(file, Loader=yaml.FullLoader)

    def get_ymal_info(self):
        return self.data


if __name__ == "__main__":
    element = ElementYamlUtils().get_ymal_info()
    print(element)
    print('******************')
    print(element['username_input_box']['element_name'])