## Kona JDK 介绍

### Kona JDK 是什么？

Tencent Kona JDK，是腾讯基于社区 Open JDK 定制开发的 JDK 版本，广泛服务于腾讯内部业务和腾讯云上客户，经过了内部大数据和AI等复杂业务场景的验证，为腾讯 JAVA 生态提供专业持续的保障，具有稳定性高、安全性高、性能好等特点。

### Kona JDK 优势

- 高性能和低成本：在腾讯大数据计算场景数万台服务器生产集群验证下，和Open JDK 8相比，Kona JDK 8吞吐提升8%，CPU 和内存使用率均降低10%左右；
- 开箱即用的 Vector API 支持：解决了向量指令适配导致的 JVM crash 等问题，业界率先落地，稳定支持广告训练场景；
- 多种 GC 优化：G1 GC 内存 overhead 和并行 Full GC 算法优化，同时针对强实时在线服务需求，推出生产级别的 ZGC；
- KonaFiber 协程：已经在IEG天美游戏业务合作落地，目前根据benchmark测试，协程创建/切换/调度等性能大幅超过社区Loom；
- 支持 ARM 国产化 CPU；

## Kona JDK 设置

1. 操作页面：集群详情页-高级配置页面。
2. 重启：切换JDK后，集群会重启，重启过程中不可进行变配升级等操作。
![](https://qcloudimg.tencent-cloud.cn/raw/112fd19cba5f57d04daa41b68721351e.png)

## 数据对比

本文提供4 核16G 3个节点的腾讯云 Elasticsearch Service 集群 切换 腾讯自研 Kona JDK + G1-GC 的集群性能指标。
>?数据为官方提供的 geonames，包含11396503条地理位置信息，总大小接近3GB，包含了 text、long、geo 等类型数据，覆盖行列存。

对比4核16GB SSD 200G 3节点的腾讯云 ES在 Kona JDK（11.0.9.1-ga+1） + G1-GC 和 Oracle JDK （1.8.0_181-b13）+CMS-GC 的集群性能指标，Kona JDK + G1-GC 各方面性能均有一定优势。主要得益于腾讯云自研 JDK 以及 GC 参数调优等方面的优化。

<table>
<thead>
<tr>
<th width=10%>说明</th>
<th width=15%>Metric</th>
<th width=15%>Task</th>
<th width=15%>腾讯云ES(Open JDK+CMS-GC)</th>
<th width=15%>腾讯云ES(Kona JDK+G1-GC)</th>
<th width=20%>差异值（Kona JDK-Open JDK）</th>
<th width=5%>Unit</th>
<th width=5%>优劣</th>
</tr>
</thead>
<tbody>
<tr>
<td>写入总耗时</td>
<td >Cumulative indexing time of  primary shards</td>
<td >&nbsp;</td>
<td >17.7745</td>
<td >17.41703333</td>
<td >-0.35747</td>
<td >min</td>
<td >优</td>
</tr><tr>
<td >GC 总次数、耗时统计</td>
<td >Total Young Gen GC time</td>
<td >&nbsp;</td>
<td >76.597</td>
<td >4.988</td>
<td >-71.609</td>
<td >s</td>
<td >优</td>
</tr><tr>
<td >Total Young Gen GC count</td>
<td >&nbsp;</td>
<td >4129</td>
<td >981</td>
<td >-3148</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Total Old Gen GC time</td>
<td >&nbsp;</td>
<td >0.175</td>
<td >0</td>
<td >-0.175</td>
<td >s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Total Old Gen GC count</td>
<td >&nbsp;</td>
<td >2</td>
<td >0</td>
<td >-2</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >存储大小</td>
<td >Store  size</td>
<td >&nbsp;</td>
<td >2.885286688</td>
<td >2.87756444</td>
<td >-0.00772</td>
<td >GB</td>
<td >-</td>
</tr><tr>
<td >Translog  size</td>
<td >&nbsp;</td>
<td >3.59E-07</td>
<td >3.59E-07</td>
<td >0</td>
<td >GB</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >堆内存使用量</td>
<td >Heap  used for segments</td>
<td >&nbsp;</td>
<td >0.045909882</td>
<td >0.045909882</td>
<td >0</td>
<td >MB</td>
<td >&nbsp;</td>
</tr><tr>
<td >Heap  used for doc values</td>
<td >&nbsp;</td>
<td >0.000507355</td>
<td >0.000507355</td>
<td >0</td>
<td >MB</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Heap  used for terms</td>
<td >&nbsp;</td>
<td >0.037261963</td>
<td >0.037261963</td>
<td >0</td>
<td >MB</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Heap  used for norms</td>
<td >&nbsp;</td>
<td >0.003967285</td>
<td >0.003967285</td>
<td >0</td>
<td >MB</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Heap  used for points</td>
<td >&nbsp;</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >MB</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Heap  used for stored fields</td>
<td >&nbsp;</td>
<td >0.004173279</td>
<td >0.004173279</td>
<td >0</td>
<td >MB</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >segment 总数量</td>
<td >Segment  count</td>
<td >&nbsp;</td>
<td >7</td>
<td >7</td>
<td >0</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >写入吞吐、耗时统计</td>
<td >Min  Throughput</td>
<td >index-append</td>
<td >82341.03288</td>
<td >83678.1806</td>
<td >1337.14773</td>
<td >docs/s</td>
<td >优</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >index-append</td>
<td >85463.64521</td>
<td >87617.83008</td>
<td >2154.18488</td>
<td >docs/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >index-append</td>
<td >85203.41999</td>
<td >87749.05385</td>
<td >2545.63387</td>
<td >docs/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >index-append</td>
<td >88282.10166</td>
<td >90448.56087</td>
<td >2166.45921</td>
<td >docs/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >index-append</td>
<td >369.9228433</td>
<td >360.6725829</td>
<td >-9.25026</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >index-append</td>
<td >582.2157889</td>
<td >521.3938987</td>
<td >-60.82189</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  latency</td>
<td >index-append</td>
<td >2566.001355</td>
<td >3331.056718</td>
<td >765.05536</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile latency</td>
<td >index-append</td>
<td >3249.023346</td>
<td >4277.054507</td>
<td >1028.03116</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >index-append</td>
<td >3677.799375</td>
<td >5966.865065</td>
<td >2289.06569</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >index-append</td>
<td >369.9228433</td>
<td >360.6725829</td>
<td >-9.25026</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >index-append</td>
<td >582.2157889</td>
<td >521.3938987</td>
<td >-60.82189</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >index-append</td>
<td >2566.001355</td>
<td >3331.056718</td>
<td >765.05536</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile service time</td>
<td >index-append</td>
<td >3249.023346</td>
<td >4277.054507</td>
<td >1028.03116</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >index-append</td>
<td >3677.799375</td>
<td >5966.865065</td>
<td >2289.06569</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >index-append</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >index 指标统计</td>
<td >Min  Throughput</td>
<td >index-stats</td>
<td >90.00917629</td>
<td >90.01515386</td>
<td >0.00598</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >index-stats</td>
<td >90.01643728</td>
<td >90.02981242</td>
<td >0.01338</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >index-stats</td>
<td >90.01545276</td>
<td >90.03117871</td>
<td >0.01573</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >index-stats</td>
<td >90.0358266</td>
<td >90.0417802</td>
<td >0.00595</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >index-stats</td>
<td >2.71807611</td>
<td >2.706557978</td>
<td >-0.01152</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >index-stats</td>
<td >3.542617336</td>
<td >3.530823253</td>
<td >-0.01179</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >index-stats</td>
<td >4.209796032</td>
<td >4.047978334</td>
<td >-0.16182</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th percentile  latency</td>
<td >index-stats</td>
<td >10.97994745</td>
<td >4.319285007</td>
<td >-6.66066</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >index-stats</td>
<td >18.87320075</td>
<td >4.494163208</td>
<td >-14.37904</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >index-stats</td>
<td >1.521472819</td>
<td >1.515000127</td>
<td >-0.00647</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  service time</td>
<td >index-stats</td>
<td >1.832026243</td>
<td >1.815253124</td>
<td >-0.01677</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >index-stats</td>
<td >2.493222319</td>
<td >2.149661649</td>
<td >-0.34356</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile service time</td>
<td >index-stats</td>
<td >3.265745808</td>
<td >2.558897269</td>
<td >-0.70685</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th percentile  service time</td>
<td >index-stats</td>
<td >18.49333011</td>
<td >2.714292146</td>
<td >-15.77904</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >index-stats</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >node 指标统计</td>
<td >Min  Throughput</td>
<td >node-stats</td>
<td >89.77465925</td>
<td >89.9748329</td>
<td >0.20017</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >node-stats</td>
<td >89.90322336</td>
<td >89.99453842</td>
<td >0.09132</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >node-stats</td>
<td >89.92739222</td>
<td >89.99716573</td>
<td >0.06977</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >node-stats</td>
<td >89.95708367</td>
<td >90.01224368</td>
<td >0.05516</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >node-stats</td>
<td >2.864421345</td>
<td >2.847921103</td>
<td >-0.0165</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >node-stats</td>
<td >4.03423449</td>
<td >4.02287906</td>
<td >-0.01136</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >node-stats</td>
<td >4.780995743</td>
<td >4.921176638</td>
<td >0.14018</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile latency</td>
<td >node-stats</td>
<td >11.95199643</td>
<td >8.974571229</td>
<td >-2.97743</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >node-stats</td>
<td >19.6932666</td>
<td >13.60371523</td>
<td >-6.08955</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >node-stats</td>
<td >2.031991258</td>
<td >2.032643184</td>
<td >0.00065</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >node-stats</td>
<td >2.502718102</td>
<td >2.520979941</td>
<td >0.01826</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >node-stats</td>
<td >3.355697962</td>
<td >3.726954078</td>
<td >0.37126</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile service time</td>
<td >node-stats</td>
<td >6.070044631</td>
<td >8.64341661</td>
<td >2.57337</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >node-stats</td>
<td >19.13440693</td>
<td >11.63361594</td>
<td >-7.50079</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >node-stats</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >默认查询，所有文档  score 为1（match_all）</td>
<td >Min  Throughput</td>
<td >default</td>
<td >49.66239789</td>
<td >49.88425331</td>
<td >0.22186</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >default</td>
<td >49.80337019</td>
<td >49.93227136</td>
<td >0.1289</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >default</td>
<td >49.8202478</td>
<td >49.93857317</td>
<td >0.11833</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >default</td>
<td >49.87518669</td>
<td >49.9563597</td>
<td >0.08117</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th percentile  latency</td>
<td >default</td>
<td >3.394149244</td>
<td >3.262675833</td>
<td >-0.13147</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >default</td>
<td >4.578030575</td>
<td >4.408122599</td>
<td >-0.16991</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >default</td>
<td >6.253439859</td>
<td >4.992298558</td>
<td >-1.26114</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile latency</td>
<td >default</td>
<td >19.66198959</td>
<td >8.490681676</td>
<td >-11.17131</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >default</td>
<td >20.0197883</td>
<td >8.887056261</td>
<td >-11.13273</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >default</td>
<td >2.622524276</td>
<td >2.356512472</td>
<td >-0.26601</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >default</td>
<td >3.102052212</td>
<td >2.851721831</td>
<td >-0.25033</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >default</td>
<td >4.579989612</td>
<td >3.174401047</td>
<td >-1.40559</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile service time</td>
<td >default</td>
<td >18.49881567</td>
<td >8.051926313</td>
<td >-10.44689</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >default</td>
<td >18.62356346</td>
<td >8.21478758</td>
<td >-10.40878</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >default</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >term 条件查询</td>
<td >Min  Throughput</td>
<td >term</td>
<td >98.93043451</td>
<td >99.71455545</td>
<td >0.78412</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >term</td>
<td >99.33413382</td>
<td >99.81852777</td>
<td >0.48439</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >term</td>
<td >99.38459416</td>
<td >99.83007784</td>
<td >0.44548</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >term</td>
<td >99.57176235</td>
<td >99.88279227</td>
<td >0.31103</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >term</td>
<td >3.250969574</td>
<td >3.228969406</td>
<td >-0.022</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >term</td>
<td >3.966032993</td>
<td >3.853681684</td>
<td >-0.11235</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >term</td>
<td >10.50691157</td>
<td >4.505703636</td>
<td >-6.00121</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile latency</td>
<td >term</td>
<td >17.10123536</td>
<td >7.033703398</td>
<td >-10.06753</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >term</td>
<td >19.53481138</td>
<td >9.737900458</td>
<td >-9.79691</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >term</td>
<td >2.501523588</td>
<td >2.488659229</td>
<td >-0.01286</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  service time</td>
<td >term</td>
<td >3.069854062</td>
<td >2.982806601</td>
<td >-0.08705</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >term</td>
<td >7.066733902</td>
<td >3.509562407</td>
<td >-3.55717</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile service time</td>
<td >term</td>
<td >16.17278317</td>
<td >6.230151438</td>
<td >-9.94263</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th percentile  service time</td>
<td >term</td>
<td >19.29396484</td>
<td >8.562799543</td>
<td >-10.73117</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >term</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >词组查询（query）</td>
<td >Min  Throughput</td>
<td >phrase</td>
<td >109.1666798</td>
<td >109.563189</td>
<td >0.39651</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >phrase</td>
<td >109.4885892</td>
<td >109.726084</td>
<td >0.23749</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median Throughput</td>
<td >phrase</td>
<td >109.531043</td>
<td >109.7627623</td>
<td >0.23172</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >phrase</td>
<td >109.6776159</td>
<td >109.8360981</td>
<td >0.15848</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >phrase</td>
<td >2.736125607</td>
<td >2.723197918</td>
<td >-0.01293</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >phrase</td>
<td >3.2537736</td>
<td >3.277133778</td>
<td >0.02336</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >phrase</td>
<td >5.174562978</td>
<td >5.252283504</td>
<td >0.07772</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile latency</td>
<td >phrase</td>
<td >17.94986153</td>
<td >11.65228278</td>
<td >-6.29758</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >phrase</td>
<td >20.16797382</td>
<td >18.0053385</td>
<td >-2.16264</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th percentile  service time</td>
<td >phrase</td>
<td >1.983109396</td>
<td >1.964103896</td>
<td >-0.01901</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >phrase</td>
<td >2.38582911</td>
<td >2.413296979</td>
<td >0.02747</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >phrase</td>
<td >4.028498856</td>
<td >3.426500661</td>
<td >-0.602</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th percentile  service time</td>
<td >phrase</td>
<td >17.23640091</td>
<td >10.3977854</td>
<td >-6.83862</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >phrase</td>
<td >19.54707783</td>
<td >17.02223159</td>
<td >-2.52485</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >不带缓存的聚合查询（aggregation）</td>
<td >error  rate</td>
<td >phrase</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
</tr><tr>
<td >Min  Throughput</td>
<td >country_agg_uncached</td>
<td >2.996727436</td>
<td >2.999315225</td>
<td >0.00259</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >country_agg_uncached</td>
<td >2.997330498</td>
<td >2.999446981</td>
<td >0.00212</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >country_agg_uncached</td>
<td >2.997367399</td>
<td >2.999449396</td>
<td >0.00208</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >country_agg_uncached</td>
<td >2.997811835</td>
<td >2.999560826</td>
<td >0.00175</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >country_agg_uncached</td>
<td >137.708772</td>
<td >138.3623141</td>
<td >0.65354</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >country_agg_uncached</td>
<td >162.6020876</td>
<td >162.0003162</td>
<td >-0.60177</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >country_agg_uncached</td>
<td >196.1384525</td>
<td >190.0452044</td>
<td >-6.09325</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >country_agg_uncached</td>
<td >208.7042201</td>
<td >205.8009086</td>
<td >-2.90331</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >country_agg_uncached</td>
<td >136.977708</td>
<td >137.0970309</td>
<td >0.11932</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  service time</td>
<td >country_agg_uncached</td>
<td >161.4701347</td>
<td >160.9131827</td>
<td >-0.55695</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >country_agg_uncached</td>
<td >195.4892302</td>
<td >188.7832217</td>
<td >-6.70601</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >country_agg_uncached</td>
<td >208.3484558</td>
<td >204.5730753</td>
<td >-3.77538</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >country_agg_uncached</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >带缓存的聚合查询（aggregation）</td>
<td >Min  Throughput</td>
<td >country_agg_cached</td>
<td >98.51641526</td>
<td >98.62990947</td>
<td >0.11349</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >country_agg_cached</td>
<td >98.94635299</td>
<td >99.03419609</td>
<td >0.08784</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median Throughput</td>
<td >country_agg_cached</td>
<td >98.99545733</td>
<td >99.08216113</td>
<td >0.0867</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >country_agg_cached</td>
<td >99.24729184</td>
<td >99.31333794</td>
<td >0.06605</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >country_agg_cached</td>
<td >2.211962827</td>
<td >2.139798366</td>
<td >-0.07216</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  latency</td>
<td >country_agg_cached</td>
<td >3.517023474</td>
<td >3.494661488</td>
<td >-0.02236</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >country_agg_cached</td>
<td >4.158023223</td>
<td >4.199306211</td>
<td >0.04128</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile latency</td>
<td >country_agg_cached</td>
<td >9.866942695</td>
<td >8.245296748</td>
<td >-1.62165</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th percentile  latency</td>
<td >country_agg_cached</td>
<td >18.06280296</td>
<td >12.30363548</td>
<td >-5.75917</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >country_agg_cached</td>
<td >1.467651688</td>
<td >1.393478829</td>
<td >-0.07417</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >country_agg_cached</td>
<td >1.777389366</td>
<td >1.689927001</td>
<td >-0.08746</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >country_agg_cached</td>
<td >2.282693414</td>
<td >3.276122157</td>
<td >0.99343</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99.9th  percentile service time</td>
<td >country_agg_cached</td>
<td >4.195660669</td>
<td >7.769071626</td>
<td >3.57341</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >country_agg_cached</td>
<td >16.24826528</td>
<td >11.39958762</td>
<td >-4.84868</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >country_agg_cached</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >分页拉取</td>
<td >Min  Throughput</td>
<td >scroll</td>
<td >20.04421286</td>
<td >20.04208025</td>
<td >-0.00213</td>
<td >pages/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >scroll</td>
<td >20.05368445</td>
<td >20.05111381</td>
<td >-0.00257</td>
<td >pages/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >scroll</td>
<td >20.05292541</td>
<td >20.05042813</td>
<td >-0.0025</td>
<td >pages/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >scroll</td>
<td >20.0660563</td>
<td >20.06287951</td>
<td >-0.00318</td>
<td >pages/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >scroll</td>
<td >272.1138773</td>
<td >259.2352917</td>
<td >-12.87859</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >scroll</td>
<td >290.9470227</td>
<td >265.0907522</td>
<td >-25.85627</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  latency</td>
<td >scroll</td>
<td >302.488716</td>
<td >284.5098141</td>
<td >-17.9789</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >scroll</td>
<td >303.7193846</td>
<td >297.6893578</td>
<td >-6.03003</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >scroll</td>
<td >270.1747189</td>
<td >257.1577448</td>
<td >-13.01697</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  service time</td>
<td >scroll</td>
<td >289.0668329</td>
<td >263.437889</td>
<td >-25.62894</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >scroll</td>
<td >300.3281443</td>
<td >282.0971792</td>
<td >-18.23097</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >scroll</td>
<td >301.2135932</td>
<td >296.1045038</td>
<td >-5.10909</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >scroll</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >脚本查询（使用  expression 脚本）</td>
<td >Min  Throughput</td>
<td >expression</td>
<td >1.500956979</td>
<td >1.501441158</td>
<td >0.00048</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >expression</td>
<td >1.501160838</td>
<td >1.501741788</td>
<td >0.00058</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >expression</td>
<td >1.501147998</td>
<td >1.501719862</td>
<td >0.00057</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >expression</td>
<td >1.501414072</td>
<td >1.502131242</td>
<td >0.00072</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >expression</td>
<td >327.3259858</td>
<td >295.2159694</td>
<td >-32.11002</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >expression</td>
<td >342.0345129</td>
<td >317.3502734</td>
<td >-24.68424</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >expression</td>
<td >372.6446468</td>
<td >378.85094</td>
<td >6.20629</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >expression</td>
<td >396.7165332</td>
<td >417.1186928</td>
<td >20.40216</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >expression</td>
<td >325.855901</td>
<td >293.9883978</td>
<td >-31.8675</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >expression</td>
<td >340.6900207</td>
<td >316.3654443</td>
<td >-24.32458</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >expression</td>
<td >370.736203</td>
<td >377.514769</td>
<td >6.77857</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >expression</td>
<td >395.4625437</td>
<td >415.9661252</td>
<td >20.50358</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >expression</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >脚本查询（使用  painless 静态脚本，不动态取字段值）</td>
<td >Min  Throughput</td>
<td >painless_static</td>
<td >1.396916338</td>
<td >1.397483837</td>
<td >0.00057</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >painless_static</td>
<td >1.397478748</td>
<td >1.397943395</td>
<td >0.00046</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >painless_static</td>
<td >1.397513941</td>
<td >1.397977624</td>
<td >0.00046</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >painless_static</td>
<td >1.397920498</td>
<td >1.398303982</td>
<td >0.00038</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >painless_static</td>
<td >431.2919118</td>
<td >371.348965</td>
<td >-59.94295</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >painless_static</td>
<td >465.1254796</td>
<td >391.1945282</td>
<td >-73.93095</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  latency</td>
<td >painless_static</td>
<td >512.2339443</td>
<td >437.3164341</td>
<td >-74.91751</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >painless_static</td>
<td >538.9131764</td>
<td >465.5702729</td>
<td >-73.3429</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >painless_static</td>
<td >429.9421017</td>
<td >369.791389</td>
<td >-60.15071</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  service time</td>
<td >painless_static</td>
<td >463.2926716</td>
<td >390.19037</td>
<td >-73.1023</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >painless_static</td>
<td >511.3802825</td>
<td >434.9970652</td>
<td >-76.38322</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >painless_static</td>
<td >537.7559569</td>
<td >464.3589323</td>
<td >-73.39702</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >painless_static</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >脚本查询（使用  painless 静态脚本，动态获取字段值）</td>
<td >Min  Throughput</td>
<td >painless_dynamic</td>
<td >1.398724661</td>
<td >1.396323104</td>
<td >-0.0024</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >painless_dynamic</td>
<td >1.398964022</td>
<td >1.396996725</td>
<td >-0.00197</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >painless_dynamic</td>
<td >1.398981831</td>
<td >1.397038282</td>
<td >-0.00194</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >painless_dynamic</td>
<td >1.399149307</td>
<td >1.397521303</td>
<td >-0.00163</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >painless_dynamic</td>
<td >432.8310895</td>
<td >356.7619352</td>
<td >-76.06915</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >painless_dynamic</td>
<td >462.9847418</td>
<td >383.0218635</td>
<td >-79.96288</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >painless_dynamic</td>
<td >494.9476089</td>
<td >428.2430825</td>
<td >-66.70453</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >painless_dynamic</td>
<td >536.4017347</td>
<td >446.9218394</td>
<td >-89.4799</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th percentile  service time</td>
<td >painless_dynamic</td>
<td >431.5832192</td>
<td >355.6409795</td>
<td >-75.94224</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >painless_dynamic</td>
<td >462.0900041</td>
<td >381.7875394</td>
<td >-80.30246</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >painless_dynamic</td>
<td >494.3205597</td>
<td >425.9035249</td>
<td >-68.41703</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >painless_dynamic</td>
<td >534.6057713</td>
<td >445.0034723</td>
<td >-89.6023</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >painless_dynamic</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >地理范围查询（基于高斯衰减函数）</td>
<td >Min  Throughput</td>
<td >decay_geo_gauss_function_score</td>
<td >1.001927565</td>
<td >1.002114687</td>
<td >0.00019</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >decay_geo_gauss_function_score</td>
<td >1.002340802</td>
<td >1.002568849</td>
<td >0.00023</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >decay_geo_gauss_function_score</td>
<td >1.002308555</td>
<td >1.002535216</td>
<td >0.00023</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >decay_geo_gauss_function_score</td>
<td >1.002881625</td>
<td >1.003158744</td>
<td >0.00028</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >decay_geo_gauss_function_score</td>
<td >387.5082242</td>
<td >332.3548282</td>
<td >-55.1534</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >decay_geo_gauss_function_score</td>
<td >397.8741518</td>
<td >344.7444949</td>
<td >-53.12966</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >decay_geo_gauss_function_score</td>
<td >407.4444408</td>
<td >356.9588375</td>
<td >-50.4856</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >decay_geo_gauss_function_score</td>
<td >409.4531341</td>
<td >369.3594299</td>
<td >-40.0937</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >decay_geo_gauss_function_score</td>
<td >386.1244814</td>
<td >331.0354254</td>
<td >-55.08906</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >decay_geo_gauss_function_score</td>
<td >396.8515609</td>
<td >343.3262392</td>
<td >-53.52532</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >decay_geo_gauss_function_score</td>
<td >406.6675034</td>
<td >355.0055938</td>
<td >-51.66191</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >decay_geo_gauss_function_score</td>
<td >407.7369291</td>
<td >368.1781357</td>
<td >-39.55879</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >decay_geo_gauss_function_score</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >地理范围查询（基于高斯衰减函数，且脚本动态获取字段值）</td>
<td >Min  Throughput</td>
<td >decay_geo_gauss_script_score</td>
<td >1.001446744</td>
<td >1.001552191</td>
<td >0.00011</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean Throughput</td>
<td >decay_geo_gauss_script_score</td>
<td >1.001755635</td>
<td >1.001885174</td>
<td >0.00013</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >decay_geo_gauss_script_score</td>
<td >1.001731537</td>
<td >1.001860497</td>
<td >0.00013</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >decay_geo_gauss_script_score</td>
<td >1.002160032</td>
<td >1.002318693</td>
<td >0.00016</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >decay_geo_gauss_script_score</td>
<td >411.4939715</td>
<td >334.8041</td>
<td >-76.68987</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >decay_geo_gauss_script_score</td>
<td >429.658707</td>
<td >345.120705</td>
<td >-84.538</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >decay_geo_gauss_script_score</td>
<td >453.6645598</td>
<td >355.949311</td>
<td >-97.71525</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >decay_geo_gauss_script_score</td>
<td >454.430094</td>
<td >358.0469266</td>
<td >-96.38317</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >decay_geo_gauss_script_score</td>
<td >409.7672189</td>
<td >333.3149343</td>
<td >-76.45228</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >decay_geo_gauss_script_score</td>
<td >428.3069702</td>
<td >343.9684012</td>
<td >-84.33857</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >decay_geo_gauss_script_score</td>
<td >451.8706388</td>
<td >354.2061434</td>
<td >-97.6645</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >decay_geo_gauss_script_score</td>
<td >452.8327445</td>
<td >356.5891208</td>
<td >-96.24362</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >decay_geo_gauss_script_score</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >自定义评分函数查询（基于字段值定义函数）</td>
<td >Min  Throughput</td>
<td >field_value_function_score</td>
<td >1.503388048</td>
<td >1.503875481</td>
<td >0.00049</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >field_value_function_score</td>
<td >1.504118746</td>
<td >1.504719285</td>
<td >0.0006</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median Throughput</td>
<td >field_value_function_score</td>
<td >1.504074621</td>
<td >1.504659173</td>
<td >0.00058</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >field_value_function_score</td>
<td >1.505051463</td>
<td >1.505800982</td>
<td >0.00075</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >field_value_function_score</td>
<td >194.2629726</td>
<td >134.5724794</td>
<td >-59.69049</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >field_value_function_score</td>
<td >203.7090491</td>
<td >150.1895525</td>
<td >-53.5195</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >field_value_function_score</td>
<td >214.6481861</td>
<td >166.6002053</td>
<td >-48.04798</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >field_value_function_score</td>
<td >217.926288</td>
<td >184.5367327</td>
<td >-33.38956</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >field_value_function_score</td>
<td >192.3880568</td>
<td >133.1520383</td>
<td >-59.23602</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >field_value_function_score</td>
<td >202.3297952</td>
<td >148.4251454</td>
<td >-53.90465</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >field_value_function_score</td>
<td >213.3810514</td>
<td >165.5014484</td>
<td >-47.8796</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >field_value_function_score</td>
<td >215.2935127</td>
<td >183.1076834</td>
<td >-32.18583</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >field_value_function_score</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >自定义评分函数查询（通过脚本动态获取字段值计算评分）</td>
<td >Min  Throughput</td>
<td >field_value_script_score</td>
<td >1.499697369</td>
<td >1.500258349</td>
<td >0.00056</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >field_value_script_score</td>
<td >1.499757694</td>
<td >1.500311799</td>
<td >0.00055</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >field_value_script_score</td>
<td >1.499759282</td>
<td >1.50030649</td>
<td >0.00055</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >field_value_script_score</td>
<td >1.499799232</td>
<td >1.500380821</td>
<td >0.00058</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >field_value_script_score</td>
<td >240.0929602</td>
<td >174.8193153</td>
<td >-65.27364</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >field_value_script_score</td>
<td >250.0571281</td>
<td >188.9238266</td>
<td >-61.1333</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >field_value_script_score</td>
<td >270.1539508</td>
<td >215.9618342</td>
<td >-54.19212</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >field_value_script_score</td>
<td >291.1372129</td>
<td >229.1083755</td>
<td >-62.02884</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th percentile  service time</td>
<td >field_value_script_score</td>
<td >238.8174967</td>
<td >173.5835276</td>
<td >-65.23397</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >field_value_script_score</td>
<td >248.7244156</td>
<td >187.4786591</td>
<td >-61.24576</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >field_value_script_score</td>
<td >268.9089779</td>
<td >214.8508051</td>
<td >-54.05817</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >field_value_script_score</td>
<td >290.2693953</td>
<td >228.2811021</td>
<td >-61.98829</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >field_value_script_score</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >大量  terms 条件查询（query）</td>
<td >Min  Throughput</td>
<td >large_terms</td>
<td >1.101304601</td>
<td >1.100700963</td>
<td >-0.0006</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >large_terms</td>
<td >1.101582867</td>
<td >1.100849475</td>
<td >-0.00073</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >large_terms</td>
<td >1.101561184</td>
<td >1.100839723</td>
<td >-0.00072</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >large_terms</td>
<td >1.101945785</td>
<td >1.101043</td>
<td >-0.0009</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >large_terms</td>
<td >211.8277326</td>
<td >242.00767</td>
<td >30.17994</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >large_terms</td>
<td >231.8088979</td>
<td >252.8580495</td>
<td >21.04915</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >large_terms</td>
<td >251.2304624</td>
<td >265.9718477</td>
<td >14.74139</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th percentile  latency</td>
<td >large_terms</td>
<td >255.3527635</td>
<td >269.8639119</td>
<td >14.51115</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >large_terms</td>
<td >203.8265727</td>
<td >233.9178906</td>
<td >30.09132</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >large_terms</td>
<td >223.8224964</td>
<td >245.1530447</td>
<td >21.33055</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  service time</td>
<td >large_terms</td>
<td >241.849935</td>
<td >258.2161737</td>
<td >16.36624</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >large_terms</td>
<td >246.3486325</td>
<td >262.1599194</td>
<td >15.81129</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error rate</td>
<td >large_terms</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >大量  terms 条件过滤查询（query、filter）</td>
<td >Min  Throughput</td>
<td >large_filtered_terms</td>
<td >1.102296697</td>
<td >1.10245872</td>
<td >0.00016</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >large_filtered_terms</td>
<td >1.102784885</td>
<td >1.102979701</td>
<td >0.00019</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >large_filtered_terms</td>
<td >1.102747397</td>
<td >1.102939052</td>
<td >0.00019</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >large_filtered_terms</td>
<td >1.103436209</td>
<td >1.103668743</td>
<td >0.00023</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >large_filtered_terms</td>
<td >227.9210831</td>
<td >243.4361419</td>
<td >15.51506</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >large_filtered_terms</td>
<td >249.2253724</td>
<td >255.9631401</td>
<td >6.73777</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  latency</td>
<td >large_filtered_terms</td>
<td >263.3142567</td>
<td >276.256653</td>
<td >12.9424</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >large_filtered_terms</td>
<td >265.4732559</td>
<td >280.1711811</td>
<td >14.69793</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >large_filtered_terms</td>
<td >220.1946224</td>
<td >235.739741</td>
<td >15.54512</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >large_filtered_terms</td>
<td >241.1826614</td>
<td >248.5632175</td>
<td >7.38056</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >large_filtered_terms</td>
<td >255.2141531</td>
<td >268.2613158</td>
<td >13.04716</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >large_filtered_terms</td>
<td >256.941474</td>
<td >272.5524893</td>
<td >15.61102</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >large_filtered_terms</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >大量条件取反查询（query、must not）</td>
<td >Min  Throughput</td>
<td >large_prohibited_terms</td>
<td >1.102827031</td>
<td >1.102357904</td>
<td >-0.00047</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >large_prohibited_terms</td>
<td >1.103422713</td>
<td >1.102860804</td>
<td >-0.00056</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >large_prohibited_terms</td>
<td >1.103376606</td>
<td >1.102821884</td>
<td >-0.00055</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >large_prohibited_terms</td>
<td >1.104211668</td>
<td >1.103525116</td>
<td >-0.00069</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >large_prohibited_terms</td>
<td >202.5767318</td>
<td >232.1078526</td>
<td >29.53112</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >large_prohibited_terms</td>
<td >220.4174595</td>
<td >247.2566163</td>
<td >26.83916</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >large_prohibited_terms</td>
<td >234.3344817</td>
<td >266.7954953</td>
<td >32.46101</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >large_prohibited_terms</td>
<td >246.6131421</td>
<td >268.8084021</td>
<td >22.19526</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >large_prohibited_terms</td>
<td >193.9010601</td>
<td >224.5439067</td>
<td >30.64285</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >large_prohibited_terms</td>
<td >212.6108234</td>
<td >239.8692667</td>
<td >27.25844</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  service time</td>
<td >large_prohibited_terms</td>
<td >226.4359237</td>
<td >258.9916089</td>
<td >32.55569</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >large_prohibited_terms</td>
<td >238.984541</td>
<td >260.8724702</td>
<td >21.88793</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >large_prohibited_terms</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >降序排序查询</td>
<td >Min  Throughput</td>
<td >desc_sort_population</td>
<td >1.504037884</td>
<td >1.504180086</td>
<td >0.00014</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >desc_sort_population</td>
<td >1.504907329</td>
<td >1.505087394</td>
<td >0.00018</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >desc_sort_population</td>
<td >1.504841628</td>
<td >1.505025118</td>
<td >0.00018</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >desc_sort_population</td>
<td >1.506034196</td>
<td >1.506249517</td>
<td >0.00022</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >desc_sort_population</td>
<td >61.13778474</td>
<td >54.50106226</td>
<td >-6.63672</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >desc_sort_population</td>
<td >73.92849587</td>
<td >69.35394919</td>
<td >-4.57455</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th percentile  latency</td>
<td >desc_sort_population</td>
<td >85.77715084</td>
<td >86.2006122</td>
<td >0.42346</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >desc_sort_population</td>
<td >85.84200498</td>
<td >87.74290979</td>
<td >1.9009</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >desc_sort_population</td>
<td >59.92501229</td>
<td >53.58439684</td>
<td >-6.34062</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >desc_sort_population</td>
<td >72.30911367</td>
<td >68.09855495</td>
<td >-4.21056</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >desc_sort_population</td>
<td >84.09957183</td>
<td >84.57749833</td>
<td >0.47793</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >desc_sort_population</td>
<td >84.19063408</td>
<td >85.95814556</td>
<td >1.76751</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >desc_sort_population</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >升序排序查询</td>
<td >Min  Throughput</td>
<td >asc_sort_population</td>
<td >1.504247142</td>
<td >1.504528234</td>
<td >0.00028</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >asc_sort_population</td>
<td >1.505166062</td>
<td >1.505508302</td>
<td >0.00034</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >asc_sort_population</td>
<td >1.505099341</td>
<td >1.505440428</td>
<td >0.00034</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >asc_sort_population</td>
<td >1.506349989</td>
<td >1.506767598</td>
<td >0.00042</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >asc_sort_population</td>
<td >63.16776341</td>
<td >62.82690261</td>
<td >-0.34086</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th percentile  latency</td>
<td >asc_sort_population</td>
<td >78.09764324</td>
<td >75.61749704</td>
<td >-2.48015</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >asc_sort_population</td>
<td >87.33172638</td>
<td >84.58683862</td>
<td >-2.74489</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >asc_sort_population</td>
<td >87.89979294</td>
<td >85.19899659</td>
<td >-2.7008</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th percentile  service time</td>
<td >asc_sort_population</td>
<td >61.90986466</td>
<td >61.71039958</td>
<td >-0.19947</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >asc_sort_population</td>
<td >76.55056985</td>
<td >74.45018981</td>
<td >-2.10038</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >asc_sort_population</td>
<td >85.81453795</td>
<td >83.30245529</td>
<td >-2.51208</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >asc_sort_population</td>
<td >86.60695888</td>
<td >84.05557927</td>
<td >-2.55138</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >asc_sort_population</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >升序排序后 after 跳转查询</td>
<td >Min  Throughput</td>
<td >asc_sort_with_after_population</td>
<td >1.503017792</td>
<td >1.503506494</td>
<td >0.00049</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >asc_sort_with_after_population</td>
<td >1.503667166</td>
<td >1.504271472</td>
<td >0.0006</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >asc_sort_with_after_population</td>
<td >1.503620246</td>
<td >1.504214876</td>
<td >0.00059</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >asc_sort_with_after_population</td>
<td >1.504506304</td>
<td >1.505248472</td>
<td >0.00074</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >asc_sort_with_after_population</td>
<td >79.49512405</td>
<td >81.97531058</td>
<td >2.48019</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >asc_sort_with_after_population</td>
<td >94.07415418</td>
<td >97.05960844</td>
<td >2.98545</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >asc_sort_with_after_population</td>
<td >115.1407234</td>
<td >110.1778366</td>
<td >-4.96289</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >asc_sort_with_after_population</td>
<td >117.4867153</td>
<td >115.6357806</td>
<td >-1.85093</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >asc_sort_with_after_population</td>
<td >78.12653808</td>
<td >80.56232799</td>
<td >2.43579</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >asc_sort_with_after_population</td>
<td >92.57791536</td>
<td >96.00112103</td>
<td >3.42321</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >asc_sort_with_after_population</td>
<td >113.538067</td>
<td >108.2517642</td>
<td >-5.2863</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th percentile  service time</td>
<td >asc_sort_with_after_population</td>
<td >116.0558164</td>
<td >114.5531256</td>
<td >-1.50269</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >asc_sort_with_after_population</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >高基字段降序排序查询（基于 DistanceFeatureQuery 快速取 topK）</td>
<td >Min  Throughput</td>
<td >desc_sort_geonameid</td>
<td >6.011806976</td>
<td >6.013534032</td>
<td >0.00173</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >desc_sort_geonameid</td>
<td >6.014040004</td>
<td >6.016121536</td>
<td >0.00208</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >desc_sort_geonameid</td>
<td >6.013860893</td>
<td >6.015844404</td>
<td >0.00198</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >desc_sort_geonameid</td>
<td >6.016975785</td>
<td >6.019491653</td>
<td >0.00252</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th percentile  latency</td>
<td >desc_sort_geonameid</td>
<td >8.037513588</td>
<td >6.896098144</td>
<td >-1.14142</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >desc_sort_geonameid</td>
<td >8.790209144</td>
<td >7.481213845</td>
<td >-1.309</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >desc_sort_geonameid</td>
<td >20.16597</td>
<td >7.890859395</td>
<td >-12.27511</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th percentile  latency</td>
<td >desc_sort_geonameid</td>
<td >22.69194461</td>
<td >8.130467497</td>
<td >-14.56148</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >desc_sort_geonameid</td>
<td >7.199986372</td>
<td >6.043605972</td>
<td >-1.15638</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >desc_sort_geonameid</td>
<td >7.634483464</td>
<td >6.330675445</td>
<td >-1.30381</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >desc_sort_geonameid</td>
<td >18.95111335</td>
<td >6.674837489</td>
<td >-12.27628</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >desc_sort_geonameid</td>
<td >22.06934988</td>
<td >6.795545109</td>
<td >-15.2738</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >desc_sort_geonameid</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >高基字段降序排序  after 跳转查询</td>
<td >Min  Throughput</td>
<td >desc_sort_with_after_geonameid</td>
<td >6.003999251</td>
<td >6.002224615</td>
<td >-0.00177</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >desc_sort_with_after_geonameid</td>
<td >6.00483332</td>
<td >6.002715504</td>
<td >-0.00212</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >desc_sort_with_after_geonameid</td>
<td >6.004831591</td>
<td >6.002684836</td>
<td >-0.00215</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >desc_sort_with_after_geonameid</td>
<td >6.005864935</td>
<td >6.003257919</td>
<td >-0.00261</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >desc_sort_with_after_geonameid</td>
<td >64.12782287</td>
<td >69.3480419</td>
<td >5.22022</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >desc_sort_with_after_geonameid</td>
<td >79.63361973</td>
<td >85.98741582</td>
<td >6.3538</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >desc_sort_with_after_geonameid</td>
<td >87.09606319</td>
<td >91.30932659</td>
<td >4.21326</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >desc_sort_with_after_geonameid</td>
<td >88.47462852</td>
<td >91.78488795</td>
<td >3.31026</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >desc_sort_with_after_geonameid</td>
<td >63.23770666</td>
<td >68.51645093</td>
<td >5.27874</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >desc_sort_with_after_geonameid</td>
<td >78.83979175</td>
<td >85.22403594</td>
<td >6.38424</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >desc_sort_with_after_geonameid</td>
<td >86.525729</td>
<td >90.76162191</td>
<td >4.23589</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >desc_sort_with_after_geonameid</td>
<td >87.29847241</td>
<td >91.3709281</td>
<td >4.07246</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >desc_sort_with_after_geonameid</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >高基字段升序排序查询（基于 DistanceFeatureQuery 快速取 topK）</td>
<td >Min  Throughput</td>
<td >asc_sort_geonameid</td>
<td >6.018840993</td>
<td >6.018470998</td>
<td >-0.00037</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >asc_sort_geonameid</td>
<td >6.022518134</td>
<td >6.022078364</td>
<td >-0.00044</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >asc_sort_geonameid</td>
<td >6.022245684</td>
<td >6.021816641</td>
<td >-0.00043</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >asc_sort_geonameid</td>
<td >6.027178807</td>
<td >6.026594943</td>
<td >-0.00058</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >asc_sort_geonameid</td>
<td >7.024060003</td>
<td >9.012220893</td>
<td >1.98816</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >asc_sort_geonameid</td>
<td >7.69297732</td>
<td >9.680523816</td>
<td >1.98755</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >asc_sort_geonameid</td>
<td >20.44826921</td>
<td >11.18117133</td>
<td >-9.2671</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >asc_sort_geonameid</td>
<td >21.87036537</td>
<td >11.28741447</td>
<td >-10.58295</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >asc_sort_geonameid</td>
<td >6.123304367</td>
<td >8.064015303</td>
<td >1.94071</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >asc_sort_geonameid</td>
<td >6.746383384</td>
<td >8.737695683</td>
<td >1.99131</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >asc_sort_geonameid</td>
<td >19.78318544</td>
<td >10.16213525</td>
<td >-9.62105</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >asc_sort_geonameid</td>
<td >21.25467733</td>
<td >10.39039157</td>
<td >-10.86429</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >asc_sort_geonameid</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >高基字段升序排序  after 跳转查询</td>
<td >Min  Throughput</td>
<td >asc_sort_with_after_geonameid</td>
<td >6.013236842</td>
<td >6.013266563</td>
<td >0.00003</td>
<td >ops/s</td>
<td >&nbsp;</td>
</tr><tr>
<td >Mean  Throughput</td>
<td >asc_sort_with_after_geonameid</td>
<td >6.015849171</td>
<td >6.015858176</td>
<td >0.00001</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Median  Throughput</td>
<td >asc_sort_with_after_geonameid</td>
<td >6.015618744</td>
<td >6.015641333</td>
<td >0.00002</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >Max  Throughput</td>
<td >asc_sort_with_after_geonameid</td>
<td >6.019167352</td>
<td >6.01911523</td>
<td >-0.00005</td>
<td >ops/s</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile latency</td>
<td >asc_sort_with_after_geonameid</td>
<td >60.27546292</td>
<td >64.3463349</td>
<td >4.07087</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile latency</td>
<td >asc_sort_with_after_geonameid</td>
<td >78.63363056</td>
<td >85.38805693</td>
<td >6.75443</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile latency</td>
<td >asc_sort_with_after_geonameid</td>
<td >89.31191583</td>
<td >91.7664034</td>
<td >2.45449</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile latency</td>
<td >asc_sort_with_after_geonameid</td>
<td >90.85853212</td>
<td >91.9917766</td>
<td >1.13324</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >50th  percentile service time</td>
<td >asc_sort_with_after_geonameid</td>
<td >59.692265</td>
<td >63.68059153</td>
<td >3.98833</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >90th  percentile service time</td>
<td >asc_sort_with_after_geonameid</td>
<td >78.16235274</td>
<td >84.53184282</td>
<td >6.36949</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >99th  percentile service time</td>
<td >asc_sort_with_after_geonameid</td>
<td >88.15484255</td>
<td >91.29356634</td>
<td >3.13872</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >100th  percentile service time</td>
<td >asc_sort_with_after_geonameid</td>
<td >89.73695803</td>
<td >91.64701309</td>
<td >1.91006</td>
<td >ms</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr><tr>
<td >error  rate</td>
<td >asc_sort_with_after_geonameid</td>
<td >0</td>
<td >0</td>
<td >0</td>
<td >%</td>
<td >&nbsp;</td>
<td >&nbsp;</td>
</tr></tbody></table>
