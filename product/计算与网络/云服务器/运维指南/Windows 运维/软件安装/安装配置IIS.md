本文档介绍在 Windows 2012 R2 系统版本和 Windows 2008 系统版本下 IIS 角色添加与安装过程。
## Windows 2012 R2 版本示例
 1. 登录 Windows 云服务器，单击左下角【开始(Start)】，选择【服务器管理器(Server Manager)】，打开服务器管理界面，如下图所示：
![](//mc.qcloudimg.com/static/img/7b433cabe3d7349b5a38b359639e4c7c/image.png)

 2. 选择【添加角色和功能】，在弹出的添加角色和功能向导弹出框 ”开始之前“页面 中单击【下一步】按钮，在 ”选择安装类型“页面 中选择【基于角色或基于功能的安装】，单击【下一步】按钮：
![](//mc.qcloudimg.com/static/img/b0f5ffb889f4d23213f0811bd945b170/image.png)
![](//mc.qcloudimg.com/static/img/027fe90a3c882520662783bdcda97b94/image.png)
![](//mc.qcloudimg.com/static/img/919430e0493d9580c33eab871ffee557/image.png)

 3. 窗口左侧选择 ”服务器角色“选项卡，勾选【Web服务器(IIS)】，在弹出框中单击【添加功能】按钮后，单击【下一步】按钮：
![](//mc.qcloudimg.com/static/img/0d69cbfd04d9a614eeb00559f34bafba/image.png)
![](//mc.qcloudimg.com/static/img/a254c87a59392801a4bf23521c9c1535/image.png)

 4. 在 ”功能“选项卡 中勾选 .Net3.5 ，单击【下一步】按钮后，选择 ” Web 服务器角色(IIS)“选项卡 同时单击【下一步】：
![](//mc.qcloudimg.com/static/img/703cda6d11a5cfc3a26f471f0535dc17/image.png)
![](//mc.qcloudimg.com/static/img/5d84575332b4c9c425bcdf0baa80f7e6/image.png)

 5. 在 ”角色服务“选项卡 中，勾选【CGI】选项，单击【下一步】：
![](//mc.qcloudimg.com/static/img/958f0c466a633ea6c58de651a4ad7982/image.png)

 6. 确认安装并等待安装完成：
![](//mc.qcloudimg.com/static/img/045b132f13b06c6e499b85ecb34a3f43/image.png)

 7. 安装完成后，在云服务器的浏览器中访问 ```http://localhost/``` 验证是否安装成功。出现以下界面即为成功安装：
![](//mc.qcloudimg.com/static/img/e064cc1f765d68edf3dcfb0051d5dbfa/image.png)

## Windows 2008 版本示例
 1. 登录 Windows 云服务器，单击左下角【开始(Start)】菜单中的【管理工具】中的【服务器管理器】按钮，打开服务器管理界面：
![](//mc.qcloudimg.com/static/img/787983bdedb15a6d496119c953d35e1a/image.png)

 2. 单击 【添加角色和功能(Add Roles)】添加服务器角色，勾选 "Web Server(IIS)"选项卡 ，单击【下一步(Next)】：
![](//mccdn.qcloud.com/img56b1bb12831b3.png)
![](//mccdn.qcloud.com/img56b1bcee2d9e8.png)

 3. 在 选择角色服务(Role Services)时，勾选 "CGI"选项卡：
![](//mccdn.qcloud.com/img56b1bd1b8f220.png)

 4. 设置完成后，单击【安装(install)】，进行安装：
![](//mccdn.qcloud.com/img56b1bd4f18f1a.png)

 5. 浏览器访问 Windows 云服务器公网 IP 查看 IIS 服务是否正常运行。如果显示如下，说明 IIS 安装配置成功：
![](//mccdn.qcloud.com/img56b1bd7c5b0be.png)

