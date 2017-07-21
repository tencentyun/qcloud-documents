本文档介绍在 Windows 2012 R2 系统版本和 Windows 2008 系统版本下 IIS 角色添加与安装过程。
## Windows 2012 R2 版本示例
 1. 登录 Windows 云服务器，单击左下角【开始(Start)】，选择【服务器管理器(Server Manager)】，打开服务器管理界面，如下图所示：
![](//mccdn.qcloud.com/static/img/d27f493d5613aa2d87a9bbd9dba59387/image.png)

 2. 选择【添加角色和功能】，在弹出的添加角色和功能向导弹出框 ”开始之前“页面 中单击【下一步】按钮，在 ”选择安装类型“页面 中选择【基于角色或基于功能的安装】，单击【下一步】按钮：
![](//mccdn.qcloud.com/static/img/36ab9d6b144c5eff7fe2b468268155f2/image.png)
![](//mccdn.qcloud.com/static/img/0375764474b419976b13b594ea328e88/image.png)
![](//mccdn.qcloud.com/static/img/b6341e1fff569f1d7fffb5b66bc14c98/image.png)

 3. 窗口左侧选择 ”服务器角色“选项卡，勾选【Web服务器(IIS)】，在弹出框中单击【添加功能】按钮后，单击【下一步】按钮：
	![](//mccdn.qcloud.com/static/img/d516d053aca89ddc0a27ebe68a8f5882/image.png)
	![](//mccdn.qcloud.com/static/img/702065dfb3620e7aa7e81a94ff87a79b/image.png)

 4. 在 ”功能“选项卡 中勾选 .Net3.5 ，单击【下一步】按钮后，在 ” Web 服务器角色(IIS)“选项卡 也单击【下一步】：
![](//mccdn.qcloud.com/static/img/6e436524609ccd6e38b7440ebb881278/image.png)
![](//mccdn.qcloud.com/static/img/b003e403fe4e8e86bb0655199bb75a19/image.png)

 5. 在 ”角色服务“选项卡 中，勾选【CGI】选项，单击【下一步】：
![](//mccdn.qcloud.com/static/img/d13a9e02730018041342ecafa1b471af/image.png)

 6. 确认安装并等待安装完成：
![](//mccdn.qcloud.com/static/img/7e295431db7ef4a43b4136c860b32b19/image.png)

 7. 安装完成后，在云服务器的浏览器中访问 ```http://localhost/``` 验证是否安装成功。出现以下界面即为成功安装：
![](//mccdn.qcloud.com/static/img/dfa6725c4358e1a4214dcceb03e87028/image.png)

## Windows 2008 版本示例
 1. 登录 Windows 云服务器，单击左下角【开始(Start)】菜单中的【管理工具】中的【服务器管理器】按钮，打开服务器管理界面：
![](//mccdn.qcloud.com/img56b1bc701ec41.png)

 2. 单击 【添加角色和功能(Add Roles)】添加服务器角色，勾选 "Web Server(IIS)"选项卡 ，单击【下一步(Next)】：
![](//mccdn.qcloud.com/img56b1bb12831b3.png)
![](//mccdn.qcloud.com/img56b1bcee2d9e8.png)

 3. 在 选择角色服务(Role Services)时，勾选 "CGI"选项卡：
![](//mccdn.qcloud.com/img56b1bd1b8f220.png)

 4. 设置完成后，单击【安装(install)】，进行安装：
![](//mccdn.qcloud.com/img56b1bd4f18f1a.png)

 5. 浏览器访问 Windows 云服务器公网 IP 查看 IIS 服务是否正常运行。如果显示如下，说明 IIS 安装配置成功：
![](//mccdn.qcloud.com/img56b1bd7c5b0be.png)

