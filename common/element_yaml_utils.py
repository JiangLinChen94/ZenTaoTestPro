import yaml

yaml_path = 'D:\selenium\ZenTaoTestPro\page_element_infos\page_element_infos.yml'


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