本文将为您介绍如何使用 Skywalking 进行Java 应用采集配置。

## 操作背景

在访问量较大时，全链路数据上报可能会导致使用应用性能观测的成本较高。在访问量级较大的情况下，往往会进行数据采样。
<dx-alert infotype="explain" title="">
采样指从全量采集的所有链路数据中，采集部分数据进行分析，减少上报数量和链路存储费用，降低使用应用性能观测的成本。
</dx-alert>

## 操作前提
已 [通过 Skywalking 协议上报 Java 应用](https://cloud.tencent.com/document/product/1463/57870)。

## 操作步骤

1. 打开 agent/config/agent.config 文件，找到 `agent.sample_n_per_3_secs=${SW_AGENT_SAMPLE:-1}` 配置项。
![](https://qcloudimg.tencent-cloud.cn/raw/71f2f5691677913a07b36e20e499406a.png)
2. 修改采样率。**`agent.sample_n_per_3_secs ` 表示设置每 3 秒可收集的链路数据（TraceSegment）的数量。负或零表示全部采样，默认全部采样。**

**示例：**

假设您需要在3秒内采集1500个 TraceSegment ，可以设置为：
```
agent.sample_n_per_3_secs=${SW_AGENT_SAMPLE:1500}
```


