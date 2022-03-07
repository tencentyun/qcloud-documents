## 操作场景

该任务指导您在购买 CKafka 服务后，使用 Kafka API。在腾讯云服务器上搭建 CKafka 环境后，本地下载并解压 Kafka 工具包，并对 Kafka API 进行简单测试。

## 操作步骤

### 步骤1：安装 JDK 环境

#### 1. 检查 Java 安装。

打开终端，执行如下命令：

```
java -version
```

如果输出 Java 版本号，说明 Java 安装成功；如果没有安装 Java，请 [下载安装 Java 软件开发套件（JDK）](http://kafka.apache.org/downloads)。


#### 2. 设置 Java 环境。

设置 `JAVA_HOME` 环境变量，并指向您机器上的 Java 安装目录。 
以 Java JDK 1.8.0_20 版本为例，操作系统的输出如下：

| 操作系统 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| Windows  | Set the environment variable JAVA_HOME to <br/>C:\Program Files\Java\jdkjdk1.8.0_20 |
| Linux    | export JAVA_HOME=/usr/local/java-current                     |
| Mac OSX  | export JAVA_HOME=/Library/Java/Home                          |

 将 Java 编译器地址添加到系统路径中：

| 操作系统 | 输出                                                         |
| -------- | ------------------------------------------------------------ |
| Windows  | 将字符串“;C:\Program Files\Java\jdk1.8.0_20\bin”添加到系统变量“Path”的末尾 |
| Linux    | export PATH=$PATH:$JAVA_HOME/bin/                            |
| Mac OSX  | not required                                                 |

 使用上面提到的 `java -version` 命令验证 Java 安装。

### 步骤2：下载 Kafka 工具包

下载并解压 Kafka 安装包。（[Kafka 安装包官网下载地址>>](http://kafka.apache.org/downloads)）
当前 CKafka 100%兼容 Kafka 0.9、0.10、1.1、2.4版本，建议您下载对应版本的安装包（本文以 kafka_2.12-1.1.1工具包为例）。

### 步骤3：Kafka API 测试

通过 CLI 命令生产和消费消息，去到`./bin`目录下。

1. 打开终端启动消费者。
   ```bash
   bash kafka-console-consumer.sh --bootstrap-server XXXX:port --topic XXXX --consumer.config ../config/consumer.properties
   ```
   >?
   >- 将 XXXX:port 替换成VPC网络访问的域名与端口，在控制台实例详情页面的**接入方式**模块获取。
   >  ![](https://main.qcloudimg.com/raw/88b29cffdf22e3a0309916ea715057a1.png)
   >- topic：将 XXXX替换成topic名称，在控制台**topic管理**页面获取。

2. 另外开一个终端窗口启动生产者。
   ``` bash
   bash kafka-console-producer.sh --broker-list XXXX:port --topic XXXX --producer.config ../config/producer.properties
   ```
   >?
   >- 将 XXXX:port 替换成VPC网络访问的域名与端口，在控制台实例详情页面的**接入方式**模块获取。
   >  ![](https://main.qcloudimg.com/raw/88b29cffdf22e3a0309916ea715057a1.png)
   >- topic：将 XXXX替换成topic名称，在控制台**topic管理**页面获取。

   输入消息内容之后按回车，即可看到消费端也几乎同时收到消息。

   生产消息：
   ![](https://main.qcloudimg.com/raw/c25bdccd293ea4382064b57eec08a2fe.png)

   消费消息：
   ![](https://main.qcloudimg.com/raw/22860d730e70cfbe9eb5fcbca215d5a5.png)

3. 在 CKafka 控制台消息查询页面，查询刚刚发送的消息内容。
   ![](https://main.qcloudimg.com/raw/cca4f62e86898eec49d8a9cde7ae9fa8.png)
    消息详情如下：
   ![](https://main.qcloudimg.com/raw/43b60e402b829faab71152274a097126.png)
