import pymysql
from data import parm


def dx_yzm(sjh):
        conn = pymysql.connect(
                user='cfsp_query',
                password='cfsp_query',
                host='172.19.34.13',
                database='cfsp_base',
                port=3306,
                charset='UTF8')

        cur = conn.cursor()

        # cur.execute("select left(substring_index(content, '您的验证码是:',-1),6) from blade_sms_record where mobiles = '17300010015' order by send_time desc limit 1")
        # cur.execute("select left(substring_index(content, '您的验证码是:',-1),6) from blade_sms_record order by send_time desc limit 1")

        cur.execute("select left(substring_index(content, '您的验证码是:',-1),6) from blade_sms_record "
                    "where mobiles = %s order by id desc limit 1" % sjh)
        data = cur.fetchall()
        for i in data:
                for j in i:
                        return j
