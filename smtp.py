import smtplib
from email.mime.text import MIMEText
from email.header import Header
from log import log
from strategy import strategy


class stmp:
    def  email_server(emailContext):
        # 第三方 SMTP 服务
        mail_host = "smtp.qq.com"  # 设置服务器
        mail_user = "1736101137@qq.com"  # 用户名
        mail_pass = "wgsmxhyptgdsbfcd"  # 口令

        sender = '1736101137@qq.com'
        receivers = ['3208703659@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        message = MIMEText(emailContext, 'plain', 'utf-8')
        message['From'] = Header("财神爷", 'utf-8')
        message['To'] = Header("zxy", 'utf-8')

        subject = 'zxy的股票邮件'
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            log.logger.info("邮件发送成功")
        except smtplib.SMTPException:
            log.logger.error("Error: 无法发送邮件")

    def task_strategy01_corn(self):
        log.logger.info("定时器开始")
        code = strategy().strategy01()
        if (len(code) > 0):
            emailContext = "买入条件：0，基金选过的股票。1，5日均线低于60日均线，当日成交量高于5日均线成交量。2，连续下跌5天以上。3，每天两点涨幅大于3%且小于5%。满足以上的股票代码：" + str(
                code)
            stmp.email_server(emailContext)
        log.logger.info("定时器结束")

    def task_strategy02_corn(self):
        log.logger.info("定时器开始")
        code = strategy().strategy02()
        if (len(code) > 0):
            emailContext = "买入条件：0，淘股吧热门前20。1，5日均线低于60日均线，当日成交量高于5日均线成交量。2，连续上涨2天以上。3，当时涨幅大于3%且小于5%。满足以上的股票代码：" + str(
                code)
            stmp.email_server(emailContext)
        log.logger.info("定时器结束")
