## 操作场景
该任务指导您在 API 网关控制台通过导入 OpenAPI 来创建 API。

## 前提条件
- 已完成 [服务创建](https://cloud.tencent.com/document/product/628/11787)。
- 准备 OpenAPI 3.0.0 标准的 API 描述文件，文本格式为 YAML 或 JSON。

## 操作步骤
1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway)，在左侧导航栏单击【服务】。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击【管理 API】标签页，查看该服务下的 API 列表。
4. 单击 API 列表上方的【导入 API】，进入导入 API 页面。
5. 选择文本格式（YAML 或 JSON），并单击【上传文件】，选择要上传的 API 描述文件；或者直接在代码编辑器中输入描述 API 的内容。
6. 单击【保存】，API 网关将根据您输入的内容创建 API，并在创建完成后返回本次创建成功的 API 列表。
![](https://main.qcloudimg.com/raw/b1ee822a7519f9452b73d99077fa27e4.png)

## 注意事项
- 目前只支持导入后端为 Mock 的 API，您可以在导入成功后通过编辑 API 来修改 API 的后端配置。
- 导入 API 支持 OpenAPI 3.0.0 标准的 API 定义，支持 YAML 和 JSON 格式的描述文件。
- 单次不能同时导入超过10个API。
- 上传 API 描述文件时，文件后缀名必须为 .yaml 或 .json；单次上传的 API 描述文件不能超过 100KB；上传的描述文件会覆盖代码编辑器里的内容。
- 创建成功的 API 将不会自动发布，需要您手动发布后方可生效。

>?
>- OpenAPI 规范和 API 网关的映射关系请参见 [定义 API](https://cloud.tencent.com/document/product/628/43135)。
>- 导入 API 的完整示例请参见 [导入 API 示例](https://cloud.tencent.com/document/product/628/43136)。
