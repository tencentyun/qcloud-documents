
## 操作场景
堡垒机支持主流的大部分资源类型，如 Linux、Windows 等其他资源类型。下面将为您详细介绍如何添加 Windows 域控资源。


## 操作步骤
1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录堡垒机。
2. 单击【资源管理】>【Active Directory】，进入域控资源管理页面。
3. 单击【新建】，配置如下信息。
 - **名称**：填写资源名称。
 - **状态**：默认状态为上线。
 - **IP**：填写资源 IP 地址。
 - **归属组**：配置资源隶属于某个组织结构。组织结构相关操作您可查看 [添加组织结构](https://cloud.tencent.com/document/product/1025/32049) 文档。
 - **域名**：填写域服务器域名。
 - **认证表达式**：填写格式为`$uid@域名`，例如域服务器域名为`example.com`，则认证表达式可以输入 $uid@example.com 或者为 example.com$uid，具体按照哪种形式输入，请参考域认证时提供的登录名称。
![](https://main.qcloudimg.com/raw/d7643fc2fa88058206976b475d7a562d.png)
4. 单击【保存】，即可添加 Windows 域控资源。
