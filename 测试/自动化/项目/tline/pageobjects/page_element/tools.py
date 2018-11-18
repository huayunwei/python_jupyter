'''
    直接执行，通过模板生成页面元素文件 - page_elements
'''

import yaml
import os
import jinja2

basepath = os.path.dirname(__file__)

# yaml文件位置
yamlpath = os.path.join(basepath,'element_desc')

def parseyaml():
    '''
    遍历读取yaml文件
    :return:
    '''
    pageElements = {}
    for fpath,dirname,fnames in os.walk(yamlpath):
        for name in fnames:
            # yaml文件绝对路径
            yaml_file_path = os.path.join(fpath,name)
            # 排除非.yaml的文件
            if ".yaml" in str(yaml_file_path):
                with open(yaml_file_path,'r',encoding='utf-8') as f:
                    page = yaml.load(f)
                    pageElements.update(page)
    return pageElements


def get_page_list(yamlpage):
    '''
    对获取到的页面元素字典进行格式化
    :param yamlpage:通过上面的函数获取到的yaml数据字典
    :return:返回一个字典
        {'login':[{desc:xxx,name:xxx}]}
    '''
    page_object = {}
    for page,names in yamlpage.items():
        loc_names = []
        locs = names['locators']
        for loc in locs:
            loc_names.append({'desc':loc['desc'],'name':loc['name']})
        page_object[page] = loc_names
    return page_object


def create_pages_py(page_list):
    '''
    根据模板生成.py文件
    :param page_list:
    :return:
    '''
    template_loader = jinja2.FileSystemLoader(searchpath=basepath)
    template_env = jinja2.Environment(loader=template_loader)

    templateVars = {
        'page_list':page_list
    }
    template = template_env.get_template("template_page")
    with open(os.path.join(basepath,"page_elements.py"),'w',encoding='utf-8') as f:
        f.write(template.render(templateVars))

if __name__ == "__main__":
    '''执行'''
    # 获取yaml中所有内容
    page_element = parseyaml()
    # 对内容进行格式化
    page_list = get_page_list(page_element)
    # 根据
    create_pages_py(page_list)