import yaml
yaml_path = 'D:\selenium\ZenTaoTestPro\page_element_infos\page_element_infos.yml'

def main():
    # 读取刚写的page_element_infos.yml
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)


if __name__ == '__main__':
    a = main()
