本文介绍如何快速地将腾讯云 TRTC ActiveX 控件集成到 IE Web 项目中。

## 开发环境要求
- 操作系统：Windows 7及以上版本。
- 浏览器：IE 9及以上版本，推荐使用 IE 11版本。
- 开发环境：VS Code 或其他可以编辑 HTML 网页代码的编辑器。

## 集成 TRTC ActiveX 控件
本节以创建一个简单的 HTML 网页为例，介绍如何在 HTML Web 工程中集成 ActiveX 控件。

[](id:step1)
### 步骤1：下载 Windows ActiveX 安装包
[下载 ActiveX 安装包](https://liteav.sdk.qcloud.com/download/latest/TXLiteAVSDK_TRTC_Win_ActiveX_latest.zip)，目录如下。

| 文件名  | 详情                                                         |
| ------- | ------------------------------------------------------------ |
| TRTC-API-Example-ActiveX    | 包含了 Demo 所需的 HTML 和 JS 源码，可以直接参考如何使用 ActiveX 插件开发音视频。 |
| SDK     | 包含了 ActiveX SDK 的产物 LiteAVActiveXSDK.cab。 |

[](id:step2)
### 步骤2：加载 ActiveX 控件
在自己的项目工程中，建立 `OBJECT` 对象，并设置 `CLASSID`，如下示例：
```html
<!DOCTYPE html>
<HTML>
<HEAD>
	<TITLE>TestMyActiveXDemo</TITLE>
</HEAD>
<BODY>
	<div class="Local">
		<OBJECT ID="obj_user_ocx" class="obj_user"
			    codebase="./SDK/LiteAVActiveXSDK.cab#version=1,0,0,1"
			    CLASSID="CLSID:99DD15EF-B353-4E47-9BE7-7DB4BC13613C">
		</OBJECT>
	</div>
	<p><input type="button" value="Get SDK Version" id="GetVersion" onclick="GetVersion();"></input>
</BODY>

<script language="javascript">
	function GetVersion() {
		var version = obj_user_ocx.getVersion();
		alert("SDK version: " + version);
	}
</script>

<script language="javascript" for="obj_user_ocx" event="onError(code, message)" type="text/javascript">
	alert('onError:' + code + ' message:' + message);
</script>
</HTML>
```
如上示例，单击按钮可调用 `getVersion()` 接口弹出 SDK 版本号。
![](https://qcloudimg.tencent-cloud.cn/raw/8fe71e851c906bb0a93e0acb1a967bd5.png)
也可监听 `onError(code, message)` 的回调通知。
```javascript
<script language="javascript" for="obj_user_ocx" event="onError(code, message)" type="text/javascript">
  alert('onError:' + code + ' message:' + message);
</script>
```

[](id:step3)
### 步骤3: 插件部署
将 [上述示例代码](#step2) 另存为 index.html 文件，存放到您的 Web 服务器上，并将 SDK 目录（内含 LiteAVActiveXSDK.cab 插件包） 拷贝到与 index.html 同级目录下（即 SDK 目录和 `index.html` 位于同一目录，LiteAVActiveXSDK.cab 位于 SDK 目录下），并启动web服务。

[](id:step4)
### 步骤4：插件安装与加载
打开 IE 浏览器，在地址栏输出您的服务器 IP 地址进行请求（即您启动的 Web 服务的地址：`http://xxx.xxx.xxx.xxx/index.html`），浏览器会弹出提示进行插件的下载和安装，完成后即可正常访问网址及加载ActiveX控件。

[](id:step5)
### 步骤5：插件升级
当有新的 `LiteAVActiveXSDK.cab` 安装包需要升级时，可以将新的 LiteAVActiveXSDK.cab 包放到 SDK 目录下覆盖原来的 LiteAVActiveXSDK.cab 包，并将新的 index.html 文件放到 Web 服务器上覆盖原来的 index.html 文件。此时，HTML 中的代码如下：
```html
<div class="Local">
	<OBJECT ID="obj_user_ocx" class="obj_user"
			codebase="./SDK/LiteAVActiveXSDK.cab#version=1,0,0,2"
			CLASSID="CLSID:99DD15EF-B353-4E47-9BE7-7DB4BC13613C">
	</OBJECT>
</div>
```
当请求时，IE 浏览器会根据 `codebase="./SDK/LiteAVActiveXSDK.cab#version=1,0,0,2` 指定的版本号与本地保存的 LiteAVActiveX.inf 中 LiteAVActiveXPlugin.dll 的版本号进行比较，如果发现有更新的版本，则会触发浏览器的重新下载页面，如下：
![](https://qcloudimg.tencent-cloud.cn/raw/835ed292950dbbe840d9c54ada538e9d.png)
单击**安装**后，即可将服务器上放的最新 LiteAVActiveXSDK.cab 中相关文件下载到本地。


## 常见问题
### 单击 Get SDK Version 按钮后，页面没有任何反应？
如果单击 **Get SDK Version** 按钮后，页面没有任何反应：请检查是否关闭了下载 LiteAVAX.cab 的提示框，导致插件没有正确下载并安装到本地。此时，您可以尝试刷新或重新加载网站首页地址，并在 IE 浏览器弹出 `此网站想要安装以下加载项：来自"Tencent Technology(Shenzhen) CompanyLimited"的"LiteAVActiveXSDK.cab"。` 时单击 **安装** 按钮以下载并安装 ActiveX 插件。
