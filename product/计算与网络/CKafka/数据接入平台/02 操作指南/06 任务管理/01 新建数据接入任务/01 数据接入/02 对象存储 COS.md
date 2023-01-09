## 操作场景

数据接入平台 DIP 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道。

本文介绍在 DIP 控制台创建 COS 数据接入任务的操作方法。



## 前提条件

- 已提前创建好数据目标 Topic。
- 已创建好存储桶和对象。

## 操作步骤

1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据目标类型选择**对象存储（COS）**，单击**下一步**。
4. 填写数据源配置信息。
![](https://qcloudimg.tencent-cloud.cn/raw/54632b84187da11af96c1226327d098e.png)
   - 源存储桶：选择源数据存储桶。
   - 源对象：选择源数据对象，当前 Topic 支持的最大消息大小为12MB，单行文本数据超过12MB 会写入失败。
   - 角色授权：使用对象存储（COS）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
5. 单击**下一步**，选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。
   - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/76516)。
   - CKafka Topic：选择在 CKafka 创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
6. 单击**提交**，可以在任务列表看到刚刚创建的任务，在状态栏可以看到创建进度。

   

