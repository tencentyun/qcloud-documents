本文主要介绍如何快速运行腾讯云 TRTC Demo（Windows ActiveX版本）。

## Windows（ActiveX）运行环境
- Windows 7及以上操作系统。
- IE 9及以上版本，推荐使用 IE 11版本。

## 前提条件
您已 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985) 账号，并完成 [实名认证](https://cloud.tencent.com/document/product/378/3629)。

## 操作步骤
[](id:step1)
### 步骤1：创建新的应用
1. 登录实时音视频控制台，选择**开发辅助** > [**快速跑通Demo**](https://console.cloud.tencent.com/trtc/quickstart)。
2. 单击**新建应用**输入应用名称，例如 `TestTRTC`；若您已创建应用可单击**选择已有应用**。
3. 根据实际业务需求添加或编辑标签，单击**创建**。
![](https://main.qcloudimg.com/raw/f04d288ed091c98a5e8056eb86fb49e8.png)
>?
>- 应用名称只能包含数字、中英文字符和下划线，长度不能超过15个字符。
>- 标签用于标识和组织您在腾讯云的各种资源。例如：企业可能有多个业务部门，每个部门有1个或多个 TRTC 应用，这时，企业可以通过给 TRTC 应用添加标签来标记部门信息。标签并非必选项，您可根据实际业务需求添加或编辑。

[](id:step2)
### 步骤2：下载 Windows ActiveX 和 Demo 源码
1. 根据实际业务需求下载 Windows（Active X） 的 ZIP 包或到 GitHub/Gitee 下载 ActiveX 的 cab 包及配套的 Demo 源码。
2. 下载完成后，单击**已下载，下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/a0817d04fb14ee9d62dd043b94854676.png)

[](id:step3)
### 步骤3：部署 ActiveX 插件
1. 将下载好的 ActiveX 压缩包解压，并将其中的 SDK 文件夹（里面包含 LiteAVActiveXSDK.cab）和 TRTC-API-Example-ActiveX 文件夹（里面包含 Demo 所需的 HTML 和 JS 文件）放到 Web 服务器的指定目录下。
2. 在 `TRTC-API-Example-ActiveX\js` 中找到并打开定义 SDKAppID 和密钥信息的文件，如下：
 <table>
     <tr>
         <th nowrap="nowrap">适用平台</th>  
         <th nowrap="nowrap">文件相对路径</th>  
     </tr>
     <tr>
         <td>Windows(ActiveX)</td>   
         <td>TRTC-API-Example-ActiveX/js/GenerateTestUserSig.js</td>
     </tr>
 </table>
3. 设置 `GenerateTestUserSig.js` 文件中的相关参数：
  <ul><li>SDKAPPID：默认为0，请设置为实际的 SDKAppID。</li>
  <li>SECRETKEY：默认为空字符串，请设置为实际的密钥信息。</li></ul>
  <img src="https://qcloudimg.tencent-cloud.cn/raw/179c8491a3fe09a52e6c4fcf99797c48.png">
4. 将页面中已生成的SDKAppID和密钥粘贴完成后，单击**已复制粘贴，下一步**即创建成功。
5. 完成后，单击**回到控制台概览**即可。

[](id:step4)
### 步骤4：运行 Demo
1. 完成以上的下载和部署后，打开 IE 浏览器 并访问 Web 服务器的地址（如` http://xx.xx.xx.xx/TRTC-API-Example-ActiveX/index.html`），IE 浏览器弹出 `此网站想要安装以下加载项：来自"Tencent Technology(Shenzhen) CompanyLimited"的"LiteAVActiveXSDK.cab"。` 如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/25dda1b82025f4901fe3416f332ce130.png)
2. 单击 **安装** 会弹出如下的下载安装页面：
![](https://qcloudimg.tencent-cloud.cn/raw/835ed292950dbbe840d9c54ada538e9d.png)
3. 安装完成后，可输出房间号和用户名进行音视频会话。

## 常见问题

### 1. 单击进入房间后，页面没有任何反应，也没有日志输出？
如果单击 **进入房间** 后，页面没有任何反应，也没有任何日志输出。请检查是否关闭了下载 LiteAVActiveXSDK.cab 的提示框，导致 LiteAVActiveXSDK.cab 没有正确下载并安装到本地（如 [步骤4](#step4) 中截图所示）。此时可以尝试刷新或重新加载网站首页，并在弹出 `此网站想要安装以下加载项：来自"Tencent Technology(Shenzhen) CompanyLimited"的"LiteAVActiveXSDK.cab"。` 时单击 **安装** 确保 LiteAVActiveXSDK.cab 正常下载安装到本地。

### 2. 单击进入房间按钮后，弹出配置信息的提示框？
单击进入房间后，弹出如下窗口：
![](https://qcloudimg.tencent-cloud.cn/raw/b6a93298e0260780a055efaafa3508d7.png)
请参照 [步骤3](#step3) 进行 SDKAPPID 和 SECRETKEY 的配置填写。
