## 操作场景
数据安全网关支持主流的大部分资源类型，如 Linux、Windows 等其他资源类型。下面将为您详细介绍如何添加 Windows 域内资源。

## 前提条件
数据安全网关系统需已添加 Windows 域控资源。具体请您查看 [添加 Windows 域控资源](https://cloud.tencent.com/document/product/1025/32500) 文档。

## 操作步骤
1. 登录腾讯云 [数据安全网关控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录数据安全网关。
2. 单击【资源管理】>【Windows】，进入 Windows 资源管理页面。
3. 单击【新建】，配置如下信息。
 - **类型**：选择 Windows 系统，如 Windows2008。
 - **名称**：填写资源名称。
 - **状态**：默认状态为上线。
 - **IP**：填写资源 IP 地址。
 - **归属组**：配置资源隶属于某个组织结构。建议您事先添加组织结构，具体您可查看 [添加组织结构](https://cloud.tencent.com/document/product/1025/32049) 文档。 
 - **字符集**：填写 Windows 资源的字符集。
 - **归属域**：在此次选择您之前创建的 Windows 域控资源。
    其中添加归属域操作如下图所示：
    第1步：选择归属域。
    第2步：选择 AD 域服务器。
![](https://main.qcloudimg.com/raw/beb41c593691a63e15b086e12c839889.png)
4. 单击【确定】，添加 Windows域。
5. 在确认配置信息无误，单击【保存】，即可完成添加 Windows 域内资源操作。
