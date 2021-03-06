'''
1.UDP通讯协议的特点：
    将数据封装为数据包。面向无连接。
    每个数据包大小限制在64K。
    因为无连接，所以不可靠。
    因为不需要建立连接，所以速度快。
    UDP通讯是不分服务端和客服端的，只分发送端和接收端。

发送端的使用步骤：
    1.建立UDP的服务
    2.准备数据，把数据封装到数据包中发送。发送端的数据包要带上IP地址与端口号
    3.调用UDP的服务，发送数据
    4.关闭资源

接收端的使用步骤：
    1.建立UDP的服务
    2.准备空的数据包接收数据
    3.调用UDP的服务接收数据
    4.关闭资源


2.TCP通讯协议的特点：
    TCP是基于IO流进行数据传输的，面向连接。
    TCP进行数据传输时是没有大小限制的。
    TCP是面向连接的，通过三次握手机制保证数据完整性。是可靠协议。
    TCP是面向连接的，所以速度慢。
    TCP是区分客户端与服务端的。

TCP的客户端使用步骤：
    1.建立TCP的客户端服务
    2.获取对应的流对象
    3.写出或读取数据
    4.关闭资源

ServerSocket的使用步骤：
    1.建立TCP服务端的服务
    2.接收客户端的连接产生一个Socket
    3.获取对应的流对象读取或者写出数据
    4.关闭资源

'''

'''
3.端口
端口（Port）可以认为是计算机与外界通信交流的出口。
其中，硬件领域的端口又称接口，如 USB 端口、串行端口等；
软件领域的端口一般指网络中面向连接服务和无连接服务的通信协议端口，
是一种抽象的软件结构，包括一些数据结构和 I/O（基本输入输出）缓冲区。
端口是传输层的内容，是面向连接的，它们对应着网络上常见的一些服务。
这些常见的服务可划分为使用 TCP 端口（面向连接，如打电话）和使用 UDP 端口（无连接，如写信）两种。
在网络中可以被命名和寻址的通信端口是一种可分配资源，
由网络 OSI（Open SystemInterconnection，开放系统互联）协议可知，
传输层与网络层的区别是传输层提供进程通信能力，网络通信的最终地址不仅包括主机地址，
还包括可描述进程的某种标识。因此，当应用程序（调入内存运行后一般称为进程）
通过系统调用与某端口建立连接（Binding，绑定）之后，传输层传给该端口的数据都被相应进程所接收，
相应进程发给传输层的数据都从该端口输出。在网络技术中，
端口大致有两种意思：一是物理意义上的商品，如集线器、交换机、路由器等用于连接其他的网络设备的接口；
二是逻辑意义上的端口，一般指 TCP/IP协议中的端口，范围为 0～65 535，
如浏览网页服务的 80 端口，用于 FTP 服务的 21端口等。
逻辑意义上的端口有多种分类标准，常见的分类标准有如下两种。
1．按端口号分布划分
按端口号分布划分，可以分为公认端口、注册端口，以及动态和/或端口等。
（1）公认端口

公认端口包括端口号范围是 0～1023。它们紧密绑定于一些服务。通常，这些端口的通信明确表明了某种服务的协议，比如 80 端口分配给 HTTP 服务，21 端口分配给FTP 服务等。

（2）注册端口

注册端口端口号为 1024～49 151。它们松散地绑定于一些服务。也就是说，有许多服务绑定于这些端口，这些端口同样用于许多其他目的，比如许多系统处理动态端口从 1024 左右开始。

（3）动态和/或私有端口

动态和/或私有端口的端口号为 49 152～65 535。理论上，不应为服务分配这些端口。但是一些木马和病毒就比较喜欢这样的端口，因为这些端口不易引起人们的注意，从而很容易屏蔽。

2．按协议类型划分
根据协议类型，端口又可分为 TCP 端口和 UDP 端口两种。一般直接与接收方进行的连接方式，大多采用 TCP 协议。只是把信息放在网上发布出去而不去关心信息是否到达（也即“无连接方式”），则大多采用 UDP。

使用 TCP 协议的常见端口主要有如下几种。

（1）FTP 协议端口

FTP 即文件传输协议，使用 21 端口。某计算机开了 FTP 服务，便启动了文件传输服务，下载文件和上传主页都要用到 FTP 服务。

（2）Telnet 协议端口

该端口是一种用于远程登录的端口，用户可通过自己的身份远程连接到计算机上，通过这种端口可提供一种基于 DOS 模式的通信服务。如支持纯字符界面 BBS 的服务器会将23 端口打开，以对外提供服务。

（3）SMTP 协议端口

现在很多邮件服务器都使用这个简单邮件传送协议来发送邮件。如常见的免费邮件服务使用的就是此邮件服务端口，所以在电子邮件设置中经常会看到 SMTP 端口设置栏，服务器开放的是 25 号端口。

（4）POP3 协议端口

POP3 协议用于接收邮件，通常使用 110 端口。只要有使用 POP3 协议的程序（如 Outlook等），就可以直接使用邮件程序收到邮件（如 126 邮箱用户就没有必要先进入 126 网站，再

进入自己的邮箱来收信了。）

使用 UDP 协议的常见端口
（1）HTTP 协议端口

HTTP 是用户使用的最多的协议，即“超文本传输协议”。当上网浏览网页时，就要在提供网页资源的计算机上打开 80 号端口以提供服务。WWW 服务和 Web 服务器等使用的就是这个端口。

（2）DNS 协议端口

DNS 用于域名解析服务，这种服务在 Windows NT 系统中用得最多。Internet 上的每一台计算机都有一个网络地址与之对应，这个地址就是 IP 地址，它以纯数字形式表示。但由于这种表示方法不便于记忆，于是就出现了域名，访问计算机时只需要知道域名即可。域名和 IP 地址之间的变换由 DNS 服务器来完成（DNS 用的是 53 号端口）。

（3）SNMP 协议端口

SNMP 即简单网络管理协议，用来管理网络设备，使用 161 号端口。

（4）QQ 协议端口

QQ 程序既提供服务又接收服务，使用无连接协议，即 UDP 协议。QQ 服务器使用 8000号端口侦听是否有信息到来，客户端使用 4000 号端口向外发送信息。
'''
