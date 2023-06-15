本文介绍通过 Logstash 将数据投递到 Elasticsearch Serverless 服务中的相关操作。

## 前提条件
- 登录 [ES 控制台](https://console.cloud.tencent.com/es)，进入**Logstash 管理**界面。
- 如果已经有 Logstash 实例，可直接进入下一步。如未购买 Logstash 实例。单击**新建实例**进入 Logstash 购买页，选择与索引相同的 VPC，Logstash版本选择为7.10.2或者7.14.2，高级特性选择为“X-Pack 版”，单击**立即购买**。

## 操作步骤
1. 在控制台 Logstash 管理 界面单击对应 Logstash 名称，进入子页面后，单击**管道管理 > 新建管道**。
![](https://qcloudimg.tencent-cloud.cn/raw/f5b62fd47a9c67bcb1a9851d4430c190.png)
2. 进入管道配置页面后，单击右上角**引用模板**，选择您的 input 端，目前可选为 elasticsearch、jdbc、http、s3、beats 以及 kafka，输出端选择为 elasticsearch，单击**引用**。
![](https://qcloudimg.tencent-cloud.cn/raw/c140e757136e77f7120678801dafc1af.png)
在 Config 配置中，输入 input 端跟 output 端的相关信息，其中，output 端的配置说明如下：
	- hosts：索引内网访问地址。
	- user：索引用户名，您可在对应索引的访问控制模块中获取。
	- password：索引密码，您可在对应索引的访问控制模块中获取。
在参数配置中，管道 ID 为必填项，其他参数您可根据业务情况自行选择是否填写。填写完成后，单击**保存并部署**，等待状态为**运行中**即可。
![](https://qcloudimg.tencent-cloud.cn/raw/a36f88c0b4d7e3a6603ed279372d9be6.png)
