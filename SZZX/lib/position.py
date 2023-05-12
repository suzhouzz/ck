# 定位方式XPATH:选取当前节点的所有后代元素（子、孙等）descendant
# following选取文档中当前节点的结束标签之后的所有节点
# preceding选取文档中当前节点的开始标签之前的所有节点
# 点击个人中心
grzx = '//*[@class="el-select area-select"]/following::input[1]'
# 企业-金融集市
jrjs = "//*[contains(text(),'金融集市')]"

# 银行融资-产品名称输入框
yhrz_cpmc = "input[placeholder='请输入产品名称']"

# 银行融资-机构名称输入框
yhrz_jgmc = "input[placeholder='请输入机构名称']"

# 银行融资-搜索
yhrz_ss = '//*[@class="filter_box"]/preceding::div[2]'

# 银行融资-列表-立即申请
yhrz_lb_ljsq = '//*[@class="filter_box"]/following::div[338]'

# 银行融资-产品详情-立即申请
yhrz_cpxq_ljsq = '//*[@class="button-item"][1]'

# 银行融资-申请界面-融资金额
yhrz_sqjm_rzje = "//*[contains(text(),'融资金额（万元）：')]/following::input[1]"

# 银行融资-申请界面-贷款期限
yhrz_sqjm_dkqx = "//*[contains(text(),'贷款期限（月）：')]/following::div[3]"
yhrz_sqjm_xzyf = "//*[contains(text(),'12个月')]"  # 选择

# 银行融资-申请界面-融资用途
yhrz_sqjm_rzyt = "//*[contains(text(),'融资用途：')]/following::div[2]"
yhrz_sqjm_gmycl = "//*[contains(text(),'流动资金周转')]"  # 选择

# 银行融资-申请界面-确认申请
yhrz_sqjm_qrsq = "//*[contains(text(),'确认申请')]"

# --------------银行登录-------------
# 进件管理
jjgl= "//*[contains(text(),'进件管理')]"

# 进件管理-一般产品-未受理需求
jjgl_ybcp = "//*[contains(text(),'一般信贷产品')]"

# 进件管理-一般产品-未受理需求
jjgl_ybcp_wsl = "//*[contains(text(),'一般信贷产品')]/following::span[1]"

# 进件管理-一般产品-需求审核管理
jjgl_ybcp_shgl = "//*[contains(text(),'一般信贷产品')]/following::span[2]"

# 进件管理-一般产品-需求授信管理
jjgl_ybcp_sxgl = "//*[contains(text(),'一般信贷产品')]/following::span[3]"

# 进件管理-一般产品-需求放款管理
jjgl_ybcp_fkgl = "//*[contains(text(),'一般信贷产品')]/following::span[4]"

# 搜索按钮
jjgl_ybcp_ss = "//*[@class='search-button'][1]"

# 确定按钮
jjgl_ybcp_qd = '//*[contains(text(),"确定")]'

jjgl_ybcp_qd1 = '//*[@class="el-dialog__wrapper alert-dialog"]/descendant::div[11]'
