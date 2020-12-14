## 操作场景

该任务指导您对免鉴权的 API 发起调用。

## 前提条件

#### 创建免鉴权的 API

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“免鉴权”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。

#### 确认信息

在发起调用前，您必须了解所调用 API 的请求路径、请求方法、请求参数等信息。这些信息可以在API详情页的默认访问地址模块找到。
![](https://main.qcloudimg.com/raw/2b0aeb46bafafce5abd68843e1edb81e.png)

#### 工具准备

您可以通过浏览器、浏览器插件、Postman 工具、客户端等来源发起请求，如果是简单验证，建议使用 Postman 工具来发起请求。

## 操作步骤

1. 某 API 的信息如下：
   公网域名：http://service-p52nqnd0-1253970226.gz.apigw.tencentcs.com
   已发布环境：release
   访问路径：/api
   请求方法：GET
   按照“公网域名或内网 VPC 域名/已发布环境/访问路径”的规则，该 API 的默认访问地址为：http://service-p52nqnd0-1253970226.gz.apigw.tencentcs.com/release/api
2. 在 Postman 工具中填写访问地址，选择请求方法为 GET，填写相应的请求参数后即可单击【Send】按钮发起调用。
   ![](https://main.qcloudimg.com/raw/ff9f2537a989ebaa646945f074a69a95.png)
