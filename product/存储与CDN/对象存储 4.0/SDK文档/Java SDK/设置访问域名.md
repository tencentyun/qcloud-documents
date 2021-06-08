## 简介

本文档提供关于如何使用非默认域名请求 COS 服务。

### 默认 CDN 加速域名

#### 功能说明

在 COS 控制台为存储桶开启默认 CDN 加速域名后，可在 SDK 代码中设置对应的域名，以便实现默认加速功能。
关于如何开启默认加速域名请参见 [开启默认 CDN 加速域名](https://cloud.tencent.com/document/product/436/36636)。

#### 方法原型

```java
void com.qcloud.cos.ClientConfig.setEndPointSuffix(String endPointSuffix)
```

#### 请求示例

```java
// 1 使用 CDN 加速域名，无需再发送 COS 的认证信息
COSCredentials cred = new AnonymousCOSCredentials();
// 2 设置 bucket 的地域简称，COS 地域简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing"));
// 推荐使用 https 协议
clientConfig.setHttpProtocol(HttpProtocol.https);
// 3 设置默认 CDN 加速域名后缀
String cdnSuffix = "file.myqcloud.com";
clientConfig.setEndPointSuffix(cdnSuffix);
// 4 生成 cos 客户端
COSClient cosclient = new COSClient(cred, clientConfig);
```

#### 参数说明

| 参数名称            | 描述                          | 类型           |
| ------------------ | ---------------------------- | -------------- |
| endPointSuffix     | 通过设置域名后缀，使用 CDN 加速域名 | String         |

### 自定义 CDN 加速域名

#### 功能说明

在 COS 控制台为存储桶设置自定义 CDN 加速域名后，可在 SDK 代码中设置对应的域名，以便实现自定义域名的加速功能。关于如何开启自定义 CDN 加速域名，请参见 [开启自定义 CDN 加速域名](https://cloud.tencent.com/document/product/436/36637)。

#### 方法原型

```java
void com.qcloud.cos.ClientConfig.setEndpointBuilder(EndpointBuilder endpointBuilder)
```

#### 请求示例

```java
// 1 使用 CDN 加速域名，无需再发送 COS 的认证信息
COSCredentials cred = new AnonymousCOSCredentials();
// 2 设置 bucket 的地域简称，COS 地域简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing"));
// 推荐使用 https 协议，如果使用 https 协议，请确保自定义域名有相关 https 证书
clientConfig.setHttpProtocol(HttpProtocol.https);
// 3 设置 CDN 自定义域名
//  get service 请求会使用这个域名，这个域名不能自定义
String serviceApiEndpoint = "service.cos.myqcloud.com";
String cdnEndpoint = "xxx.xxx.com";
UserSpecifiedEndpointBuilder endPointBuilder = new UserSpecifiedEndpointBuilder(cdnEndpoint, serviceApiEndpoint);
clientConfig.setEndpointBuilder(endPointBuilder);
// 4 生成 cos 客户端
COSClient cosclient = new COSClient(cred, clientConfig);
```

#### 参数说明

| 参数名称               | 描述                          | 类型                            |
| --------------------- | ---------------------------- | ------------------------------ |
| endPointerBuilder     | 参数用于构建自定义  CDN 加速域名  | UserSpecifiedEndpointBuilder   |

UserSpecifiedEndpointBuilder 说明：

| 参数名称                  | 描述                                | 类型                            |
| ------------------------ | ---------------------------------- | ------------------------------ |
| generalApiEndpoint       | 填写用户的自定义  CDN 加速域名                    | String                         |
| getServiceApiEndpoint    | 只能填写 `service.cos.myqcloud.com` | String                         |


### 自定义源站域名

#### 功能说明

在 COS 控制台为存储桶设置自定义源站域名后，可在 SDK 代码中设置对应的域名，以便实现访问 COS 资源。关于如何设置自定义源站域名请参见 [自定义源站域名](https://cloud.tencent.com/document/product/436/36638)。

#### 方法原型

```java
void com.qcloud.cos.ClientConfig.setEndpointBuilder(EndpointBuilder endpointBuilder)
```

#### 请求示例

```java
// 1 初始化用户身份信息(secretId, secretKey)
// SECRETID和SECRETKEY请登录访问管理控制台进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 2 设置 bucket 的地域简称，COS 地域简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing"));
// 推荐使用 https 协议
clientConfig.setHttpProtocol(HttpProtocol.https);
// 3 设置自定义域名
//  get service 请求会使用这个域名，这个域名不能自定义
String serviceApiEndpoint = "service.cos.myqcloud.com";
String userEndpoint = "xxx.xxx.com";
UserSpecifiedEndpointBuilder endPointBuilder = new UserSpecifiedEndpointBuilder(userEndpoint, serviceApiEndpoint);
clientConfig.setEndpointBuilder(endPointBuilder);
// 4 生成 cos 客户端
COSClient cosclient = new COSClient(cred, clientConfig);
```

#### 参数说明

| 参数名称               | 描述                          | 类型                            |
| --------------------- | ---------------------------- | ------------------------------ |
| endPointerBuilder     | 参数用于构建自定义源站域名           | UserSpecifiedEndpointBuilder   |

UserSpecifiedEndpointBuilder 说明：

| 参数名称                  | 描述                                 | 类型                            |
| --------------------- | ------------------------- | ------------------------------ |
| generalApiEndpoint       | 填写自定义源站域名                        | String      |
| getServiceApiEndpoint    | 只能填写 `service.cos.myqcloud.com`  | String         |


### 全球加速域名

#### 功能说明

在 COS 控制台为存储桶开启全球加速域名后，可在 SDK 代码中设置对应的域名，以便实现全球加速功能。关于全球加速的功能介绍，请参见 [全球加速功能概述](https://cloud.tencent.com/document/product/436/38866)。

#### 方法原型

```java
void com.qcloud.cos.ClientConfig.setEndPointSuffix(String endPointSuffix)
```

#### 请求示例

```java
// 1 初始化用户身份信息(secretId, secretKey)
// SECRETID和SECRETKEY请登录访问管理控制台进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 2 设置 bucket 的地域简称，COS 地域简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("ap-beijing"));
// 推荐使用 https 协议
clientConfig.setHttpProtocol(HttpProtocol.https);
// 3 设置全球加速域名后缀
String cosSuffix = "cos.accelerate.myqcloud.com";
clientConfig.setEndPointSuffix(cosSuffix);
// 4 生成 cos 客户端
COSClient cosclient = new COSClient(cred, clientConfig);
```

#### 参数说明

| 参数名称            | 描述                          | 类型           |
| ------------------ | ---------------------------- | -------------- |
| endPointSuffix     | 通过设置域名后缀，使用全球加速域名 | String         |
