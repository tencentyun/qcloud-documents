本文介绍 CKafka 内核小版本升级变更记录。

## 2.8.1 版本
<table>
<thead>
<tr>
<th style = "width:20%">版本</th>
<th>功能</th>
<th style = "width:30%">备注</th>
</tr>
</thead>
<tbody><tr>
<td>2.8.1_1.0.3</td>
<td>监控上报禁止#。</td>
<td>无</td>
</tr>
<tr>
<td>2.8.1_1.0.4</td>
<td>1. 自动创建 Consumer Group 开关。 <br>2. 支持 Scram 鉴权方式。<br> 3. 添加查看生产者的连接数。</td>
<td>无</td>
</tr>
</tbody></table>

## 2.4.2 版本
<table>
<thead>
<tr>
<th style = "width:20%">版本</th>
<th>功能</th>
<th style = "width:30%">备注</th>
</tr>
</thead>
<tbody><tr>
<td>2.12-2.4.2_1.0.5</td>
<td>支持 Producer 连接数统计。</td>
<td>无</td>
</tr>
<tr>
<td>2.12-2.4.2_1.0.6</td>
<td>1. 支持生产耗时日志输出。  <br>2. 监控上报禁止#。</td>
<td>无</td>
</tr>
<tr>
<td>2.12-2.4.2_1.0.7</td>
<td>支持 token 鉴权。</td>
<td>无</td>
</tr>
<tr>
<td>2.12-2.4.2_1.0.8</td>
<td>1. 支持限制自动创建 Consumer Group  <br>2. 支持 Scram 鉴权方式。</td>
<td>无</td>
</tr>
<tr>
<td>2.12-2.4.2_1.1.1</td>
<td>判断是否是保护端口时，listenerName 和 listenersSize 先放到变量里面，避免请求量太高，导致消耗 CPU。</td>
<td>无</td>
</tr>
<tr>
<td>2.12-2.4.2_1.1.2</td>
<td>Consumer offset reset after new segment rolling 合回了一个社区的 bug，详情请参见 <a href = "https://issues.apache.org/jira/browse/KAFKA-9543">KAFKA-9543</a>。</td>
<td>无</td>
</tr>
</tbody></table>

## 1.1.1 版本

<table>
<thead>
<tr>
<th style = "width:20%">版本</th>
<th>功能</th>
<th style = "width:30%">备注</th>
</tr>
</thead>
<tbody><tr>
<td>2.11-1.1.1_1.0.11</td>
<td>支持 Producer 连接数统计。</td>
<td>无</td>
</tr>
<tr>
<td>2.11-1.1.1_1.0.12</td>
<td>支持生产耗时日志输出。</td>
<td>无</td>
</tr>
<tr>
<td>2.11-1.1.1_1.0.13</td>
<td>支持 token 鉴权。</td>
<td>无</td>
</tr>
<tr>
<td>2.11-1.1.1_1.1.0</td>
<td>getMetadata 锁性能优化。</td>
<td>无</td>
</tr>
<tr>
<td>2.11-1.1.1_1.1.1</td>
<td>ack=all 软性降级。</td>
<td>1. 这个版本独立于分支1.1.1_1.1.1-ackDowngrade。 <br>2. 代码不合并回 1.1.1-publish。 <br>3. 客户提单升级。</td>
</tr>
<tr>
<td>2.11-1.1.1_1.1.2</td>
<td>getMetadata 添加 client IP日志。</td>
<td>无</td>
</tr>
</tbody></table>





## 0.10.2 版本

<table>
<thead>
<tr>
<th style = "width:20%">版本</th>
<th>功能</th>
<th style = "width:30%">备注</th>
</tr>
</thead>
<tbody><tr>
<td>0.10.2.1_1.2.8</td>
<td>支持 producer 连接数统计。</td>
<td>无</td>
</tr>
</tbody></table>



