### 第二章

#### 课件作业 telnet whu.edu.cn 25

输入如下指令或执行相应操作，以实现登录邮箱并发送邮件（默认地，每一行的结尾均存在换行\r\n，对应于‘ENTER’键）：

```
telnet whu.edu.cn 25
[同时按下 ‘CTRL’+‘]’ ]
[按‘ENTER’]
HELO ***
AUTH LOGIN
[输入邮箱的base64编码]
[输入密码的base64编码]
MAIL FROM: <***@whu.edu.cn>
RCPT TO: <***@outlook.com>
DATA
Date: Sat Mar 14 21:04:27 2020
From: ***@whu.edu.cn
To: ***@outlook.com
Cc: ***@whu.edu.cn
Subject: test

This is the body of test mail.
.
QUIT
```

值得注意的是，在验证身份时需要输入邮箱、密码的base64编码表示。可以使用Python的bytes函数转换成字节表示，再调用base64模块的b64encode函数得到。指令内容、响应内容、邮件接收结果如下：

<img src="static\telnet_whu_25.png" alt="telnet_whu_25" style="zoom: 67%;" />

<img src="static\smtp_mail_received.png" alt="smtp_mail_received" style="zoom:50%;" />

#### 课件作业 telnet maths.whu.edu.cn 80

输入如下指令或执行相应操作（默认地，每一行的结尾均存在换行\r\n，对应于‘ENTER’键）：

```
telnet maths.whu.edu.cn 80
[同时按下 ‘CTRL’+‘]’ ]
[按‘ENTER’]
GET https://maths.whu.edu.cn/ HTTP/2.0
Host: maths.whu.edu.cn
[按‘ENTER’]
```

指令内容、响应内容如下：

<img src="static\telnet_maths_80.png" alt="telnet_maths_80" style="zoom:67%;" />

***

#### P5

a. 由状态码200以及状态短语OK可知服务器成功找到那个文档了。头部域名“Date“指示的值表明，该文档提供回答的时间为”Tue, 07 Mar 2008 12:39:45 GMT”。

b. 头部域名“Last-Modified“指示的值表明，文档最后修改的时间为”Sat, 10 Dec 2005 18:27:46 GMT”。

c. 头部域名“Content-Length”指示的值表明，该文档被返回的字节有3874个。

d. 观察两个连续的“\<cr\>\<lf\>”后的主体可知，文档被返回的前5个字节是“<!doc“。由“Connection: Keep-Alive"可知，该服务器同意一条持续连接。

#### P9

a.

已知接入链路速率为15Mbps，接入链路的因特网一侧的路由器转发一个HTTP请求开始，到接收到其相应的平均时间为3sec，对象平均大小为850,000bit，从这个机构的浏览器到初始服务器的平均请求率是16/sec。

首先，跨越接入链路发送一个对象的平均时间Δ =

850000bit / 15Mbps ≈ 0.057 sec，对象对该接入链路的平均到达率等于从机构网的浏览器到初始服务器的平均请求率，即β = 16/sec。根据题意描述，平均因特网时延t = 3 sec。

根据题目定义，总的平均响应时间 T = Δ / (1 - Δβ) + t = 0.057sec / (1 - 0.057sec  * 16/sec) + 3sec ≈ 0.648sec + 3sec = 3.648 sec。

b.

此时对象对该接入链路的平均到达率β = 16/sec * 0.6 = 9.6/sec。

从而，平均接入时延<img src='http://latex.codecogs.com/gif.latex?t_{access}' alt="t_{access}">= Δ / (1 - Δβ) ≈ 0.126 sec。

总的平均响应时间 T = 0.6 * (<img src='http://latex.codecogs.com/gif.latex?t_{access}' alt="t_{access}"> + t) + 0.4 * (~msecs) ≈ 0.6 * (0.126sec + 3sec) + 0.4 * 0sec ≈ 1.876 sec。

