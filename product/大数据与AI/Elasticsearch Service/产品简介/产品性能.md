使用 Elasticsearch 官方提供的 rally 压测工具和 geonames 数据集（大小3.2G，共11523468个文档），对腾讯云 Elasticsearch Service 构建的两种规格的 ES 集群进行压测，性能结果如下：

#### 2核8G 3个节点：

|                          Metric   |                    Task   | Value | Unit  |
|---------|---------|---------|---------|
|             Total indexing time   |               -            | 18.5837 |      min  |
|     Min indexing time per shard   |           -                | 0.000533333 |      min  |
|  Median indexing time per shard   |                 -          | 3.4134  |      min  |
|     Max indexing time per shard   |               -            | 4.21195 |      min  |
|              Total refresh time   |                    -       | 2.40147 |      min  |
|      Min refresh time per shard   |              -             | 0.0009  |      min  |
|   Median refresh time per shard   |            -               | 0.45715 |      min  |
|      Max refresh time per shard   |               -            | 0.5655  |      min  |
|                Total flush time   |                        -   | 0.328317  |      min  |
|        Min flush time per shard   |                    -       | 0.0004  |      min  |
|     Median flush time per shard   |                   -        | 0.0643583 |      min  |
|        Max flush time per shard   |                      -     | 0.0972167 |      min  |
|              Total Young Gen GC   |                        -   | 127.992 |        s  |
|                Total Old Gen GC   |          -                 | 1.327 |        s  |
|                      Store size   |                -           | 3.22145 |       GB  |
|                   Translog size   |               -            | 2.80E-07  |       GB  |
|          Heap used for segments   |         -                  | 10.8161 |       MB  |
|        Heap used for doc values   |          -                 | 0.0831299 |       MB  |
|             Heap used for terms   |              -             | 9.62618 |       MB  |
|             Heap used for norms   |              -             | 0.0795288 |       MB  |
|            Heap used for points   |                -           | 0.217488  |       MB  |
|     Heap used for stored fields   |               -            | 0.809799  |       MB  |
|                   Segment count   |                    -       | 102 |     -      |
|                  Min Throughput   |            index-append   | 41895.6 |   docs/s  |
|               Median Throughput   |            index-append   | 42562 |   docs/s  |
|                  Max Throughput   |            index-append   | 43352 |   docs/s  |
|         50th percentile latency   |            index-append   | 757.636 |       ms  |
|         90th percentile latency   |            index-append   | 1388.11 |       ms  |
|         99th percentile latency   |            index-append   | 2650.44 |       ms  |
|       99.9th percentile latency   |            index-append   | 5270.13 |       ms  |
|        100th percentile latency   |            index-append   | 6535.29 |       ms  |
|    50th percentile service time   |            index-append   | 757.636 |       ms  |
|    90th percentile service time   |            index-append   | 1388.11 |       ms  |
|    99th percentile service time   |            index-append   | 2650.44 |       ms  |
|  99.9th percentile service time   |            index-append   | 5270.13 |       ms  |
|   100th percentile service time   |            index-append   | 6535.29 |       ms  |
|                      error rate   |            index-append   | 0 |        %  |
|                  Min Throughput   |             index-stats   | 99.99 |    ops/s  |
|               Median Throughput   |             index-stats   | 100.04  |    ops/s  |
|                  Max Throughput   |             index-stats   | 100.06  |    ops/s  |
|         50th percentile latency   |             index-stats   | 6.04131 |       ms  |
|         90th percentile latency   |             index-stats   | 6.56561 |       ms  |
|         99th percentile latency   |             index-stats   | 10.7941 |       ms  |
|       99.9th percentile latency   |             index-stats   | 22.6768 |       ms  |
|        100th percentile latency   |             index-stats   | 24.5623 |       ms  |
|    50th percentile service time   |             index-stats   | 5.9341  |       ms  |
|    90th percentile service time   |             index-stats   | 6.42644 |       ms  |
|    99th percentile service time   |             index-stats   | 7.56809 |       ms  |
|  99.9th percentile service time   |             index-stats   | 22.5948 |       ms  |
|   100th percentile service time   |             index-stats   | 24.4467 |       ms  |
|                      error rate   |             index-stats   | 0 |        %  |
|                  Min Throughput   |              node-stats   | 99.93 |    ops/s  |
|               Median Throughput   |              node-stats   | 100.06  |    ops/s  |
|                  Max Throughput   |              node-stats   | 100.33  |    ops/s  |
|         50th percentile latency   |              node-stats   | 6.74088 |       ms  |
|         90th percentile latency   |              node-stats   | 7.28822 |       ms  |
|         99th percentile latency   |              node-stats   | 8.62256 |       ms  |
|       99.9th percentile latency   |              node-stats   | 13.271  |       ms  |
|        100th percentile latency   |              node-stats   | 13.9379 |       ms  |
|    50th percentile service time   |              node-stats   | 6.64634 |       ms  |
|    90th percentile service time   |              node-stats   | 7.18403 |       ms  |
|    99th percentile service time   |              node-stats   | 8.34209 |       ms  |
|  99.9th percentile service time   |              node-stats   | 13.1784 |       ms  |
|   100th percentile service time   |              node-stats   | 13.8411 |       ms  |
|                      error rate   |              node-stats   | 0 |        %  |
|                  Min Throughput   |                 default   | 46.85 |    ops/s  |
|               Median Throughput   |                 default   | 47.58 |    ops/s  |
|                  Max Throughput   |                 default   | 47.7  |    ops/s  |
|         50th percentile latency   |                 default   | 1023.59 |       ms  |
|         90th percentile latency   |                 default   | 1890.67 |       ms  |
|         99th percentile latency   |                 default   | 2017.58 |       ms  |
|       99.9th percentile latency   |                 default   | 2026.21 |       ms  |
|        100th percentile latency   |                 default   | 2026.21 |       ms  |
|    50th percentile service time   |                 default   | 20.2853 |       ms  |
|    90th percentile service time   |                 default   | 24.3425 |       ms  |
|    99th percentile service time   |                 default   | 33.3526 |       ms  |
|  99.9th percentile service time   |                 default   | 54.702  |       ms  |
|   100th percentile service time   |                 default   | 74.2832 |       ms  |
|                      error rate   |                 default   | 0 |        %  |
|                  Min Throughput   |                    term   | 199.82  |    ops/s  |
|               Median Throughput   |                    term   | 200.02  |    ops/s  |
|                  Max Throughput   |                    term   | 200.05  |    ops/s  |
|         50th percentile latency   |                    term   | 4.54844 |       ms  |
|         90th percentile latency   |                    term   | 9.97587 |       ms  |
|         99th percentile latency   |                    term   | 18.3546 |       ms  |
|       99.9th percentile latency   |                    term   | 21.2112 |       ms  |
|        100th percentile latency   |                    term   | 21.5267 |       ms  |
|    50th percentile service time   |                    term   | 4.39147 |       ms  |
|    90th percentile service time   |                    term   | 4.84527 |       ms  |
|    99th percentile service time   |                    term   | 6.62189 |       ms  |
|  99.9th percentile service time   |                    term   | 19.4932 |       ms  |
|   100th percentile service time   |                    term   | 21.4435 |       ms  |
|                      error rate   |                    term   | 0 |        %  |
|                  Min Throughput   |                  phrase   | 199.68  |    ops/s  |
|               Median Throughput   |                  phrase   | 200.03  |    ops/s  |
|                  Max Throughput   |                  phrase   | 200.11  |    ops/s  |
|         50th percentile latency   |                  phrase   | 3.57488 |       ms  |
|         90th percentile latency   |                  phrase   | 4.62139 |       ms  |
|         99th percentile latency   |                  phrase   | 19.6935 |       ms  |
|       99.9th percentile latency   |                  phrase   | 24.9076 |       ms  |
|        100th percentile latency   |                  phrase   | 25.0486 |       ms  |
|    50th percentile service time   |                  phrase   | 3.4742  |       ms  |
|    90th percentile service time   |                  phrase   | 4.0265  |       ms  |
|    99th percentile service time   |                  phrase   | 7.57333 |       ms  |
|  99.9th percentile service time   |                  phrase   | 18.9011 |       ms  |
|   100th percentile service time   |                  phrase   | 23.8045 |       ms  |
|                      error rate   |                  phrase   | 0 |        %  |
|                  Min Throughput   |    country_agg_uncached   | 4.99  |    ops/s  |
|               Median Throughput   |    country_agg_uncached   | 5 |    ops/s  |
|                  Max Throughput   |    country_agg_uncached   | 5 |    ops/s  |
|         50th percentile latency   |    country_agg_uncached   | 197.534 |       ms  |
|         90th percentile latency   |    country_agg_uncached   | 217.842 |       ms  |
|         99th percentile latency   |    country_agg_uncached   | 271.988 |       ms  |
|        100th percentile latency   |    country_agg_uncached   | 275.963 |       ms  |
|    50th percentile service time   |    country_agg_uncached   | 194.061 |       ms  |
|    90th percentile service time   |    country_agg_uncached   | 209.086 |       ms  |
|    99th percentile service time   |    country_agg_uncached   | 216.432 |       ms  |
|   100th percentile service time   |    country_agg_uncached   | 217.275 |       ms  |
|                      error rate   |    country_agg_uncached   | 0 |        %  |
|                  Min Throughput   |      country_agg_cached   | 99.97 |    ops/s  |
|               Median Throughput   |      country_agg_cached   | 100.05  |    ops/s  |
|                  Max Throughput   |      country_agg_cached   | 100.08  |    ops/s  |
|         50th percentile latency   |      country_agg_cached   | 4.9212  |       ms  |
|         90th percentile latency   |      country_agg_cached   | 5.44065 |       ms  |
|         99th percentile latency   |      country_agg_cached   | 7.15509 |       ms  |
|       99.9th percentile latency   |      country_agg_cached   | 16.9407 |       ms  |
|        100th percentile latency   |      country_agg_cached   | 17.8111 |       ms  |
|    50th percentile service time   |      country_agg_cached   | 4.81515 |       ms  |
|    90th percentile service time   |      country_agg_cached   | 5.29377 |       ms  |
|    99th percentile service time   |      country_agg_cached   | 6.38482 |       ms  |
|  99.9th percentile service time   |      country_agg_cached   | 16.8318 |       ms  |
|   100th percentile service time   |      country_agg_cached   | 17.7311 |       ms  |
|                      error rate   |      country_agg_cached   | 0 |        %  |
|                  Min Throughput   |                  scroll   | 25.02 |  pages/s  |
|               Median Throughput   |                  scroll   | 25.02 |  pages/s  |
|                  Max Throughput   |                  scroll   | 25.03 |  pages/s  |
|         50th percentile latency   |                  scroll   | 760.634 |       ms  |
|         90th percentile latency   |                  scroll   | 794.699 |       ms  |
|         99th percentile latency   |                  scroll   | 864.897 |       ms  |
|        100th percentile latency   |                  scroll   | 874.768 |       ms  |
|    50th percentile service time   |                  scroll   | 760.32  |       ms  |
|    90th percentile service time   |                  scroll   | 794.397 |       ms  |
|    99th percentile service time   |                  scroll   | 864.658 |       ms  |
|   100th percentile service time   |                  scroll   | 874.556 |       ms  |
|                      error rate   |                  scroll   | 0 |        %  |
|                  Min Throughput   |              expression   | 2 |    ops/s  |
|               Median Throughput   |              expression   | 2 |    ops/s  |
|                  Max Throughput   |              expression   | 2 |    ops/s  |
|         50th percentile latency   |              expression   | 382.483 |       ms  |
|         90th percentile latency   |              expression   | 414.775 |       ms  |
|         99th percentile latency   |              expression   | 455.236 |       ms  |
|        100th percentile latency   |              expression   | 473.181 |       ms  |
|    50th percentile service time   |              expression   | 382.298 |       ms  |
|    90th percentile service time   |              expression   | 414.577 |       ms  |
|    99th percentile service time   |              expression   | 455.11  |       ms  |
|   100th percentile service time   |              expression   | 472.998 |       ms  |
|                      error rate   |              expression   | 0 |        %  |
|                  Min Throughput   |         painless_static   | 1.5 |    ops/s  |
|               Median Throughput   |         painless_static   | 1.5 |    ops/s  |
|                  Max Throughput   |         painless_static   | 1.5 |    ops/s  |
|         50th percentile latency   |         painless_static   | 480.188 |       ms  |
|         90th percentile latency   |         painless_static   | 505.003 |       ms  |
|         99th percentile latency   |         painless_static   | 529.066 |       ms  |
|        100th percentile latency   |         painless_static   | 547.199 |       ms  |
|    50th percentile service time   |         painless_static   | 479.938 |       ms  |
|    90th percentile service time   |         painless_static   | 504.731 |       ms  |
|    99th percentile service time   |         painless_static   | 528.857 |       ms  |
|   100th percentile service time   |         painless_static   | 546.954 |       ms  |
|                      error rate   |         painless_static   | 0 |        %  |
|                  Min Throughput   |        painless_dynamic   | 1.5 |    ops/s  |
|               Median Throughput   |        painless_dynamic   | 1.5 |    ops/s  |
|                  Max Throughput   |        painless_dynamic   | 1.5 |    ops/s  |
|         50th percentile latency   |        painless_dynamic   | 469.434 |       ms  |
|         90th percentile latency   |        painless_dynamic   | 508.615 |       ms  |
|         99th percentile latency   |        painless_dynamic   | 581.127 |       ms  |
|        100th percentile latency   |        painless_dynamic   | 621.998 |       ms  |
|    50th percentile service time   |        painless_dynamic   | 469.178 |       ms  |
|    90th percentile service time   |        painless_dynamic   | 508.349 |       ms  |
|    99th percentile service time   |        painless_dynamic   | 580.819 |       ms  |
|   100th percentile service time   |        painless_dynamic   | 621.799 |       ms  |
|                      error rate   |        painless_dynamic   | 0 |        %  |
|                      error rate   |             large_terms   | 0 |        %  |
|                  Min Throughput   |    large_filtered_terms   | 1.52  |    ops/s  |
|               Median Throughput   |    large_filtered_terms   | 1.52  |    ops/s  |
|                  Max Throughput   |    large_filtered_terms   | 1.52  |    ops/s  |
|         50th percentile latency   |    large_filtered_terms   | 39664.6 |       ms  |
|         90th percentile latency   |    large_filtered_terms   | 46001.3 |       ms  |
|         99th percentile latency   |    large_filtered_terms   | 47328 |       ms  |
|        100th percentile latency   |    large_filtered_terms   | 47488.6 |       ms  |
|    50th percentile service time   |    large_filtered_terms   | 651.731 |       ms  |
|    90th percentile service time   |    large_filtered_terms   | 673.319 |       ms  |
|    99th percentile service time   |    large_filtered_terms   | 715.941 |       ms  |
|   100th percentile service time   |    large_filtered_terms   | 723.06  |       ms  |
|                      error rate   |    large_filtered_terms   | 0 |        %  |
|                  Min Throughput   |  large_prohibited_terms   | 1.55  |    ops/s  |
|               Median Throughput   |  large_prohibited_terms   | 1.56  |    ops/s  |
|                  Max Throughput   |  large_prohibited_terms   | 1.57  |    ops/s  |
|         50th percentile latency   |  large_prohibited_terms   | 35606.8 |       ms  |
|         90th percentile latency   |  large_prohibited_terms   | 40847.6 |       ms  |
|         99th percentile latency   |  large_prohibited_terms   | 42170.5 |       ms  |
|        100th percentile latency   |  large_prohibited_terms   | 42329.2 |       ms  |
|    50th percentile service time   |  large_prohibited_terms   | 648.82  |       ms  |
|    90th percentile service time   |  large_prohibited_terms   | 672.114 |       ms  |
|    99th percentile service time   |  large_prohibited_terms   | 722.666 |       ms  |
|   100th percentile service time   |  large_prohibited_terms   | 733.307 |       ms  |
|                      error rate   |  large_prohibited_terms   | 0 |        %  |


#### 4核16G 3个节点：

|                          Metric   |                    Task     |        Value  | Unit  |
|---------|---------|---------|---------|
|                   Total indexing time   |              -               | 20.1957 |      min  |
|           Min indexing time per shard   |          -                   | 0.000733333 |      min  |
|        Median indexing time per shard   |         -                    | 3.77953 |      min  |
|           Max indexing time per shard   |            -                 | 4.63752 |      min  |
|                      Total merge time   |                   -          | 1.57487 |      min  |
|              Min merge time per shard   |               -              | 0 |      min  |
|           Median merge time per shard   |              -               | 0.176658  |      min  |
|              Max merge time per shard   |                 -            | 0.634067  |      min  |
|             Total merge throttle time   |                      -       | 0.55105 |      min  |
|     Min merge throttle time per shard   |                  -           | 0 |      min  |
|  Median merge throttle time per shard   |                 -            | 0.065 |      min  |
|     Max merge throttle time per shard   |                    -         | 0.217033  |      min  |
|                    Total refresh time   |      -                       | 1.41135 |      min  |
|            Min refresh time per shard   |  -                           | 0.00106667  |      min  |
|         Median refresh time per shard   | -                            | 0.269958  |      min  |
|            Max refresh time per shard   |    -                         | 0.345733  |      min  |
|                      Total flush time   |            -                 | 0.533133  |      min  |
|              Min flush time per shard   |        -                     | 0.000566667 |      min  |
|           Median flush time per shard   |       -                      | 0.115592  |      min  |
|              Max flush time per shard   |          -                   | 0.136683  |      min  |
|                    Total Young Gen GC   |            -                 | 70.747  |        s  |
|                      Total Old Gen GC   |               -              | 0.92  |        s  |
|                            Store size   |                     -        | 3.31581 |       GB  |
|                         Translog size   |                    -         | 2.80E-07  |       GB  |
|                Heap used for segments   |              -               | 11.0486 |       MB  |
|              Heap used for doc values   |                -             | 0.100529  |       MB  |
|                   Heap used for terms   |                    -         | 9.84413 |       MB  |
|                   Heap used for norms   |                    -         | 0.0755005 |       MB  |
|                  Heap used for points   |                      -       | 0.216421  |       MB  |
|           Heap used for stored fields   |                     -        | 0.811981  |       MB  |
|                         Segment count   |                          -   | 97  |    -       |
|                        Min Throughput   |            index-append     | 74421.1 |   docs/s  |
|                     Median Throughput   |            index-append     | 75636.9 |   docs/s  |
|                        Max Throughput   |            index-append     | 76877.4 |   docs/s  |
|               50th percentile latency   |            index-append     | 377.922 |       ms  |
|               90th percentile latency   |            index-append     | 663.055 |       ms  |
|               99th percentile latency   |            index-append     | 3068.99 |       ms  |
|              100th percentile latency   |            index-append     | 5554.97 |       ms  |
|          50th percentile service time   |            index-append     | 377.922 |       ms  |
|          90th percentile service time   |            index-append     | 663.055 |       ms  |
|          99th percentile service time   |            index-append     | 3068.99 |       ms  |
|         100th percentile service time   |            index-append     | 5554.97 |       ms  |
|                            error rate   |            index-append     | 0 |        %  |
|                        Min Throughput   |             index-stats     | 99.93 |    ops/s  |
|                     Median Throughput   |             index-stats     | 100.04  |    ops/s  |
|                        Max Throughput   |             index-stats     | 100.06  |    ops/s  |
|               50th percentile latency   |             index-stats     | 6.62305 |       ms  |
|               90th percentile latency   |             index-stats     | 7.35102 |       ms  |
|               99th percentile latency   |             index-stats     | 18.0909 |       ms  |
|             99.9th percentile latency   |             index-stats     | 24.5381 |       ms  |
|              100th percentile latency   |             index-stats     | 24.7431 |       ms  |
|          50th percentile service time   |             index-stats     | 6.50957 |       ms  |
|          90th percentile service time   |             index-stats     | 7.18652 |       ms  |
|          99th percentile service time   |             index-stats     | 9.38455 |       ms  |
|        99.9th percentile service time   |             index-stats     | 24.4424 |       ms  |
|         100th percentile service time   |             index-stats     | 24.6576 |       ms  |
|                            error rate   |             index-stats     | 0 |        %  |
|                        Min Throughput   |              node-stats     | 99.92 |    ops/s  |
|                     Median Throughput   |              node-stats     | 100.04  |    ops/s  |
|                        Max Throughput   |              node-stats     | 100.25  |    ops/s  |
|               50th percentile latency   |              node-stats     | 7.15655 |       ms  |
|               90th percentile latency   |              node-stats     | 7.96104 |       ms  |
|               99th percentile latency   |              node-stats     | 10.2362 |       ms  |
|             99.9th percentile latency   |              node-stats     | 25.7397 |       ms  |
|              100th percentile latency   |              node-stats     | 29.1573 |       ms  |
|          50th percentile service time   |              node-stats     | 7.04389 |       ms  |
|          90th percentile service time   |              node-stats     | 7.84655 |       ms  |
|          99th percentile service time   |              node-stats     | 9.13249 |       ms  |
|        99.9th percentile service time   |              node-stats     | 10.7357 |       ms  |
|         100th percentile service time   |              node-stats     | 29.072  |       ms  |
|                            error rate   |              node-stats     | 0 |        %  |
|                        Min Throughput   |                 default     | 41.88 |    ops/s  |
|                     Median Throughput   |                 default     | 42.18 |    ops/s  |
|                        Max Throughput   |                 default     | 42.52 |    ops/s  |
|               50th percentile latency   |                 default     | 3789.31 |       ms  |
|               90th percentile latency   |                 default     | 5170.79 |       ms  |
|               99th percentile latency   |                 default     | 5582.03 |       ms  |
|             99.9th percentile latency   |                 default     | 5610.7  |       ms  |
|              100th percentile latency   |                 default     | 5618.05 |       ms  |
|          50th percentile service time   |                 default     | 23.1496 |       ms  |
|          90th percentile service time   |                 default     | 25.8865 |       ms  |
|          99th percentile service time   |                 default     | 33.249  |       ms  |
|        99.9th percentile service time   |                 default     | 45.493  |       ms  |
|         100th percentile service time   |                 default     | 62.4174 |       ms  |
|                            error rate   |                 default     | 0 |        %  |
|                        Min Throughput   |                    term     | 199.08  |    ops/s  |
|                     Median Throughput   |                    term     | 200 |    ops/s  |
|                        Max Throughput   |                    term     | 200.03  |    ops/s  |
|               50th percentile latency   |                    term     | 5.02391 |       ms  |
|               90th percentile latency   |                    term     | 21.18 |       ms  |
|               99th percentile latency   |                    term     | 35.2251 |       ms  |
|             99.9th percentile latency   |                    term     | 37.4827 |       ms  |
|              100th percentile latency   |                    term     | 37.6907 |       ms  |
|          50th percentile service time   |                    term     | 4.61812 |       ms  |
|          90th percentile service time   |                    term     | 5.10619 |       ms  |
|          99th percentile service time   |                    term     | 6.8135  |       ms  |
|        99.9th percentile service time   |                    term     | 22.1183 |       ms  |
|         100th percentile service time   |                    term     | 25.0033 |       ms  |
|                            error rate   |                    term     | 0 |        %  |
|                        Min Throughput   |                  phrase     | 199.61  |    ops/s  |
|                     Median Throughput   |                  phrase     | 200.04  |    ops/s  |
|                        Max Throughput   |                  phrase     | 200.8 |    ops/s  |
|               50th percentile latency   |                  phrase     | 3.86572 |       ms  |
|               90th percentile latency   |                  phrase     | 4.96583 |       ms  |
|               99th percentile latency   |                  phrase     | 22.5681 |       ms  |
|             99.9th percentile latency   |                  phrase     | 33.5684 |       ms  |
|              100th percentile latency   |                  phrase     | 28.2658 |       ms  |
|          50th percentile service time   |                  phrase     | 3.5689  |       ms  |
|          90th percentile service time   |                  phrase     | 4.2535  |       ms  |
|          99th percentile service time   |                  phrase     | 8.6957  |       ms  |
|        99.9th percentile service time   |                  phrase     | 24.5685 |       ms  |
|         100th percentile service time   |                  phrase     | 27.6584 |       ms  |
|                            error rate   |                  phrase     | 0 |        %  |
|                        Min Throughput   |    country_agg_uncached     | 4.99  |    ops/s  |
|                     Median Throughput   |    country_agg_uncached     | 5 |    ops/s  |
|                        Max Throughput   |    country_agg_uncached     | 5 |    ops/s  |
|               50th percentile latency   |    country_agg_uncached     | 182.291 |       ms  |
|               90th percentile latency   |    country_agg_uncached     | 201.585 |       ms  |
|               99th percentile latency   |    country_agg_uncached     | 257.343 |       ms  |
|              100th percentile latency   |    country_agg_uncached     | 267.904 |       ms  |
|          50th percentile service time   |    country_agg_uncached     | 181.161 |       ms  |
|          90th percentile service time   |    country_agg_uncached     | 196.189 |       ms  |
|          99th percentile service time   |    country_agg_uncached     | 216.762 |       ms  |
|         100th percentile service time   |    country_agg_uncached     | 267.778 |       ms  |
|                            error rate   |    country_agg_uncached     | 0 |        %  |
|                        Min Throughput   |      country_agg_cached     | 99.95 |    ops/s  |
|                     Median Throughput   |      country_agg_cached     | 100.05  |    ops/s  |
|                        Max Throughput   |      country_agg_cached     | 100.07  |    ops/s  |
|               50th percentile latency   |      country_agg_cached     | 5.57249 |       ms  |
|               90th percentile latency   |      country_agg_cached     | 6.47982 |       ms  |
|               99th percentile latency   |      country_agg_cached     | 9.33674 |       ms  |
|             99.9th percentile latency   |      country_agg_cached     | 27.5319 |       ms  |
|              100th percentile latency   |      country_agg_cached     | 32.0567 |       ms  |
|          50th percentile service time   |      country_agg_cached     | 5.4601  |       ms  |
|          90th percentile service time   |      country_agg_cached     | 6.25153 |       ms  |
|          99th percentile service time   |      country_agg_cached     | 7.83564 |       ms  |
|        99.9th percentile service time   |      country_agg_cached     | 13.6439 |       ms  |
|         100th percentile service time   |      country_agg_cached     | 31.9487 |       ms  |
|                            error rate   |      country_agg_cached     | 0 |        %  |
|                        Min Throughput   |                  scroll     | 25.01 |  pages/s  |
|                     Median Throughput   |                  scroll     | 25.03 |  pages/s  |
