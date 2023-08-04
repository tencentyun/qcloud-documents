ES Serverless 服务目前支持 [按量计费](https://cloud.tencent.com/document/product/555/9617) 计费模式，采用小时结后付费模式，基于前一小时用量按量扣费。
>? 您可通过 [价格计算器](https://buy.cloud.tencent.com/price/es/calculator)，估算使用 ES Serverless 服务的费用。

## 计费项介绍
计费项包括计算流量、数据存储以及接口调用，其介绍如下：
<table>
<tr>
<th class="tg-llyw" colspan="2" width=15%>计费项</th>
<th class="tg-llyw" colspan="2" width=40%>计费项描述</th>
<th class="tg-llyw" colspan="2" width=40%>计费说明</th>
</tr>
<tr>
<td class="tg-llyw" colspan="2" width=15%>计算流量</td>
<td class="tg-llyw" colspan="2" width=40%>数据写入、构建索引以及分词时产生的流量大小，计算流量的大小和您数据中的字段以及字段长度有关。</td>
<td class="tg-llyw" colspan="2" width=40%>计算公式：（0.1 + 索引字段占比）* 日增原始数据大小，索引字段占比默认一般为100%。<br>例如，您每天写入的原始数据大小为1GB，对所有字段构建索引，则计算流量的大小为1.1GB。</td>
</tr>
<tr>
<td class="tg-llyw" colspan="2" width=15%>数据存储</td>
<td class="tg-llyw" colspan="2" width=40%>数据存储大小和原始数据大小、构建索引产生的数据膨胀以及存储时长相关。</td>
<td class="tg-llyw" colspan="2" width=40%>计算公式：（0.12+索引字段占比）* 日增原始数据大小 * 存储时长，索引字段占比默认一般为100%。<br>例如，您每天写入的原始数据大小为1GB，数据存储3天，对所有字段构建索引，则在第4天之后，数据存储的大小将稳定在3.36GB。</td>
<tr>
<td class="tg-llyw" colspan="2" width=15%>接口调用</td>
<td class="tg-llyw" colspan="2" width=40%>根据读写时调用 ES Serverless 服务的接口的总次数进行计费。</td>
<td class="tg-llyw" colspan="2" width=40%>例如您有1亿条数据，通过 bulk API 进行批量写入，bulk size 为100条/次，则写入过程中将产生1百万次写入请求。（接口调用费用很低廉，可忽略不计，建议单次批量写入的文档数设置为2000-5000条，有助于提升写入性能。）</td>
</tr>
</table>

## 定价介绍
<table>
<tr>
<th rowspan="2" width=25%>地域</th>
<th colspan=3>计费项</th>
</tr>
<tr>
<th class="tg-llyw" width=25%>计算流量（元/GB）</th>
<th class="tg-llyw"  width=25%>数据存储（元/GB/天）</th>
<th class="tg-llyw" width=25%>接口调用（元/百万次）</th>
</tr>
<tr>
<td width=25%>北京/上海/广州/南京</td>
<td width=25%>0.29</td>
<td width=25%>0.01</td>
<td width=25%>0.1</td>
</tr>
<tr>
<td width=25%>中国香港</td>
<td width=25%>0.34</td>
<td width=25%>0.014</td>
<td width=25%> 0.12</td>
</tr>
</table>

## 费用计算案例
假设您 App 的访问日志平均为100 Byte/条，1天共1亿条日志（即每天原始日志大小约为9.3GB），数据存储7天，对所有字段构建索引，通过使用广州地域的 ES Serverless 服务进行 App 日志分析。经计算，在第8天之后，数据存储大小将稳定在72.9GB，1天的费用约为3.7元，具体明细如下表所示：
<table>
<tr>
<th class="tg-llyw" width=10%>计费项</th>
<th class="tg-llyw"  width=10%>说明</th>
<th class="tg-llyw"  width=35%>用量估算</th>
<th class="tg-llyw"  width=25%>单价</th>
<th class="tg-llyw"  width=10%><nobr>费用估算（元）</th>
</tr>
<tr>
<td class="tg-llyw"  width=15%>计算流量</td>
<td class="tg-llyw"  width=40%>对所有字段构建索引，索引字段占比为100%。</td>
<td class="tg-llyw"  width=15%>（0.1 + 100%）* 9.3 = 10.23（GB）</td>
<td class="tg-llyw"  width=15%>0.29元/GB</td>
<td class="tg-llyw"  width=15%>2.97</td>
</tr>
<tr>
<td class="tg-llyw"  width=15%>数据存储</td>
<td class="tg-llyw"  width=40%>对所有字段构建索引，索引字段占比为100%。</td>
<td class="tg-llyw"  width=15%>（0.12 + 100%）* 9.3 * 7 = 72.9（GB）</td>
<td class="tg-llyw"  width=15%>0.01元/天</td>
<td class="tg-llyw"  width=15%>0.729</td>
</tr>
<tr>
<td class="tg-llyw"  width=15%>接口调用</td>
<td class="tg-llyw"  width=40%>bulk size 为5,000条/次</td>
<td class="tg-llyw"  width=15%>1亿条文档/bulk size = 20,000次</td>
<td class="tg-llyw"  width=15%><nobr>0.1元/百万次</td>
<td class="tg-llyw"  width=15%>0.002</td>
</tr>
</table>

## 新用户体验券
自2023年8月1日起，开通 ES Serverless 服务的新用户，可免费 [领取50元代金券](https://cloud.tencent.com/act/pro/es_serverless)，抵扣使用 Serverless 服务产生的费用，有效期自领取之日起持续90天，超出的费用，将按照对应计费项定价进行扣费。
>? 索引字段占比主要用于估算构建索引产生的流量与存储消耗。例如，您有10个类型、长度相等的字段，您对其中的5个字段构建索引，则索引字段占比为50%，该计算方法仅供参考，实际资源消耗与您的字段值以及字段长度相关，当索引字段占比小于40%时，默认按照40%计算。


