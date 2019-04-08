## 官网 SDK 和 Demo

- 单击体验 [官网 Demo](http://avc.qcloud.com/demo/webim/index.html)

- 单击体验 [官网直播聊天室 Demo](http://avc.qcloud.com/demo/webim/biggroup/mobile/index.html)

- 单击查看 [直播聊天室 Demo 运行指引](https://cloud.tencent.com/doc/product/269/4105)

- 单击下载 [SDK 包](http://sqimg.qq.com/expert_qq/webim/WEB_IMSDK.zip)

## 准备环境

操作系统：Windows 7 64 位
Web 服务器软件：Apache 2.4 64 位
>注：运行 Demo 也可以是其他 Web 服务器软件，比如 nginx。

### 安装 Apache

- 单击下载 [64 位 Apache](http://www.apachehaus.com/cgi-bin/download.plx?dli=StmURFWaNJzTEx2KWVkRwAlVOpkVFVFdSxGZPVWQ)。其他版本的 Apache 请单击了解 [其他版本的 Apache ](http://www.apachehaus.com/cgi-bin/download.plx)。

- 将下载的压缩包，解压到本地某个目录下，比如，放在 `D:\Program Files\ ` 目录下。

- 编辑 Apache配置文件：

```
D:\Program Files\Apache24\conf\httpd.conf
```

- 找到 `Define SRVROOT` 这一项，将其右方的值改为当前您 Apache 安装存放的目录地址，如下：

```
Define SRVROOT "D:/Program Files/Apache24"
```

- 继续找，找到 `Listene 80`，若您电脑的 80 端口被占用（可在 `cmd` 下用命令 `netstat -a` 查看），则将 80 端口改为别的端口，这里我们使用 8080 端口，如下：

```
Listen 8080
```

- 改完以上两个地方，记得保存 `httpd.conf` 文件。

- 接下来需要配置安装Apache的主服务，有了它，Apache才可启动。打开CMD窗口，输入以下命令，该命令的意思是，安装 Apache 服务，并将该服务名称命名为 Apache（也可以改成别的），回车。

```
"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
```

- 正常安装完毕如下所示：

```
C:\Users\peakerdong>"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
[Fri May 20 13:39:16.474314 2016] [mpm_winnt:error] [pid 14884:tid 144] AH00433: apache: Service is already installed.
```

>注：其中，`Errors reported here must be corrected before the service can be started.` 意思是，若该句话后面有错误信息，则表示服务安装失败，需要先改正错误。若没有，则成功。

- 在安装目录中，找到 `D:\Program Files\Apache24\bin\ApacheMonitor.exe` 可执行文件，双击运行，桌面右下角会出现图标，双击打开窗口界面，会看到如图所示。
-
![](//mccdn.qcloud.com/static/img/02ef4d509e5579661953a9cc3dc4ee59/image.png)

- 单击左侧 【start】，启动 Apache 服务。

- 打开浏览器，输入访问 `http://localhost`，如果您设置的端口是 8080，则访问地址是 `http://localhost:8080/`，出现以下界面，表示 Apahce启动成功。

![](//mccdn.qcloud.com/static/img/1a051fa9cbedf08e55a979f732e824ef/image.png)

## 运行 Demo

从官网下载 SDK 和 Demo，将 Demo 拷贝到 Apache web 运行目录下。

```
D:\Program Files\Apache24\htdocs
```

### 运行 Demo（托管模式）

- 编辑 Demo根目录下的 `index.html`。

- 修改帐号模式为 1。

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=1;
```

- 修改业务信息。

```
//默认业务 ID
var sdkAppID = 1400001533;//开发者改成自己的业务 ID
```

- 访问 Demo，这里拿谷歌浏览器举例。打开浏览器输入地址。

```
http://localhost:8080/webim/index.html
```

- 显示 Demo 首页。

![](//mccdn.qcloud.com/static/img/deaf3ceeb96916e35ce611602f4c0074/image.png)


- 单击确认会跳转到 TLS 登录界面，直接单击游客登录，会跳回到首页，效果如下：

 ![](//mccdn.qcloud.com/static/img/37f008df51e98574886ac25a9becbd9f/image.png)

 ![](//mccdn.qcloud.com/static/img/0e1c29203362cac113a13ff1547dca47/image.png)

- 登录之后，可以搜素、添加好友，建群。搜索好友：

 ![](//mccdn.qcloud.com/static/img/389d6b93abaa22584b176bfb8c8927b4/image.png)

- 单击添加好友：

 ![](//mccdn.qcloud.com/static/img/af15ddc4be05fb0de7c276cb18f6e375/image.png)

- 创建群：

![](//mccdn.qcloud.com/static/img/1a56d476ae8a092e0e9b3eab7597495e/image.png)

- 创建成功：

 ![](//mccdn.qcloud.com/static/img/0e5911c2b0ff9e9d899e159bd57fe628/image.png)



### 运行 Demo（独立模式）


- 编辑 Demo 根目录下的 `index.html`，修改帐号模式为 0。

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=0;
```

- 修改业务信息：

```
//demo appid
var sdkAppID = 1400001533;//开发者改成自己的业务 ID
```

- 访问 Demo，这里拿谷歌浏览器举例。进入登录页：

![](//mccdn.qcloud.com/static/img/100c4f8b786c2ffa2f0c3ee3cff5f226/image.png)

- 填写登录用户信息 `identifier` 和 `userSig`，`userSig` 需要开发者在自己的服务器调用 TLS API 生成。详细参见 [TLS 后台 API 使用手册](https://cloud.tencent.com/document/product/269/1510)。

![](//mccdn.qcloud.com/static/img/8ae083b639696feec038a69861464e46/image.png)

- 单击确定，拿到登录用户信息 `identifier` 和 `userSig` 放入 `loginInfo` 去登录 SDK。

```
//当前用户身份
var loginInfo = {
     'sdkAppID': sdkAppID, //用户所属应用 ID,必填
     'appIDAt3rd': sdkAppID, //用户所属应用 ID，必填
      'identifier': ‘xxxxxx’, //当前用户 ID，需要开发者填写
      'identifierNick': null, //当前用户昵称，选填
      'userSig': 'xxxxxxx', //当前用户身份凭证，需要开发者填写
      'headurl': 'img/2016.gif'//当前用户默认头像，选填
 };
```

- 登录成功，这样就可以进行查找好友，建群，聊天等操作了。
 ![](//mccdn.qcloud.com/static/img/fd864c05877f3d2d7229041a0e33ca9d/image.png)

- 和好友聊天：
 ![](//mccdn.qcloud.com/static/img/456ac262b7b13ae8946e2875c68bd3de/image.png)

- 群聊：
 ![](//mccdn.qcloud.com/static/img/22b8afaab9f244e9bcf4cf34c4f0e42a/image.png)
