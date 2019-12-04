### 依赖关系

| EMR 版本 | Spark | Kafka               | maven example                   |
| ------- | ----- | ------------------- | ------------------------------- |
| v1.3.1  | 2.0.2 | 0.8.2.1 or   higher | spark-streaming-kafka-0-8_2.11  |
| v2.0.1  | 2.2.1 | 0.8.2.1 or   higher | spark-streaming-kafka-0-8_2.11  |
| v2.1.0  | 2.3.2 | 0.10.0 or   higher  | spark-streaming-kafka-0-10_2.11 |
| v3.0.0  | 2.4.3 | 0.10.0 or   higher  | spark-streaming-kafka-0-10_2.12 |

>!从 Spark2.3 起不再支持 Kafka0.8.2。

### 查找方法

1. 访问官网链接，输入版本号链接模板：
```
https://spark.apache.org/docs/{spark.version}/streaming-kafka-integration.html
```
将`{spark.version}`替换为对应的 Spark 版本。例如查看2.0.2版本的依赖关系，访问链接如下：
```
https://spark.apache.org/docs/2.0.2/streaming-kafka-integration.html
```
2. 查看依赖，单击相应链接可看到详细说明。
![](https://main.qcloudimg.com/raw/490029cb98805a5c1a861adbc1ec2f70.png)
