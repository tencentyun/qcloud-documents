本文为您介绍通过 EMR 控制台快速创建一个 EMR on CVM 集群、提交作业并查看运行结果的操作流程。
## 准备工作
1. 在使用 EMR 集群前，需要注册腾讯云账号并完成实名认证，具体操作请参见 [实名认证账号归属介绍](https://cloud.tencent.com/document/product/378/3629)。
2. 完成对弹性 MapReduce 的服务账号授予系统默认角色 EMR_QCSRole，具体操作请参见 [角色授权](https://cloud.tencent.com/document/product/589/37899)。
3. 在线账号充值，EMR on CVM 提供两种计费模式：按量计费和包年包月计费，在创建集群前需要进行账号余额充值，确保余额大于等于创建集群所需配置费用（不包含：代金券、折扣卷、优惠券等）；具体操作请参见考 [在线充值](https://cloud.tencent.com/document/product/555/7425)。

## 创建集群
登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在 EMR on CVM 集群列表页单击**创建集群**，在购买页面完成相关配置；当集群列表中集群状态显示为运行中时，表示集群创建成功。
<table>
<thead>
<tr>
<th>购买步骤</th>
<th>配置项</th>
<th>配置项说明</th>
<th>示例</th>
</tr>
</thead>
<tbody><tr>
<td rowspan=4>软件配置</td>
<td>地域</td>
<td>集群所部署的物理数据中心<br>注意：集群创建后，无法更改地域，请谨慎选择</td>
<td>北京、上海、广州、南京、成都、硅谷等</td>
</tr>
<tr>
<td>集群类型</td>
<td>EMR on CVM 支持多种集群类，默认 Hadoop 集群类型</td>
<td>Hadoop、StarRocks 等</td>
</tr>
<tr>
<td>产品版本</td>
<td>不同产品版本上捆绑的组件和组件的版本不同</td>
<td>EMR-V2.7.0 版本中内置的是 Hadoop 2.8.5、Spark 3.2.1 等</td>
</tr>
<tr>
<td>部署组件</td>
<td>非必选组件，根据自身需求组合搭配自定义部署</td>
<td>Hive-2.3.9、Impala-3.4.1等</td>
</tr>
<tr>
<td rowspan=4>区域与硬件配置</td>
<td>计费模式</td>
<td>集群部署计费模式</td>
<td>按量计费</td>
</tr>
<tr>
<td>可用区及网络配置</td>
<td>可用区、集群网络设置<br>注意：集群创建后，无法直接更改可用区，请谨慎选择</td>
<td>广州七区</td>
</tr>
<tr>
<td>安全登录</td>
<td>用于设置节点的网络访问控制，安全组同防火墙功能</td>
<td>创建新安全组</td>
</tr>
<tr>
<td>节点配置</td>
<td>根据业务需要为不同节点类型选择合适机型配置。详情请参见 <a href="https://cloud.tencent.com/document/product/589/10982">业务评估</a></td>
<td>开启节点部署高可用</td>
</tr>
<tr>
<td rowspan=3>基础配置</td>
<td>所属项目</td>
<td>将当前集群分配给不同的项目组</td>
<td>集群创建后暂不支持修改所属项目</td>
</tr>
<tr>
<td>集群名称</td>
<td>集群的名称，可自定义</td>
<td>EMR-7sx2aqmu</td>
</tr>
<tr>
<td>登录方式</td>
<td>自定义设置密码方式和关联密钥方式；SSH 密钥仅用于 EMR-UI 快捷入口登录</td>
<td>密码</td>
</tr>
<tr>
<td>确认配置</td>
<td>配置清单</td>
<td>确认所部署信息是否有误</td>
<td>选中服务协议，单击<strong>立即购买</strong></td>
</tr>
</tbody></table>

>! 您可以在 CVM 控制台中查看各节点信息，为保证 EMR 集群的正常运行，请勿在 CVM 控制台中更改节点配置信息。

## 提交作业及查看运行结果
集群创建成功后，您可以在该集群创建并提交作业；本文已提交 spark 任务为例，操作如下。
>! 在创建 EMR 集群的时候需要在软件配置界面选择 Spark 组件。
>
1. 使用 SSH 登录并连接集群（本地系统为 Linux/Mac OS），详情请参见 [登录集群](https://cloud.tencent.com/document/product/589/34358)。
2. 在 EMR 命令行先使用以下指令切换到 Hadoop 用户，并进入 Spark 安装目录/usr/local/service/spark：
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ cd /usr/local/service/spark
```
3. 通过如下指令提交任务并运行：
```
/usr/local/service/spark/bin/spark-submit \
--class org.apache.spark.examples.SparkPi \
--master yarn \
--deploy-mode cluster \
--proxy-user hadoop \
--driver-memory 1g \
--executor-memory 1g \
--executor-cores 1 \
/usr/local/service/spark/examples/jars/spark-examples*.jar \
10
```
4. 提交作业后，在 EMR on CVM 页面，单击目标集群所在行的**集群服务**；单击 YARN UI 所在行的 **WebUI 链接**。登录认证后即可进入YARN UI 页面；单击目标作业的 **ID**，可以查看作业运行的详情。

## 销毁集群
- 当创建的集群不再使用时，可以销毁集群，退还资源；毁集群将强制终止集群所提供的服务，并释放资源。
- 在 EMR on CVM 页面，选择目标集群的**更多 > 销毁**；在弹出的对话框中，单击**立即销毁**。
