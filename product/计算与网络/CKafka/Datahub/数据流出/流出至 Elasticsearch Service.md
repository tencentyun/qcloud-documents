## 操作场景

Datahub 提供数据流出能力，您可以将 CKafka 数据分发至 Elasticsearch Service（ES）便于海量数据存储搜索、实时日志分析等操作。

## 前提条件

该功能目前依赖 Elasticsearch Service 服务，使用时需开通相关产品功能。

## 操作步骤

### 创建数据流出任务

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。
3. 目标类型选择 **Elasticsearch Service**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/714f7fe3a3a9c50b929682943b2bffc7.png)
   - 任务名称：只能包含字母、数字、下划线、"-"、"."。
   - CKafka 实例：选择数据源 CKafka。
   - 源 Topic：选择源 Topic。
   - 源数据：支持拉取源数据。
   - 实例集群：选取腾讯云 Elasticsearch Service 实例集群信息。
   - 实例用户名：输入 Elasticsearch 实例用户名，腾讯云 Elasticsearch 默认用户名为 elastic，且不可更改。
   - 实例密码：输入 Elasticsearch 实例密码。
   - 起始位置：转储时历史消息的处理方式，topic offset 设置。
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








## 产品限制和费用计算

转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 CKafka 实例的峰值带宽。

  
