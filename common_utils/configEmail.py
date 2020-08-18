import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail(object):
    def __init__(self, username, passwd, recv, title, content, file=None, ssl=False,
                 email_host='smtp.163.com', port=25, ssl_port=465):
        self.username = username
        self.passwd = passwd
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file
        self.email_host = email_host
        self.port = port
        self.ssl = ssl
        self.ssl_port = ssl_port

    def send_email(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file: #处理附件
            file_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！')
            else:
                att = MIMEText(f, "base64", "utf--8")
                att["Content-Type"] = 'application/octet-stream'
                new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (new_file_name)
                msg.attach(att)
        msg.attach(MIMEText(self.content))  # 邮件正文的内容
        msg['Subject'] = self.title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(self.username, self.passwd)
        try:
            self.smtp.sendmail(self.username, self.recv, msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


# if __name__ == '__main__':
#
#     m = SendEmail(
#         username='m18994736992_1@163.com',
#         passwd='AKZFZWBJQCUPTYIZ',
#         recv=['929240396@qq.com'],
#         title='测试邮件',
#         content='测试发送邮件',
#         file=r'C:\Users\Administrator\PycharmProjects\untitled2\reports\2020-08-16 01-32-38_result.html',
#         ssl=True,
#     )
#     m.send_email()