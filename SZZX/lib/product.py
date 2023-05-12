import allure
from lib import login, position
from selenium.webdriver.common.by import By
from time import sleep
from data import parm
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 银行产品申请
def qy_cpsq():
    # 点击金融集市
    login.driver.find_element(By.XPATH, position.jrjs).click()
    sleep(2)
    # 切换句柄
    win1 = login.driver.window_handles
    login.driver.switch_to.window(win1[-1])
    # 银行融资-搜索信保贷
    login.driver.find_element(By.CSS_SELECTOR, position.yhrz_cpmc).send_keys(parm.cpmc)
    # 银行融资-搜索苏州银行
    login.driver.find_element(By.CSS_SELECTOR, position.yhrz_jgmc).send_keys(parm.yinh)
    sleep(1)
    # 银行融资-点击搜索
    login.driver.find_element(By.XPATH, position.yhrz_ss).click()
    sleep(2)
    # 点击列表立即申请
    login.driver.find_element(By.XPATH, position.yhrz_lb_ljsq).click()
    sleep(2)
    # 切换句柄
    win2 = login.driver.window_handles
    login.driver.switch_to.window(win2[-1])
    # 点击详情立即申请
    login.driver.find_element(By.XPATH, position.yhrz_cpxq_ljsq).click()

    # 企业申请产品
def qy_sq():
    # 输入银行融资-申请界面-融资金额
    login.driver.find_element(By.XPATH, position.yhrz_sqjm_rzje).send_keys(parm.jine)
    # 选择贷款期限银行融资-申请界面-贷款期限
    login.driver.find_element(By.XPATH, position.yhrz_sqjm_dkqx).click()
    sleep(1)
    login.driver.find_element(By.XPATH, position.yhrz_sqjm_xzyf).click()
    # 选择用途银行融资-申请界面-融资用途
    login.driver.find_element(By.XPATH, position.yhrz_sqjm_rzyt).click()
    sleep(1)
    login.driver.find_element(By.XPATH, position.yhrz_sqjm_gmycl).click()
    # 确认申请银行融资-申请界面-确认申请
    login.driver.find_element(By.XPATH, position.yhrz_sqjm_qrsq).click()
    grzx = '//*[@class="el-select area-select"]/following::input[1]'
    WebDriverWait(login.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, grzx)))
    with allure.step("企业申请产品完成后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\sq.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\sq.png",
                           attachment_type=allure.attachment_type.PNG)
    print('企业申请业务产品成功')
    login.qysq_tui()  # 企业登录退出
# 银行一般信贷产品审核
def bank_yib_wsl():
    # 点击进件管理
    login.driver.find_element(By.XPATH, position.jjgl).click()
    # 点击一般信贷产品
    login.driver.find_element(By.XPATH, position.jjgl_ybcp).click()
    # --------------------点击未受理需求--------------------
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_wsl).click()
    # 点击搜索
    sleep(1)
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_ss).click()
    # 点击处理
    cl = '//*[@id="avue-view"]/div/div/div[1]/div[5]/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/div/div'
    WebDriverWait(login.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, cl)))
    login.driver.find_element(By.XPATH, cl).click()
    sleep(1)
    # 点击受理
    login.driver.find_element(By.XPATH, '//*[@class="footer-button certainly"]/following::div[4]').click()
    # 点击确认
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_qd1).click()
    sleep(1)
    with allure.step("未受理需求提交后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\wsl.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\wsl.png",
                           attachment_type=allure.attachment_type.PNG)
    print('银行完成未受理需求')

    # ----------点击需求审核管理-----------------------------
def bank_yib_shgl():
    sleep(1)
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_shgl).click()
    # 点击搜索
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_ss).click()
    sleep(1)
    # 点击处理
    cl1 = '//*[@id="avue-view"]/div/div/div/div[5]/div/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/div/div'
    login.driver.find_element(By.XPATH, cl1).click()
    sleep(1)
    # 启动待审
    login.driver.find_element(By.XPATH, '//*[@class="button"][2]').click()
    sleep(1)
    with allure.step("需求审核提交后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\shgl.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\shgl.png",
                           attachment_type=allure.attachment_type.PNG)
    print('银行完成需求审核')

    # -------------点击需求授信管理---------------------
def bank_yib_sxgl():
    sleep(1)
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_sxgl).click()
    # # 点击搜索
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_ss).click()
    sleep(1)
    # 点击处理
    cl2 = '//*[@id="avue-view"]/div/div/div/div[5]/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/div/div'
    login.driver.find_element(By.XPATH, cl2).click()
    # 输入授信编号
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[1]").send_keys(parm.sxbh())
    # 输入授信开始日期2023-05-09
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[2]").send_keys(parm.start_rq)
    # 输入授信结束日期
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[3]").send_keys(parm.end_rq)
    sleep(1)
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[1]").click()
    sleep(1)
    # 银行经办人
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[4]").send_keys(parm.jbr)
    # 输入联系人电话
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[5]").send_keys(parm.sjh)
    # 输入授信金额
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[7]").send_keys(parm.sxjine)
    sleep(1)
    # 点击担保类型
    login.driver.find_element(By.XPATH, "//*[contains(text(),'授信合同编号')]/following::input[6]").click()
    # 选择第一个担保方式，抵押
    dy = '//*[@class="v-modal"]/following::li[1]'
    element = login.driver.find_element(By.XPATH, dy)
    login.driver.execute_script("arguments[0].click();", element)

    # login.driver.find_element(By.XPATH, '//*[@class="v-modal"]/following::li[1]').click()
    # 点击授信通过
    login.driver.find_element(By.XPATH, '//*[contains(text(),"授信通过")]').click()
    sleep(1)
    with allure.step("需求授信提交后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\sxgl.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\sxgl.png",
                           attachment_type=allure.attachment_type.PNG)
    print('银行完成需求授信')
    # -----------------需求放款管理--------------------
def bank_yib_fkgl():
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_fkgl).click()
    # 点击搜索
    login.driver.find_element(By.XPATH, position.jjgl_ybcp_ss).click()
    sleep(1)
    # 点击放款
    fk = '//*[@id="avue-view"]/div/div/div[1]/div[4]/div/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/div/div[2]'
    login.driver.find_element(By.XPATH, fk).click()
    # 点击新增
    login.driver.find_element(By.XPATH, '//*[@class="add-button"]').click()
    sleep(1)
    # 输入放款合同号
    login.driver.find_element(By.XPATH, '//*[@class="el-dialog__wrapper apply-dialog add-loan-dialog"]/descendant::input[1]').send_keys(parm.fkbh())
    # 输入利率
    login.driver.find_element(By.XPATH, '//*[@class="el-dialog__wrapper apply-dialog add-loan-dialog"]/descendant::input[2]').send_keys(parm.fkll)
    # 输入贷款开始日期
    login.driver.find_element(By.XPATH, '//*[@class="el-dialog__wrapper apply-dialog add-loan-dialog"]/descendant::input[3]').send_keys(parm.start_rq)
    # 输入贷款结束日期
    login.driver.find_element(By.XPATH, '//*[@class="el-dialog__wrapper apply-dialog add-loan-dialog"]/descendant::input[4]').send_keys(parm.fk_end_rq)
    login.driver.find_element(By.XPATH, '//*[@class="el-dialog__wrapper apply-dialog add-loan-dialog"]/descendant::input[1]').click()
    sleep(1)
    # 输入放款金额
    login.driver.find_element(By.XPATH, '//*[@class="el-dialog__wrapper apply-dialog add-loan-dialog"]/descendant::input[5]').send_keys(parm.sxjine)
    # 点击保存
    login.driver.find_element(By.XPATH, '//*[contains(text(),"保存")]').click()
    sleep(1)
    # 点击确定
    login.driver.find_element(By.XPATH, "//*[@class='el-button el-button--default el-button--small el-button--primary ']").click()
    sleep(1)
    with allure.step("需求放款提交后截图"):
        login.driver.save_screenshot("D:\\Desktop\\login\SZZX\\report\\testwj\\fkgl.png")
        allure.attach.file("D:\\Desktop\\login\SZZX\\report\\testwj\\fkgl.png",
                           attachment_type=allure.attachment_type.PNG)
    print('银行完成需求放款')




