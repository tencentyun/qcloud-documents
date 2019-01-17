## 操作场景
您可将腾讯云资源添加到数据安全网关系统，数据安全网关系统能够管控和审计用户的运维操作。该指南指导您在数据安全网关系统如何添加 Windows 域控资源。


## 操作步骤
1. 进入 [腾讯云数据安全网关控制台](https://console.cloud.tencent.com/dasb)，使用管理员账号登录数据安全网关系统。
2. 在数据安全网关系统单击【资源管理】>【Active Directory】，即可进入域控资源管理页面，如下图所示。
![1](https://main.qcloudimg.com/raw/70eaa348c679b73a1de8255724ba3579.png)
3. 在域控资源管理页面，单击【新建】，配置如下信息。
**名称**：填写资源名称。
**状态**：默认状态为上线。
**IP**：填写资源 IP 地址。
**归属组**：配置资源隶属于某个组织结构。组织结构相关操作您可查看 [添加组织结构](https://cloud.tencent.com/document/product/1025/32049) 文档。
**域名**：填写域服务器域名。
**认证表达式**：填写格式为`$uid@域名`，例如域服务器域名为`example.com`，则认证表达式可以输入`$uid@example.com`或者为`example.com$uid`，具体按照哪种形式输入，请参考域认证时提供的登录名称。
![1](https://main.qcloudimg.com/raw/1cdb5cf0f5b7d63bf54714656dfa08b2.png)
4. 单击【保存】，即可添加 Windows 域控资源。
