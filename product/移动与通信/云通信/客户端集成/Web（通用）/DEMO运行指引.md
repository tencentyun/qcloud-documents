## 1 官网sdk和demo

官网demo体验地址：
http://avc.qcloud.com/demo/webim/index.html

官网直播聊天室demo地址：
http://avc.qcloud.com/demo/webim/biggroup/mobile/index.html

直播聊天室demo运行指引地址：
https://www.qcloud.com/doc/product/269/4105

SDK包下载地址：
https://www.qcloud.com/product/im.html

## 2 准备环境

操作系统：windows 7 64位
web服务器软件：Apache 2.4 64位
运行demo也可以是其他web服务器软件，比如nginx。

### 2.1 安装apache

下载 64位 apache，地址：
http://www.apachehaus.com/cgi-bin/download.plx?dli=StmURFWaNJzTEx2KWVkRwAlVOpkVFVFdSxGZPVWQ

查看其他版本，地址
http://www.apachehaus.com/cgi-bin/download.plx

将下载的压缩包，解压到本地某个目录下，比如，放在D:\Program Files\目录下。

编辑apache配置文件：

```
D:\Program Files\Apache24\conf\httpd.conf
```

找到：Define SRVROOT 这一项，将其右方的值改为当前你Apache安装存放的目录地址，如下：

```
Define SRVROOT "D:/Program Files/Apache24"
```

继续找，找到：Listene 80，若你电脑的80端口被占用（可在cmd下用命令netstat -a查看），则将80端口改为别的端口，这里我们使用8080端口，如下：

```
Listen 8080
```

改完以上两个地方，记得保存httpd.conf文件。

接下来需要配置安装Apache的主服务，有了它，Apache才可启动：
打开CMD窗口，输入：

```
"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
```
该命令的意思是，安装apache服务，并将该服务名称命名为apache(你也可以改成别的)，回车。

正常安装完毕如下所示：

```
C:\Users\peakerdong>"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
[Fri May 20 13:39:16.474314 2016] [mpm_winnt:error] [pid 14884:tid 144] AH00433: apache: Service is already installed.
```

其中，Errors reported here must be corrected before the service can be started.意思是，若该句话后面有错误信息，则表示服务安装失败，需要先改正错误。若没有，则成功。

在安装目录中，找到D:\Program Files\Apache24\bin\ApacheMonitor.exe可执行文件，双击运行，桌面右下角会出现图标，双击打开窗口界面，会看到如图所示：
![](//mccdn.qcloud.com/static/img/02ef4d509e5579661953a9cc3dc4ee59/image.png)

点击左侧start，启动apache服务。

打开浏览器，输入访问 http://localhost
如果你设置的端口是8080，则访问地址是http://localhost:8080/
出现以下界面，表示apahce启动成功。
![](//mccdn.qcloud.com/static/img/1a051fa9cbedf08e55a979f732e824ef/image.png)

## 3 运行demo

从官网下载sdk和demo，将demo拷贝到apache web运行目录下：

```
D:\Program Files\Apache24\htdocs
```

### 3.1 运行demo（托管模式）

编辑demo根目录下的index.html。

修改帐号模式为1：

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=1;
```

修改业务信息：

```
//默认业务id
var sdkAppID = 1400001533;//开发者改成自己的业务id
var accountType = 792; //开发者改成自己的业务帐号类型
```


访问demo，这里拿谷歌浏览器举例。

打开浏览器输入地址：
http://localhost:8080/webim/index.html

显示demo首页：
![](//mccdn.qcloud.com/static/img/deaf3ceeb96916e35ce611602f4c0074/image.png)


点击确认会跳转到tls登录界面，直接点击游客登录，会跳回到首页，效果如下：

 ![](//mccdn.qcloud.com/static/img/37f008df51e98574886ac25a9becbd9f/image.png)

 ![](//mccdn.qcloud.com/static/img/0e1c29203362cac113a13ff1547dca47/image.png)

登录之后，可以搜素、添加好友，建群：

搜索好友：
 ![](//mccdn.qcloud.com/static/img/389d6b93abaa22584b176bfb8c8927b4/image.png)

点击添加好友：
 ![](//mccdn.qcloud.com/static/img/af15ddc4be05fb0de7c276cb18f6e375/image.png)

创建群：
![](//mccdn.qcloud.com/static/img/1a56d476ae8a092e0e9b3eab7597495e/image.png)

创建成功：
 ![](//mccdn.qcloud.com/static/img/0e5911c2b0ff9e9d899e159bd57fe628/image.png)



### 3.2 运行demo（独立模式）


编辑demo根目录下的index.html，

修改帐号模式为0：

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=0;
```

修改业务信息：

```
//demo appid 
var sdkAppID = 1400001533;//开发者改成自己的业务id
var accountType = 792; //开发者改成自己的业务帐号类型
```

访问demo，这里拿谷歌浏览器举例。

进入登录页：
![](//mccdn.qcloud.com/static/img/100c4f8b786c2ffa2f0c3ee3cff5f226/image.png)


填写登录用户信息identifier和userSig，userSig需要开发者在自己的服务器调用tls api生成。
独立模式生成usersig，请参考链接：
https://www.qcloud.com/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C
 ![](//mccdn.qcloud.com/static/img/8ae083b639696feec038a69861464e46/image.png)

点击确定，登录成功，这样就可以进行查找好友，建群，聊天等操作了。
 ![](//mccdn.qcloud.com/static/img/fd864c05877f3d2d7229041a0e33ca9d/image.png)

和好友聊天：
 ![](//mccdn.qcloud.com/static/img/456ac262b7b13ae8946e2875c68bd3de/image.png)

群聊：
 ![](//mccdn.qcloud.com/static/img/22b8afaab9f244e9bcf4cf34c4f0e42a/image.png)
