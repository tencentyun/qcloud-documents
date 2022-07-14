本文档将为您介绍 Mac 系统如何登录堡垒机。

## 操作场景

运维用户如需通过 Mac 系统登录堡垒机，可使用 Mac_SecureCRT、Mac_Terminal  或 Mac_Iterm 工具进行登录。
>!仅3.0.7版本堡垒机支持使用 Mac 系统登录堡垒机功能，如需升级请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=517&level2_id=727&source=0&data_title=%E5%85%B6%E4%BB%96%E8%85%BE%E8%AE%AF%E4%BA%91%E4%BA%A7%E5%93%81&level3_id=728&radio_title=%E5%8A%9F%E8%83%BD%E5%92%A8%E8%AF%A2&queue=3026&scene_code=17783&step=2) 联系我们。

## 操作步骤
### 步骤1：下载并运行控件
1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh) ，选择一台已部署好的堡垒机实例，在右侧操作栏，单击**管理**，进入堡垒机登录页面。
2. 使用运维用户账号登录堡垒机。
>?若运维用户忘记密码，可以联系管理员进行重置，详情请参见 [设置口令](https://cloud.tencent.com/document/product/1025/41852)。
3. 单击<img src=" https://main.qcloudimg.com/raw/606f82657fccfac739b26e67d57abef7.png"  style="margin:0;">，进入套件中心，下载 macos 控件包。
![](https://main.qcloudimg.com/raw/e3a83159c2f1736484d1c682781afb62.png)
4. 将 OAMPlugin.app 程序移动到 macos 应用程序文件夹中，并运行一次。
![](https://main.qcloudimg.com/raw/a533a8acc18a94c68ed4b6043179c835.png)
5. （可选）若出现无法打开 OAMPlugin.app 问题：
![](https://main.qcloudimg.com/raw/fca421e5e032d8080c14cef92fc33a81.png)
需到隐私中进行设置，允许控制 App。
![](https://main.qcloudimg.com/raw/578cd5a846c9ac43ca5aa721b02a6a21.png)

### 步骤2：使用 Mac_SecureCRT、Mac_Terminal 、Mac_Iterm 登录
1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/dsgc/bh)。
2. 使用运维用户账号登录堡垒机。
>?若运维用户忘记密码，可以联系管理员进行重置，详情请参见 [设置口令](https://cloud.tencent.com/document/product/1025/41852)。
3. 单击**授权列表**，进入资源列表页。
4. 找到您需要登录的 Linux 资源，在其右侧单击**登录**，在弹出的窗口中，进行登录配置。
![](https://main.qcloudimg.com/raw/949b357bb91840f7e18b745cfae30fe5.png)
5. 在配置登录页面，根据需求填写相关字段，进行登录。
	- **使用 Mac_SecureCRT 登录** 
	选择 IP 、协议、输入账号、口令并选择 Mac_SecureCRT 工具，单击**登录**。
![](https://main.qcloudimg.com/raw/32c710ab549c94e410d49490378afac2.png)
		成功登录系统，如下图所示：
![](https://main.qcloudimg.com/raw/17606c51fcfc3c798a3f1dcf2bbc3bb5.png)
	- **使用 Mac_Terminal 登录** 
选择 IP 、协议、输入账号、口令并选择 Mac_Terminal 工具，单击**登录**。
![](https://main.qcloudimg.com/raw/98be1e2c54953773c1b7b908cd1baca1.png)
成功登录系统，如下图所示：
![](https://main.qcloudimg.com/raw/a38ee3ffcaa83edd73d1ac36ccf396b0.png)
	- **使用 Mac_Iterm 登录** 
选择 IP 、协议、输入账号、口令并选择 Mac_Iterm 工具，单击**登录**。
![](https://main.qcloudimg.com/raw/d167cca8f52885b1b3b1b30334ca1a7b.png)
成功登录系统，如下图所示：
![](https://main.qcloudimg.com/raw/c667217cc896311d935820f9b693a039.png)
