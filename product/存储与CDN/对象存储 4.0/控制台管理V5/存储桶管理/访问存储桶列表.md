## 简介
子账号（或协作者账号）默认没有拉取存储桶列表数据的权限，因此使用子账号登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)，在存储桶列表中无法访问存储桶及其列表和统计数据（示例图如下）。

子账号需要通过 **添加访问路径** 访问存储桶或 **获取存储桶列表访问权限（添加预设策略 QcloudCOSGetServiceAccess）** 实现对存储桶及其列表的访问。

- 访问存储桶列表受限示例
![](https://main.qcloudimg.com/raw/a6ccdd6c2929e106811ea7b9743dbb20.png)

- 访问统计数据受限示例
![](https://main.qcloudimg.com/raw/6b067cc708d48d7322ed12a4ad63d86c.png)

## 添加访问路径
默认情况下，子账号没有被授予预设策略 QcloudCOSGetServiceAccess，此时子账号没有权限拉取存储桶列表；但是当根账号授予给子账号某一存储桶的权限后，子账号可以通过添加访问路径的方式访问对应的存储桶。操作步骤如下：

1. 请使用子账号登录对象存储控制台，单击 [访问路径列表](https://console.cloud.tencent.com/cos5/access_path) 导航栏，然后单击【添加访问路径】按钮。
![](https://main.qcloudimg.com/raw/ee5c67c4144d98b0a2528be09b0a9f39.png)

2. 在 **添加访问路径** 弹窗中，选择存储桶所在地域，并输入访问路径。
![](https://main.qcloudimg.com/raw/12f559f9bdd69ebad4379a58db5e0065.png)
>**注意：**
> 1. 访问路径可填写某个存储桶，如 bucket1-1250000000。
> 2. 访问路径可填写某个存储桶下的路径，如 bucket1-1250000000/a/。
> 3. 请确保填写的是已被授权的访问路径，同时存储桶名称需与地域对应。

3. 确认地域和访问路径无误后，单击【确定】按钮，即可添加被授权的存储桶。
![](https://main.qcloudimg.com/raw/34b812cf9b6146da99206c93c4e2b1a9.png)

## 获取存储桶列表访问权限

1. 请使用根账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam)，单击已创建的子账号。
![](https://main.qcloudimg.com/raw/e0c74c136565592bd9f903551f949303.png)

2. 单击【关联策略】，在策略列表中选择添加预设策略 [QcloudCOSGetServiceAccess](https://console.cloud.tencent.com/cam/policy/detail/2158379&QcloudCOSGetServiceAccess&2)（策略对应的权限是对象存储 COS 的存储桶列表访问权限），单击 【确定】完成授权配置。
![](https://main.qcloudimg.com/raw/5f1f8666a35f1c175c45ba54024ffe1d.png)
>**注意：**
> 1. 根账号为子账号添加 QcloudCOSFullAccess 或 QcloudCOSReadOnlyAccess 预设策略，子账号同样可以获取存储桶列表访问权限。但由于这两个策略授予的权限范围较广，**出于安全考虑，不建议使用**。
> 2. 统计数据的访问权限：统计数据的访问权限依赖于存储桶列表的访问权限。当子账号需要拉取统计数据时，请确保根账号已为子账号添加预设策略 [QcloudCOSGetServiceAccess](https://console.cloud.tencent.com/cam/policy/detail/2158379&QcloudCOSGetServiceAccess&2)，否则会提示无权限访问统计数据。
