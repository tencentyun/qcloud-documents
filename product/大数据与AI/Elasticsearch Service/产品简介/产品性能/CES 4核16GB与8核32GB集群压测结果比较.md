

| Unit    | Metric                                      | Task                           | 4核16GB   | 8核32GB   | 差异值 | 差异百分比 |
| ------- | ------------------------------------------- | ------------------------------ | --------- | --------- | ------ | ---------- |
| min     | Cumulative  indexing time of primary shards | -                              | 16.3633   | 14.2567   | 2.1066 | 14.78%     |
| s       | Total Young Gen GC time                     | -                              | 6.26      | 3.544     | 2.716  | 76.64%     |
|         | Total Young Gen GC count                    | -                              | 892       | 447       | 445    | 99.55%     |
| s       | Total Old Gen GC time                       | -                              | 0         | 0         | 0      |            |
|         | Total Old Gen GC count                      | -                              | 0         | 0         | 0      |            |
| GB      | Store size                                  | -                              | 2.51866   | 2.59725   | -0.079 | -3.03%     |
| GB      | Translog size                               | -                              | 3.59E-07  | 3.59E-07  | 0      | 0.00%      |
| MB      | Heap used for segments                      | -                              | 0.803783  | 0.534325  | 0.2695 | 50.43%     |
| MB      | Heap used for doc values                    | -                              | 0.0284767 | 0.0507355 | -0.022 | -43.87%    |
| MB      | Heap used for terms                         | -                              | 0.655075  | 0.370026  | 0.285  | 77.03%     |
| MB      | Heap used for norms                         | -                              | 0.0732422 | 0.0396729 | 0.0336 | 84.62%     |
| MB      | Heap used for points                        | -                              | 0         | 0         | 0      |            |
| MB      | Heap used for stored fields                 | -                              | 0.0469894 | 0.0119553 | 0.035  | 293.04%    |
|         | Segment count                               | -                              | 6         | 7         | -1     | -14.29%    |
| docs/s  | Min Throughput                              | index-append                   | 89331.9   | 153730    | -64398 | -41.89%    |
| docs/s  | Median Throughput                           | index-append                   | 90268.8   | 159765    | -69496 | -43.50%    |
| docs/s  | Max Throughput                              | index-append                   | 90516.1   | 162791    | -72275 | -44.40%    |
| ms      | 50th percentile latency                     | index-append                   | 233.258   | 130.877   | 102.38 | 78.23%     |
| ms      | 90th percentile latency                     | index-append                   | 314.558   | 162.969   | 151.59 | 93.02%     |
| ms      | 99th percentile latency                     | index-append                   | 341.303   | 181.428   | 159.88 | 88.12%     |
| ms      | 100th percentile latency                    | index-append                   | 354.657   | 225.98    | 128.68 | 56.94%     |
| ms      | 50th percentile service time                | index-append                   | 233.258   | 130.877   | 102.38 | 78.23%     |
| ms      | 90th percentile service time                | index-append                   | 314.558   | 162.969   | 151.59 | 93.02%     |
| ms      | 99th percentile service time                | index-append                   | 341.303   | 181.428   | 159.88 | 88.12%     |
| ms      | 100th percentile service time               | index-append                   | 354.657   | 225.98    | 128.68 | 56.94%     |
| %       | error rate                                  | index-append                   | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | index-stats                    | 90.04     | 90.05     | -0.01  | -0.01%     |
| ops/s   | Median Throughput                           | index-stats                    | 90.07     | 90.06     | 0.01   | 0.01%      |
| ops/s   | Max Throughput                              | index-stats                    | 90.14     | 90.12     | 0.02   | 0.02%      |
| ms      | 50th percentile latency                     | index-stats                    | 2.91003   | 2.76736   | 0.1427 | 5.16%      |
| ms      | 90th percentile latency                     | index-stats                    | 3.82882   | 3.58235   | 0.2465 | 6.88%      |
| ms      | 99th percentile latency                     | index-stats                    | 4.2378    | 3.95798   | 0.2798 | 7.07%      |
| ms      | 99.9th percentile latency                   | index-stats                    | 4.34459   | 4.39377   | -0.049 | -1.12%     |
| ms      | 100th percentile latency                    | index-stats                    | 8.22393   | 9.00375   | -0.78  | -8.66%     |
| ms      | 50th percentile service time                | index-stats                    | 1.78268   | 1.57744   | 0.2052 | 13.01%     |
| ms      | 90th percentile service time                | index-stats                    | 2.07484   | 1.8317    | 0.2431 | 13.27%     |
| ms      | 99th percentile service time                | index-stats                    | 2.43121   | 2.0752    | 0.356  | 17.16%     |
| ms      | 99.9th percentile service time              | index-stats                    | 3.09198   | 2.24891   | 0.8431 | 37.49%     |
| ms      | 100th percentile service time               | index-stats                    | 7.29974   | 2.31078   | 4.989  | 215.90%    |
| %       | error rate                                  | index-stats                    | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | node-stats                     | 90.06     | 90.06     | 0      | 0.00%      |
| ops/s   | Median Throughput                           | node-stats                     | 90.09     | 90.12     | -0.03  | -0.03%     |
| ops/s   | Max Throughput                              | node-stats                     | 90.34     | 90.36     | -0.02  | -0.02%     |
| ms      | 50th percentile latency                     | node-stats                     | 3.17223   | 2.9754    | 0.1968 | 6.62%      |
| ms      | 90th percentile latency                     | node-stats                     | 3.70681   | 4.07929   | -0.372 | -9.13%     |
| ms      | 99th percentile latency                     | node-stats                     | 5.01334   | 5.0754    | -0.062 | -1.22%     |
| ms      | 99.9th percentile latency                   | node-stats                     | 6.75018   | 6.53613   | 0.2141 | 3.27%      |
| ms      | 100th percentile latency                    | node-stats                     | 7.98905   | 6.93454   | 1.0545 | 15.21%     |
| ms      | 50th percentile service time                | node-stats                     | 2.43876   | 2.23841   | 0.2004 | 8.95%      |
| ms      | 90th percentile service time                | node-stats                     | 2.78272   | 2.65367   | 0.1291 | 4.86%      |
| ms      | 99th percentile service time                | node-stats                     | 4.12234   | 3.92073   | 0.2016 | 5.14%      |
| ms      | 99.9th percentile service time              | node-stats                     | 6.35902   | 4.92842   | 1.4306 | 29.03%     |
| ms      | 100th percentile service time               | node-stats                     | 7.4313    | 5.92757   | 1.5037 | 25.37%     |
| %       | error rate                                  | node-stats                     | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | default                        | 50.03     | 50.03     | 0      | 0.00%      |
| ops/s   | Median Throughput                           | default                        | 50.04     | 50.04     | 0      | 0.00%      |
| ops/s   | Max Throughput                              | default                        | 50.08     | 50.08     | 0      | 0.00%      |
| ms      | 50th percentile latency                     | default                        | 3.89929   | 3.53894   | 0.3604 | 10.18%     |
| ms      | 90th percentile latency                     | default                        | 4.39236   | 4.11403   | 0.2783 | 6.77%      |
| ms      | 99th percentile latency                     | default                        | 4.78834   | 4.92737   | -0.139 | -2.82%     |
| ms      | 99.9th percentile latency                   | default                        | 7.10486   | 5.74037   | 1.3645 | 23.77%     |
| ms      | 100th percentile latency                    | default                        | 8.75822   | 7.32557   | 1.4327 | 19.56%     |
| ms      | 50th percentile service time                | default                        | 3.18269   | 2.7831    | 0.3996 | 14.36%     |
| ms      | 90th percentile service time                | default                        | 3.49347   | 3.17322   | 0.3203 | 10.09%     |
| ms      | 99th percentile service time                | default                        | 3.8746    | 3.77477   | 0.0998 | 2.64%      |
| ms      | 99.9th percentile service time              | default                        | 6.68581   | 4.19186   | 2.494  | 59.50%     |
| ms      | 100th percentile service time               | default                        | 8.30396   | 6.58243   | 1.7215 | 26.15%     |
| %       | error rate                                  | default                        | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | term                           | 100.05    | 99.66     | 0.39   | 0.39%      |
| ops/s   | Median Throughput                           | term                           | 100.07    | 100.07    | 0      | 0.00%      |
| ops/s   | Max Throughput                              | term                           | 100.14    | 100.11    | 0.03   | 0.03%      |
| ms      | 50th percentile latency                     | term                           | 3.17419   | 2.83987   | 0.3343 | 11.77%     |
| ms      | 90th percentile latency                     | term                           | 3.62229   | 3.32569   | 0.2966 | 8.92%      |
| ms      | 99th percentile latency                     | term                           | 4.03812   | 3.96055   | 0.0776 | 1.96%      |
| ms      | 99.9th percentile latency                   | term                           | 5.9753    | 4.33961   | 1.6357 | 37.69%     |
| ms      | 100th percentile latency                    | term                           | 8.03321   | 5.70421   | 2.329  | 40.83%     |
| ms      | 50th percentile service time                | term                           | 2.49755   | 2.08935   | 0.4082 | 19.54%     |
| ms      | 90th percentile service time                | term                           | 2.71322   | 2.53284   | 0.1804 | 7.12%      |
| ms      | 99th percentile service time                | term                           | 3.20673   | 2.99484   | 0.2119 | 7.08%      |
| ms      | 99.9th percentile service time              | term                           | 5.17998   | 3.37709   | 1.8029 | 53.39%     |
| ms      | 100th percentile service time               | term                           | 6.95227   | 5.24029   | 1.712  | 32.67%     |
| %       | error rate                                  | term                           | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | phrase                         | 110.05    | 110.04    | 0.01   | 0.01%      |
| ops/s   | Median Throughput                           | phrase                         | 110.07    | 110.08    | -0.01  | -0.01%     |
| ops/s   | Max Throughput                              | phrase                         | 110.12    | 110.11    | 0.01   | 0.01%      |
| ms      | 50th percentile latency                     | phrase                         | 3.09905   | 2.74088   | 0.3582 | 13.07%     |
| ms      | 90th percentile latency                     | phrase                         | 3.62549   | 3.30207   | 0.3234 | 9.79%      |
| ms      | 99th percentile latency                     | phrase                         | 4.55457   | 4.8127    | -0.258 | -5.36%     |
| ms      | 99.9th percentile latency                   | phrase                         | 8.29519   | 5.57204   | 2.7232 | 48.87%     |
| ms      | 100th percentile latency                    | phrase                         | 9.39771   | 6.54587   | 2.8518 | 43.57%     |
| ms      | 50th percentile service time                | phrase                         | 2.38248   | 1.98839   | 0.3941 | 19.82%     |
| ms      | 90th percentile service time                | phrase                         | 2.77084   | 2.41365   | 0.3572 | 14.80%     |
| ms      | 99th percentile service time                | phrase                         | 3.75448   | 4.00121   | -0.247 | -6.17%     |
| ms      | 99.9th percentile service time              | phrase                         | 7.5974    | 4.70793   | 2.8895 | 61.37%     |
| ms      | 100th percentile service time               | phrase                         | 8.98362   | 5.67829   | 3.3053 | 58.21%     |
| %       | error rate                                  | phrase                         | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | country_agg_uncached           | 3.6       | 3.6       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | country_agg_uncached           | 3.61      | 3.61      | 0      | 0.00%      |
| ops/s   | Max Throughput                              | country_agg_uncached           | 3.61      | 3.61      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | country_agg_uncached           | 157.466   | 130.314   | 27.152 | 20.84%     |
| ms      | 90th percentile latency                     | country_agg_uncached           | 217.148   | 147.567   | 69.581 | 47.15%     |
| ms      | 99th percentile latency                     | country_agg_uncached           | 233.185   | 165.174   | 68.011 | 41.18%     |
| ms      | 100th percentile latency                    | country_agg_uncached           | 233.227   | 174.015   | 59.212 | 34.03%     |
| ms      | 50th percentile service time                | country_agg_uncached           | 156.197   | 129.186   | 27.011 | 20.91%     |
| ms      | 90th percentile service time                | country_agg_uncached           | 215.852   | 146.921   | 68.931 | 46.92%     |
| ms      | 99th percentile service time                | country_agg_uncached           | 232.177   | 164.579   | 67.598 | 41.07%     |
| ms      | 100th percentile service time               | country_agg_uncached           | 232.321   | 172.827   | 59.494 | 34.42%     |
| %       | error rate                                  | country_agg_uncached           | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | country_agg_cached             | 100.03    | 100.04    | -0.01  | -0.01%     |
| ops/s   | Median Throughput                           | country_agg_cached             | 100.05    | 100.05    | 0      | 0.00%      |
| ops/s   | Max Throughput                              | country_agg_cached             | 100.08    | 100.08    | 0      | 0.00%      |
| ms      | 50th percentile latency                     | country_agg_cached             | 2.44457   | 2.29531   | 0.1493 | 6.50%      |
| ms      | 90th percentile latency                     | country_agg_cached             | 2.97922   | 3.57418   | -0.595 | -16.65%    |
| ms      | 99th percentile latency                     | country_agg_cached             | 3.96393   | 3.91685   | 0.0471 | 1.20%      |
| ms      | 99.9th percentile latency                   | country_agg_cached             | 5.3294    | 4.19749   | 1.1319 | 26.97%     |
| ms      | 100th percentile latency                    | country_agg_cached             | 7.9529    | 4.51842   | 3.4345 | 76.01%     |
| ms      | 50th percentile service time                | country_agg_cached             | 1.71924   | 1.57861   | 0.1406 | 8.91%      |
| ms      | 90th percentile service time                | country_agg_cached             | 1.97892   | 1.89111   | 0.0878 | 4.64%      |
| ms      | 99th percentile service time                | country_agg_cached             | 2.22611   | 2.19488   | 0.0312 | 1.42%      |
| ms      | 99.9th percentile service time              | country_agg_cached             | 5.0967    | 3.42563   | 1.6711 | 48.78%     |
| ms      | 100th percentile service time               | country_agg_cached             | 7.02246   | 4.28971   | 2.7328 | 63.70%     |
| %       | error rate                                  | country_agg_cached             | 0         | 0         | 0      |            |
| pages/s | Min Throughput                              | scroll                         | 20.04     | 20.04     | 0      | 0.00%      |
| pages/s | Median Throughput                           | scroll                         | 20.04     | 20.05     | -0.01  | -0.05%     |
| pages/s | Max Throughput                              | scroll                         | 20.05     | 20.06     | -0.01  | -0.05%     |
| ms      | 50th percentile latency                     | scroll                         | 576.675   | 538.421   | 38.254 | 7.10%      |
| ms      | 90th percentile latency                     | scroll                         | 585.156   | 543.566   | 41.59  | 7.65%      |
| ms      | 99th percentile latency                     | scroll                         | 598.95    | 582.263   | 16.687 | 2.87%      |
| ms      | 100th percentile latency                    | scroll                         | 602.009   | 584.75    | 17.259 | 2.95%      |
| ms      | 50th percentile service time                | scroll                         | 575.118   | 537.068   | 38.05  | 7.08%      |
| ms      | 90th percentile service time                | scroll                         | 583.906   | 542.428   | 41.478 | 7.65%      |
| ms      | 99th percentile service time                | scroll                         | 597.482   | 580.372   | 17.11  | 2.95%      |
| ms      | 100th percentile service time               | scroll                         | 600.578   | 583.612   | 16.966 | 2.91%      |
| %       | error rate                                  | scroll                         | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | expression                     | 2         | 2         | 0      | 0.00%      |
| ops/s   | Median Throughput                           | expression                     | 2         | 2         | 0      | 0.00%      |
| ops/s   | Max Throughput                              | expression                     | 2         | 2         | 0      | 0.00%      |
| ms      | 50th percentile latency                     | expression                     | 299.685   | 265.631   | 34.054 | 12.82%     |
| ms      | 90th percentile latency                     | expression                     | 416.613   | 287.121   | 129.49 | 45.10%     |
| ms      | 99th percentile latency                     | expression                     | 465.776   | 311.788   | 153.99 | 49.39%     |
| ms      | 100th percentile latency                    | expression                     | 468.083   | 391.745   | 76.338 | 19.49%     |
| ms      | 50th percentile service time                | expression                     | 298.594   | 264.462   | 34.132 | 12.91%     |
| ms      | 90th percentile service time                | expression                     | 415.045   | 285.113   | 129.93 | 45.57%     |
| ms      | 99th percentile service time                | expression                     | 464.598   | 310.991   | 153.61 | 49.39%     |
| ms      | 100th percentile service time               | expression                     | 467.106   | 390.33    | 76.776 | 19.67%     |
| %       | error rate                                  | expression                     | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | painless_static                | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | painless_static                | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | painless_static                | 1.5       | 1.5       | 0      | 0.00%      |
| ms      | 50th percentile latency                     | painless_static                | 383.485   | 337.96    | 45.525 | 13.47%     |
| ms      | 90th percentile latency                     | painless_static                | 514.495   | 358.738   | 155.76 | 43.42%     |
| ms      | 99th percentile latency                     | painless_static                | 561.342   | 375.017   | 186.33 | 49.68%     |
| ms      | 100th percentile latency                    | painless_static                | 568.066   | 395.417   | 172.65 | 43.66%     |
| ms      | 50th percentile service time                | painless_static                | 382.158   | 337.111   | 45.047 | 13.36%     |
| ms      | 90th percentile service time                | painless_static                | 513.202   | 357.771   | 155.43 | 43.44%     |
| ms      | 99th percentile service time                | painless_static                | 560.61    | 374.121   | 186.49 | 49.85%     |
| ms      | 100th percentile service time               | painless_static                | 567.419   | 394.632   | 172.79 | 43.78%     |
| %       | error rate                                  | painless_static                | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | painless_dynamic               | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | painless_dynamic               | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | painless_dynamic               | 1.5       | 1.5       | 0      | 0.00%      |
| ms      | 50th percentile latency                     | painless_dynamic               | 377.278   | 334.684   | 42.594 | 12.73%     |
| ms      | 90th percentile latency                     | painless_dynamic               | 517.496   | 354.406   | 163.09 | 46.02%     |
| ms      | 99th percentile latency                     | painless_dynamic               | 576.697   | 377.214   | 199.48 | 52.88%     |
| ms      | 100th percentile latency                    | painless_dynamic               | 580.017   | 381.276   | 198.74 | 52.13%     |
| ms      | 50th percentile service time                | painless_dynamic               | 376.339   | 333.654   | 42.685 | 12.79%     |
| ms      | 90th percentile service time                | painless_dynamic               | 516.407   | 353.246   | 163.16 | 46.19%     |
| ms      | 99th percentile service time                | painless_dynamic               | 575.714   | 375.956   | 199.76 | 53.13%     |
| ms      | 100th percentile service time               | painless_dynamic               | 579.642   | 379.75    | 199.89 | 52.64%     |
| %       | error rate                                  | painless_dynamic               | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | decay_geo_gauss_function_score | 1         | 1         | 0      | 0.00%      |
| ops/s   | Median Throughput                           | decay_geo_gauss_function_score | 1         | 1         | 0      | 0.00%      |
| ops/s   | Max Throughput                              | decay_geo_gauss_function_score | 1         | 1         | 0      | 0.00%      |
| ms      | 50th percentile latency                     | decay_geo_gauss_function_score | 348.531   | 327.972   | 20.559 | 6.27%      |
| ms      | 90th percentile latency                     | decay_geo_gauss_function_score | 398.351   | 336.979   | 61.372 | 18.21%     |
| ms      | 99th percentile latency                     | decay_geo_gauss_function_score | 411.483   | 343.562   | 67.921 | 19.77%     |
| ms      | 100th percentile latency                    | decay_geo_gauss_function_score | 457.615   | 344.135   | 113.48 | 32.98%     |
| ms      | 50th percentile service time                | decay_geo_gauss_function_score | 346.881   | 326.554   | 20.327 | 6.22%      |
| ms      | 90th percentile service time                | decay_geo_gauss_function_score | 397.08    | 336.053   | 61.027 | 18.16%     |
| ms      | 99th percentile service time                | decay_geo_gauss_function_score | 410.421   | 342.151   | 68.27  | 19.95%     |
| ms      | 100th percentile service time               | decay_geo_gauss_function_score | 455.704   | 342.843   | 112.86 | 32.92%     |
| %       | error rate                                  | decay_geo_gauss_function_score | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | decay_geo_gauss_script_score   | 1         | 1         | 0      | 0.00%      |
| ops/s   | Median Throughput                           | decay_geo_gauss_script_score   | 1         | 1         | 0      | 0.00%      |
| ops/s   | Max Throughput                              | decay_geo_gauss_script_score   | 1         | 1         | 0      | 0.00%      |
| ms      | 50th percentile latency                     | decay_geo_gauss_script_score   | 368.275   | 341.152   | 27.123 | 7.95%      |
| ms      | 90th percentile latency                     | decay_geo_gauss_script_score   | 414.905   | 349.94    | 64.965 | 18.56%     |
| ms      | 99th percentile latency                     | decay_geo_gauss_script_score   | 468.888   | 354.76    | 114.13 | 32.17%     |
| ms      | 100th percentile latency                    | decay_geo_gauss_script_score   | 477.25    | 364.169   | 113.08 | 31.05%     |
| ms      | 50th percentile service time                | decay_geo_gauss_script_score   | 366.945   | 339.967   | 26.978 | 7.94%      |
| ms      | 90th percentile service time                | decay_geo_gauss_script_score   | 413.609   | 348.493   | 65.116 | 18.69%     |
| ms      | 99th percentile service time                | decay_geo_gauss_script_score   | 467.627   | 353.559   | 114.07 | 32.26%     |
| ms      | 100th percentile service time               | decay_geo_gauss_script_score   | 475.367   | 362.748   | 112.62 | 31.05%     |
| %       | error rate                                  | decay_geo_gauss_script_score   | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | field_value_function_score     | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | field_value_function_score     | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | field_value_function_score     | 1.51      | 1.51      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | field_value_function_score     | 139.661   | 120.538   | 19.123 | 15.86%     |
| ms      | 90th percentile latency                     | field_value_function_score     | 183.675   | 137.702   | 45.973 | 33.39%     |
| ms      | 99th percentile latency                     | field_value_function_score     | 197.653   | 147.851   | 49.802 | 33.68%     |
| ms      | 100th percentile latency                    | field_value_function_score     | 202.345   | 169.961   | 32.384 | 19.05%     |
| ms      | 50th percentile service time                | field_value_function_score     | 138.423   | 119.159   | 19.264 | 16.17%     |
| ms      | 90th percentile service time                | field_value_function_score     | 182.404   | 136.338   | 46.066 | 33.79%     |
| ms      | 99th percentile service time                | field_value_function_score     | 196.734   | 146.981   | 49.753 | 33.85%     |
| ms      | 100th percentile service time               | field_value_function_score     | 201.442   | 168.964   | 32.478 | 19.22%     |
| %       | error rate                                  | field_value_function_score     | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | field_value_script_score       | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | field_value_script_score       | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | field_value_script_score       | 1.51      | 1.51      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | field_value_script_score       | 188.952   | 168.069   | 20.883 | 12.43%     |
| ms      | 90th percentile latency                     | field_value_script_score       | 264.095   | 178.933   | 85.162 | 47.59%     |
| ms      | 99th percentile latency                     | field_value_script_score       | 271.153   | 196.982   | 74.171 | 37.65%     |
| ms      | 100th percentile latency                    | field_value_script_score       | 271.901   | 198.722   | 73.179 | 36.82%     |
| ms      | 50th percentile service time                | field_value_script_score       | 187.218   | 166.827   | 20.391 | 12.22%     |
| ms      | 90th percentile service time                | field_value_script_score       | 263.207   | 177.869   | 85.338 | 47.98%     |
| ms      | 99th percentile service time                | field_value_script_score       | 269.578   | 195.586   | 73.992 | 37.83%     |
| ms      | 100th percentile service time               | field_value_script_score       | 270.138   | 197.054   | 73.084 | 37.09%     |
| %       | error rate                                  | field_value_script_score       | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | large_terms                    | 1.1       | 1.1       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | large_terms                    | 1.1       | 1.1       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | large_terms                    | 1.1       | 1.1       | 0      | 0.00%      |
| ms      | 50th percentile latency                     | large_terms                    | 265.007   | 241.322   | 23.685 | 9.81%      |
| ms      | 90th percentile latency                     | large_terms                    | 296.009   | 252.637   | 43.372 | 17.17%     |
| ms      | 99th percentile latency                     | large_terms                    | 310.358   | 265.807   | 44.551 | 16.76%     |
| ms      | 100th percentile latency                    | large_terms                    | 311.049   | 272.611   | 38.438 | 14.10%     |
| ms      | 50th percentile service time                | large_terms                    | 256.372   | 233.129   | 23.243 | 9.97%      |
| ms      | 90th percentile service time                | large_terms                    | 287.851   | 244.494   | 43.357 | 17.73%     |
| ms      | 99th percentile service time                | large_terms                    | 301.827   | 258.894   | 42.933 | 16.58%     |
| ms      | 100th percentile service time               | large_terms                    | 302.251   | 264.352   | 37.899 | 14.34%     |
| %       | error rate                                  | large_terms                    | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | large_filtered_terms           | 1.1       | 1.1       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | large_filtered_terms           | 1.1       | 1.1       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | large_filtered_terms           | 1.1       | 1.1       | 0      | 0.00%      |
| ms      | 50th percentile latency                     | large_filtered_terms           | 268.135   | 233.192   | 34.943 | 14.98%     |
| ms      | 90th percentile latency                     | large_filtered_terms           | 304.158   | 241.102   | 63.056 | 26.15%     |
| ms      | 99th percentile latency                     | large_filtered_terms           | 351.209   | 251.835   | 99.374 | 39.46%     |
| ms      | 100th percentile latency                    | large_filtered_terms           | 352.003   | 260.27    | 91.733 | 35.25%     |
| ms      | 50th percentile service time                | large_filtered_terms           | 259.546   | 225.052   | 34.494 | 15.33%     |
| ms      | 90th percentile service time                | large_filtered_terms           | 295.721   | 233.16    | 62.561 | 26.83%     |
| ms      | 99th percentile service time                | large_filtered_terms           | 342.342   | 243.603   | 98.739 | 40.53%     |
| ms      | 100th percentile service time               | large_filtered_terms           | 343.378   | 252.129   | 91.249 | 36.19%     |
| %       | error rate                                  | large_filtered_terms           | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | large_prohibited_terms         | 1.1       | 1.1       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | large_prohibited_terms         | 1.1       | 1.1       | 0      | 0.00%      |
| ops/s   | Max Throughput                              | large_prohibited_terms         | 1.1       | 1.1       | 0      | 0.00%      |
| ms      | 50th percentile latency                     | large_prohibited_terms         | 270.041   | 235.179   | 34.862 | 14.82%     |
| ms      | 90th percentile latency                     | large_prohibited_terms         | 310.351   | 241.076   | 69.275 | 28.74%     |
| ms      | 99th percentile latency                     | large_prohibited_terms         | 347.414   | 255.983   | 91.431 | 35.72%     |
| ms      | 100th percentile latency                    | large_prohibited_terms         | 349.499   | 259.046   | 90.453 | 34.92%     |
| ms      | 50th percentile service time                | large_prohibited_terms         | 261.734   | 227.487   | 34.247 | 15.05%     |
| ms      | 90th percentile service time                | large_prohibited_terms         | 302.279   | 233.792   | 68.487 | 29.29%     |
| ms      | 99th percentile service time                | large_prohibited_terms         | 339.278   | 248.53    | 90.748 | 36.51%     |
| ms      | 100th percentile service time               | large_prohibited_terms         | 340.817   | 251.083   | 89.734 | 35.74%     |
| %       | error rate                                  | large_prohibited_terms         | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | desc_sort_population           | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | desc_sort_population           | 1.51      | 1.51      | 0      | 0.00%      |
| ops/s   | Max Throughput                              | desc_sort_population           | 1.51      | 1.51      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | desc_sort_population           | 58.5828   | 48.387    | 10.196 | 21.07%     |
| ms      | 90th percentile latency                     | desc_sort_population           | 77.9981   | 63.073    | 14.925 | 23.66%     |
| ms      | 99th percentile latency                     | desc_sort_population           | 80.8863   | 71.7498   | 9.1365 | 12.73%     |
| ms      | 100th percentile latency                    | desc_sort_population           | 83.1661   | 83.3593   | -0.193 | -0.23%     |
| ms      | 50th percentile service time                | desc_sort_population           | 57.1212   | 47.0436   | 10.078 | 21.42%     |
| ms      | 90th percentile service time                | desc_sort_population           | 76.7082   | 61.3731   | 15.335 | 24.99%     |
| ms      | 99th percentile service time                | desc_sort_population           | 79.2907   | 70.4811   | 8.8096 | 12.50%     |
| ms      | 100th percentile service time               | desc_sort_population           | 81.6364   | 81.6517   | -0.015 | -0.02%     |
| %       | error rate                                  | desc_sort_population           | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | asc_sort_population            | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | asc_sort_population            | 1.51      | 1.51      | 0      | 0.00%      |
| ops/s   | Max Throughput                              | asc_sort_population            | 1.51      | 1.51      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | asc_sort_population            | 62.4328   | 49.2469   | 13.186 | 26.78%     |
| ms      | 90th percentile latency                     | asc_sort_population            | 79.8441   | 67.5894   | 12.255 | 18.13%     |
| ms      | 99th percentile latency                     | asc_sort_population            | 83.9411   | 84.6384   | -0.697 | -0.82%     |
| ms      | 100th percentile latency                    | asc_sort_population            | 84.3925   | 85.8124   | -1.42  | -1.65%     |
| ms      | 50th percentile service time                | asc_sort_population            | 61.0637   | 47.8438   | 13.22  | 27.63%     |
| ms      | 90th percentile service time                | asc_sort_population            | 78.4101   | 66.0821   | 12.328 | 18.66%     |
| ms      | 99th percentile service time                | asc_sort_population            | 82.2652   | 83.6026   | -1.337 | -1.60%     |
| ms      | 100th percentile service time               | asc_sort_population            | 82.5616   | 84.2175   | -1.656 | -1.97%     |
| %       | error rate                                  | asc_sort_population            | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | asc_sort_with_after_population | 1.5       | 1.5       | 0      | 0.00%      |
| ops/s   | Median Throughput                           | asc_sort_with_after_population | 1.51      | 1.51      | 0      | 0.00%      |
| ops/s   | Max Throughput                              | asc_sort_with_after_population | 1.51      | 1.51      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | asc_sort_with_after_population | 88.1871   | 99.1943   | -11.01 | -11.10%    |
| ms      | 90th percentile latency                     | asc_sort_with_after_population | 127.995   | 86.0298   | 41.965 | 48.78%     |
| ms      | 99th percentile latency                     | asc_sort_with_after_population | 131.171   | 102.268   | 28.903 | 28.26%     |
| ms      | 100th percentile latency                    | asc_sort_with_after_population | 132.181   | 106.33    | 25.851 | 24.31%     |
| ms      | 50th percentile service time                | asc_sort_with_after_population | 87.132    | 68.2272   | 18.905 | 27.71%     |
| ms      | 90th percentile service time                | asc_sort_with_after_population | 126.818   | 84.685    | 42.133 | 49.75%     |
| ms      | 99th percentile service time                | asc_sort_with_after_population | 129.453   | 101.133   | 28.32  | 28.00%     |
| ms      | 100th percentile service time               | asc_sort_with_after_population | 130.452   | 105.094   | 25.358 | 24.13%     |
| %       | error rate                                  | asc_sort_with_after_population | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | desc_sort_geonameid            | 6.02      | 6.02      | 0      | 0.00%      |
| ops/s   | Median Throughput                           | desc_sort_geonameid            | 6.02      | 6.02      | 0      | 0.00%      |
| ops/s   | Max Throughput                              | desc_sort_geonameid            | 6.03      | 6.03      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | desc_sort_geonameid            | 7.4659    | 5.53008   | 1.9358 | 35.01%     |
| ms      | 90th percentile latency                     | desc_sort_geonameid            | 8.26766   | 6.20276   | 2.0649 | 33.29%     |
| ms      | 99th percentile latency                     | desc_sort_geonameid            | 8.72369   | 6.67673   | 2.047  | 30.66%     |
| ms      | 100th percentile latency                    | desc_sort_geonameid            | 8.79956   | 6.95103   | 1.8485 | 26.59%     |
| ms      | 50th percentile service time                | desc_sort_geonameid            | 6.59986   | 4.61231   | 1.9876 | 43.09%     |
| ms      | 90th percentile service time                | desc_sort_geonameid            | 7.24539   | 5.45982   | 1.7856 | 32.70%     |
| ms      | 99th percentile service time                | desc_sort_geonameid            | 7.57925   | 5.65304   | 1.9262 | 34.07%     |
| ms      | 100th percentile service time               | desc_sort_geonameid            | 7.64471   | 5.65578   | 1.9889 | 35.17%     |
| %       | error rate                                  | desc_sort_geonameid            | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | desc_sort_with_after_geonameid | 6.01      | 6.01      | 0      | 0.00%      |
| ops/s   | Median Throughput                           | desc_sort_with_after_geonameid | 6.01      | 6.02      | -0.01  | -0.17%     |
| ops/s   | Max Throughput                              | desc_sort_with_after_geonameid | 6.02      | 6.02      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | desc_sort_with_after_geonameid | 89.4587   | 56.5947   | 32.864 | 58.07%     |
| ms      | 90th percentile latency                     | desc_sort_with_after_geonameid | 119.777   | 79.6503   | 40.127 | 50.38%     |
| ms      | 99th percentile latency                     | desc_sort_with_after_geonameid | 123.271   | 87.7773   | 35.494 | 40.44%     |
| ms      | 100th percentile latency                    | desc_sort_with_after_geonameid | 123.628   | 89.3947   | 34.233 | 38.29%     |
| ms      | 50th percentile service time                | desc_sort_with_after_geonameid | 88.512    | 55.4855   | 33.027 | 59.52%     |
| ms      | 90th percentile service time                | desc_sort_with_after_geonameid | 118.72    | 79.2349   | 39.485 | 49.83%     |
| ms      | 99th percentile service time                | desc_sort_with_after_geonameid | 122.79    | 87.3803   | 35.41  | 40.52%     |
| ms      | 100th percentile service time               | desc_sort_with_after_geonameid | 122.791   | 88.3606   | 34.43  | 38.97%     |
| %       | error rate                                  | desc_sort_with_after_geonameid | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | asc_sort_geonameid             | 6.02      | 6.02      | 0      | 0.00%      |
| ops/s   | Median Throughput                           | asc_sort_geonameid             | 6.02      | 6.02      | 0      | 0.00%      |
| ops/s   | Max Throughput                              | asc_sort_geonameid             | 6.03      | 6.03      | 0      | 0.00%      |
| ms      | 50th percentile latency                     | asc_sort_geonameid             | 5.80593   | 5.19317   | 0.6128 | 11.80%     |
| ms      | 90th percentile latency                     | asc_sort_geonameid             | 6.55438   | 5.74438   | 0.81   | 14.10%     |
| ms      | 99th percentile latency                     | asc_sort_geonameid             | 7.36432   | 6.22846   | 1.1359 | 18.24%     |
| ms      | 100th percentile latency                    | asc_sort_geonameid             | 7.49672   | 11.6377   | -4.141 | -35.58%    |
| ms      | 50th percentile service time                | asc_sort_geonameid             | 4.91916   | 4.35586   | 0.5633 | 12.93%     |
| ms      | 90th percentile service time                | asc_sort_geonameid             | 5.61126   | 4.92152   | 0.6897 | 14.01%     |
| ms      | 99th percentile service time                | asc_sort_geonameid             | 6.12285   | 5.38949   | 0.7334 | 13.61%     |
| ms      | 100th percentile service time               | asc_sort_geonameid             | 6.51222   | 10.6436   | -4.131 | -38.82%    |
| %       | error rate                                  | asc_sort_geonameid             | 0         | 0         | 0      |            |
| ops/s   | Min Throughput                              | asc_sort_with_after_geonameid  | 6.01      | 6.01      | 0      | 0.00%      |
| ops/s   | Median Throughput                           | asc_sort_with_after_geonameid  | 6.01      | 6.02      | -0.01  | -0.17%     |
| ops/s   | Max Throughput                              | asc_sort_with_after_geonameid  | 6.01      | 6.02      | -0.01  | -0.17%     |
| ms      | 50th percentile latency                     | asc_sort_with_after_geonameid  | 70.994    | 58.1403   | 12.854 | 22.11%     |
| ms      | 90th percentile latency                     | asc_sort_with_after_geonameid  | 104.817   | 76.5695   | 28.248 | 36.89%     |
| ms      | 99th percentile latency                     | asc_sort_with_after_geonameid  | 108.797   | 91.6296   | 17.167 | 18.74%     |
| ms      | 100th percentile latency                    | asc_sort_with_after_geonameid  | 108.929   | 91.6364   | 17.293 | 18.87%     |
| ms      | 50th percentile service time                | asc_sort_with_after_geonameid  | 69.7056   | 57.1683   | 12.537 | 21.93%     |
| ms      | 90th percentile service time                | asc_sort_with_after_geonameid  | 103.875   | 75.7573   | 28.118 | 37.12%     |
| ms      | 99th percentile service time                | asc_sort_with_after_geonameid  | 107.828   | 91.1533   | 16.675 | 18.29%     |
| ms      | 100th percentile service time               | asc_sort_with_after_geonameid  | 108.539   | 91.3662   | 17.173 | 18.80%     |
| %       | error rate                                  | asc_sort_with_after_geonameid  | 0         | 0         | 0      |            |

