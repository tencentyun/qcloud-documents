## 操作场景

您可以根据请求的参数取值与系统参数取值，例如请求 Header 中的 Host 或 UserName 转发到不同的 TKE 后端，用户灰度发布、蓝绿发布、租户路由等场景。TKE 后端通道可以结合条件路由插件，实现数据分流的功能。

更多条件路由的使用和功能可以参考 [条件路由插件](https://cloud.tencent.com/document/product/628/62922)。

## 前提条件

- 用户有专享型的服务。
- 已经创建多个 TKE 通道。

## 操作步骤

1. 在 [API 网关](https://console.cloud.tencent.com/apigateway/service) 服务页面新建一个 API，API 的后端类型选择 VPC 内资源，通道选择 TKE 通道。[](id:step1)
   ![](https://qcloudimg.tencent-cloud.cn/raw/f35af2e585b2542a647dadcdef158a46.png)        
2. API 发布后，创建一个条件路由插件。
   1. 控制台左侧导航栏**插件** > **系统插件**。
   2. 点击**新建**，类型选择**条件路由**。
      <img src="https://qcloudimg.tencent-cloud.cn/raw/2291584bab61ecc63b2e1dec59879783.png" width="450px">                         
   3. 创建条件路由策略：下面举例中的条件路由语义是，请求 Header 中 UserName 的值是 admin 的时候，就转发到 TKE 通道upstream-1ca1d6yi。
      ![](https://qcloudimg.tencent-cloud.cn/raw/2dfe8aa99b540e172305f4d4d6d0cb3e.png)        
      策略详情：
```yaml
ServiceType: HTTP
ServiceConfig:
  Method: ANY
  Path: /
  Url: 'http://127.0.0.1/'
  UniqVpcId: vpc-s0g8gpo5
  UpstreamId: upstream-1ca1d6yi
  Product: upstream
```
3. 条件路由插件绑定到 **[步骤1](#step1)** 创建的 API 中。
4. 请求如果匹配到条件路由的策略（Header 带上 UserName 为 admin），就转发到 upstream-1ca1d6yi；如果请求没有匹配到条件路由的策略，就使用 API 配置的默认后端。


## 注意事项

条件路由不仅仅有匹配请求 Header 的功能，还能匹配如 clientIp 的功能。条件路由更多的能力可参考 [条件路由插件](https://cloud.tencent.com/document/product/628/62922)。
