import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_case import reg_aut
from test_case import smtp_email_send
from data import parm
from lib import login, product, position
from selenium.webdriver.common.by import By
from time import sleep
from re import sub
import allure

# 定义测试用例类
@allure.feature("苏融通自动化测试")
class TestSzfsp:

    # 定义测试初始化方法
    def setup_class(self):
        login.login_url(parm.url_uat)        # 登录uat网址
        login.driver.implicitly_wait(10)    # 隐式等待10s

    # 定义测试销毁方法
    def teardown_class(self):
        smtp_email_send.send_report()
        sleep(10)
        login.driver.quit()

    # --------------------注册认证--------------------------
    @allure.story("注册")
    def test_reg(self):
        reg_aut.zc(parm.zc_zh)      # 注册
        print('企业注册成功')

    @allure.story("申请认证")
    def test_aut(self):
        reg_aut.rz(parm.yyzz, parm.uscc, parm.zzmc, parm.dz, parm.xm, parm.sfz, parm.zc_zh, parm.sqs)  # 提交认证

    @allure.story("初审")
    def test_chus(self):
        reg_aut.chus(parm.uscc)  # 企业认证初审

    @allure.story("复审")
    def test_fus(self):
        reg_aut.fus(parm.uscc)  # 企业认证复审

    # ---------------- 银行审核一般信贷产品，企业申请----------------------
    @allure.story("企业申请业务产品")
    def test_qy_sq(self):
        login.login(parm.lg_qy, parm.login_mima)         # 企业登录
        product.qy_cpsq()       # 企业产品申请
        product.qy_sq()         # 录入信息并提交

    # 银行未受理需求
    @allure.story("银行处理未受理需求")
    def test_bank_yib_wsl(self):
        login.login(parm.lg_yh, parm.login_mima)  # 银行登录
        product.bank_yib_wsl()      # 未受理需求

    # 银行需求审核管理
    @allure.story("银行需求审核管理")
    def test_bank_yib_shgl(self):
        product.bank_yib_shgl()     # 需求审核

    # 银行需求授信管理
    @allure.story("银行需求授信管理")
    def test_bank_yib_sxgl(self):
        product.bank_yib_sxgl()     # 授信管理

    # 银行需求放款管理
    @allure.story("银行需求放款管理")
    def test_bank_yib_fkgl(self):
        product.bank_yib_fkgl()     # 放款管理
        # 刷新界面
        login.driver.refresh()
        # 点击进件管理
        login.driver.find_element(By.XPATH, position.jjgl).click()
        # 点击一般信贷产品
        login.driver.find_element(By.XPATH, position.jjgl_ybcp).click()
        # 点击放款管理
        login.driver.find_element(By.XPATH, position.jjgl_ybcp_fkgl).click()
        jjgl_ybcp_ss = position.jjgl_ybcp_ss
        # 点击搜索
        WebDriverWait(login.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, jjgl_ybcp_ss)))
        login.driver.find_element(By.XPATH, jjgl_ybcp_ss).click()
        # 查看放款金额并断言
        xpath_jine =  '//*[@id="avue-view"]/div/div/div[1]/div[4]/div/div[3]/table/tbody/tr[1]/td[6]/div'
        WebDriverWait(login.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath_jine)))
        je = login.driver.find_element(By.XPATH, xpath_jine).text
        assert sub(r'[^\d.]', '', je) == str(parm.sxjine)
    @allure.story("ces")
    def test_mowe21i(self):
        print('ces')        # 123

if __name__ == "__main":
    pytest.main()