通过 OpenAPI 规范能够定义标准的 RESTful 风格的 API。一般来说，OpenAPI 文档有三个必须的对象：
- openapi：OpenAPI 规范的版本号。
- info：API 的元数据。
- paths：API 的请求路径与操作。

本文将分对象介绍 OpenAPI 规范与 API 网关的映射关系。

## openapi
API 网关支持 3.0.0 版本的 OpenAPI 规范。

## info
OpenAPI 和 API 网关 info 对象的映射关系如下表：

| OpenAPI 对象     | 数据类型 | OpenAPI 对象说明   | API 网关对象 |
|------------------|----------|--------------------|--------------|
| info.title       | String   | API 所属服务的名称 | 未使用       |
| info.description | String   | API 所属服务的描述 | 未使用       |
| info.version     | String   | 版本号             | 未使用       |

## paths
OpenAPI 和 API 网关 paths 对象的映射关系如下表：

| OpenAPI 对象          | 数据类型 | OpenAPI 对象说明 | API 网关对象     |
|-----------------------|----------|------------------|------------------|
| paths.path            | Object   | API 请求路径     | API 前端请求路径 |
| operation.operationId | String   | API 名称         | API 名称         |
| operation.description | String   | API 描述         | 未使用           |
| operation.parameters  | Object   | API 请求参数     | API 请求参数     |
| operation.responses   | String   | API 响应         | 未使用           |

>?
>- OpenAPI 3.0.0 规范的对象定义请参考 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。
>- 导入 API 功能的操作流程请参见 [导入 API](https://cloud.tencent.com/document/product/628/43133)。
>- 导入 API 的完整示例请参见 [导入 API 示例](https://cloud.tencent.com/document/product/628/43136)。
