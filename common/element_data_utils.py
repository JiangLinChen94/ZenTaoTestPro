import os
import xlrd
from common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
excel_path = os.path.join(current_path, '..', local_config.excel_path)


class ElementDataUtils:
    def __init__(self, module_name, page_name, element_path=excel_path):
        self.element_path = element_path
        self.workbook = xlrd.open_workbook(excel_path)
        self.page_name = page_name
        self.sheet = self.workbook.sheet_by_name(module_name)

        self.row_count = self.sheet.nrows

    def get_element_info(self):
        element_infos = {}
        for i in range(1, self.row_count):
            if self.sheet.cell_value(i, 2) == self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['page_name'] = self.sheet.cell_value(i, 2)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                timeout_value = self.sheet.cell_value(i, 5)
                element_info['timeout'] = timeout_value if isinstance(timeout_value, float)\
                    else local_config.time_out
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos


if __name__ == '__main__':
    elements = ElementDataUtils('login', 'login_page').get_element_info()
    print(elements)