# 这只是简单的C-S模式的网络编程的基础 任何应用层协议都是通过这一套模版来通信
# 不同的应用层协议在于客户端服务器双方使用同一套报文格式 按照约定的格式交换数据
# 使得双方能有效提取自己想要的信息 而不同协议用的这一套报文格式不同 因此不能交叉通信
# 而这里只是简单的发送一段text 这在所有的应用层协议里都是共通的 浏览器则是通过http来访问
# 例如之前写的flask模版 确确实实是使用了http协议 本地flask识别浏览器发送的报文 而浏览器也能
# 识别flask 其中涉及的socket写入指定http报文等网络编程部分已经由flask和浏览器给出 包括更底层的
# 如何识别给定http协议的各个字段则 socket在创建时仅指定了ip版本和tcp 可见涉及到应用层的部分
# 都得由浏览器和服务器共同完成 类似的邮件服务器上运行了不同的应用层协议 因此浏览器对另一套应用层协议不再服务
# # 当然webEmail涉及到其他 而邮件服务器上只识别SMTP协议的字段
# 目前的理解是 网络编程主要就是应用层协议编程 对于TCP/IP部分只需在创建socket时声明即可
from socket import *

serverName = '127.0.0.1'
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_STREAM)  # 指定IPv4和TCP
clientSocket.connect((serverName, serverPort))
message = input("请输入一段小写字母:")
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print(modifiedMessage.decode())
