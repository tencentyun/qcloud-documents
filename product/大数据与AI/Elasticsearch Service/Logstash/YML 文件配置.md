本文为您介绍如何通过 Elasticsearch Service 控制台配置腾讯云 Logstash 实例的 YML 参数。

## 操作步骤
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，在左侧导航栏单击 **Logstash 实例**，进入 Logstash 实例列表页。
2. 选择要修改 YML 参数配置的实例，单击 **ID/名称**，进入实例基本信息页。
3. 在实例基本信息页面，切换到 **YML 配置**页签，单击**修改**，根据业务需求修改 YML 参数。详细参数说明，可参见 [Logstash 配置文件](https://www.elastic.co/guide/en/logstash/current/logstash-settings-file.html)。
![](https://main.qcloudimg.com/raw/8846144fbb6998163c7205ee0af8c0cb.png)
4. YML 参数配置完成后，单击**保存**。将提示您是否重启实例，因修改 YML 参数需要重启 Logstash 实例才能生效，所以确认后 Logstash 实例将会重启，重启进度可查看**变更记录**。
