## 功能介绍
EMR 容器版集群支持在控制台提交 Spark 作业，查看作业信息。
>!
>1. 提交作业的文件格式为 yaml，大小10M 以内。
>2. 不可重复提交同一份作业。

## 操作步骤
1. 登录 [EMR 容器版控制台](https://console.cloud.tencent.com/emr/static/containerdeploy)，在集群列表中单击对应的集群 **ID/名称**进入集群详情页。
2. 在集群详情页中单击**作业管理**，即可进行相关作业查询。
3. EMR 支持 CRD 方式提交作业。

>? 通过 CRD 方式提交 Spark 作业的一般流程如下：
- 编写 Spark 程序；
- 编译打包，编写 Dockerfile 将 Spark 程序打成镜像；
- 编写 yaml 文件，在控制台进行提交。

新建 spark-pi.yaml 文 件，文件示例内容如下：
```
apiVersion: "sparkoperator.k8s.io/v1beta2"
kind: SparkApplication
metadata:
  name: testspark
  namespace: emrtest
spec:
  type: Scala
  mode: cluster
  image: "spark:3.2.0"
  imagePullPolicy: IfNotPresent
  mainClass: org.apache.spark.examples.SparkPi
  mainApplicationFile: "local:///opt/spark/examples/jars/spark-examples_2.12-3.2.0.jar"
  sparkVersion: "3.2.0"
  restartPolicy:
    type: Never
  volumes:
    - name: "test-volume"
      hostPath:
        path: "/tmp"
        type: Directory
  driver:
    cores: 1
    coreLimit: "1200m"
    memory: "512m"
    labels:
      version: 3.2.0
    serviceAccount: spark
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
  executor:
    env:
      - name: "KUBERNETES_REQUEST_TIMEOUT"
        value: "100000"
    cores: 1
    instances: 1
    memory: "512m"
    labels:
      version: 3.2.0
    volumeMounts:
      - name: "test-volume"
        mountPath: "/tmp"
```


本文示例中的参数描述，请参见 [sparkoperator](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/v1beta2-1.2.0-3.0.0/docs/api-docs.md)。示例代码中的集群对应的 namespace 需要替换为集群的名称空间，您可以登录控制台，在集群详情页面查看。

4. 使用 COS 存储 Spark 作业日志。
如果您的作业需要读写 COS，则需要在 hadoopConf 中额外增加 AccessKey 的配置。配置信息如下：
```
<configuration>
    <!-- COS配置 -->
    <property>
        <name>fs.defaultFS</name>
        <value>cosn://xx</value>
        <description>COS bucket name</description>
    </property>
    <property>
        <name>fs.cosn.userinfo.secretId</name>
        <value>xxx</value>
    <description>Tencent Cloud Secret Id</description>
    </property>
    <property>
        <name>fs.cosn.userinfo.secretKey</name>
        <value>xxx</value>
        <description>Tencent Cloud Secret Key</description>
    </property>
    <property>
        <name>fs.cosn.bucket.region</name>
        <value>xxx</value>
        <description>The region where the bucket is located.</description>
    </property>
    <property>
        <name>fs.cosn.impl</name>
        <value>org.apache.hadoop.fs.CosFileSystem</value>
        <description>The implementation class of the CosN Filesystem.</description>
    </property>
    <property>
        <name>fs.AbstractFileSystem.cosn.impl</name>
        <value>org.apache.hadoop.fs.CosN</value>
        <description>The implementation class of the CosN AbstractFileSystem.</description>
    </property>
</configuration>
```

如果需要将 Spark 作业信息存储到 COS，以便在 Spark Historyserver UI 链接查看作业详情，需要在 Spark 作业文件中增加如下参数：

```
sparkConf：
"spark.eventLog.enabled": "true"
"spark.eventLog.dir": "cosn://sparkhistorytest-1258469122"
```
   

5. 单击作业列表上方的**提交作业**，打开提交作业弹框。选择需要提交的作业文件，单击**确认**后，即可提交作业。
![](https://qcloudimg.tencent-cloud.cn/raw/a4c32b79d816ea7f65ac0e800b2c915c.png)
6. 单击作业列表中的**详情**，可跳转 Spark Historyserver UI 链接查看作业详情。


