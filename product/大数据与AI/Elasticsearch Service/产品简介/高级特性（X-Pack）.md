## 简介
高级特性，Elasticsearch 官方商业特性（原 X-Pack 商业版插件），包含了安全-权限管理（Security）、SQL、JDBC、告警（Alerting）、机器学习（Machine Learning）、监控等能力，可以为集群多用户权限管理，JDBC开发，以及日志分析等业务应用场景提供有力帮助，腾讯云 ES 提供了包含商业特性的版本，可以在创建购买集群时选择。

## 高级特性说明
![](https://main.qcloudimg.com/raw/de50a8ca3ee5ae61ca140e4ce5aa497c.png)

上图为腾讯云 ES 创建购买页高级特性版本选项的说明。腾讯云 ES 提供了3种可选的高级特性版本，其中基础版和白金版均集成了官方的商业特性（原 X-Pack 插件），开源版不包含；白金版包含了全部商业特性，基础版只包含了部分。
为了能够使用腾讯云 Elasticsearch 更多高级功能，建议您在创建购买集群时，选择白金版，各版本具体功能介绍及区别见下文。

### 基础版高级特性
以下为基础版部分能力说明，基础版和白金版都具备，开源版不具备。
- **监控**
![](https://main.qcloudimg.com/raw/012416b4755bed7e6cf8b57d0d0fa23a.png)
- **SQL**
提供了同传统数据库相同的 SQL 语句，对 Elasticsearch 数据进行全文搜索和分析，以及 JDBC 连接等。可以实现同原有业务系统的无缝对接，降低新技术学习成本。
![](https://main.qcloudimg.com/raw/ca19a8665919a85b9a08b5d9451ec3de.png)

目前开源版也集成了其他的 SQL 插件，详细使用可参见 [elasticsearch-sql](https://github.com/NLPchina/elasticsearch-sql)。

### 白金版高级特性
以下为白金版部分能力说明，只有白金版具备，基础版和开源版都不具备。

- **安全-权限管理**
多用户、分角色、权限控制能力，通过该项功能，可以向正确的人员授予访问权限，阻止恶意破坏和数据泄露，有效地保障数据安全。
![](https://main.qcloudimg.com/raw/e5106097fd4976e8e666061d619f16f3.png)
- **告警（Alerting）**
提供了针对数据变化的告警能力，并通过电子邮件等方式通知用户。如在日志分析场景中，结合 Elasticsearch 查询统计能力，监测到某类错误日志量突然增大，超过某个阈值时，触发告警。
![](https://main.qcloudimg.com/raw/b6e782614017d54bc89222c72a35bda0.png)
- **机器学习（Machine Learning）**
在自定义数据告警的应用场景中，有时候不容易设置规则和阈值来定义的变化，这种情况下，就可以通过结合非监督型机器学习来预测数据的变化趋势和合理的波动范围，在数据偏离正常变化趋势时，发出告警通知。

更多功能，请参考官方说明 [Elastic Stack](https://www.elastic.co/cn/products/stack) 、[API 文档](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/xpack-api.html)。

### 高级特性版本功能详细对比
各版本支持的具体功能详情请参见 [官方 Elastic Stack 介绍](https://www.elastic.co/cn/subscriptions)。

<table>
<thead>
<tr>
<th colspan="2"align="center"width="30%">Elastic Stack</th>
<th align="center">开源版</th>
<th align="center">基础版</th>
<th align="center">白金版</th>
</tr>
</thead>
<tbody>
<tr>
    <td rowspan="7">Elasticsearch</td>
<td align="center">可扩展性和弹性</td>
<td align="center">****</td>
<td align="center">****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">查询和分析</td>
<td align="center">****</td>
<td align="center">****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">数据扩充</td>
<td align="center">*****</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">管理和工具</td>
<td align="center">*</td>
<td align="center">****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">Security</td>
<td align="center">-</td>
<td align="center">-</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">Alerting</td>
<td align="center">-</td>
<td align="center">-</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">Machine Learning</td>
<td align="center">-</td>
<td align="center">-</td>
<td align="center">*****</td>
</tr>
<tr>
<td rowspan="8">Kibana</td>
<td align="center">探索和可视化</td>
<td align="center">**</td>
<td align="center">***</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">堆栈管理和工具</td>
<td align="center">*</td>
<td align="center">***</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">堆栈监测</td>
<td align="center">-</td>
<td align="center">*</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">分享与合作</td>
<td align="center">*</td>
<td align="center">***</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">本地化 UI</td>
<td align="center">***</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">Security</td>
<td align="center">-</td>
<td align="center">-</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">Alerting</td>
<td align="center">-</td>
<td align="center">-</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">Machine Learning</td>
<td align="center">-</td>
<td align="center">-</td>
<td align="center">*****</td>
</tr>
<tr>
<td rowspan="4">Beats</td>
<td align="center">数据收集</td>
<td align="center">****</td>
<td align="center">****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">数据传输</td>
<td align="center">*****</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">模块</td>
<td align="center">**</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">监测和管理</td>
<td align="center">-</td>
<td align="center">***</td>
<td align="center">*****</td>
</tr>
<tr>
<td rowspan="5">Logstash</td>
<td align="center">数据收集</td>
<td align="center">*****</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">数据扩充</td>
<td align="center">*****</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">数据传输</td>
<td align="center">*****</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">模块</td>
<td align="center">*</td>
<td align="center">*****</td>
<td align="center">*****</td>
</tr>
<tr>
<td align="center">监测和管理</td>
<td align="center">-</td>
<td align="center">**</td>
<td align="center">*****</td>
</tr>
</tbody></table>



