本文介绍 TDSQL-C MySQL 版 Serverless 服务的计费说明。

## 计费模式
Serverless 服务的计算和存储独立计费：计算按 CCU 个数计费，存储按使用量 GB 计费，计费系统按秒计费，按小时结算。

## 计费公式
**Serverless 总费用 = 计算节点费用 + 存储空间费用 = Serverless 算力价格 × CCU 量 + 存储空间价格 × 存储空间**

## Serverless 算力价格
<table>
<thead><tr>
<th rowspan=2 >计费单元</th>
<th >广州、上海、北京、南京</th>
<tr>
<th>CCU 按使用计费价格（元/个/秒）</th></tr></thead>
<tbody><tr>
<td>Serverless 实例</td>
<td>0.000095</td></tr>
</tbody></table>

>?
>- CCU（TDSQL-C Compute Unit）为 Serverless 的计算计费单位，一个 CCU 近似等于1个 CPU 和 2GB 内存的计算资源，每个计费周期的 CCU 使用数量为：`数据库所使用的 CPU 核数` 与 `内存大小的1/2` 二者中取最大值。
>- 您可参考 [服务算力配置](https://cloud.tencent.com/document/product/1003/81821) 选择相应的 CCU 最大最小值，存储空间上限与最大值相对应的 [普通计算节点规格](https://cloud.tencent.com/document/product/1003/71887#CYNOSJSJDGE) 的最大存储空间一致。

## [存储空间价格](id:cckjjg)
Serverless 服务版集群存储空间计费方式为按量计费，按照0.00486元/GB/小时收费。
