本文提供4核16G 3个节点与8核32G 3个节点规格的腾讯云 Elasticsearch Service 集群的压测比较结果。

>?数据为官方提供的 [geonames](http://www.geonames.org/)，包含11396503条地理位置信息，总大小接近3GB，包含了 text、long、geo 等类型数据，覆盖行列存。

<table>
<thead>
<tr>
<th>说明</th>
<th>Unit</th>
<th>Metric</th>
<th>Task</th>
<th>4核16GB</th>
<th>8核32GB</th>
<th>差异值</th>
<th>差异百分比</th>
</tr>
</thead>
<tbody><tr>
<td>写入总耗时</td>
<td>min</td>
<td>Cumulative  indexing time of primary shards</td>
<td>-</td>
<td>16.3633</td>
<td>14.2567</td>
<td>2.1066</td>
<td>14.78%</td>
</tr>
<tr>
<td rowspan="4">GC 总次数、耗时统计</td>
<td>s</td>
<td>Total Young Gen GC time</td>
<td>-</td>
<td>6.26</td>
<td>3.544</td>
<td>2.716</td>
<td>76.64%</td>
</tr>
<tr>
<td></td>
<td>Total Young Gen GC count</td>
<td>-</td>
<td>892</td>
<td>447</td>
<td>445</td>
<td>99.55%</td>
</tr>
<tr>
<td>s</td>
<td>Total Old Gen GC time</td>
<td>-</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td></td>
<td>Total Old Gen GC count</td>
<td>-</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="2">存储大小</td>
<td>GB</td>
<td>Store size</td>
<td>-</td>
<td>2.51866</td>
<td>2.59725</td>
<td>-0.079</td>
<td>-3.03%</td>
</tr>
<tr>
<td>GB</td>
<td>Translog size</td>
<td>-</td>
<td>3.59E-07</td>
<td>3.59E-07</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td rowspan="6">堆内存使用量</td>
<td>MB</td>
<td>Heap used for segments</td>
<td>-</td>
<td>0.803783</td>
<td>0.534325</td>
<td>0.2695</td>
<td>50.43%</td>
</tr>
<tr>
<td>MB</td>
<td>Heap used for doc values</td>
<td>-</td>
<td>0.0284767</td>
<td>0.0507355</td>
<td>-0.022</td>
<td>-43.87%</td>
</tr>
<tr>
<td>MB</td>
<td>Heap used for terms</td>
<td>-</td>
<td>0.655075</td>
<td>0.370026</td>
<td>0.285</td>
<td>77.03%</td>
</tr>
<tr>
<td>MB</td>
<td>Heap used for norms</td>
<td>-</td>
<td>0.0732422</td>
<td>0.0396729</td>
<td>0.0336</td>
<td>84.62%</td>
</tr>
<tr>
<td>MB</td>
<td>Heap used for points</td>
<td>-</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td>MB</td>
<td>Heap used for stored fields</td>
<td>-</td>
<td>0.0469894</td>
<td>0.0119553</td>
<td>0.035</td>
<td>293.04%</td>
</tr>
<tr>
<td>segment 总数量</td>
<td>-</td>
<td>Segment count</td>
<td>-</td>
<td>6</td>
<td>7</td>
<td>-1</td>
<td>-14.29%</td>
</tr>
<tr>
<td rowspan="12">写入吞吐、耗时统计</td>
<td>docs/s</td>
<td>Min Throughput</td>
<td>index-append</td>
<td>89331.9</td>
<td>153730</td>
<td>-64398</td>
<td>-41.89%</td>
</tr>
<tr>
<td>docs/s</td>
<td>Median Throughput</td>
<td>index-append</td>
<td>90268.8</td>
<td>159765</td>
<td>-69496</td>
<td>-43.50%</td>
</tr>
<tr>
<td>docs/s</td>
<td>Max Throughput</td>
<td>index-append</td>
<td>90516.1</td>
<td>162791</td>
<td>-72275</td>
<td>-44.40%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>index-append</td>
<td>233.258</td>
<td>130.877</td>
<td>102.38</td>
<td>78.23%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>index-append</td>
<td>314.558</td>
<td>162.969</td>
<td>151.59</td>
<td>93.02%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>index-append</td>
<td>341.303</td>
<td>181.428</td>
<td>159.88</td>
<td>88.12%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>index-append</td>
<td>354.657</td>
<td>225.98</td>
<td>128.68</td>
<td>56.94%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>index-append</td>
<td>233.258</td>
<td>130.877</td>
<td>102.38</td>
<td>78.23%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>index-append</td>
<td>314.558</td>
<td>162.969</td>
<td>151.59</td>
<td>93.02%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>index-append</td>
<td>341.303</td>
<td>181.428</td>
<td>159.88</td>
<td>88.12%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>index-append</td>
<td>354.657</td>
<td>225.98</td>
<td>128.68</td>
<td>56.94%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>index-append</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="14">index 指标统计</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>index-stats</td>
<td>90.04</td>
<td>90.05</td>
<td>-0.01</td>
<td>-0.01%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>index-stats</td>
<td>90.07</td>
<td>90.06</td>
<td>0.01</td>
<td>0.01%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>index-stats</td>
<td>90.14</td>
<td>90.12</td>
<td>0.02</td>
<td>0.02%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>index-stats</td>
<td>2.91003</td>
<td>2.76736</td>
<td>0.1427</td>
<td>5.16%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>index-stats</td>
<td>3.82882</td>
<td>3.58235</td>
<td>0.2465</td>
<td>6.88%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>index-stats</td>
<td>4.2378</td>
<td>3.95798</td>
<td>0.2798</td>
<td>7.07%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile latency</td>
<td>index-stats</td>
<td>4.34459</td>
<td>4.39377</td>
<td>-0.049</td>
<td>-1.12%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>index-stats</td>
<td>8.22393</td>
<td>9.00375</td>
<td>-0.78</td>
<td>-8.66%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>index-stats</td>
<td>1.78268</td>
<td>1.57744</td>
<td>0.2052</td>
<td>13.01%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>index-stats</td>
<td>2.07484</td>
<td>1.8317</td>
<td>0.2431</td>
<td>13.27%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>index-stats</td>
<td>2.43121</td>
<td>2.0752</td>
<td>0.356</td>
<td>17.16%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile service time</td>
<td>index-stats</td>
<td>3.09198</td>
<td>2.24891</td>
<td>0.8431</td>
<td>37.49%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>index-stats</td>
<td>7.29974</td>
<td>2.31078</td>
<td>4.989</td>
<td>215.90%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>index-stats</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="14">node 指标统计</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>node-stats</td>
<td>90.06</td>
<td>90.06</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>node-stats</td>
<td>90.09</td>
<td>90.12</td>
<td>-0.03</td>
<td>-0.03%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>node-stats</td>
<td>90.34</td>
<td>90.36</td>
<td>-0.02</td>
<td>-0.02%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>node-stats</td>
<td>3.17223</td>
<td>2.9754</td>
<td>0.1968</td>
<td>6.62%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>node-stats</td>
<td>3.70681</td>
<td>4.07929</td>
<td>-0.372</td>
<td>-9.13%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>node-stats</td>
<td>5.01334</td>
<td>5.0754</td>
<td>-0.062</td>
<td>-1.22%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile latency</td>
<td>node-stats</td>
<td>6.75018</td>
<td>6.53613</td>
<td>0.2141</td>
<td>3.27%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>node-stats</td>
<td>7.98905</td>
<td>6.93454</td>
<td>1.0545</td>
<td>15.21%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>node-stats</td>
<td>2.43876</td>
<td>2.23841</td>
<td>0.2004</td>
<td>8.95%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>node-stats</td>
<td>2.78272</td>
<td>2.65367</td>
<td>0.1291</td>
<td>4.86%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>node-stats</td>
<td>4.12234</td>
<td>3.92073</td>
<td>0.2016</td>
<td>5.14%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile service time</td>
<td>node-stats</td>
<td>6.35902</td>
<td>4.92842</td>
<td>1.4306</td>
<td>29.03%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>node-stats</td>
<td>7.4313</td>
<td>5.92757</td>
<td>1.5037</td>
<td>25.37%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>node-stats</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="14">默认查询，所有文档 score 为1（match_all）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>default</td>
<td>50.03</td>
<td>50.03</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>default</td>
<td>50.04</td>
<td>50.04</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>default</td>
<td>50.08</td>
<td>50.08</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>default</td>
<td>3.89929</td>
<td>3.53894</td>
<td>0.3604</td>
<td>10.18%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>default</td>
<td>4.39236</td>
<td>4.11403</td>
<td>0.2783</td>
<td>6.77%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>default</td>
<td>4.78834</td>
<td>4.92737</td>
<td>-0.139</td>
<td>-2.82%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile latency</td>
<td>default</td>
<td>7.10486</td>
<td>5.74037</td>
<td>1.3645</td>
<td>23.77%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>default</td>
<td>8.75822</td>
<td>7.32557</td>
<td>1.4327</td>
<td>19.56%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>default</td>
<td>3.18269</td>
<td>2.7831</td>
<td>0.3996</td>
<td>14.36%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>default</td>
<td>3.49347</td>
<td>3.17322</td>
<td>0.3203</td>
<td>10.09%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>default</td>
<td>3.8746</td>
<td>3.77477</td>
<td>0.0998</td>
<td>2.64%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile service time</td>
<td>default</td>
<td>6.68581</td>
<td>4.19186</td>
<td>2.494</td>
<td>59.50%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>default</td>
<td>8.30396</td>
<td>6.58243</td>
<td>1.7215</td>
<td>26.15%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>default</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="14">term 条件查询（query）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>term</td>
<td>100.05</td>
<td>99.66</td>
<td>0.39</td>
<td>0.39%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>term</td>
<td>100.07</td>
<td>100.07</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>term</td>
<td>100.14</td>
<td>100.11</td>
<td>0.03</td>
<td>0.03%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>term</td>
<td>3.17419</td>
<td>2.83987</td>
<td>0.3343</td>
<td>11.77%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>term</td>
<td>3.62229</td>
<td>3.32569</td>
<td>0.2966</td>
<td>8.92%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>term</td>
<td>4.03812</td>
<td>3.96055</td>
<td>0.0776</td>
<td>1.96%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile latency</td>
<td>term</td>
<td>5.9753</td>
<td>4.33961</td>
<td>1.6357</td>
<td>37.69%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>term</td>
<td>8.03321</td>
<td>5.70421</td>
<td>2.329</td>
<td>40.83%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>term</td>
<td>2.49755</td>
<td>2.08935</td>
<td>0.4082</td>
<td>19.54%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>term</td>
<td>2.71322</td>
<td>2.53284</td>
<td>0.1804</td>
<td>7.12%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>term</td>
<td>3.20673</td>
<td>2.99484</td>
<td>0.2119</td>
<td>7.08%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile service time</td>
<td>term</td>
<td>5.17998</td>
<td>3.37709</td>
<td>1.8029</td>
<td>53.39%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>term</td>
<td>6.95227</td>
<td>5.24029</td>
<td>1.712</td>
<td>32.67%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>term</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="14">词组查询（query）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>phrase</td>
<td>110.05</td>
<td>110.04</td>
<td>0.01</td>
<td>0.01%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>phrase</td>
<td>110.07</td>
<td>110.08</td>
<td>-0.01</td>
<td>-0.01%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>phrase</td>
<td>110.12</td>
<td>110.11</td>
<td>0.01</td>
<td>0.01%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>phrase</td>
<td>3.09905</td>
<td>2.74088</td>
<td>0.3582</td>
<td>13.07%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>phrase</td>
<td>3.62549</td>
<td>3.30207</td>
<td>0.3234</td>
<td>9.79%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>phrase</td>
<td>4.55457</td>
<td>4.8127</td>
<td>-0.258</td>
<td>-5.36%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile latency</td>
<td>phrase</td>
<td>8.29519</td>
<td>5.57204</td>
<td>2.7232</td>
<td>48.87%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>phrase</td>
<td>9.39771</td>
<td>6.54587</td>
<td>2.8518</td>
<td>43.57%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>phrase</td>
<td>2.38248</td>
<td>1.98839</td>
<td>0.3941</td>
<td>19.82%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>phrase</td>
<td>2.77084</td>
<td>2.41365</td>
<td>0.3572</td>
<td>14.80%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>phrase</td>
<td>3.75448</td>
<td>4.00121</td>
<td>-0.247</td>
<td>-6.17%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile service time</td>
<td>phrase</td>
<td>7.5974</td>
<td>4.70793</td>
<td>2.8895</td>
<td>61.37%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>phrase</td>
<td>8.98362</td>
<td>5.67829</td>
<td>3.3053</td>
<td>58.21%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>phrase</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">不带缓存的聚合查询（aggregation）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>country_agg_uncached</td>
<td>3.6</td>
<td>3.6</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>country_agg_uncached</td>
<td>3.61</td>
<td>3.61</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>country_agg_uncached</td>
<td>3.61</td>
<td>3.61</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>country_agg_uncached</td>
<td>157.466</td>
<td>130.314</td>
<td>27.152</td>
<td>20.84%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>country_agg_uncached</td>
<td>217.148</td>
<td>147.567</td>
<td>69.581</td>
<td>47.15%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>country_agg_uncached</td>
<td>233.185</td>
<td>165.174</td>
<td>68.011</td>
<td>41.18%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>country_agg_uncached</td>
<td>233.227</td>
<td>174.015</td>
<td>59.212</td>
<td>34.03%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>country_agg_uncached</td>
<td>156.197</td>
<td>129.186</td>
<td>27.011</td>
<td>20.91%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>country_agg_uncached</td>
<td>215.852</td>
<td>146.921</td>
<td>68.931</td>
<td>46.92%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>country_agg_uncached</td>
<td>232.177</td>
<td>164.579</td>
<td>67.598</td>
<td>41.07%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>country_agg_uncached</td>
<td>232.321</td>
<td>172.827</td>
<td>59.494</td>
<td>34.42%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>country_agg_uncached</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="14">带缓存的聚合查询（aggregation）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>country_agg_cached</td>
<td>100.03</td>
<td>100.04</td>
<td>-0.01</td>
<td>-0.01%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>country_agg_cached</td>
<td>100.05</td>
<td>100.05</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>country_agg_cached</td>
<td>100.08</td>
<td>100.08</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>country_agg_cached</td>
<td>2.44457</td>
<td>2.29531</td>
<td>0.1493</td>
<td>6.50%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>country_agg_cached</td>
<td>2.97922</td>
<td>3.57418</td>
<td>-0.595</td>
<td>-16.65%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>country_agg_cached</td>
<td>3.96393</td>
<td>3.91685</td>
<td>0.0471</td>
<td>1.20%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile latency</td>
<td>country_agg_cached</td>
<td>5.3294</td>
<td>4.19749</td>
<td>1.1319</td>
<td>26.97%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>country_agg_cached</td>
<td>7.9529</td>
<td>4.51842</td>
<td>3.4345</td>
<td>76.01%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>country_agg_cached</td>
<td>1.71924</td>
<td>1.57861</td>
<td>0.1406</td>
<td>8.91%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>country_agg_cached</td>
<td>1.97892</td>
<td>1.89111</td>
<td>0.0878</td>
<td>4.64%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>country_agg_cached</td>
<td>2.22611</td>
<td>2.19488</td>
<td>0.0312</td>
<td>1.42%</td>
</tr>
<tr>
<td>ms</td>
<td>99.9th percentile service time</td>
<td>country_agg_cached</td>
<td>5.0967</td>
<td>3.42563</td>
<td>1.6711</td>
<td>48.78%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>country_agg_cached</td>
<td>7.02246</td>
<td>4.28971</td>
<td>2.7328</td>
<td>63.70%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>country_agg_cached</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">分页拉取</td>
<td>pages/s</td>
<td>Min Throughput</td>
<td>scroll</td>
<td>20.04</td>
<td>20.04</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>pages/s</td>
<td>Median Throughput</td>
<td>scroll</td>
<td>20.04</td>
<td>20.05</td>
<td>-0.01</td>
<td>-0.05%</td>
</tr>
<tr>
<td>pages/s</td>
<td>Max Throughput</td>
<td>scroll</td>
<td>20.05</td>
<td>20.06</td>
<td>-0.01</td>
<td>-0.05%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>scroll</td>
<td>576.675</td>
<td>538.421</td>
<td>38.254</td>
<td>7.10%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>scroll</td>
<td>585.156</td>
<td>543.566</td>
<td>41.59</td>
<td>7.65%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>scroll</td>
<td>598.95</td>
<td>582.263</td>
<td>16.687</td>
<td>2.87%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>scroll</td>
<td>602.009</td>
<td>584.75</td>
<td>17.259</td>
<td>2.95%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>scroll</td>
<td>575.118</td>
<td>537.068</td>
<td>38.05</td>
<td>7.08%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>scroll</td>
<td>583.906</td>
<td>542.428</td>
<td>41.478</td>
<td>7.65%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>scroll</td>
<td>597.482</td>
<td>580.372</td>
<td>17.11</td>
<td>2.95%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>scroll</td>
<td>600.578</td>
<td>583.612</td>
<td>16.966</td>
<td>2.91%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>scroll</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">脚本查询（使用 expression 脚本）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>expression</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>expression</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>expression</td>
<td>2</td>
<td>2</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>expression</td>
<td>299.685</td>
<td>265.631</td>
<td>34.054</td>
<td>12.82%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>expression</td>
<td>416.613</td>
<td>287.121</td>
<td>129.49</td>
<td>45.10%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>expression</td>
<td>465.776</td>
<td>311.788</td>
<td>153.99</td>
<td>49.39%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>expression</td>
<td>468.083</td>
<td>391.745</td>
<td>76.338</td>
<td>19.49%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>expression</td>
<td>298.594</td>
<td>264.462</td>
<td>34.132</td>
<td>12.91%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>expression</td>
<td>415.045</td>
<td>285.113</td>
<td>129.93</td>
<td>45.57%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>expression</td>
<td>464.598</td>
<td>310.991</td>
<td>153.61</td>
<td>49.39%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>expression</td>
<td>467.106</td>
<td>390.33</td>
<td>76.776</td>
<td>19.67%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>expression</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">脚本查询（使用 painless 静态脚本，不动态取字段值）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>painless_static</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>painless_static</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>painless_static</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>painless_static</td>
<td>383.485</td>
<td>337.96</td>
<td>45.525</td>
<td>13.47%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>painless_static</td>
<td>514.495</td>
<td>358.738</td>
<td>155.76</td>
<td>43.42%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>painless_static</td>
<td>561.342</td>
<td>375.017</td>
<td>186.33</td>
<td>49.68%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>painless_static</td>
<td>568.066</td>
<td>395.417</td>
<td>172.65</td>
<td>43.66%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>painless_static</td>
<td>382.158</td>
<td>337.111</td>
<td>45.047</td>
<td>13.36%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>painless_static</td>
<td>513.202</td>
<td>357.771</td>
<td>155.43</td>
<td>43.44%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>painless_static</td>
<td>560.61</td>
<td>374.121</td>
<td>186.49</td>
<td>49.85%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>painless_static</td>
<td>567.419</td>
<td>394.632</td>
<td>172.79</td>
<td>43.78%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>painless_static</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">脚本查询（使用 painless 静态脚本，动态获取字段值）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>painless_dynamic</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>painless_dynamic</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>painless_dynamic</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>painless_dynamic</td>
<td>377.278</td>
<td>334.684</td>
<td>42.594</td>
<td>12.73%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>painless_dynamic</td>
<td>517.496</td>
<td>354.406</td>
<td>163.09</td>
<td>46.02%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>painless_dynamic</td>
<td>576.697</td>
<td>377.214</td>
<td>199.48</td>
<td>52.88%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>painless_dynamic</td>
<td>580.017</td>
<td>381.276</td>
<td>198.74</td>
<td>52.13%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>painless_dynamic</td>
<td>376.339</td>
<td>333.654</td>
<td>42.685</td>
<td>12.79%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>painless_dynamic</td>
<td>516.407</td>
<td>353.246</td>
<td>163.16</td>
<td>46.19%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>painless_dynamic</td>
<td>575.714</td>
<td>375.956</td>
<td>199.76</td>
<td>53.13%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>painless_dynamic</td>
<td>579.642</td>
<td>379.75</td>
<td>199.89</td>
<td>52.64%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>painless_dynamic</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">地理范围查询（基于高斯衰减函数）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>decay_geo_gauss_function_score</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>decay_geo_gauss_function_score</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>decay_geo_gauss_function_score</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>decay_geo_gauss_function_score</td>
<td>348.531</td>
<td>327.972</td>
<td>20.559</td>
<td>6.27%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>decay_geo_gauss_function_score</td>
<td>398.351</td>
<td>336.979</td>
<td>61.372</td>
<td>18.21%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>decay_geo_gauss_function_score</td>
<td>411.483</td>
<td>343.562</td>
<td>67.921</td>
<td>19.77%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>decay_geo_gauss_function_score</td>
<td>457.615</td>
<td>344.135</td>
<td>113.48</td>
<td>32.98%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>decay_geo_gauss_function_score</td>
<td>346.881</td>
<td>326.554</td>
<td>20.327</td>
<td>6.22%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>decay_geo_gauss_function_score</td>
<td>397.08</td>
<td>336.053</td>
<td>61.027</td>
<td>18.16%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>decay_geo_gauss_function_score</td>
<td>410.421</td>
<td>342.151</td>
<td>68.27</td>
<td>19.95%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>decay_geo_gauss_function_score</td>
<td>455.704</td>
<td>342.843</td>
<td>112.86</td>
<td>32.92%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>decay_geo_gauss_function_score</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">地理范围查询（基于高斯衰减函数，且脚本动态获取字段值）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>decay_geo_gauss_script_score</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>decay_geo_gauss_script_score</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>decay_geo_gauss_script_score</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>decay_geo_gauss_script_score</td>
<td>368.275</td>
<td>341.152</td>
<td>27.123</td>
<td>7.95%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>decay_geo_gauss_script_score</td>
<td>414.905</td>
<td>349.94</td>
<td>64.965</td>
<td>18.56%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>decay_geo_gauss_script_score</td>
<td>468.888</td>
<td>354.76</td>
<td>114.13</td>
<td>32.17%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>decay_geo_gauss_script_score</td>
<td>477.25</td>
<td>364.169</td>
<td>113.08</td>
<td>31.05%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>decay_geo_gauss_script_score</td>
<td>366.945</td>
<td>339.967</td>
<td>26.978</td>
<td>7.94%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>decay_geo_gauss_script_score</td>
<td>413.609</td>
<td>348.493</td>
<td>65.116</td>
<td>18.69%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>decay_geo_gauss_script_score</td>
<td>467.627</td>
<td>353.559</td>
<td>114.07</td>
<td>32.26%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>decay_geo_gauss_script_score</td>
<td>475.367</td>
<td>362.748</td>
<td>112.62</td>
<td>31.05%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>decay_geo_gauss_script_score</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">自定义评分函数查询（基于字段值定义函数）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>field_value_function_score</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>field_value_function_score</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>field_value_function_score</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>field_value_function_score</td>
<td>139.661</td>
<td>120.538</td>
<td>19.123</td>
<td>15.86%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>field_value_function_score</td>
<td>183.675</td>
<td>137.702</td>
<td>45.973</td>
<td>33.39%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>field_value_function_score</td>
<td>197.653</td>
<td>147.851</td>
<td>49.802</td>
<td>33.68%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>field_value_function_score</td>
<td>202.345</td>
<td>169.961</td>
<td>32.384</td>
<td>19.05%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>field_value_function_score</td>
<td>138.423</td>
<td>119.159</td>
<td>19.264</td>
<td>16.17%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>field_value_function_score</td>
<td>182.404</td>
<td>136.338</td>
<td>46.066</td>
<td>33.79%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>field_value_function_score</td>
<td>196.734</td>
<td>146.981</td>
<td>49.753</td>
<td>33.85%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>field_value_function_score</td>
<td>201.442</td>
<td>168.964</td>
<td>32.478</td>
<td>19.22%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>field_value_function_score</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">自定义评分函数查询（通过脚本动态获取字段值计算评分）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>field_value_script_score</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>field_value_script_score</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>field_value_script_score</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>field_value_script_score</td>
<td>188.952</td>
<td>168.069</td>
<td>20.883</td>
<td>12.43%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>field_value_script_score</td>
<td>264.095</td>
<td>178.933</td>
<td>85.162</td>
<td>47.59%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>field_value_script_score</td>
<td>271.153</td>
<td>196.982</td>
<td>74.171</td>
<td>37.65%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>field_value_script_score</td>
<td>271.901</td>
<td>198.722</td>
<td>73.179</td>
<td>36.82%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>field_value_script_score</td>
<td>187.218</td>
<td>166.827</td>
<td>20.391</td>
<td>12.22%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>field_value_script_score</td>
<td>263.207</td>
<td>177.869</td>
<td>85.338</td>
<td>47.98%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>field_value_script_score</td>
<td>269.578</td>
<td>195.586</td>
<td>73.992</td>
<td>37.83%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>field_value_script_score</td>
<td>270.138</td>
<td>197.054</td>
<td>73.084</td>
<td>37.09%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>field_value_script_score</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">大量 terms 条件查询（query）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>large_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>large_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>large_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>large_terms</td>
<td>265.007</td>
<td>241.322</td>
<td>23.685</td>
<td>9.81%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>large_terms</td>
<td>296.009</td>
<td>252.637</td>
<td>43.372</td>
<td>17.17%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>large_terms</td>
<td>310.358</td>
<td>265.807</td>
<td>44.551</td>
<td>16.76%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>large_terms</td>
<td>311.049</td>
<td>272.611</td>
<td>38.438</td>
<td>14.10%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>large_terms</td>
<td>256.372</td>
<td>233.129</td>
<td>23.243</td>
<td>9.97%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>large_terms</td>
<td>287.851</td>
<td>244.494</td>
<td>43.357</td>
<td>17.73%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>large_terms</td>
<td>301.827</td>
<td>258.894</td>
<td>42.933</td>
<td>16.58%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>large_terms</td>
<td>302.251</td>
<td>264.352</td>
<td>37.899</td>
<td>14.34%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>large_terms</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">大量 terms 条件过滤查询（query、filter）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>large_filtered_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>large_filtered_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>large_filtered_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>large_filtered_terms</td>
<td>268.135</td>
<td>233.192</td>
<td>34.943</td>
<td>14.98%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>large_filtered_terms</td>
<td>304.158</td>
<td>241.102</td>
<td>63.056</td>
<td>26.15%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>large_filtered_terms</td>
<td>351.209</td>
<td>251.835</td>
<td>99.374</td>
<td>39.46%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>large_filtered_terms</td>
<td>352.003</td>
<td>260.27</td>
<td>91.733</td>
<td>35.25%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>large_filtered_terms</td>
<td>259.546</td>
<td>225.052</td>
<td>34.494</td>
<td>15.33%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>large_filtered_terms</td>
<td>295.721</td>
<td>233.16</td>
<td>62.561</td>
<td>26.83%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>large_filtered_terms</td>
<td>342.342</td>
<td>243.603</td>
<td>98.739</td>
<td>40.53%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>large_filtered_terms</td>
<td>343.378</td>
<td>252.129</td>
<td>91.249</td>
<td>36.19%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>large_filtered_terms</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">大量条件取反查询（query、must not）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>large_prohibited_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>large_prohibited_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>large_prohibited_terms</td>
<td>1.1</td>
<td>1.1</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>large_prohibited_terms</td>
<td>270.041</td>
<td>235.179</td>
<td>34.862</td>
<td>14.82%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>large_prohibited_terms</td>
<td>310.351</td>
<td>241.076</td>
<td>69.275</td>
<td>28.74%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>large_prohibited_terms</td>
<td>347.414</td>
<td>255.983</td>
<td>91.431</td>
<td>35.72%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>large_prohibited_terms</td>
<td>349.499</td>
<td>259.046</td>
<td>90.453</td>
<td>34.92%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>large_prohibited_terms</td>
<td>261.734</td>
<td>227.487</td>
<td>34.247</td>
<td>15.05%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>large_prohibited_terms</td>
<td>302.279</td>
<td>233.792</td>
<td>68.487</td>
<td>29.29%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>large_prohibited_terms</td>
<td>339.278</td>
<td>248.53</td>
<td>90.748</td>
<td>36.51%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>large_prohibited_terms</td>
<td>340.817</td>
<td>251.083</td>
<td>89.734</td>
<td>35.74%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>large_prohibited_terms</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">降序排序查询</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>desc_sort_population</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>desc_sort_population</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>desc_sort_population</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>desc_sort_population</td>
<td>58.5828</td>
<td>48.387</td>
<td>10.196</td>
<td>21.07%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>desc_sort_population</td>
<td>77.9981</td>
<td>63.073</td>
<td>14.925</td>
<td>23.66%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>desc_sort_population</td>
<td>80.8863</td>
<td>71.7498</td>
<td>9.1365</td>
<td>12.73%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>desc_sort_population</td>
<td>83.1661</td>
<td>83.3593</td>
<td>-0.193</td>
<td>-0.23%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>desc_sort_population</td>
<td>57.1212</td>
<td>47.0436</td>
<td>10.078</td>
<td>21.42%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>desc_sort_population</td>
<td>76.7082</td>
<td>61.3731</td>
<td>15.335</td>
<td>24.99%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>desc_sort_population</td>
<td>79.2907</td>
<td>70.4811</td>
<td>8.8096</td>
<td>12.50%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>desc_sort_population</td>
<td>81.6364</td>
<td>81.6517</td>
<td>-0.015</td>
<td>-0.02%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>desc_sort_population</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">升序排序查询</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>asc_sort_population</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>asc_sort_population</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>asc_sort_population</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>asc_sort_population</td>
<td>62.4328</td>
<td>49.2469</td>
<td>13.186</td>
<td>26.78%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>asc_sort_population</td>
<td>79.8441</td>
<td>67.5894</td>
<td>12.255</td>
<td>18.13%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>asc_sort_population</td>
<td>83.9411</td>
<td>84.6384</td>
<td>-0.697</td>
<td>-0.82%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>asc_sort_population</td>
<td>84.3925</td>
<td>85.8124</td>
<td>-1.42</td>
<td>-1.65%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>asc_sort_population</td>
<td>61.0637</td>
<td>47.8438</td>
<td>13.22</td>
<td>27.63%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>asc_sort_population</td>
<td>78.4101</td>
<td>66.0821</td>
<td>12.328</td>
<td>18.66%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>asc_sort_population</td>
<td>82.2652</td>
<td>83.6026</td>
<td>-1.337</td>
<td>-1.60%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>asc_sort_population</td>
<td>82.5616</td>
<td>84.2175</td>
<td>-1.656</td>
<td>-1.97%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>asc_sort_population</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">升序排序后 after 跳转查询</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>asc_sort_with_after_population</td>
<td>1.5</td>
<td>1.5</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>asc_sort_with_after_population</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>asc_sort_with_after_population</td>
<td>1.51</td>
<td>1.51</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>asc_sort_with_after_population</td>
<td>88.1871</td>
<td>99.1943</td>
<td>-11.01</td>
<td>-11.10%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>asc_sort_with_after_population</td>
<td>127.995</td>
<td>86.0298</td>
<td>41.965</td>
<td>48.78%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>asc_sort_with_after_population</td>
<td>131.171</td>
<td>102.268</td>
<td>28.903</td>
<td>28.26%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>asc_sort_with_after_population</td>
<td>132.181</td>
<td>106.33</td>
<td>25.851</td>
<td>24.31%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>asc_sort_with_after_population</td>
<td>87.132</td>
<td>68.2272</td>
<td>18.905</td>
<td>27.71%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>asc_sort_with_after_population</td>
<td>126.818</td>
<td>84.685</td>
<td>42.133</td>
<td>49.75%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>asc_sort_with_after_population</td>
<td>129.453</td>
<td>101.133</td>
<td>28.32</td>
<td>28.00%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>asc_sort_with_after_population</td>
<td>130.452</td>
<td>105.094</td>
<td>25.358</td>
<td>24.13%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>asc_sort_with_after_population</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">高基字段降序排序查询（基于 DistanceFeatureQuery 快速取 topK）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>desc_sort_geonameid</td>
<td>6.02</td>
<td>6.02</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>desc_sort_geonameid</td>
<td>6.02</td>
<td>6.02</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>desc_sort_geonameid</td>
<td>6.03</td>
<td>6.03</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>desc_sort_geonameid</td>
<td>7.4659</td>
<td>5.53008</td>
<td>1.9358</td>
<td>35.01%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>desc_sort_geonameid</td>
<td>8.26766</td>
<td>6.20276</td>
<td>2.0649</td>
<td>33.29%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>desc_sort_geonameid</td>
<td>8.72369</td>
<td>6.67673</td>
<td>2.047</td>
<td>30.66%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>desc_sort_geonameid</td>
<td>8.79956</td>
<td>6.95103</td>
<td>1.8485</td>
<td>26.59%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>desc_sort_geonameid</td>
<td>6.59986</td>
<td>4.61231</td>
<td>1.9876</td>
<td>43.09%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>desc_sort_geonameid</td>
<td>7.24539</td>
<td>5.45982</td>
<td>1.7856</td>
<td>32.70%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>desc_sort_geonameid</td>
<td>7.57925</td>
<td>5.65304</td>
<td>1.9262</td>
<td>34.07%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>desc_sort_geonameid</td>
<td>7.64471</td>
<td>5.65578</td>
<td>1.9889</td>
<td>35.17%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>desc_sort_geonameid</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">高基字段降序排序 after 跳转查询</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>desc_sort_with_after_geonameid</td>
<td>6.01</td>
<td>6.01</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>desc_sort_with_after_geonameid</td>
<td>6.01</td>
<td>6.02</td>
<td>-0.01</td>
<td>-0.17%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>desc_sort_with_after_geonameid</td>
<td>6.02</td>
<td>6.02</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>desc_sort_with_after_geonameid</td>
<td>89.4587</td>
<td>56.5947</td>
<td>32.864</td>
<td>58.07%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>desc_sort_with_after_geonameid</td>
<td>119.777</td>
<td>79.6503</td>
<td>40.127</td>
<td>50.38%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>desc_sort_with_after_geonameid</td>
<td>123.271</td>
<td>87.7773</td>
<td>35.494</td>
<td>40.44%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>desc_sort_with_after_geonameid</td>
<td>123.628</td>
<td>89.3947</td>
<td>34.233</td>
<td>38.29%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>desc_sort_with_after_geonameid</td>
<td>88.512</td>
<td>55.4855</td>
<td>33.027</td>
<td>59.52%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>desc_sort_with_after_geonameid</td>
<td>118.72</td>
<td>79.2349</td>
<td>39.485</td>
<td>49.83%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>desc_sort_with_after_geonameid</td>
<td>122.79</td>
<td>87.3803</td>
<td>35.41</td>
<td>40.52%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>desc_sort_with_after_geonameid</td>
<td>122.791</td>
<td>88.3606</td>
<td>34.43</td>
<td>38.97%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>desc_sort_with_after_geonameid</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">高基字段升序排序查询（基于 DistanceFeatureQuery 快速取 topK）</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>asc_sort_geonameid</td>
<td>6.02</td>
<td>6.02</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>asc_sort_geonameid</td>
<td>6.02</td>
<td>6.02</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>asc_sort_geonameid</td>
<td>6.03</td>
<td>6.03</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>asc_sort_geonameid</td>
<td>5.80593</td>
<td>5.19317</td>
<td>0.6128</td>
<td>11.80%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>asc_sort_geonameid</td>
<td>6.55438</td>
<td>5.74438</td>
<td>0.81</td>
<td>14.10%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>asc_sort_geonameid</td>
<td>7.36432</td>
<td>6.22846</td>
<td>1.1359</td>
<td>18.24%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>asc_sort_geonameid</td>
<td>7.49672</td>
<td>11.6377</td>
<td>-4.141</td>
<td>-35.58%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>asc_sort_geonameid</td>
<td>4.91916</td>
<td>4.35586</td>
<td>0.5633</td>
<td>12.93%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>asc_sort_geonameid</td>
<td>5.61126</td>
<td>4.92152</td>
<td>0.6897</td>
<td>14.01%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>asc_sort_geonameid</td>
<td>6.12285</td>
<td>5.38949</td>
<td>0.7334</td>
<td>13.61%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>asc_sort_geonameid</td>
<td>6.51222</td>
<td>10.6436</td>
<td>-4.131</td>
<td>-38.82%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>asc_sort_geonameid</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
<tr>
<td rowspan="12">高基字段升序排序 after 跳转查询</td>
<td>ops/s</td>
<td>Min Throughput</td>
<td>asc_sort_with_after_geonameid</td>
<td>6.01</td>
<td>6.01</td>
<td>0</td>
<td>0.00%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Median Throughput</td>
<td>asc_sort_with_after_geonameid</td>
<td>6.01</td>
<td>6.02</td>
<td>-0.01</td>
<td>-0.17%</td>
</tr>
<tr>
<td>ops/s</td>
<td>Max Throughput</td>
<td>asc_sort_with_after_geonameid</td>
<td>6.01</td>
<td>6.02</td>
<td>-0.01</td>
<td>-0.17%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile latency</td>
<td>asc_sort_with_after_geonameid</td>
<td>70.994</td>
<td>58.1403</td>
<td>12.854</td>
<td>22.11%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile latency</td>
<td>asc_sort_with_after_geonameid</td>
<td>104.817</td>
<td>76.5695</td>
<td>28.248</td>
<td>36.89%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile latency</td>
<td>asc_sort_with_after_geonameid</td>
<td>108.797</td>
<td>91.6296</td>
<td>17.167</td>
<td>18.74%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile latency</td>
<td>asc_sort_with_after_geonameid</td>
<td>108.929</td>
<td>91.6364</td>
<td>17.293</td>
<td>18.87%</td>
</tr>
<tr>
<td>ms</td>
<td>50th percentile service time</td>
<td>asc_sort_with_after_geonameid</td>
<td>69.7056</td>
<td>57.1683</td>
<td>12.537</td>
<td>21.93%</td>
</tr>
<tr>
<td>ms</td>
<td>90th percentile service time</td>
<td>asc_sort_with_after_geonameid</td>
<td>103.875</td>
<td>75.7573</td>
<td>28.118</td>
<td>37.12%</td>
</tr>
<tr>
<td>ms</td>
<td>99th percentile service time</td>
<td>asc_sort_with_after_geonameid</td>
<td>107.828</td>
<td>91.1533</td>
<td>16.675</td>
<td>18.29%</td>
</tr>
<tr>
<td>ms</td>
<td>100th percentile service time</td>
<td>asc_sort_with_after_geonameid</td>
<td>108.539</td>
<td>91.3662</td>
<td>17.173</td>
<td>18.80%</td>
</tr>
<tr>
<td>%</td>
<td>error rate</td>
<td>asc_sort_with_after_geonameid</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-</td>
</tr>
</tbody></table>
