
## 操作场景

运行在 TEM 上的应用，由于业务需求等原因，通常会有访问公网的需求。而许多场景下，都是这些请求都是 HTTP/HTTPS 请求。您可以使用 API 网关，轻松的通过简单的配置，访问公网的 HTTP/HTTPS 请求。
>?如您的访问公网需求不只包含 HTTP/HTTPS 时，请参见 [TEM 应用访问公网](https://cloud.tencent.com/document/product/1371/59302) 来通过配置 NAT 网关实现。

## 前提条件

请先完成 [环境创建](https://cloud.tencent.com/document/product/1371/53293) 和 [创建并部署应用](https://cloud.tencent.com/document/product/1371/53294)。

## 操作步骤

### 步骤1：在 API 网关中关联公网 HTTP/HTTPS 请求

1. 前往 [API网关控制台](https://console.cloud.tencent.com/apigateway)，在左侧导航栏，单击**服务**，进入服务列表页。
2. 选择与部署TEM应用相同的地域，单击页面左上角的**新建**，新建一个服务。
    新建服务时，前端类型可选择 HTTP、HTTPS、HTTP 与 HTTPS 任一种，访问模式选择选择 VPC 内网，实例类型选择共享型。（关于实例类型的选择，请参见 API 网关文档 [实例选择指南](https://cloud.tencent.com/document/product/628/55510)）
<img src = "https://qcloudimg.tencent-cloud.cn/raw/be69633b2d4ca21dc29b1af93ea56df8.png" style="width: 60%">  
3. 单击 API 网关服务 ID 进入 API 管理页面。单击**新建 API**。
4. 在前端配置中填写 API 名称，前端类型选择 HTTP&amp;HTTPS，路径为“/”，请求方法选择 ANY 以包含所有请求，鉴权类型选择“免认证”，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/f3ecf9cf75b1b625beae7d6dfd8a8395.png)
5. 在后端配置中，选择 公网URL/IP，配置您需要访问的公网域名以及路径（此处以腾讯云官网为例），单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/500c72ee8d3fb382605fafbc739d33c9.png)
6. 设置应用的返回类型，此处为 HTML，RESTful 服务可选择为 JSON，点击完成。发布服务。

### 步骤2：验证公网请求连通性

1. 前往 API 网关服务基础配置页面，复制服务的内网 VPC 访问地址。
![](https://qcloudimg.tencent-cloud.cn/raw/12787f416718171cd1d95e85aa4243cc.png)
2. 打开部署好的 TEM 应用页面，进入应用实例的 webshell，访问 API 网关内网 VPC 访问地址验证网络连通性。
![](https://qcloudimg.tencent-cloud.cn/raw/aa94effbebdc1abfc27d4fe4ee9a3c6d.png)
