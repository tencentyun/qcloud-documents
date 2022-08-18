## 操作场景

Datahub 支持接入各种数据源产生的不同类型的数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道。

本文以 COS 数据为例介绍如何在 CKafka 控制台创建数据异步拉取任务，并对任务进行修改配置，帮助您更好地了解数据接入功能。

## 操作步骤

### 创建数据接入任务

**前提条件**

- 已创建好目标 CKafka 实例和 Topic。
- 已创建好存储桶和对象。

**操作步骤**：

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据流入**，选择好地域后，单击**新建任务**。
3. 在弹窗中数据源类型选择**异步拉取** > **COS**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/6ee25c43707018b5983f41192c79da32.png)
4. 单击**下一步**，填写任务详情。
   ![](https://qcloudimg.tencent-cloud.cn/raw/da7e3f4f59e8a020bd460288990eb8c0.png)
   - 任务名称：只能包含字母、数字、下划线、"-"、"."。
   - CKafka 实例：选择 CKafka 实例。
   - 目标 CKafak topic：选择数据投递的目标 CKafka Topic。
   - 源存储桶：选择源数据存储桶。
   - 源对象：选择源数据对象，当前 Topic 支持的最大消息大小为12MB，单行文本数据超过12MB 会写入失败。
   - 角色授权：使用对象存储（COS）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
5. 单击**提交**，完成任务创建。

   

### 编辑数据目标

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka)。
2. 在左侧导航栏单击**数据接入**，单击目标任务的**ID**，进入任务基本信息页面。
3. 单击**数据目标**模块右上角的**更改数据目标**，修改数据目标信息。



### 暂停任务

在 **[数据接入](https://console.cloud.tencent.com/ckafka/datahub-access)** 页面，单击目标任务的操作栏的**更多** > **暂停任务**，二次确认后可暂停任务。

> ?当您发现数据接入任务影响了 CKafka 正常服务时，可以暂停数据接入。

### 启动任务

在 **[数据接入](https://console.cloud.tencent.com/ckafka/datahub-access)** 页面，单击目标任务的操作栏的**更多** >**启动任务**，二次确认后可将暂停任务恢复。

>?处于暂停状态的任务可以重新启动，将继续转储数据。

### 重启任务

在 **[数据接入](https://console.cloud.tencent.com/ckafka/datahub-access)** 页面，单击目标任务的操作栏的**更多** >**重启任务**，二次确认后可以重新开始任务。

> ?任务在**异常**状态时，可以重启任务，重启任务表示重新开始任务，不会影响到已经转储的数据和相关的 CKafka 实例。

### 重建任务

创建失败的任务可能是因为创建任务时的配置失误，用户可以手动重建任务。

1. 在 **[数据接入](https://console.cloud.tencent.com/ckafka/datahub-access)** 页面，单击目标任务的操作栏的**更多** >**重建任务**，进入任务设置页面。
2. 指定新的任务名称并编辑数据目标后，单击**提交**，完成任务重建。

### 复制任务

当您有大量配置相似的任务时，在第一个任务创建成功后可以通过复制任务功能将任务进行复制。

1. 在 **[数据接入](https://console.cloud.tencent.com/ckafka/datahub-access)** 页面，单击目标任务的操作栏的**更多** >**复制任务**，进入任务设置页面。
2. 指定新的任务名称并编辑数据目标后，单击**提交**，完成任务重建。

### 删除任务

在  **[数据接入](https://console.cloud.tencent.com/ckafka/datahub-access)** 页面，单击目标任务的操作栏的**删除**，在二次确认弹窗中单击**确认**，可删除任务。

> ?
>
> - 删除任务表示停止数据接入并删除任务记录，不会影响到已经转储的数据和相关的 CKafka 实例。
> - 任务一旦删除不可恢复，请您谨慎操作。



### 查看监控

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据接入**，单击目标任务的**ID**，进入任务基本信息页面。
3. 选择**监控**页签，可查看目标 Topic 监控数据。

<table>
    <tr>
        <th>图标</th>
        <th>说明</th>
    </tr>
    <tr>
        <td><img src ="https://main.qcloudimg.com/raw/9ba57bbd3b8ef3efc4f687d63d27a46d.png" style ="margin:0"></td>
        <td>单击可查看监控指标同环比。</td>
    </tr>
    <tr>
        <td><img src ="https://main.qcloudimg.com/raw/34bdbdbdabb7b5720bf17d78c636a4ad.png" style ="margin:0"></td>
        <td>单击可刷新获取最新的监控数据。</td>
    </tr>
    <tr>
        <td><img src ="https://main.qcloudimg.com/raw/8f2bf7f4df9ddd959f0ecb69fdda8e4c.png" style ="margin:0"></td>
        <td>单击可将图表复制到 Dashboard，关于 Dashboard 请参见 <a href="https://cloud.tencent.com/document/product/248/47161">什么是 Dashboard</a>。</td>
    </tr>
    <tr>
        <td><img src ="https://main.qcloudimg.com/raw/af20129df7be46f33ab7d3598f6e9213.png" style ="margin:0"></td>
        <td>勾选后可在图表上显示图例信息。</td>
    </tr>
</table>
 选择分区后，可以查看指定 Partition 的监控数据。
 <img src ="https://qcloudimg.tencent-cloud.cn/raw/3ee5cf22055038671f968749876c960c.png">  
   不选择时默认全部，展示现有的 Topic 级别的监控数据。
	 <img src ="https://qcloudimg.tencent-cloud.cn/raw/c06058596c2c093ba6a54bbe7397713d.png"> 	  

### 查看消息

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据接入**，单击目标任务的**ID**，进入任务基本信息页面。
3. 单击**查看消息**页签，选择好 Topic 和分区后，可以查看数据接入成功的最近5条、20条、60条和100条消息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/171fd12cb463579aec77a1702cbcf988.png)

