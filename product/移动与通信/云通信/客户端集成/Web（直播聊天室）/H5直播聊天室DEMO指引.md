## 官网 SDK 和 Demo

- 单击下载 [SDK 包](http://sqimg.qq.com/expert_qq/webim/WEB_IMSDK.zip)。

- 单击体验 [直播聊天室 Demo](http://avc.cloud.tencent.com/demo/webim/biggroup/mobile/index.html)，或者扫描下方二维码：

	![](//mccdn.qcloud.com/static/img/a188f7fd653c8237b362a7adea1f63b1/image.png)

-  单击体验 [通用 Demo](http://avc.cloud.tencent.com/demo/webim/index.html)。

-  单击了解 [通用 Demo 运行指引](https://cloud.tencent.com/doc/product/269/4196)。

## 准备环境

**操作系统：**Windows 7 64 位
**Web 服务器软件：**Apache 2.4 64 位

> 注：运行 Demo 也可以是其他 Web 服务器软件，比如 nginx。

### 安装 Apache

单击下载 [64 位 Apache](http://www.apachehaus.com/cgi-bin/download.plx?dli=StmURFWaNJzTEx2KWVkRwAlVOpkVFVFdSxGZPVWQ)，或者单击下载 [其他版本](http://www.apachehaus.com/cgi-bin/download.plx)。将下载的压缩包，解压到本地某个目录下，比如，放在 `D:\Program Files\ `目录下，编辑 Apache 配置文件。

```
D:\Program Files\Apache24\conf\httpd.conf
```

找到 `Define SRVROOT` 这一项，将其右方的值改为当前您 Apache 安装存放的目录地址。

```
Define SRVROOT "D:/Program Files/Apache24"
```

继续找，找到 `Listene 80`，若您电脑的 80 端口被占用（可在 CMD 下用命令 `netstat -a` 查看），则将 80 端口改为别的端口，这里我们使用 8080 端口。

```
Listen 8080
```

> **注意：**
> 改完以上两个地方，记得保存 `httpd.conf` 文件。

接下来需要配置安装 Apache 的主服务，有了它，Apache 才可启动。打开 CMD 窗口，输入以下命令。该命令的意思是，安装 Apache 服务，并将该服务名称命名为 Apache（您也可以改成别的），回车。

```
"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
```

正常安装完毕如下所示，其中 `Errors reported here must be corrected before the service can be started.` 意思是，若该句话后面有错误信息，则表示服务安装失败，需要先改正错误。若没有，则成功。

```
C:\Users\peakerdong>"D:\Program Files\Apache24\bin\httpd.exe" -k install -n apache
[Fri May 20 13:39:16.474314 2016] [mpm_winnt:error] [pid 14884:tid 144] AH00433: apache: Service is already installed.
```

在安装目录中，找到 `D:\Program Files\Apache24\bin\ApacheMonitor.exe` 可执行文件，双击运行，桌面右下角会出现图标，双击打开窗口界面，会看到如图所示。单击左侧 start，启动 Apache 服务。

![](//mccdn.qcloud.com/static/img/02ef4d509e5579661953a9cc3dc4ee59/image.png)

打开浏览器，输入访问 `http://localhost`。如果您设置的端口是 8080，则访问地址是 `http://localhost:8080/`
出现以下界面，表示 Apahce 启动成功。

![](//mccdn.qcloud.com/static/img/1a051fa9cbedf08e55a979f732e824ef/image.png)

## 运行 Demo

从官网下载 SDK 和 Demo，将 Demo 拷贝到 Apache Web 运行目录下。

```
D:\Program Files\Apache24\htdocs
```

### 准备直播大群 ID

运行 Demo 之前，需要创建一个 AVChatRoom 类型（直播聊天室）的群组 ID。可以通过 restapi 创建，也可以使用在其他平台（Android 或者 iOS）上创建的直播聊天室 ID。详情请参考 [创建群组](https://cloud.tencent.com/doc/product/269/%E5%88%9B%E5%BB%BA%E7%BE%A4%E7%BB%84) 。

**restapi 调试地址：**

`https://avc.cloud.tencent.com/im/APITester/APITester.html`

### 运行 Demo（托管模式）

编辑 SDK 包中的直播聊天室 Demo 根目录下的 `index.html`，**修改帐号模式为 1：**

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=1;
```

**修改业务信息：**

```
//默认业务 ID
var sdkAppID = 1400001692;//开发者改成自己的业务 ID
var accountType = 884; //开发者改成自己的业务帐号类型
```

**修改直播大群 ID：**

```
//默认房间群 ID，开发者可以改成自己的直播聊天室 ID
var avChatRoomId = '@TGS#aJIPTVAEE';
```

访问 Demo，这里以谷歌浏览器为例。**打开浏览器输入地址：**

`http://localhost:8080/webim/biggroup/mobile/index.html`

**效果如下：**

![](//mccdn.qcloud.com/static/img/9994fb0d0f4073a77f5766a7abd5283d/image.png)

**模拟手机访问，按 F12，单击下图箭头所指的手机图标：**

![](//mccdn.qcloud.com/static/img/e71c925af3ea9d2e04ca0dbbea86fcee/image.png)

**单击下方评论或点赞按钮，会跳转到 TLS 登录界面，直接单击游客登录，会跳回到首页：**

![](//mccdn.qcloud.com/static/img/c604fbde4569278532eebc6d5eb7ebc7/image.png)

![](//mccdn.qcloud.com/static/img/1f39be07a839ff47bd13a08a58b64647/image.png)

**登录之后，可以评论，点赞：**

![](//mccdn.qcloud.com/static/img/aa37dcc2c32aa47c57f107bd0ea8785c/image.png)

### 运行 Demo（独立模式）


编辑 Demo 根目录下的 `index.html`，**修改帐号模式为 0：**

```
//帐号模式，0-表示独立模式，1-表示托管模式，开发者根据自己的模式，改成相应的值。
var accountMode=0;
```

**修改业务信息：**

```
//demo appid
var sdkAppID = 1400001692;//开发者改成自己的业务 ID
var accountType = 884; //开发者改成自己的业务帐号类型
```

**修改直播大群 ID：**

```
//默认房间群ID，开发者可以改成自己的直播聊天室 ID
var avChatRoomId = '@TGS#aJIPTVAEE';
```

访问 Demo，这里以谷歌浏览器为例，**打开浏览器输入地址：**

`http://localhost:8080/webim/biggroup/mobile/index.html`

**效果如下：**

![](//mccdn.qcloud.com/static/img/9994fb0d0f4073a77f5766a7abd5283d/image.png)

**模拟手机访问，按 F12，单击下图箭头所指的手机图标：**


![](//mccdn.qcloud.com/static/img/e71c925af3ea9d2e04ca0dbbea86fcee/image.png)

填写登录用户信息 `identifier` 和 `userSig`，`userSig` 需要开发者在自己的服务器调用 TLS API 生成。详情参考 [TLS 后台 API 使用手册](https://cloud.tencent.com/doc/product/269/TLS%E5%90%8E%E5%8F%B0API%E4%BD%BF%E7%94%A8%E6%89%8B%E5%86%8C)。

![](//mccdn.qcloud.com/static/img/c604fbde4569278532eebc6d5eb7ebc7/image.png)

单击确定，拿到登录用户信息 `identifier` 和 `userSig` 放入 `loginInfo` 去登录 SDK。

```
//当前用户身份
var loginInfo = {
     'sdkAppID': sdkAppID, //用户所属应用 ID,必填
     'appIDAt3rd': sdkAppID, //用户所属应用 ID，必填
     'accountType': accountType, //用户所属应用帐号类型，必填
      'identifier': ‘xxxxxx’, //当前用户 ID，需要开发者填写
      'identifierNick': null, //当前用户昵称，选填
      'userSig': 'xxxxxxx', //当前用户身份凭证，需要开发者填写
      'headurl': 'img/2016.gif'//当前用户默认头像，选填
 };
```

**登录成功可以进行评论，点赞：**

![](//mccdn.qcloud.com/static/img/aa37dcc2c32aa47c57f107bd0ea8785c/image.png)
