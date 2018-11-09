from tools import parseyaml
pages = parseyaml()


# 获取
def get_locater(clazz_name,method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator



'''
下面类中变量的结构如下：
{'desc': '选择页跳转链接', 'name': 'login_text', 'type': 'id', 'value': 'com.liukena.android:id/logintext'}
'''

class LoginPage:

    # 选择页跳转链接
    login_text = get_locater('LoginPage','login_text')
    
    # 未登录的首页 - 我的按钮
    me_btn = get_locater('LoginPage','me_btn')
    
    # 未登录的首页 - 我的按钮 - 登录按钮
    me_ok_btn = get_locater('LoginPage','me_ok_btn')
    
    # 密码登录页面 - 手机号输入框
    phone_input = get_locater('LoginPage','phone_input')
    
    # 密码登录页面 - 密码输入框
    pwd_input = get_locater('LoginPage','pwd_input')
    
    # 密码登录页面 - 登录按钮
    login_btn = get_locater('LoginPage','login_btn')
    

'''
if __name__ == "__main__":
    a = LoginPage()
    print(a.login_text)
'''