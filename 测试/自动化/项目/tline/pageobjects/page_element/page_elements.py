from tools import parseyaml
pages = parseyaml()


# 获取
def get_locater(clazz_name,method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator



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
    
    # 微信登录按钮
    wechat_login = get_locater('LoginPage','wechat_login')
    
    # 微信确认按钮
    ok_btn = get_locater('LoginPage','ok_btn')
    
    # 微信账号输入框
    wechat_name_input = get_locater('LoginPage','wechat_name_input')
    
    # 微信账号密码框
    wechat_pwd_input = get_locater('LoginPage','wechat_pwd_input')
    
    # 微信中的登录按钮
    login_wechat = get_locater('LoginPage','login_wechat')
    
    # 微信登录失败重试
    wechat_login_retry = get_locater('LoginPage','wechat_login_retry')
    
    # 设置按钮
    setting_btn = get_locater('LoginPage','setting_btn')
    
    # 退出按钮
    logout_btn = get_locater('LoginPage','logout_btn')
    
    # 退出确认按钮
    logout_ok = get_locater('LoginPage','logout_ok')
    

