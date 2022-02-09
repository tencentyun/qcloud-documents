## 操作场景

该任务指导您使用 Nacos 原生账号及腾讯云账号登录 Nacos 控制台。

## 前提条件

已 [创建 Nacos 引擎](https://cloud.tencent.com/document/product/1364/63997)。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏，单击 **nacos**，进入 Nacos 注册中心页面。
3. 单击目标实例的 ID，从基本信息页中，找到 控制台访问 的公网地址，通过 web 访问 Nacos 原生控制台。
![](https://qcloudimg.tencent-cloud.cn/raw/5530fc3bc6965da07ca6d79a2eb01971.png)

## 登录账号

在控制台登录页面，您可以通过 Nacos 原生账号（初始登录账号及由初始账号创建的账号）进行登录，也可以使用腾讯云账号下的 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 中的 SecretId 和 SecretKey 进行登录，如果子用户没有 SecretId 和 SecretKey ，请联系主账号申请。

- **Nacos原生账号登录**：使用初始登录账号登录，或由初始账号创建的账号登录。
  ![](https://qcloudimg.tencent-cloud.cn/raw/421b6a82b0a1037fdbe67d73a28ab912.png)
- **腾讯云账号 API 密钥登录**：使用腾讯云账号API密钥中的 SecretId 和 SecretKey 进行登录。
![](https://qcloudimg.tencent-cloud.cn/raw/766e559ede87743e1a8d321c80fccf23.png)

## 注意事项

目前，从 [TSE 控制台](https://console.cloud.tencent.com/tse) 新创建的 Nacos 实例，控制台访问默认开启鉴权，当使用非 Nacos 初始账号登录控制台时，会出现无权限获取配置信息、服务信息的问题，此时需要通过 Nacos 初始账号用户对其他账号进行角色、权限设置，步骤参见 [使用权限控制](#control)。

![](https://qcloudimg.tencent-cloud.cn/raw/7cbe45e0c80655317edd6e7ff1367bc1.png)

[](id:control)
## 使用权限控制

1. 管理用户。使用 Nacos 初始账号登录控制台，进入 **权限控制** > **用户列表** > **用户管理**页面，可以进行用户的创建、修改和删除操作。
![](https://qcloudimg.tencent-cloud.cn/raw/582b706abdd68784310c02d0edcf118f.png)
2. 管理角色。因为 Nacos 的自带的权限是基于角色来进行分配的，因此需要单击右上角**绑定角色**给创建好的用户进行绑定。
![](https://qcloudimg.tencent-cloud.cn/raw/dac4687b8949d90accc19c0091e05fb9.png)
3. 管理权限。角色创建好以后，单击右上角**添加权限**，就可以给这个角色赋予特定的权限了。
![](https://qcloudimg.tencent-cloud.cn/raw/69338e51d58d8be12f1523e27494b22a.png)
