

## 操作场景

Datahub 提供数据流出能力，您可以将 CKafka 数据分发至分布式数据仓库 TDW 以对数据进行存储、查询和分析。

## 前提条件

该功能目前依赖分布式数据仓库（TDW）产品，使用时需开通相关产品功能。

## 操作步骤

### 创建任务

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。
3. 目标类型选择**分布式数据仓库（TDW）**，单击**下一步**。
   ![](https://qcloudimg.tencent-cloud.cn/raw/b9cd20132c4e6a7e1bd1427c2637ec90.png)
   - 任务名称：只能包含字母、数字、下划线、"-"、"."。
   - CKafka 实例：选择数据源 CKafka。
   - 源 Topic：选择源 Topic。
   - 源数据：支持拉取源数据。
   - 起始位置：转储时历史消息的处理方式，topic offset 设置。
   - TDW BID：填写 TDW 业务 BID。
   - TDW TID：填写 TDW 业务 TID。
4. 单击**提交**，完成任务创建。



### 查看监控

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据流出**，单击目标任务的**ID**，进入任务基本信息页面。
3. 在任务详情页顶部，单击**监控**，选择要查看资源，设置好时间范围，可以查看对应的监控数据。
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
<img src ="https://qcloudimg.tencent-cloud.cn/raw/7dbbfca73fd617ea96e276c7ab55370a.png"> 
   不选择时默认全部，展示现有的 Topic 级别的监控数据。
<img src ="https://qcloudimg.tencent-cloud.cn/raw/7ad8dd52abe75bda0e827c71c6d1da16.png"> 




### 更改数据源和数据目标

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据流出**，单击目标任务的**ID**，进入任务基本信息页面。
3. 单击**数据源**模块右上角的**更改数据源**，修改数据源信息。
4. 单击**数据目标**模块右上角的**更改数据目标**，修改数据目标信息。
   ![](https://qcloudimg.tencent-cloud.cn/raw/4cb4d3c1a68450f2c76335212f6b6506.png)

>?
>- 更改数据目标，不会重置消费组 offset。
>- 任务暂停过程中，不支持修改数据源和数据目标。


## 产品限制和费用计算

- 转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 CKafka 实例的峰值带宽或增加 CKafka partition 数。
- 转储速度与 CKafka 单个文件大小相关，如超过该500M，会自动分包上传。
