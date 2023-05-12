from selenium import webdriver
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import ddddocr
from data import parm
from lib import position

chrome_options = webdriver.ChromeOptions()
# # GPU硬件加速
# chrome_options.add_argument('–-disable-gpu')
# # 彻底停用沙箱
# chrome_options.add_argument('--no-sandbox')
# # 创建临时文件共享内存
# chrome_options.add_argument('--disable-dev-shm-usage')
# # 单进程运行
# chrome_options.add_argument('-–single-process')
chrome_options.add_argument('--start-maximized')  # 浏览器窗口最大化
driver = webdriver.Chrome(options=chrome_options)


#---------------------
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)  # 不自动关闭浏览器
# options.add_argument('--start-maximized')  # 浏览器窗口最大化
# driver = webdriver.Chrome(options=options)


def login_url(url):
    driver.get(url)  # 请求网站
    sleep(3)

# 登录------------------------------------------------------------------
def login_yw(zh,mm):
    # 输入账号
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入账号"]').send_keys(zh)
    sleep(1)
    # 输入密码
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入登录密码"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入登录密码"]').send_keys(mm)
    # 隐私政策
    driver.find_element(By.XPATH, "//*[@class='el-checkbox__inner']").click()
    # 获取验证码
    for i in range(4):
        i = i + 1
        try:
            qingchu_code()  # 清除验证码输入框
            login_yan()
            driver.find_element(By.XPATH, "//*[contains(text(),'系统管理')]")  # 查找登录成功后的元素“退出登录”，找不到则捕获异常
        except NoSuchElementException:
            print(zh, '第', i, '次登录失败')
        # 无异常则执行else
        else:
            sleep(0.5)
            break

    # 获取验证码并登录
def login(zh,mm):

    # 输入账号
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入您的用户名"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入您的用户名"]').send_keys(zh)
    sleep(1)
    # 输入密码
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入您的密码"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入您的密码"]').send_keys(mm)
    # 隐私政策
    driver.find_element(By.XPATH, "//*[@class='el-checkbox__inner']").click()
    # 获取验证码
    for i in range(4):
        i = i + 1
        try:
            qingchu_code()  # 清除验证码输入框
            login_yan()
            driver.find_element(By.XPATH, "//*[contains(text(),'退出登录')]")  # 查找登录成功后的元素“退出登录”，找不到则捕获异常
        except NoSuchElementException:
                print(zh,'第',i,'次登录失败')
        # 无异常则执行else
        else:
            sleep(1)
            break

    # 获取验证码并登录
def login_yan():
    # 获取验证码
    elc = driver.find_element(By.XPATH, "//*[@class='login-code-img']")
    ocr = ddddocr.DdddOcr()
    code_text = ocr.classification(elc.screenshot_as_png)
    # 输入验证码
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys(code_text)
    # 点击登录
    driver.find_element(By.XPATH, "//*[text()='立即登录']").click()
    sleep(1)
# 定位验证码输入框,并清除输入框
def qingchu_code():
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').clear()
# 退出
def login_tui():
    # 点击个人中心
    sleep(1)
    driver.find_element(By.XPATH, '//*[@class="el-select area-select"]/following::input[1]').click()
    sleep(1)
    # 点击退出登录
    tc= '//*[@class="top-bar-exit-text"]'
    element = driver.find_element(By.XPATH, tc)
    driver.execute_script("arguments[0].click();", element)

    # driver.find_element(By.XPATH,'').click()
    # 点击确定
    driver.find_element(By.XPATH, "//*[@class='el-message-box__btns']/child::button[2]").click()
    sleep(1)
# 业务申请退出
def qysq_tui():
    # 点击个人中心
    sleep(1)
    driver.find_element(By.XPATH, position.grzx).click()
    sleep(1)
    # 点击退出登录
    tc= '//*[contains(text(),"退出登录")]'
    element = driver.find_element(By.XPATH, tc)
    driver.execute_script("arguments[0].click();", element)
    # 点击确定
    driver.find_element(By.XPATH, "//*[@class='el-message-box__btns']/child::button[2]").click()
    sleep(1)
# 循环登录
def login_canshu(lb):
    for login_zh in lb:
        try:
            # 调用登录方法
            login(login_zh, parm.login_mima)
            driver.find_element(By.XPATH, "//*[contains(text(),'退出登录')]")  # 查找登录成功后的元素“退出登录”，找不到则捕获异常
            get_uscc_qy()
        except:
            # 登录失败
            print(login_zh, '-----------------登录失败，循环下一个')
            # 点击隐私政策，解释：登录失败隐私政策已勾选需要清空，再重新循环登录方法
            driver.find_element(By.XPATH, "//*[@class='el-checkbox__inner']").click()
        # 无异常则执行“退出”方法
        else:
            login_tui()
 #  获取统一社会信用代码
def get_uscc_qy():
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[text()='我的企业']").click()
    sleep(0.5)
    driver.find_element(By.XPATH, "//*[text()='信息维护']").click()
    sleep(0.5)
    # xpath所有后代轴定位，descendant，
    get_uscc = driver.find_element(By.XPATH, "//*[@class='display-info']/descendant::div[5]")
    print(get_uscc.text)





