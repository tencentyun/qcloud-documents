## 简介
高级特性，是指 Elasticsearch 官方商业特性（原 X-Pack 商业版插件包含的特性），包含了安全（Security）、SQL、机器学习（Machine Learning）、监控（Monitor）等高级功能，可以为 Elasticsearch 服务的的应用开发和运维管理，提供更有力的帮助。腾讯云 ES 已提供了包含高级特性的版本，您可以在创建购买集群时选择，下文介绍各版本详细功能。

## 购买指引
![](https://main.qcloudimg.com/raw/2a4012362412758e950aff249bf4e4a3.png)
如上图所示，在腾讯云 ES 创建购买页，有高级特性版本选项。腾讯云 ES 提供了3种可选的高级特性版本，版本说明如下：

| 对比项            | 基础版 | 白金版 | 开源版 |
| ----------------- | ------ | ------ | ------ |
| 是否包含 X-Pack   | ✓      | ✓      | ✕      |
| X-Pack 功能完整度 | 部分   | 全部   | 无     |

**购买推荐**  
为了能够使用腾讯云 Elasticsearch 更多高级功能，我们建议您在创建购买集群时，选择**白金版**，各版本具体功能介绍及区别见下文，产品的定价信息详见 [定价](https://cloud.tencent.com/document/product/845/18376)。

## 高级特性介绍
本文对部分常用高级特性进行了说明，完整的高级特性及说明，可查看官方说明 [Elastic Stack](https://www.elastic.co/cn/products/stack) 、[API 文档](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/xpack-api.html)。

>!  
>- 部分功能在不同的高级特性版本（基础、白金、开源）间有区别，请注意查看本文的说明。
>- 安全、告警、机器学习白金版特有，开源和基础版不包含。

- **安全（Security）**  
支持索引和字段级别，读写等细分权限的控制管理，实现数据安全防护、业务访问隔离，向正确的人员授予访问权限，阻止恶意破坏和数据泄露，有效地保障数据安全。
![](https://main.qcloudimg.com/raw/ec7529df345ebbf27db0453292eafe8d.png)
- **机器学习（Machine Learning）**  
在自定义数据告警的应用场景中，有时候不容易设置规则和阈值来定义的变化，这种情况下，就可以通过结合非监督型机器学习来预测数据的变化趋势和合理的波动范围，在数据偏离正常变化趋势时，发出告警通知。

>!监控、SQL，白金版、基础版包含，开源版不包含。不过，SQL 支持方面，开源版集成了其他的 SQL 插件，详细了解和使用，可查看 [elasticsearch-sql](https://github.com/NLPchina/elasticsearch-sql)。

- **监控**   
集群、节点、索引多个维度，全方位监控，实时了解集群运行情况，辅助应用开发及运维。  
![](https://main.qcloudimg.com/raw/012416b4755bed7e6cf8b57d0d0fa23a.png)
- **SQL**  
提供了通过传统数据库 SQL 工具 ，实现对 Elasticsearch 数据进行全文本检索、数据统计分析功能，支持 CLI、REST 等接入方式，**白金版还支持 JDBC 连接**。可以实现同原有业务系统的无缝对接，降低新技术学习成本。
![](https://main.qcloudimg.com/raw/ca19a8665919a85b9a08b5d9451ec3de.png)

### 高级特性版本功能详细对比
本章节对各版本的部分重点功能进行了对比说明，完整的功能对比，可查看官方介绍 [Elastic 各版本功能说明](https://www.elastic.co/cn/subscriptions)。

>?下表中 ⚫、◑、- 用于表示对应特性的功能完整度，⚫：包含全部功能；◑：包含部分功能；-：不包含。

<table class="tg">
  <tr>
    <th class="tg-s268">模块</th>
    <th class="tg-s268">特性</th>
    <th class="tg-s268">开源版</th>
    <th class="tg-s268">基础版</th>
    <th class="tg-s268">白金版</th>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="6">Elasticsearch</td>
    <td class="tg-s268">可扩展性和弹性</td>
    <td class="tg-s6z2">◑</td>
    <td class="tg-s6z2">◑</td>
    <td class="tg-s6z2">⚫</td>
  </tr>
  <tr>
    <td class="tg-s268">查询和分析</td>
    <td class="tg-s6z2">◑</td>
    <td class="tg-s6z2">◑</td>
    <td class="tg-s6z2">⚫</td>
  </tr>
  <tr>
    <td class="tg-s268">数据扩充</td>
    <td class="tg-s6z2">⚫</td>
    <td class="tg-s6z2">⚫</td>
    <td class="tg-s6z2">⚫</td>
  </tr>
  <tr>
    <td class="tg-s268"><a href="#manage_tool">管理和工具</a></td>
    <td class="tg-s6z2">◑</td>
    <td class="tg-s6z2">◑</td>
    <td class="tg-s6z2">⚫</td>
  </tr>
  <tr>
    <td class="tg-s268"><a href="#Security">Security</a></td>
    <td class="tg-s6z2">-</td>
    <td class="tg-s6z2">-</td>
    <td class="tg-s6z2">⚫</td>
  </tr>

  <tr>
    <td class="tg-s268"><a href="#machine_learning">Machine Learning</a></td>
    <td class="tg-s6z2">-</td>
    <td class="tg-s6z2">-</td>
    <td class="tg-s6z2">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="7">Kibana</td>
    <td class="tg-0lax">探索和可视化</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">堆栈管理和工具</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">堆栈监测</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">分享与合作</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">本地化 UI</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Security</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Machine Learning</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="4">Beats</td>
    <td class="tg-0lax">数据收集</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">数据传输</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">模块</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">监测和管理</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="5">Logstash</td>
    <td class="tg-0lax">数据收集</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">数据扩充</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">数据传输</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">模块</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">监测和管理</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">◑</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="7">ELASTIC APM</td>
    <td class="tg-0lax">APM 服务器</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">APM 代理</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Kibana 中的 APM 仪表板</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">APM UI</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">分布式追踪</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Alerting  整合</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Machine  Learning 整合</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">ELASTIC 日志</td>
    <td class="tg-0lax">日志采集器（Filebeat）</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">常用数据源的仪表板</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Logs UI</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">ELASTIC 基础设施</td>
    <td class="tg-0lax">指标采集器（Metricbeat）</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">常用数据源的仪表板</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Infrastructure  UI</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="3">ELASTIC 运行状态监控</td>
    <td class="tg-0lax">运行状态监测（Heartbeat）</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">Kibana 里的运行状态仪表板</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
  <tr>
    <td class="tg-0lax">运行状态监测 UI</td>
    <td class="tg-baqh">-</td>
    <td class="tg-baqh">⚫</td>
    <td class="tg-baqh">⚫</td>
  </tr>
</table>

**Elasticsearch 部分功能详细说明：**

>?下表中 ✓ 用于表示是否拥有对应特性的功能，✓：表示具备；-：表示不具备。

<table class="tg">
  <tr>
    <th class="tg-s268">Elasticsearch功能模块</th>
    <th class="tg-s268">细项</th>
    <th class="tg-s268">开源版</th>
    <th class="tg-s268">基础版</th>
    <th class="tg-s268">白金版</th>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="11"><a id="manage_tool">管理和工具</a></td>
    <td class="tg-s268">REST API</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">语言客户端</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">快照/恢复</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">_仅源快照</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">SQL 解释器 CLI</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">数据汇总</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">索引生命周期管理</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">冻结索引</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">升级助手 API</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">JDBC 客户端</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">ODBC 客户端</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="6"><a id="Security">Security</a></td>
    <td class="tg-s268">加密通信</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">基于角色的访问控制</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">文件和原生身份验证</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">审核日志</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>  
  <tr>
    <td class="tg-s268">基于属性的权限控制</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">字段和文档级别安全性</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-0lax" rowspan="6"><a id="machine_learning">机器学习</a></td>
    <td class="tg-s268">时序型异常监测</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">输入/实体分析</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">日志消息分类</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">根本原因指示</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">异常情况警报</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
  <tr>
    <td class="tg-s268">时序型预测</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">-</td>
    <td class="tg-s268">✓</td>
  </tr>
</table>



