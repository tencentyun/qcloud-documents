## 操作场景

运行在 TEM 上的应用，由于业务需求等原因，通常会有访问公网的需求。而许多场景下，这些请求都是 HTTP/HTTPS 请求。您可以使用 API 网关，轻松的通过简单的配置，访问公网的 HTTP/HTTPS 请求。

>?如您的访问公网需求不只包含 HTTP/HTTPS 时，请参见 [TEM 应用访问公网（通过 NAT 网关）](https://cloud.tencent.com/document/product/1371/59302) 通过配置 NAT 网关实现。

## 操作步骤

### 步骤1：部署 TEM 应用

参考 [应用管理]( https://cloud.tencent.com/document/product/1371/53294) 在 TEM 控制台中部署应用。



### 步骤2：在 API 网关中关联公网 HTTP/HTTPS 请求

1. 登录 [API网关控制台](https://console.cloud.tencent.com/apigateway)，在左侧导航栏，单击**服务**，进入服务列表页。

2. 选择与部署TEM应用相同的地域，单击页面左上角的**新建**，新建一个服务。

   - 实例类型：选择**共享型**（关于实例类型的选择，请参见 API 网关文档 [实例选择指南](https://cloud.tencent.com/document/product/628/55510)）。
   - 前端类型：可选择 HTTP、HTTPS、HTTP & HTTPS 任意一种。
   - 访问方式：选择选择 **VPC 内网**。
     <img src = "https://qcloudimg.tencent-cloud.cn/raw/be69633b2d4ca21dc29b1af93ea56df8.png" style="width: 60%">  

3. 在服务列表页面，单击创建好的 API 网关服务的 “ID” 进入 API 管理页面，单击**新建 API**。

4. 设置前端配置信息，单击**下一步**。

  - 前端类型：选择 HTTP&amp;HTTPS。
  - 路径：填写 “/”。
  - 请求方法：选择 **ANY** 以包含所有请求。
  - 鉴权类型：选择**免认证**。

  ![](https://qcloudimg.tencent-cloud.cn/raw/f3ecf9cf75b1b625beae7d6dfd8a8395.png)

5. 在后端配置中，选择 公网URL/IP，配置您需要访问的公网域名以及路径（此处以腾讯云官网为例），单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/500c72ee8d3fb382605fafbc739d33c9.png)

6. 设置应用的返回类型，此处为 HTML，RESTful 服务可选择为 JSON，单击**完成**，发布服务。

### 步骤3：验证公网请求连通性

1. 登录 [API网关控制台](https://console.cloud.tencent.com/apigateway)，单击创建好的 API 网关服务的 “ID” ，进入 API 管理页面。
2. 在页面上方页签选择**基础配置**页面，复制服务的内网 VPC 访问地址。
   ![](https://qcloudimg.tencent-cloud.cn/raw/12787f416718171cd1d95e85aa4243cc.png)
3. 在 TEM 控制台的 [**应用管理**](https://console.cloud.tencent.com/tem/application?rid=4) 页面单击部署好的 TEM 应用的“ID”，进入应用实例列表页面。
4. 单击应用实例操作栏的**Webshell**，进入到 Webshell 中，访问 API 网关内网 VPC 访问地址验证网络连通性。
   ![](https://qcloudimg.tencent-cloud.cn/raw/aa94effbebdc1abfc27d4fe4ee9a3c6d.png)
