## 操作场景

使用 API 网关后端对接云函数 SCF 时，由于触发器限制，不支持直接上传二进制文件，必须经过 Base64 编码后上传。API 网关支持将客户端请求体 Base64 编码后传递给云函数 SCF，为 API 开启此功能后，您无需改造客户端代码即可将二进制文件上传至云函数 SCF。

为满足不同场景的要求，腾讯云 API 网关 Base64 编码功能提供了“全部触发”和“Header 触发”两种触发方式供您选择：
- **全部触发**：API 开启全部触发后，每次请求的请求内容都会被 Base64 编码后再传递给云函数。
- **Header 触发**：API 开启 Header 触发后，必须配置触发规则。API 网关将根据触发规则对请求头进行校验，只有拥有特定 Content-Type 或 Accept 请求头的请求会被 Base64 编码后再传递给云函数，不满足条件的请求将不进行 Base64 编码，直接传递给云函数。

## 交互流程

![](https://main.qcloudimg.com/raw/9fbb169958e4ea1087d13cdb2b2d2721.svg)

## 操作步骤

### 配置全部触发

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) ，在左侧导航栏单击【服务】。
2. 在服务列表中，单击目标服务的服务 ID，查看 API 列表。
3. 单击【新建】，填写 API 前端配置，单击【下一步】。
4. API 后端类型选择【云函数SCF】，勾选“Base64编码”，完成后续配置流程。此时创建的 API 已经开启了 Base64 编码，并默认为“全部触发”。
![](https://main.qcloudimg.com/raw/c116fc0017274148daf0290c8a20f445.png)

### 配置 Header 触发

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1) ，在左侧导航栏单击【服务】。
2. 在服务列表中，单击目标服务的服务 ID，查看 API 列表。
3. 在 API 列表中，单击目标 API 的 API ID（目标 API 必须是后端对接 SCF 的 API），即可查看 API 详情页。 在 API 详情页中，单击【基础配置】标签页，找到【Base64编码】配置项。
4. 单击"Base64"后的【编辑】，选择触发方式为【Header触发】。单击【添加触发规则】，选择参数并填写参数值。
5. 确认配置信息无误后，最后单击【保存】即可。
![](https://main.qcloudimg.com/raw/fedbf7b330ddfe846b39b48aaa7c2771.png)

## 注意事项
- 对于每次成功触发 Base64 编码的请求，API 网关不仅会对请求体进行 Base64 编码，还会把 isBase64Encoded 字段的值设置为 True 一起传递给云函数，该字段可用于通知云函数本次请求是否经过 Base64 编码（后端对接云函数的结构体请参考 [API 网关传递给后端的结构体](https://cloud.tencent.com/document/product/628/50421)）。
- 由于触发器限制，API 网关单次传递给云函数的请求内容不能大于 6MB。因此，本功能只适用于传递 Base64 编码后小于 6MB 的文件，传递大于 6MB 的文件请您参考 [上传文件](https://cloud.tencent.com/document/product/628/49883) 采用 COS 方式上传。
- Header 触发的触发规则采用模糊匹配，仅支持 Content-Type 和 Accept 请求头。多条触发规则间是“或”的关系，只需满足其中一条触发规则就可以触发 Base64 编码。
