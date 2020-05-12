#!/usr/bin/env python
# encoding: utf-8
# @author: Alin
# @file: .py
# @time: 2020/5/11 22:21

import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
test_data_path = os.path.join(current_path, '..', local_config.testdata_path)


class TestDataUtils:
    def __init__(self,test_suit_name, test_class_name):
        self.test_class_name = test_class_name
        self.excel_data = ExcelUtils(test_data_path, test_suit_name).get_sheet_data_by_list()
        self.excel_rows = len(self.excel_data)

    def convert_excel_data_to_test_data(self):
        """
          {'test_login_success':
             {'test_name':'验证是否能成功进行登录','isnot':'是','expected_result':'测试人员1',
             'test_parameter':{'username':'test01','password':'newdream123'} }
         }
        :return:
        """
        test_data_infos = {}
        for data_rows in range(1, self.excel_rows):
            test_data_info = {}
            if self.excel_data[data_rows][2].__eq__(self.test_class_name):
                test_data_info['test_name'] = self.excel_data[data_rows][1]
                test_data_info['isnot'] = False if self.excel_data[data_rows][3].__eq__('是') else True
                test_data_info['expected_result'] = self.excel_data[data_rows][4]
                test_data_info['test_message'] = self.excel_data[data_rows][5]
                test_parameter = {}
                for data_columns in range(5, len(self.excel_data[data_rows])):
                    if self.excel_data[data_rows][data_columns].__contains__('=') \
                            and len(self.excel_data[data_rows][data_columns]) > 2:
                        parameter_info = self.excel_data[data_rows][data_columns].split('=')
                        test_parameter[parameter_info[0]] = parameter_info[1]
                test_data_info['test_parameter'] = test_parameter
            test_data_infos[self.excel_data[data_rows][0]] = test_data_info
        return test_data_infos


if __name__ == '__main__':
    infos = TestDataUtils('login_suit', 'TestZenTaoLogin').convert_excel_data_to_test_data()
    for i in infos.values():
        print(i)
