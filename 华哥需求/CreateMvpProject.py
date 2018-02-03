# -*- coding: utf-8 -*-
import json
import os
import shutil

"""模板信息json文件"""
TEMPLATE_INFO_JSON_FILE = "templet.json"

"""模板代码路径"""
TEMPLATE_FILE = "templet"

__moduleName = None
__prefix = None
__author = None
__time = None
__year = None
__superclass_model = None
__superclass_view = None
__superclass_presenter = None


def __parse_template_info(templ):
    """
    解析json得到模板信息
    :param templ 保存模板信息的json
    """
    templJson = json.loads(templ)
    global __moduleName, __prefix, __author, __time, __year, __superclass_model, __superclass_view, __superclass_presenter
    __moduleName = templJson.pop("module")
    __prefix = templJson.pop("prefix")
    __author = templJson.pop("author")
    __time = templJson.pop("time")
    __year = templJson.pop("year")
    __superclass_model = templJson.pop("model").pop("superclass")
    __superclass_view = templJson.pop("view").pop("superclass")
    __superclass_presenter = templJson.pop("presenter").pop("superclass")
    print("parse template info success!")


def __copy_file_directory(template_file):
    """复制模板项目目录"""
    # 复制之前先判断目录是否存在
    if (os.path.exists(__moduleName)):
        shutil.rmtree(__moduleName)
        print("删除已存在的文件夹")
    return shutil.copytree(template_file, __moduleName)


def __replace_content(file, rep_dict):
    """
    替换文件中的字符串
    :param file:文件名
    :param rep_dict: 替换内容键值对
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            for (key, value) in rep_dict.items():
                if key in line:
                    line = line.replace(key, value)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def __replace_file_info(rt, fname):
    """
    替换文件信息
    :param rt 根目录
    :param fname 文件名
    """
    # 要替换的内容键值对
    replace_list = {"<prefix>": __prefix, "<module>": __moduleName, "<author>": __author, "<time>": __time, "<year>": __year}
    if "ViewModel" in fname:
        replace_list["<superclass>"] = __superclass_view
    elif 'Presenter' in fname:
        replace_list["<superclass>"] = __superclass_presenter
    elif 'ViewController' in fname:
        replace_list["<superclass>"] = __superclass_model
    # print(replace_list)
    # 替换文件内容
    s_file = os.path.join(rt, fname.encode(encoding='utf-8'))
    __replace_content(s_file, replace_list)
    # 替换文件名
    new_name = fname.replace('_prefix_', __prefix).replace('_module_', __moduleName)
    os.rename(os.path.join(rt, fname.encode(encoding='utf-8')), os.path.join(rt, new_name.encode(encoding='utf-8')))


def __iterate_dir(new_dir):
    """
    遍历文件夹
    :param new_dir 要替换模板信息的目录
    """
    for rt, dirs, files in os.walk(new_dir.encode('utf-8')):
        for f in files:
            __replace_file_info(rt, str(f, encoding='utf-8'))


def create_template_project(template_file, template_json):
    with open(template_json) as f:
        templ = f.read()
    # print("template json file info : " + templ)
    # 解析json得到模板信息
    __parse_template_info(templ=templ)
    # 复制template文件夹， 重命名为 module
    new_dir = __copy_file_directory(template_file)
    # 遍历所有文件
    __iterate_dir(new_dir)
    print("成功创建模板工程 ： " + new_dir)


if __name__ == '__main__':
    create_template_project(TEMPLATE_FILE, TEMPLATE_INFO_JSON_FILE)
