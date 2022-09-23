## 操作场景

数据接入平台支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道。

本文介绍在 DIP 控制台创建 HTTP 数据主动上报任务的操作方法。

## 前提条件

已创建好数据目标 Topic。

## 操作步骤


1. 登录 [DIP 控制台](https://console.cloud.tencent.com/ckafka/datahub-overview)。
2. 在左侧导航栏单击**任务管理** > **任务列表**，选择好地域后，单击**新建任务**。
3. 填写任务名称，任务类型选择**数据接入**，数据目标类型选择**数据上报（HTTP）**，单击**下一步**。
4. 选择是否**是否对上报数据进行格式校验**，选择绑定的 Schema 后，将会按该 Schema 对所有流入的数据进行格式校验。
   ![](https://qcloudimg.tencent-cloud.cn/raw/0f912ad283e90bd19bb39d45eb188c1b.png)
5. 单击**下一步**，选择数据目标 Topic，支持选择 **DIP Topic** 或者 **CKafka Topic**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/9cad0d6de6be9a50284b7aa905e2b14a.png)
   - DIP Topic：选择在数据接入平台提前创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/76516)。
   - CKafka Topic：选择在 CKafka 创建好的 Topic，详情参见 [Topic 管理](https://cloud.tencent.com/document/product/597/73566)。
6. 单击**提交**，任务创建成功后会生成接入点信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/c99a1f809ecb66155807ab396c3ecffd.png)

## 后续处理


接入点生成后，您可以复制接入点信息到 SDK 中使用，用于写入数据，详细说明请参见 [数据上报 SDK](https://cloud.tencent.com/document/product/597/71210)。



