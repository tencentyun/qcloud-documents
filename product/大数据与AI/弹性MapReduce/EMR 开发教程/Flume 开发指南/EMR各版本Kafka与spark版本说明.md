### 依赖关系
>! Spark 从2.3 起不再支持 Kafka0.8.2，EMR 现网版本已集成 Spark2.4.3及以上版本，需要集成 kafka 0.10.0及更高版本。
>

| EMR 版本 | Spark | Kafka               | maven example                   |
| ------- | ----- | ------------------- | ------------------------------- |
| v1.3.1  | 2.0.2 | 0.8.2.1 or higher | spark-streaming-kafka-0-8_2.11  |
| v2.0.1  | 2.2.1 | 0.8.2.1 or higher | spark-streaming-kafka-0-8_2.11  |
| v2.1.0  | 2.3.2 | 0.10.0 or higher  | spark-streaming-kafka-0-10_2.11 |
| v3.0.0  | 2.4.3 | 0.10.0 or higher  | spark-streaming-kafka-0-10_2.12 |

### 查找方法
1. 访问官网链接，输入版本号链接模板：
```
https://spark.apache.org/docs/{spark.version}/streaming-kafka-integration.html
```
将 `{spark.version}` 替换为对应的 Spark 版本。例如查看3.2.2版本的依赖关系，访问链接如下：
```
https://spark.apache.org/docs/3.2.2/streaming-kafka-integration.html
```
2. 单击相应链接可看到详细集成说明。
![](https://qcloudimg.tencent-cloud.cn/raw/652cc1ceb647278672314c2a552c316a.png)
