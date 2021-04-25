## 操作场景

本文介绍如何通过配置 X-Pack，来通过 Kibana 监控腾讯云 Logstash 服务。

>? 
>
>对于 X-Pack 版 Logstash，关联基础版或白金版腾讯云 ES 实例后，可以在 Kibana 中监控 Logstash 服务，开源版 Logstash 不支持此能力。
>
>Logstash 实例需要和 ES 实例在同一个 VPC 内，且大版本相同。

## 操作步骤

1. 登录 [ES 控制台](https://console.cloud.tencent.com/es)，在左侧导航栏单击【 Logstash 实例】，进入 Logstash 实例列表页。

2. 单击实例列表中要操作的实例的 ID，进入实例基本信息页。

3. 选择【监控】页。

4. 在【监控配置】区域，单击【 X-Pack 监控】行的【立即关联】。
![监控配置入口](https://main.qcloudimg.com/raw/cd16963053f206fee81cccfddeee183f.png)

5. 在弹窗中选择要关联的腾讯云 Elasticsearch 实例，点击【确定】。

   ![开启X-Pack监控](https://main.qcloudimg.com/raw/153355efb853b1d14f31fa601040a9a7.png)

   | 参数               | 说明                                                         |
| :----------------- | :----------------------------------------------------------- |
   | Elasticsearch 集群 | 选择要关联的腾讯云 Elasticsearch 集群，需要与 Logstash 实例在相同VPC，且大版本相同。 |
   
   > ! 关联操作涉及修改X-Pack配置，将触发实例重启。
   
8. 查看Logstash监控信息

   实例重启完成后，【X-Pack监控】状态变为开启，同时会显示当前关联的腾讯云Elasticsearch实例。

   - 在【监控】页单击【前往Kibana控制台】

      ![X-Pack监控开启状态](https://main.qcloudimg.com/raw/56b99fac12cfd5c8cddeddb1f6b27e7b.png)

   - 登录Kibana控制台后，在左侧导航栏单击【Stack Monitoring】切换到监控页面，在【Logstash】区域就可以相应的监控信息。

      ![Kibana的Logstash监控](https://main.qcloudimg.com/raw/9ed80ffa85fb661624607ebb9f47be72.png)