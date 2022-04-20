## 2022年04月

<table><tr>
<th width="20%">动态名称</th>
<th width="45%">动态描述</th>
<th width="15%">发布时间</th>
<th width="20%">相关文档</th>
</tr><tr>
<td>支持 Schema 管理功能</td>
<td>Datahub 支持 Schema 管理功能，您可以将创建好的 Schema 绑定到具体的数据流入任务上，将会按该 Schema 对流入的数据进行格式校验。</td>
<td>2022-04-08</td>
<td><a href="https://cloud.tencent.com/document/product/597/72321">Schema 管理</a></td>
</tr><tr>
<td>HTTP 支持 Schema</td>
<td>Datahub 支持在 HTTP 接收数据上报的时候，根据指定的 Schema，对上报数据进行格式校验。</td>
<td>2022-04-08</td>
<td><a href="https://cloud.tencent.com/document/product/597/66017">HTTP 上报</a></td>
  </tr><tr>
<td>数据同步支持指定起始位置</td>
<td>-</td>
<td>2022-04-08</td>
<td><a href="https://cloud.tencent.com/document/product/597/59357">数据同步</a></td>
   </tr><tr> 
  <td>支持数据流出至对象存储 COS</td>
<td>Datahub 支持数据流出至对象存储 COS，您可以将 CKafka 数据分发至 COS 以便于对数据进行分析与下载等操作。</td>
<td>2022-04-08</td>
<td><a href="https://cloud.tencent.com/document/product/597/72322">流出至对象存储 COS</a></td>
   </tr><tr>
  <td>数据源类型支持对象存储 COS</td>
<td>Datahub 支持接入对象存储 COS 数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道。</td>
<td>2022-04-08</td>
<td><a href="https://cloud.tencent.com/document/product/597/72323">对象存储 COS</a></td>
</tr></table>




## 2022年03月

<table><tr>
<th width="20%">动态名称</th>
<th width="45%">动态描述</th>
<th width="15%">发布时间</th>
<th width="20%">相关文档</th>
</tr><tr>
<td>ES/clickhouse 数据流出任务支持丢弃解析失败消息</td>
<td>ES/clickhouse 数据流出任务支持丢弃解析失败消息，若不丢弃解析失败消息，则任务异常，转储不再继续。</td>
<td>2022-03-09</td>
<td><a href="https://cloud.tencent.com/document/product/597/66025">流出至 Elasticsearch Service</a></td>
</tr><tr>
<td>简单数据处理规格支持 JSONPATH 类型</td>
<td>JSONPATH 类型用于解析多层嵌套的 JSON 数据，用$符号开头，.符号定位到多层 JSON 的具体字段。</td>
<td>2022-03-09</td>
<td><a href="https://cloud.tencent.com/document/product/597/66020">简单数据处理</a></td>
</tr><tr>
<td>支持数据流出至日志服务 CLS</td>
<td>Datahub 支持数据流出至日志服务 CLS，您可以将 CKafka 数据分发至日志服务 CLS 便于解决业务问题定位，指标监控，安全审计等日问题。</td>
<td>2022-04-08</td>
<td><a href="https://cloud.tencent.com/document/product/597/70078">流出至日志服务 CLS</a></td>
</tr></table>




## 2022年01月

<table><tr>
<th width="20%">动态名称</th>
<th width="45%">动态描述</th>
<th width="15%">发布时间</th>
<th width="20%">相关文档</th>
</tr><tr>
  <td>数据源类型支持数据传输服务 DTS</td>
<td>Datahub 支持接入 DTS 数据，统一管理，再分发给下游的离线/在线处理平台，构建清晰的数据通道。</td>
<td>2022-01-23</td>
<td><a href="https://cloud.tencent.com/document/product/597/67389">数据传输服务 DTS</a></td>
  </tr><tr>
<td>支持数据流出至分布式数据仓库 TDW</td>
<td>Datahub 支持数据流出至分布式数据仓库 TDW，您可以将 CKafka 数据分发至分布式数据仓库 TDW 以对数据进行存储、查询和分析。</td>
<td>2022-01-23</td>
<td><a href="https://cloud.tencent.com/document/product/597/67388">流出至分布式数据仓库 TDW</a></td>
</tr><tr>
<td>支持数据流出至日志服务 CLS</td>
<td>Datahub 支持数据流出至日志服务 CLS，您可以将 CKafka 数据分发至日志服务 CLS 便于解决业务问题定位，指标监控，安全审计等日问题。</td>
<td>2022-01-23</td>
<td><a href="https://cloud.tencent.com/document/product/597/70078">流出至日志服务 CLS</a></td>
 </tr><tr>
<td>支持数据流出至 Clickhouse</td>
<td>Datahub 支持数据流出至 Clickhouse，您可以将 CKafka 数据分发至数据仓库 Clickhouse 以对数据进行存储、查询和分析。</td>
<td>2022-01-23</td>
<td><a href="https://cloud.tencent.com/document/product/597/67387">流出至 Clickhouse</a></td>
</tr></table>




## 2021年12月

<table><tr>
<th width="20%">动态名称</th>
<th width="45%">动态描述</th>
<th width="15%">发布时间</th>
<th width="20%">相关文档</th>
</tr><tr>
<td>Datahub 正式上线</td>
<td>数据接入平台（DataHub）是腾讯云上的数据接入和处理平台，一站式提供对数据的接入、处理和分发功能。Datahub 可以持续不断地接收和采集(APP、Web、云产品日志等)数据，实时处理，低成本搭建数据流转链路，构建数据源和数据处理系统间的桥梁。</td>
<td>2021-12-21</td>
<td><a href="https://cloud.tencent.com/document/product/597/66014">Datahub 概述</a></td>
</tr></table>

