

## 操作场景

Datahub 提供数据流出能力，您可以将 CKafka 数据分发至日志服务 CLS 便于解决业务问题定位，指标监控，安全审计等日问题。

## 前提条件

该功能目前依赖 CLS 服务，使用时需开通相关产品功能。

## 操作步骤

1. 登录 [CKafka 控制台](https://console.cloud.tencent.com/ckafka) 。
2. 在左侧导航栏单击**数据流出**，选择好地域后，单击**新建任务**。
3. 目标类型选择**日志服务（CLS）**，单击**下一步**。
![](https://qcloudimg.tencent-cloud.cn/raw/16a343d95ec1a9ff4906606fd4b995ac.png)
   - 任务名称：只能包含字母、数字、下划线、"-"、"."。
   - CKafka 实例：选择数据源 CKafka。
   - 源 Topic：选择源 Topic。
   - 起始位置：转储时历史消息的处理方式，topic offset 设置。
   - 日志集：选择日志集，日志集日志服务的项目管理单元，用于区分不同项目的日志。
   - 日志主题：自动创建日志主题或者选择已有日志主题。一个 [日志集](https://cloud.tencent.com/document/product/614/35676) 可以包含多个日志主题，一个日志主题对应一类应用或服务，建议将不同机器上的同类日志收集到同一个日志主题。
   - 角色授权：使用日志服务（CLS）产品功能，您需要授予一个第三方角色代替您执行访问相关产品权限。
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

![](https://qcloudimg.tencent-cloud.cn/raw/715a7c26f1fe4639fae7a2c2a6d5bf23.png)
   
   

### 产品限制和费用计算

- 转储速度与 CKafka 实例峰值带宽上限有关，如出现消费速度过慢，请检查 CKafka 实例的峰值带宽或增加 CKafka partition 数。
- 转储速度与 CKafka 单个文件大小相关，如超过该500M，会自动分包上传。
- 该功能基于云函数 SCF 服务提供。SCF为用户提供了一定 [免费额度](https://cloud.tencent.com/document/product/583/12282) ，超额部分产生的收费，请以 SCF 服务的 [计费规则](https://cloud.tencent.com/document/product/583/17299) 为准。
