## 操作场景

[腾讯云数字身份管控平台（EIAM）](https://console.cloud.tencent.com/eiam)是腾讯云推出的集中式的数字身份管控服务，EIAM 可以为您集中管理用户账号、分配访问权限以及配置身份认证规则，避免因员工账号、授权分配不当导致的安全事故。
EIAM 和腾讯云 API 网关通过 OAuth2.0 协议深度整合，您可以便捷的将两者组合起来，使用 EIAM 维护用户池，并授权池中的用户访问您在 API 网关中托管的 API，以实现 RESTful Web API 的身份认证。

该任务将指导您在 EIAM 中创建用户池、将 API 网关与用户池集成，以及调用与用户池集成的 API。

## 前提条件

已开通 [EIAM 服务](https://console.cloud.tencent.com/eiam)。

## 方案优势

与传统的 OAuth2.0 方式相比，API 网关 EIAM 认证主要有以下优势：

- 使用标准 OAuth2.0 协议；
- EIAM 维护用户池，免自建认证服务器；
- 在认证能力基础上支持鉴权功能，保护 API 安全；
- EIAM 内置多种 RBAC 模型，免自建鉴权服务器和授权模型；
- 可一键创建授权 API 和业务 API，轻配置；
- 内置缓存机制，更快的访问速度。

<img src="https://main.qcloudimg.com/raw/a7c9c61a515f0159e992564486ca0f4e.png" width="450px">

## 操作步骤

### 步骤1：创建认证方式为“EIAM 认证”的 API

1. 登录 [API 网关控制台](https://console.cloud.tencent.com/apigateway/service) ，在左侧导航栏单击**服务**。
2. 在服务列表中，单击目标服务的服务名，查看该服务。
3. 在服务信息中，单击**管理 API**标签页，单击 API列表上的**新建**，即可开始创建 API。
4. 在 API 创建页，选择 API 鉴权类型为“EIAM 认证”，API 网关提供两种接入方式：
   - 新建 EIAM 应用：新创建一个 EIAM 应用与当前 API 网关 API 建立绑定关系。
   - 选择已有 EIAM 应用：选择之前已经创建好的 EIAM 应用与当前 API 网关 API 建立绑定关系。

>?您可以点击以下页签，查看两种接入方式的配置项：

<dx-tabs>
::: 新建 EIAM 应用

| 参数           | 是否必填 | 说明                                                         |
| -------------- | -------- | ------------------------------------------------------------ |
| 认证与鉴权     | 是       | 提供两种认证与鉴权方式：“只认证不鉴权”与“既认证又鉴权”：<li>认证：提供用户名密码，做身份认证；</li><li>鉴权：通过用户名判断是否有访问网关资源的权限。</li> |
| EIAM 应用类型  | 是       | 提供两种应用类型：“非 Web 客户端”与“Web 客户端”：<li>非 Web 客户端：适用于非 Web 客户端发起的API调用，如服务器端、C/S架构系统客户端、App 客户端、小程序客户端，能支持以 POST 方式发起请求，需要自行请求授权 API 获取 Token，再使用 Token 请求业务 API；</li><li>Web 客户端：适用于 Web 客户端发起的 API 调用，如浏览器、客户端应用 Web Viewer 等 Web 客户端，能支持以 Web 重定向方式接收返回信息。</li> |
| Token 有效时间 | 是       | 单个签发的 Token 有效期，超过有效期后，必须重新获取 Token。  |

:::                    
::: 选择已有 EIAM 应用 

| 参数           | 是否必填 | 说明                                                         |
| -------------- | -------- | ------------------------------------------------------------ |
| 选择 EIAM 应用 | 是       | 从列表中选择一个已经创建好的 EIAM 应用建立绑定关系。         |
| 认证与鉴权     | 是       | 提供两种认证与鉴权方式：“只认证不鉴权”与“既认证又鉴权”：<li>认证：提供用户名密码，做身份认证；</li><li>鉴权：通过用户名判断是否有访问网关资源的权限。</li> |
| EIAM 应用类型  | 是       | 提供两种应用类型：“非 Web 客户端”与“Web 客户端”：<li>非 Web 客户端：适用于非 Web 客户端发起的 API 调用，如服务器端、C/S架构系统客户端、App客户端、小程序客户端，能支持以 POST 方式发起请求，需要自行请求授权 API 获取Token，再使用 Token 请求业务 API；</li><li>Web 客户端：适用于Web客户端发起的API调用，如浏览器、客户端应用 Web Viewer 等 Web 客户端，能支持以 Web 重定向方式接收返回信息。</li> |
| Token 有效时间 | 是       | 单个签发的 Token 有效期，超过有效期后，必须重新获取 Token。当接入方式为“选择已有 EIAM 应用”时，该配置项继承已选择的 EIAM 应用的配置，不支持自行配置。 |

:::   

</dx-tabs>            

**非 Web 客户端架构图**
![](https://main.qcloudimg.com/raw/adce9c932cadfb70af7ea3ffdd7dc141.png)

**Web 客户端架构图**
![](https://main.qcloudimg.com/raw/51d0a6ae8f2f00eeae87a9e8d65a733d.png)

> ?
> - 选择“只认证不鉴权”方式，请求授权 API 时，API 网关将校验传入的用户访问凭证，认证通过后，颁发 id_token。使用 id_token 请求业务 API 时，API 网关将检验 id_token 的合法性，校验通过后转发给业务后端。
> - 选择“既认证又鉴权”方式，请求授权 API 时，API 网关将校验传入的用户访问凭证，认证通过后，颁发 id_token。使用 id_token 请求业务 API 时，API 网关将检验 id_token 的合法性，同时校验访问用户是否具有访问该 API 的权限，API 网关将只放行具有访问权限的用户请求。用户与资源的授权关系可参考 [步骤3](#step3) 进行配置。

5. 依次完成后续创建过程，单击**完成**，即可完成认证方式为“EIAM 认证”的 API 的创建。
   ![](https://main.qcloudimg.com/raw/aba88527aa46af44f4202ef75ec06966.png)

### 步骤2：在 EIAM 中创建用户池和用户[](id:step2)

1. 登录 [EIAM 控制台](https://console.cloud.tencent.com/eiam) ，在左侧导航栏单击**用户管理**>**组织机构管理**。
2. 选择合适的组织机构，单击**新建用户**。
3. 填写表单，完成用户的创建。
   ![](https://main.qcloudimg.com/raw/2ad13ffffeacc1aa8b18ffce01fbdd82.png)

### 步骤3：在 EIAM 中授权[](id:step3)

1. 登录 [EIAM 控制台](https://console.cloud.tencent.com/eiam) ，在左侧导航栏单击**授权管理**>**资源级授权**。
2. 在下拉列表中选择第一步中创建或绑定的EIAM应用，选择**用户授权**Tab 页，单击**新建授权**。
3. 选择需要关联的网关资源（服务和API），选择在第二步中创建的用户，将 API网关资源对用户授权。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c3f4d87c30371c516af46a85b785d1a8.png)

### 步骤4：使用用户信息调用 API 网关 API

使用 [步骤2](#step2) 中创建的用户的账号和密码，对 API 网关 API 发起访问。

>?您可以点击以下页签，查看非 Web 客户端和 Web 客户端的调用方法。

<dx-tabs>
::: 非 Web 客户端

1. 请求授权 API 获取 id token。
   Query 请求参数 username：为 [步骤2](#step2) 中创建的用户账号。
   Query 请求参数 password： 为 [步骤2](#step2) 中创建的用户密码。
   ![](https://main.qcloudimg.com/raw/aa53522a3084a8e7eb8a5db434cb00bc.png)

2. 使用已获取的 Token 请求业务 API。
   Header 参数 Authorization：格式为 `Bear id_token="<获取的Token内容>"`

   ```
   curl http://service-xxxxxxxx-1234567890.gz.apigw.tencentcs.com/work -H'Authorization:Bearer id_token="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1OTIyNzk3MTAsImZvbyI6ImJhciIsImlhdCI6MTU5MjI3OTQxMCwianRpIjoiZlBGYlFZRkR4REx3d0lXTFl0aHBBQSIsIm5iZiI6MTU5MjI3OTQxMCwid3VwIjo5MH0.0JQquNRVCQ8n9hPV-mJi6Mku_7G3T1jFp68Sk2AYBijpzzBMQ1KOcREyo9G6QOpvdctynGOAPkL3cwqeTzkFhWgGj633pu_MdLjlectEBMGyVQIv6pL8OBMCHMQzTUTpHWJ_NoUkLpRLKGqZFFcXW8q7v4KeCbf8xHUa9OCH5VF2JxYOnFWDVgucSqao06r0Jaq64LDwKIhLw77ujheKpcBjRrf1kqoIpqk2qhb8CzxM36g_DawMadzKmX49dT-k7auNnI2xUtu5CZdXZ3lSmLeicXfGjc66rrH_acqUqipZRKeeQ5F3Ma467jPQaTeOKiCMHwS2_yp-sXNU2GzxOA"'
   ```

   - 对于未授权的用户：
     鉴权验证，返回403，“Access not authorized”，表明用户没有通过鉴权。
     ![](https://main.qcloudimg.com/raw/dbf69b0bbc346900c299bbf506abe4fc.png)

   - 对于完成授权的用户：
     鉴权验证，返回 API 后端调用结果，user001即可进行 API 的调用。
     ![](https://main.qcloudimg.com/raw/f7df9b839b44744af1909c120b435337.png)
     :::
     ::: Web 客户端

1. 在浏览器输入 API 访问地址，可以看到弹出登录页面：
   <img src="https://main.qcloudimg.com/raw/eef8349bdc4aa266c59545be7bc0f95f.png" width="450px">

2. 在登录页面中输入步骤2设置的用户登录账号和密码，即可进行 API 的调用。
   :::
   </dx-tabs>



## 注意事项

- EIAM 认证仅对开通了公网访问的 API 网关服务开放，若您的 API 网关服务访问方式为“内网 VPC ”，将无法使用 EIAM 认证。
- 如果在 EIAM 侧授权关系发生变更，需要重新请求授权 API 获取 Token。






























