## 功能介绍
EMR 容器版集群支持在控制台提交 Spark 作业，查看作业信息。
>! 提交作业的文件格式为 yaml，大小10M 以内。

## 操作步骤
1. 登录 [EMR 容器版控制台](https://console.cloud.tencent.com/emr/static/containerdeploy)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击**作业管理**，即可进行相关作业提交和查询。
3. EMR 支持 CRD 方式提交作业，用户编写 yaml 作业文件后，由控制台进行作业提交。
4. 单击作业列表上方的**提交作业**，打开提交作业弹框。选择需要提交的作业文件，单击**确认**后，即可提交作业。
![](https://qcloudimg.tencent-cloud.cn/raw/6c24bc7f507a3b713fbac4fcfe1ecacc.png)
5. 单击作业列表中的**详情**，可跳转 Spark Historyserver UI 链接查看作业详情。
6. 单击作业列表中的**删除**，打开删除弹框。在删除作业页面，确认需要删除的作业信息，确认无误后，单击**确定**，即可删除作业。

## 作业示例
通过 CRD 方式提交 Spark 作业的一般流程如下：
1. 编写 Spark 程序。
2. 编译打成 jar 包，将 jar 包放到 cos 或者 hdfs 等文件系统，或编写 Dockerfile 将 Spark 程序 jar 包打到镜像。
3. 编写 yaml 文件，在控制台进行提交。

下面将给出4种 Spark 作业示例：
### 示例1. 使用 Spark 官方 jar 包
新建 yaml 作业文件示例内容如下：
```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: test1
spec:
  hadoopConf:
    "fs.cosn.userinfo.secretId":"$SecretId"
    "fs.cosn.userinfo.secretKey":"$SecretKey" 
  type: Scala
  mode: cluster
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///opt/spark/examples/jars/spark-examples_2.12-3.2.0.jar"
```
本文示例中的参数描述，请参见 [sparkoperator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/v1beta2-1.2.0-3.0.0/docs/api-docs.md) 。其中：
- apiVersion 和 kind 为 k8s 中资源种类和版本，此处不能更改。
- Metadata.name 定义作业名称，本文以 test1为例，用户可以自定义。
- Spec.hadoopConf 定义与 hadoop 相关配置信息，与 cos 交互需要配置密钥信息，可通过 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取密钥信息，代码中的 `$SecretId`、`$Secretkey` 需要替换成业务对应的 SecretId 和 Secretkey。
- type 定义 spark 的程序种类，包括 Java、Scala、Python、R。本文以 Scala 为例，您可根据需要选填。
- mode 定义 sparkApplication 的部署模式，包括 cluster 和 client。本文以 cluster 为例，您可根据需要选填。
- driver 和 executor 分别定义 spark 的驱动器和执行器，由后台自动生成，其默认参数如下： 
```
driver:
  cores: 1
  memory: 512m
executor:
  cores: 1
  instances: 2
  memory: 512m

```
用户可以自定义 driver 和 executor 参数，补充在 yaml 作业文件示例1中，此时自定义参数会覆盖默认参数，示例如下：
```
driver:
    cores: 1
    coreLimit: "1200m"
    memory: "512m"
  executor:
    cores: 1
    instances: 1
    memory: "512m"
```

### 示例2. 自行编译打包并将 jar 包放到 cos（推荐）
以下示例演示用户编写 spark 程序，打 jar 包，编写 yaml 作业进行提交的完整流程。
1. 开发准备
因为任务中需要访问腾讯云对象存储（COS），所以需要在 COS 中存在一个存储桶（Bucket），该存储桶可以是创建集群时的存储桶，也可以创建新的存储桶（需与创建集群时选择的存储桶位于同一地域）。
2. 使用 Maven 创建工程
在本次演示中，自己建立工程编译打包之后上传。推荐您使用 Maven 来管理您的工程。Maven 是一个项目管理工具，能够帮助您方便的管理项目的依赖信息。
3. 编写 wordcount 程序，添加样例代码：
```
import java.util.Arrays;
import java.util.regex.Pattern;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;

public class WordCountOnCos {
    private static final Pattern SPACE = Pattern.compile(" ");
    public static void main(String[] args){
        if (args.length < 1) {
            System.err.println("Usage: JavaWordCount <file>");
            System.exit(1);
        }
        SparkSession spark = SparkSession.builder().appName("wordCountOnCos").getOrCreate();
        JavaRDD<String> lines = spark.read().textFile(args[0]).javaRDD();
        JavaRDD<String> words = lines.flatMap(s -> Arrays.<String>asList(SPACE.split(s)).iterator());
        JavaPairRDD<String, Integer> ones = words.mapToPair(s -> new Tuple2(s, Integer.valueOf(1)));
        JavaPairRDD<String, Integer> counts = ones.reduceByKey((i1, i2) -> Integer.valueOf(i1.intValue() + i2.intValue()));
        counts.saveAsTextFile(args[1]);
        spark.stop();
    }
}
```
4. 执行 mvn package 命令对整个工程进行打包。
5. 将 jar 包上传到 cos 桶，编写 yaml 文件如下：
```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: test2
spec:
  hadoopConf:
    "fs.cosn.userinfo.secretId":"$SecretId"
    "fs.cosn.userinfo.secretKey":"$SecretKey" 
  type: Java
  mode: cluster
  mainClass: com.tencent.WordCountOnCos
  mainApplicationFile: "cosn://kt-test-251007880/sparkapp/jar/wordcount.jar"
  arguments:
    - "cosn://kt-test-251007880/sparkapp/input/input"
    - "cosn://kt-test-251007880/sparkapp/output"

```
其中 arguments 是传递给主类的参数，本例中表示 wordcount 程序的输入和输出目录。本文中 mainApplicationFile 和 wordcount 程序的输入和输出目录为示例，用户可以自定义。

### 示例3. 自行编译打包并将 jar 包放到 HDFS 
用户编写 spark 程序，打 jar 包同示例2，然后将 jar 包上传到 HDFS，编写 yaml 文件如下：
```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: test3
spec:
  hadoopConf:
    "fs.cosn.userinfo.secretId":"$SecretId"
    "fs.cosn.userinfo.secretKey":"$SecretKey" 
  type: Java
  mode: cluster
  mainClass: com.tencent.WordCountOnCos
  mainApplicationFile: "hdfs://$ip:$port/sparkapp/jar/wordcount.jar"
  arguments:
    - "cosn://kt-test-251007880/sparkapp/input/input"
    - "hdfs://$ip:$port/sparkapp/output"

```
>! 若使用 HFDS 存放 jar 包，HDFS 需要和容器集群位于同一 VPC。

### 示例4. 自行编译打包并将 jar 包打到镜像
用户编写 spark 程序，打 jar 包同示例2，然后建立 Dockerfile 如下：
```
FROM ccr.ccs.tencentyun.com/emr-image/spark:BaseImage
USER root
RUN mkdir -p /sparkapp
COPY jars/wordcount.jar /sparkapp
ENTRYPOINT [ "/opt/entrypoint.sh" ]
```
需要继承基础镜像 `ccr.ccs.tencentyun.com/emr-image/spark:BaseImage`，该镜像包含了与 cos 交互所需要的 jar 包。
```
docker build -t ccr.ccs.tencentyun.com/emr-image/spark:wc -f ./bin/Dockerfile .
```
编写作业 yaml 如下：
```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: test4
spec:
  hadoopConf:
    "fs.cosn.userinfo.secretId":"$SecretId"
    "fs.cosn.userinfo.secretKey":"$SecretKey" 
  type: Java
  mode: cluster
  mainClass: com.tencent.WordCountOnCos
  image: ccr.ccs.tencentyun.com/emr-image/spark:wc
  mainApplicationFile: "local:///sparkapp/wordcount.jar"
  arguments:
    - "cosn://kt-test-251007880/sparkapp/input/input"
    - "cosn://kt-test-251007880/sparkapp/output"
```
其中 image 为您打包的镜像，mainApplicationFile 是 jar 包在镜像中的路径。







