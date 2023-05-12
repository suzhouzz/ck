import sys
from selenium.common import NoSuchElementException
import ddddocr
from lib import login
from selenium.webdriver.common.by import By
from time import sleep
from data import parm
from conn_myql import connect
import allure

# ------------注册-认证-----------------
#   造数，循环注册
# def zcrz(q):
#     zc_zh = '17600'        # 手机号
#     uscc = '913205837965'   # 统一社会信用代码
#     zzmc = 'SZGYYQuLtd&'        # 企业名称
#     for j in range(6):
#         for i in range(q):
#             h = random.choice(string.ascii_letters)
#             k = random.randint(0,9)
#             zc_zh += str(k)             # 随机添加数字的 手机号
#             uscc += str(k)              # 随机添加数字的 统一社会信用代码
#             zzmc += h               # 添加随机字母后的 企业名称

def zc(sjh):

    # 点击立即注册

    login.driver.find_element(By.XPATH, "//*[contains(text(),'立即注册')]").click()
    # 输入手机号
    login.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入手机号码"]').send_keys(sjh)
    # 获取验证码
    for i in range(3):
        i = i + 1
        try:
            login.qingchu_code()  # 清除验证码输入框
            zhuc_yan()
            login.driver.find_element(By.XPATH, '//*[@class="el-icon-error" and @style="display: none;"]')  # 查询验证码是不是有×，找不到则捕获异常
        except NoSuchElementException:
            print('第', i, '次获取验证码失败')
            if i == 3:
                print('图形验证码错误')
                sys.exit(0)
        # 无异常则执行else
        else:
            sleep(0.5)
            break
    # 获取短信验证码
    yzm = connect.dx_yzm(sjh)
    #输入密码
    login.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="密码由8-16位字母、数字和字符组成"]').send_keys(parm.login_mima)
    login.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="再次输入密码"]').send_keys(parm.login_mima)
    # 隐私政策
    login.driver.find_element(By.XPATH, "//*[@class='el-checkbox__inner']").click()
    # 输入验证码并注册
    for j in range(3):
        j = j + 1
        try:
            login.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="短信验证码"]').clear()
            login.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="短信验证码"]').send_keys(yzm)
            login.driver.find_element(By.XPATH, "//*[contains(text(),'立即注册')]").click()
            sleep(2)
            with allure.step("注册完成后截图"):
                login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\reg.png")
                allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\reg.png", attachment_type=allure.attachment_type.PNG)
            sleep(1)
            login.driver.find_element(By.XPATH, '//*[@class="el-icon-success" and @style="display: none;"]')    # 查询验证码勾是否隐藏，找不到则捕获异常
        except NoSuchElementException:
                print('第', j, '次获取短信验证码失败')
                if j == 3:
                    print('短信验证码错误')
                    sys.exit(0)
            # 无异常则执行else
        else:
            sleep(0.5)
            break
    sleep(1)
# 获取验证码
def zhuc_yan():
        # 获取验证码
        elc = login.driver.find_element(By.XPATH, "//*[@class='login-code-img']")
        ocr = ddddocr.DdddOcr()
        code_text = ocr.classification(elc.screenshot_as_png)
        # 输入验证码
        login.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="请输入验证码"]').send_keys(code_text)
        # 点击获取验证码
        login.driver.find_element(By.XPATH, "//*[text()='获取验证码']").click()
        sleep(1)


def rz(yyzz,uscc,zzmc,dz,xm,sfz,sjh,sqs) :
    # 打开网址 ——UAT
    login.login_url(parm.url_uat)
    # 用户登录
    login.login(sjh, parm.login_mima)
    # 未认证的企业，登录提示认证，点击【立即认证】
    login.driver.find_element(By.XPATH, "//*[@class='confirm-btn']").click()
    login.driver.find_element(By.XPATH, "//*[contains(text(),'立即认证')]").click()
    # 上传图片
    login.driver.find_element(By.XPATH, "//*[@class='img-upload file-upload']//child::input").send_keys(yyzz)
    sleep(1)
    # 【组织类型】选择法人企业
    login.driver.find_element(By.XPATH, "//*[contains(text(),'组织类型')]//following::input[1]").click()
    sleep(1)
    login.driver.find_element(By.XPATH, "//*[contains(text(),'法人企业')]").click()
    sleep(0.5)
    # 录入【统一社会信用代码】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'统一社会信用代码：')]//following::input[1]").send_keys(uscc)
    # 录入【组织名称】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'组织名称：')]//following::input[1]").send_keys(zzmc)
    # 录入【开户行】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'开户行：')]//following::input[1]").click()
    sleep(1)
    login.driver.find_element(By.XPATH, "//*[contains(text(),'苏州银行')]").click()
    # 录入【实际经营地址】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'实际经营地址：')]//following::input[1]").send_keys(dz)
    # 录入【法人/经营者姓名】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'法人/经营者姓名：')]//following::input[1]").send_keys(xm)
    # 录入【法人/经营者身份信息】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'法人/经营者身份信息：')]//following::input[1]").send_keys(sfz)
    # 录入【法人/经营者手机号】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'法人/经营者手机号：')]//following::input[1]").send_keys(sjh)
    # 上传征信授权书
    login.driver.find_element(By.XPATH, "//*[@class='file-upload']//child::input").send_keys(sqs)
    sleep(2)
    # 录入【法人/经营者手机号】
    login.driver.find_element(By.XPATH, "//*[contains(text(),'提交激活')]").click()
    sleep(2)
    print('提交认证成功')
    sleep(1)
    with allure.step("认证提交后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\aut.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\aut.png",
                           attachment_type=allure.attachment_type.PNG)
    login.login_tui()
def chus(uscc):
    # 登录运维端,打开网址
    login.login_url(parm.url_uat_yw)
    # 录入账号密码登录
    login.login_yw(parm.lg_yw, parm.login_mima)
    # 进入初审界面
    login.driver.find_element(By.XPATH, "//*[contains(text(),'企业认证审核管理')]").click()
    sleep(1)
    login.driver.find_element(By.XPATH, "//*[contains(text(),'企业认证初审管理 ')]").click()
    sleep(1)
    # 搜索需要审核的企业
    login.driver.find_element(By.XPATH, "//*[contains(text(),'关键词搜索')]//following::input[1]").send_keys(uscc)
    login.driver.find_element(By.XPATH, '//*[@class="search-button"]').click()
    sleep(1)
    # 点击审核
    #login.driver.find_element(By.XPATH, "//*[@class='has-gutter']//following::button[1]").click()
    login.driver.find_element(By.XPATH, '//*[@id="avue-view"]/div/div[1]/div[5]/div/div[4]/div[2]/table/tbody/tr/td[8]/div/div/button/span').click()
    sleep(1)
    # 输入审批意见
    login.driver.find_element(By.XPATH, "//*[@class='el-textarea__inner']").send_keys('同意')
    login.driver.find_element(By.XPATH, '//*[@class="yellow-bg-btn"]').click()
    sleep(1)
    with allure.step("初审完成后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\chus.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\chus.png",
                           attachment_type=allure.attachment_type.PNG)
    print('企业初审成功')
def fus(uscc):
    # 企业认证复审，打开网址 ——UAT
    login.login_url(parm.url_uat)
    # 用户登录
    login.login(parm.lg_yw_fs, parm.login_mima)
    # 进入初审界面
    login.driver.find_element(By.XPATH, "//*[contains(text(),'企业认证审核管理')]").click()
    sleep(1)
    login.driver.find_element(By.XPATH, "//*[contains(text(),'企业认证复审管理')]").click()
    sleep(1)
    # 搜索需要审核的企业
    login.driver.find_element(By.XPATH, "//*[contains(text(),'关键词搜索')]//following::input[1]").send_keys(uscc)
    login.driver.find_element(By.XPATH, "//*[@class='search-button']").click()
    sleep(1)
    # 点击审核/
    login.driver.find_element(By.XPATH,
                              '//*[@id="avue-view"]/div/div[1]/div[5]/div[1]/div[4]/div[2]/table/tbody/tr/td[8]/div/div/div').click()
    sleep(1)
    # 输入审批意见
    login.driver.find_element(By.XPATH, "//*[@class='el-textarea__inner']").send_keys('同意')
    login.driver.find_element(By.XPATH, '//*[@class="yellow-bg-btn"]').click()
    sleep(1)
    with allure.step("复审完成后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\fus.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\fus.png",
                           attachment_type=allure.attachment_type.PNG)
    print('企业复审成功')
    login.login_tui()


