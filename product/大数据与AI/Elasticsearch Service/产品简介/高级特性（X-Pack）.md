## 简介
高级特性，原 Elasticsearch 官方 X-Pack 商业付费插件，该插件提供了安全-权限管理（Security）、SQL、JDBC、告警（Alerting）、机器学习（Machine Learning）等多项能力，可以进一步丰富您的业务应用场景。

## 高级特性介绍
- **安全-权限管理**
提供了多用户、分角色、权限控制能力，通过该项功能，可以向正确的人员授予访问权限，阻止恶意破坏和数据泄露，有效地保障数据安全。
![](https://main.qcloudimg.com/raw/9e5000a25b9e9cf428a2f2f606fe6533.png)
- **SQL**
提供了同传统数据库相同的 SQL 语句，对 Elasticsearch 数据进行全文搜索和分析，以及 JDBC 连接等。可以实现同原有业务系统的无缝对接，降低新技术学习成本。
![](https://main.qcloudimg.com/raw/dc4e012bc026f684feec45a685a7f700.png)
- **告警（Alerting）**
提供了针对数据变化的告警能力，并通过电子邮件等方式通知用户。如在日志分析场景中，结合 Elasticsearch 查询统计能力，监测到某类错误日志量突然增大，超过某个阈值时，触发告警。
![](https://main.qcloudimg.com/raw/847984a82bcfe9b21b18b5df8dfb89fb.png)
- **机器学习（Machine Learning）**
在自定义数据告警的应用场景中，有时候不容易设置规则和阈值来定义的变化，这种情况下，就可以通过结合非监督型机器学习来预测数据的变化趋势和合理的波动范围，在数据偏离正常变化趋势时，发出告警通知。
更多功能，请参考官方说明 [Elastic Stack](https://www.elastic.co/cn/products/stack) 和 [API 文档](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/xpack-api.html)。

## 不同版本功能
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

具体功能详情请参见 [高级功能](https://www.elastic.co/cn/subscriptions)。

