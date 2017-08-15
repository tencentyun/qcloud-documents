## 1 官网sdk和demo

SDK包下载地址：
https://www.qcloud.com/product/im.html

直播聊天室demo体验地址：
http://avc.qcloud.com/demo/webim/biggroup/mobile/index.html

直播聊天室demo二维码：
![](//mccdn.qcloud.com/static/img/a188f7fd653c8237b362a7adea1f63b1/image.png)

通用demo地址：
http://avc.qcloud.com/demo/webim/index.html

通用demo运行指引地址：
https://www.qcloud.com/doc/product/269/4196


## 2 准备环境

操作系统：windows 7 64位
web服务器软件：Apache 2.4 64位
运行demo也可以是其他web服务器软件，比如nginx。

### 2.1 安装apache

下载 64位 apache，地址：
http://www.apachehaus.com/cgi-bin/download.plx?dli=StmURFWaNJzTEx2KWVkRwAlVOpkVFVFdSxGZPVWQ

查看其他版本，地址：
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

### 3.1 准备直播大群id

运行Demo之前，需要创建一个AVChatRoom类型（直播聊天室）的群组id。

可以通过restapi 创建，参考连接：
https://www.qcloud.com/doc/product/269/%E5%88%9B%E5%BB%BA%E7%BE%A4%E7%BB%84

也可以使用在其他平台（android或者ios）上创建的直播聊天室id。

restapi调试地址：
https://avc.qcloud.com/im/APITester/APITester.html

### 3.2 运行demo（托管模式）

编辑sdk包中的直播聊天室demo根目录下的index.html。

修改帐号模式为1：

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=1;
```

修改业务信息：

```
//默认业务id
var sdkAppID = 1400001692;//开发者改成自己的业务id
var accountType = 884; //开发者改成自己的业务帐号类型
```

修改直播大群id：

```
//默认房间群ID，开发者可以改成自己的直播聊天室id
var avChatRoomId = '@TGS#aJIPTVAEE'; 
```

访问demo，这里拿谷歌浏览器举例。

打开浏览器输入地址：
http://localhost:8080/webim/biggroup/mobile/index.html

效果如下：
![](//mccdn.qcloud.com/static/img/9994fb0d0f4073a77f5766a7abd5283d/image.png)

模拟手机访问，按F12，点击下图箭头所指的手机图标：
![](//mccdn.qcloud.com/static/img/e71c925af3ea9d2e04ca0dbbea86fcee/image.png)

点击下方评论或点赞按钮，会跳转到tls登录界面，直接点击游客登录，会跳回到首页：
![](//mccdn.qcloud.com/static/img/c604fbde4569278532eebc6d5eb7ebc7/image.png)

![](//mccdn.qcloud.com/static/img/1f39be07a839ff47bd13a08a58b64647/image.png)

登录之后，可以评论，点赞：
![](//mccdn.qcloud.com/static/img/aa37dcc2c32aa47c57f107bd0ea8785c/image.png)

### 3.3 运行demo（独立模式）


编辑demo根目录下的index.html，

修改帐号模式为0：

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=0;
```

修改业务信息：

```
//demo appid 
var sdkAppID = 1400001692;//开发者改成自己的业务id
var accountType = 884; //开发者改成自己的业务帐号类型
```

修改直播大群id：

```
//默认房间群ID，开发者可以改成自己的直播聊天室id
var avChatRoomId = '@TGS#aJIPTVAEE'; 
```

访问demo，这里拿谷歌浏览器举例。

打开浏览器输入地址：
http://localhost:8080/webim/biggroup/mobile/index.html

效果如下：

![](http://cs-1253400008.coscd.myqcloud.com/%E7%8B%AC%E7%AB%8B%E6%A8%A1%E5%BC%8F%E4%B8%80%E5%BC%80%E5%A7%8B%E6%95%88%E6%9E%9C.png)

模拟手机访问，按F12，点击下图箭头所指的手机图标：

![](http://cs-1253400008.coscd.myqcloud.com/%E7%8B%AC%E7%AB%8B%E6%A8%A1%E5%BC%8F%E7%99%BB%E5%BD%95demo.png)

填写登录用户信息identifier和userSig，userSig需要开发者在自己的服务器调用tls api生成。
独立模式生成usersig，请参考链接：
https://www.qcloud.com/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C
 ![](http://cs-1253400008.coscd.myqcloud.com/%E7%8B%AC%E7%AB%8B%E6%A8%A1%E5%BC%8F%E7%99%BB%E5%BD%95%E5%B7%B2%E8%BE%93%E5%85%A5%E5%B8%90%E5%8F%B7.png)

点击确定，拿到登录用户信息identifier和userSig放入loginInfo去登录sdk：

```
//当前用户身份
var loginInfo = {
     'sdkAppID': sdkAppID, //用户所属应用id,必填
     'appIDAt3rd': sdkAppID, //用户所属应用id，必填
     'accountType': accountType, //用户所属应用帐号类型，必填
      'identifier': ‘xxxxxx’, //当前用户ID，需要开发者填写
      'identifierNick': null, //当前用户昵称，选填
      'userSig': 'xxxxxxx', //当前用户身份凭证，需要开发者填写
      'headurl': 'img/2016.gif'//当前用户默认头像，选填
 };

```
登录成功：
评论，点赞：

![](http://cs-1253400008.coscd.myqcloud.com/%E7%82%B9%E8%B5%9E%E3%80%81%E8%AF%84%E8%AE%BA.png)
