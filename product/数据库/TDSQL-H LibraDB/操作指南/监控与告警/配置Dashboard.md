当需要通过云监控的Dashboard监控LibraSQL、LibraSQL ZooKeeper、CDC的指标时，可在云监控中新建指标。

## 监控指标

请参见监控指标。

## 前提条件

- 已开通腾讯云云监控（Cloud Monitor，CM）服务。
- 数据库实例状态为**运行中**。
- 已收集告警通知对象的信息，包括：邮件、短信、电话等。

## 操作步骤

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。

2. 在左侧导航栏选择**Dashboard** > **Dashboard列表**。

3. 在页面上方单击**新建Dashboard**， 进入新建 Dashboard 管理页。

4. 单击**新建图表**，新建指标。

   详细操作及参数说明请参见[新建指标](https://cloud.tencent.com/document/product/248/46761)。其中，监控类型和指标选择如下表所示。

   ![](https://qcloudimg.tencent-cloud.cn/raw/ae2c45bbe3f8a5c2ed65a65d9bddb0a7.png)
   
   <table>
   <tr>
   <th width="20%">配置项</th><th width="80%">说明</th></tr>
   <tr>
   <td>监控类型</td><td>请选择<b>云产品监控</b>。</td></tr>
   <tr>
   <td>指标</td>
   <td>选择您需要监控的产品类型及对应指标。产品类型如下：
   <ul>
   <li>LibraSQL：请选择<b>云数据库/TDSQL-H LibraDB/libraSQL</b>。</li>
   <li>LibraSQL ZooKeeper：请选择<b>云数据库/TDSQL-H LibraDB/LibraSQL ZooKeeper</b>。</li>
   <li>CDC：请选择<b>云数据库/TDSQL-H LibraDB/CDC</b>。</li></ul></td></tr>
   </table>
   >?
   >如果需要配置图表，请参见<a href="https://cloud.tencent.com/document/product/248/46762" target="_blank">图表配置</a>。
   
5. 配置完成后， 单击![img](https://main.qcloudimg.com/raw/2cf48d6910973ec3dc7074e05bac24db.png) 。

   保存后可在**Dashboard列表**中查看对应的Dashboard。

## 后续操作

查看已创建的Dashboard操作请参见[查看Dashboard](https://cloud.tencent.com/document/product/248/46748)。