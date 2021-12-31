本文主要介绍通过配置 X-Pack，来通过 Kibana 监控腾讯云 Logstash 服务。
>? 
>- 对于 X-Pack 版 Logstash，关联基础版或白金版腾讯云 ES 实例后，可以在 Kibana 中监控 Logstash 服务，开源版 Logstash 不支持此能力。
>- Logstash 实例需要和 ES 实例在同一个 VPC 内，且大版本相同。

## 操作步骤
1. 登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，在左侧导航栏单击 **Logstash 实例**，进入 Logstash 实例列表页。
2. 单击实例列表中要操作的实例的 **ID/名称**，进入实例基本信息页，然后切换到**监控**页签。在“监控配置”中，单击“X-Pack 监控”中的**立即关联**。
![](https://main.qcloudimg.com/raw/fc2961b17df722ae9542c7493f21a482.png)
3. 在弹窗中选择要关联的腾讯云 Elasticsearch 实例，单击**确定**。
![](https://main.qcloudimg.com/raw/8e9b452aec391d87619497a888028cf2.png)
>! 关联操作涉及修改 X-Pack 配置，会触发实例重启。
<table>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td>Elasticsearch 集群</td>
<td>选择要关联的腾讯云 Elasticsearch 集群，需要与 Logstash 实例在相同 VPC，且大版本相同。</td>
</tr>
</table>
4. 查看 Logstash 监控信息。
实例重启完成后，“X-Pack 监控”状态变为开启，同时会显示当前关联的腾讯云 Elasticsearch 实例。
 - 在**监控**页签，单击**前往 Kibana 控制台**，跳转到 Kibana 控制台。
![](https://main.qcloudimg.com/raw/bb083ebbfcd24cc4491b97dd185d9602.png)
 - 登录 Kibana 控制台后，在左侧导航栏单击 **Stack Monitoring** 切换到监控页面，在 **Logstash** 区域就可以相应的监控信息。
![Kibana的Logstash监控](https://main.qcloudimg.com/raw/9ed80ffa85fb661624607ebb9f47be72.png)
