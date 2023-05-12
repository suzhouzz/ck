import string,random,datetime

# ------传参------------------
# 登录账户
lg_dan = ["17300010014"]
lg_duo = ["91320583338789088W", "91320506791986258J"]


lg_yw = 'admin666'  # 运维账号
lg_yw_fs = 'JFF001'  # 企业认证复审账号
# 设置密码
login_mima = 'szzx_1234'

# 登录地址
url_uat = 'http://121.229.17.62:10070/#/login'  # uat环境
url_uat_yw = 'http://121.229.17.62:10090/#/login'  # uat运维端

# --------注册认证--------
# 认证参数
def cs():
    zc_zh = '17600'        # 手机号
    uscc = '913205837965'   # 统一社会信用代码
    zzmc = 'SZGYYQuLtdd'        # 企业名称
    for j in range(6):
        h = random.choice(string.ascii_letters)
        k = random.randint(0,9)
        zc_zh += str(k)             # 随机添加数字的 手机号
        uscc += str(k)              # 随机添加数字的 统一社会信用代码
        zzmc += h               # 添加随机字母后的 企业名称
    return zc_zh, uscc, zzmc

zc_zh = cs()[0]     # 取手机号
uscc = cs()[1]      # 取统一社会信用代码
zzmc = cs()[2]      # 取企业名称

yyzz = r'D:\Desktop\测试相关\2-图片\33333.png'    # 营业执照图片地址
zzlx = '法人企业'       # 组织类型
khh = '苏州银行'        # 开户行
dz = '江苏省苏州市苏州工业园区苏桐路1号'        # 地址
xm = '肖天成'      # 姓名
sfz = '340311199007131813'      # 身份证
sjh = '17301112244'     # 手机号
sqs = r'D:\Desktop\测试相关\2-图片\担保确认函.pdf'     # 征信授权书
# ---------------企业申请银行产品----------
cpmc = '抵押快贷'
yinh = '建设银行'
jine = 6
lg_qy =  ["91320594692569651Q"]
# -----------银行产品审核参数-----------
# 建设银行二级管理员
lg_yh = ["jianshebank001"]

def sxbh():
    sxbh = 'YBCP'
    for j in range(10):
        k = random.randint(0, 9)
        sxbh += str(k)  # 随机添加数字的 手机号
    return sxbh                 # 授信编号


start_rq = datetime.datetime.now().strftime('%Y-%m-%d')     # 授信开始日期
end_rq = '2024-12-12'       # 授信结束日期
jbr = '张测试'             # 银行经办人
sxjine = jine * 10000
# 放款数据
def fkbh():
    fkbh = 'BPYBCP'
    for j in range(10):
        k = random.randint(0, 9)
        fkbh += str(k)  # 随机添加数字的 手机号
    return fkbh                 # 授信编号


fkll = 5        # 放款利率
fk_end_rq = '2024-05-09'        # 放款结束日期

