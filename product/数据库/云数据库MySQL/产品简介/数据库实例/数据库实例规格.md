本文为您介绍云数据库 MySQL 的实例规格，帮助您了解 MySQL 实例的最新规格信息，您可以查看本文了解各规格的具体配置。

## 双节点/三节点（本地 SSD 盘）
主实例（双节点/三节点结构）、只读实例、灾备实例的规格信息可参考此表。
<table class="table-striped">
<tbody>
<tr><th>隔离策略</th><th>CPU 和内存</th><th>最大 IOPS</th><th>存储空间</th></tr>
<tr>
<td rowspan="14">通用型</td>
<td>1核 1000MB</td><td>1200</td><td rowspan="4">25GB - 3000GB</td></tr>        
<tr>
<td>1核 2000MB</td><td>2000</td></tr>
<tr>
<td>2核 4000MB</td><td>4000</td></tr>
<tr>
<td>4核 8000MB</td><td>8000</td></tr>
<tr>
<td>4核 16000MB</td><td>14000</td><td rowspan="6">25GB - 4000GB</td></tr>
<tr>
<td>8核 16000MB</td><td>20000</td></tr>
<tr>
<td>8核 32000MB</td><td>28000</td></tr>
<tr>
<td>16核 32000MB</td><td>32000</td></tr>
<tr>
<td>16核 64000MB</td><td>40000</td></tr>
<tr>
<td>16核 96000MB</td><td>40000</td></tr>
<tr>
<td>16核 128000MB</td><td>40000</td><td rowspan="3">25GB - 8000GB</td></tr>
<tr>
<td>24核 244000MB</td><td>60000</td></tr>
<tr>
<td>32核 256000MB</td><td>80000</td></tr>
<tr>
<td>48核 488000MB</td><td>120000</td><td rowspan="1">25GB - 12000GB</td></tr>
<tr>
<td rowspan="26">独享型</td>
<td>2核 16000MB</td><td>8000</td><td rowspan="7">25GB - 3000GB</td></tr>        
<tr>
<td>4核 16000MB</td><td>10000</td></tr>
<tr>
<td>4核 24000MB</td><td>13000</td></tr>
<tr>
<td>4核 32000MB</td><td>16000</td></tr>
<tr>
<td>8核 32000MB</td><td>32000</td></tr>
<tr>
<td>8核 48000MB</td><td>36000</td></tr>
<tr>
<td>8核 64000MB</td><td>40000</td></tr>
<tr>
<td>12核 48000MB</td><td>36000</td><td rowspan="15">25GB - 6000GB</td></tr>
<tr>
<td>16核 64000MB</td><td>60000</td></tr>
<tr>
<td>12核 72000MB</td><td>40000</td></tr>
<tr>
<td>12核 96000MB</td><td>48000</td></tr>
<tr>
<td>16核 96000MB</td><td>60000</td></tr>
<tr>
<td>24核 96000MB</td><td>72000</td></tr>
<tr>
<td>16核 128000MB</td><td>60000</td></tr>
<tr>
<td>32核 128000MB</td><td>80000</td></tr>
<tr>
<td>24核 144000MB</td><td>76000</td></tr>
<tr>
<td>24核 192000MB</td><td>80000</td></tr>
<tr>
<td>32核 192000MB</td><td>90000</td></tr>
<tr>
<td>48核 192000MB</td><td>120000</td></tr>
<tr>
<td>32核 256000MB</td><td>100000</td></tr>
<tr>
<td>48核 288000MB</td><td>140000</td></tr>
<tr>
<td>48核 384000MB</td><td>140000</td></tr>
<tr>
<td>64核 256000MB</td><td>150000</td><td rowspan="2">25GB - 9000GB</td></tr>
<tr>
<td>64核 384000MB</td><td>150000</td></tr>
<tr>
<td>64核 512000MB</td><td>150000</td><td rowspan="2">25GB - 12000GB</td></tr>
<tr>
<td>90核 720000MB</td><td>150000</td></tr>
</tbody></table>        

>?不同地域的实例规格对应的存储空间上限可能不同，请以实际购买页为准。

## 单节点（SSD 云硬盘）
<table class="table-striped">
<thead><tr><th>隔离策略</th><th>CPU 和内存</th><th>最大 IOPS</th><th>最大吞吐量</th><th>存储空间</th></tr></thead>
<tbody>
<tr>
<td rowspan="8">基础型</td>
<td>1核 1000MB</td><td rowspan="8">随机 IOPS 性能计算公式：随机 IOPS = min{1800 + 30 × 容量（GB）, 26000}<br>最大 IOPS：26000</td><td rowspan="8">吞吐性能计算公式（MB/s）：吞吐 = min{120 + 0.2 × 容量（GB）, 260}<br>最大吞吐量（MB/s）：260MB/s</td><td rowspan="8">20GB - 32000GB</td></tr>
<tr>
<td>1核 2000MB</td></tr>
<tr>
<td>2核 4000MB</td></tr>
<tr>
<td>2核 8000MB</td></tr>
<tr>
<td>4核 8000MB</td></tr>
<tr>
<td>4核 16000MB</td></tr>
<tr>
<td>8核 16000MB</td></tr>
<tr>
<td>8核 32000MB</td></tr>
</tbody></table>

## 单节点（增强型 SSD 云硬盘）
<table class="table-striped">
<thead><tr><th>隔离策略</th><th>CPU 和内存</th><th>最大 IOPS</th><th>最大吞吐量</th><th>存储空间</th></tr></thead>
<tbody>
<tr>
<td rowspan="8">基础型</td>
<td>1核 1000MB</td><td rowspan="8">随机 IOPS 性能计算公式：随机 IOPS = min{1800 + 50 × 容量（GB）, 50000}<br>最大 IOPS：50000</td><td rowspan="8">吞吐性能计算公式（MB/s）：吞吐 = min{120 + 0.5 × 容量（GB）, 350}<br>最大吞吐量（MB/s）：350MB/s</td><td rowspan="8">20GB - 32000GB</td></tr>
<tr>
<td>1核 2000MB</td></tr>
<tr>
<td>2核 4000MB</td></tr>
<tr>
<td>2核 8000MB</td></tr>
<tr>
<td>4核 8000MB</td></tr>
<tr>
<td>4核 16000MB</td></tr>
<tr>
<td>8核 16000MB</td></tr>
<tr>
<td>8核 32000MB</td></tr>
</tbody></table>
