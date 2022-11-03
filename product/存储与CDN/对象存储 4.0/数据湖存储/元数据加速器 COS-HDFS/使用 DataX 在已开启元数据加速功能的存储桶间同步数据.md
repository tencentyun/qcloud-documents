## 简介

DataX 是开源异构数据源离线同步工具，实现了包括 MySQL、SQL Server、Oracle、PostgreSQL、HDFS、Hive、HBase、OTS、ODPS 等各种异构数据源之间高效的数据同步功能。

已开启元数据加速功能的 COS 存储桶可以为业务提供 HCFS（Hadoop Compatible File System）语义访问，充当 Hadoop 系统中的 HDFS 服务的作用。

本文将介绍如何使用 DataX 在两个开启了元数据加速功能的存储桶之间同步数据。

## 环境依赖

- [HADOOP-COS](https://github.com/tencentyun/hadoop-cos/releases) 与对应版本的 [cos_api-bundle](https://github.com/tencentyun/hadoop-cos/releases)。
- DataX 版本：[DataX-3.0](https://github.com/alibaba/DataX)。

## 下载与安装

#### 获取 HADOOP-COS

- 在官方 Github 上下载 [HADOOP-COS](https://github.com/tencentyun/hadoop-cos/releases) 与对应版本的 [cos_api-bundle](https://github.com/tencentyun/hadoop-cos/releases)。
- 在官方 Github 上下载 [chdfs-hadoop-plugin](https://github.com/tencentyun/chdfs-hadoop-plugin)。

#### 获取 DataX 软件包

在官方 Github 上下载 [DataX](https://github.com/alibaba/DataX)。

#### 安装 HADOOP-COS

下载 HADOOP-COS 后，将 `hadoop-cos-2.x.x-${version}.jar` 、 `cos_api-bundle-${version}.jar` 和 `chdfs_hadoop_plugin_network-${version}.jar` 这三个 jar 包分别拷贝到 Datax 解压路径 `plugin/reader/hdfsreader/libs/` 和 `plugin/writer/hdfswriter/libs/` 下。

## 使用方法

### 存储桶配置

进入已开启元数据加速功能的存储桶，在 **HDFS 权限配置**中，配置运行 DataX 机器的 VPC 网络。
>? 数据源存储桶至少需要允许该 VPC 内的读请求，数据写入目标存储桶至少需要允许该 VPC 内的写请求。

![](https://qcloudimg.tencent-cloud.cn/raw/2628f6f8b58abdb5566c2a464a3c3a3a.png)

### DataX 配置

#### 1. 修改 datax.py 脚本

打开 DataX 解压目录下的 bin/datax.py 脚本，修改脚本中的 CLASS_PATH 变量为如下：

```plaintext
CLASS_PATH = ("%s/lib/*:%s/plugin/reader/hdfsreader/libs/*:%s/plugin/writer/hdfswriter/libs/*:.") % (DATAX_HOME, DATAX_HOME, DATAX_HOME)
```

#### 2. 在配置 JSON 文件里配置 hdfsreader 和 hdfswriter

示例 JSON 如下：
```json
{
  "job": {
  "setting": {
    "speed": {
      "byte": 10485760
    },
    "errorLimit": {
      "record": 0,
      "percentage": 0.02
    }
  },
  "content": [{
    "reader": {
      "name": "hdfsreader",
      "parameter": {
        "path": "/test/",
        "defaultFS": "cosn://examplebucket1-1250000000/",
        "column": ["*"],
        "fileType": "text",
        "encoding": "UTF-8",
        "hadoopConfig": {
          "fs.cosn.impl": "org.apache.hadoop.fs.CosFileSystem",
          "fs.cosn.trsf.fs.ofs.bucket.region": "ap-guangzhou",
          "fs.cosn.bucket.region": "ap-guangzhou",
          "fs.cosn.tmp.dir": "/tmp/hadoop_cos",
          "fs.cosn.trsf.fs.ofs.tmp.cache.dir": "/tmp/",
          "fs.cosn.userinfo.secretId": "COS_SECRETID",
          "fs.cosn.userinfo.secretKey": "COS_SECRETKEY",
          "fs.cosn.trsf.fs.ofs.user.appid": "1250000000"
        },
        "fieldDelimiter": ","
      }
    },
    "writer": {
      "name": "hdfswriter",
      "parameter": {
        "path": "/",
        "fileName": "hive.test",
        "defaultFS": "cosn://examplebucket2-1250000000/",
        "column": [
          {"name":"col1","type":"int"},
          {"name":"col2","type":"string"}
        ],
        "fileType": "text",
        "encoding": "UTF-8",
        "hadoopConfig": {
          "fs.cosn.impl": "org.apache.hadoop.fs.CosFileSystem",
          "fs.cosn.trsf.fs.ofs.bucket.region": "ap-guangzhou",
          "fs.cosn.bucket.region": "ap-guangzhou",
          "fs.cosn.tmp.dir": "/tmp/hadoop_cos",
          "fs.cosn.trsf.fs.ofs.tmp.cache.dir": "/tmp/",
          "fs.cosn.userinfo.secretId": "COS_SECRETID",
          "fs.cosn.userinfo.secretKey": "COS_SECRETKEY",
          "fs.cosn.trsf.fs.ofs.user.appid": "1250000000"
        },
        "fieldDelimiter": ",",
        "writeMode": "append"
      }
    }
  }]
 }
}
```

配置说明如下：
- hadoopConfig 配置为 cosn 所需要的配置。
- defaultFS 填写为 cosn 的路径，例如 `cosn://examplebucket-1250000000/`。
- fs.cosn.userinfo.region 和 fs.cosn.trsf.fs.ofs.bucket.region 修改为存储桶所在的地域，例如 `ap-guangzhou`，详情请参见 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224)。
- COS_SECRETID 和 COS_SECRETKEY 修改为 COS 密钥。
- fs.ofs.user.appid 和 fs.cosn.trsf.fs.ofs.user.appid 修改为用户 appid。

>!
>fs.cosn.trsf.fs.ofs.bucket.region 和 fs.cosn.trsf.fs.ofs.user.appid 在 hadoop-cos 8.1.7及以上版本中已去除，使用时请注意版本差异。其他配置请参考 HDFS [reader](https://github.com/alibaba/DataX/blob/master/hdfsreader/doc/hdfsreader.md)、[writer](https://github.com/alibaba/DataX/blob/master/hdfswriter/doc/hdfswriter.md) 配置项。

### 执行数据迁移

将配置文件保存为 hdfs_job.json 文件，存放到 job 目录下，并执行以下命令行：

```bash
[root@172 /usr/local/service/datax]# python bin/datax.py job/hdfs_job.json 
```

观察屏幕正常输出如下：

```plaintext
2022-10-23 00:25:24.954 [job-0] INFO  JobContainer - 
         [total cpu info] => 
                averageCpu                     | maxDeltaCpu                    | minDeltaCpu                    
                -1.00%                         | -1.00%                         | -1.00%
                        
         [total gc info] => 
                 NAME                 | totalGCCount       | maxDeltaGCCount    | minDeltaGCCount    | totalGCTime        | maxDeltaGCTime     | minDeltaGCTime     
                 PS MarkSweep         | 1                  | 1                  | 1                  | 0.034s             | 0.034s             | 0.034s             
                 PS Scavenge          | 14                 | 14                 | 14                 | 0.059s             | 0.059s             | 0.059s             
2022-10-23 00:25:24.954 [job-0] INFO  JobContainer - PerfTrace not enable!
2022-10-23 00:25:24.954 [job-0] INFO  StandAloneJobContainerCommunicator - Total 1000003 records, 9322478 bytes | Speed 910.40KB/s, 100000 records/s | Error 0 records, 0 bytes |  All Task WaitWriterTime 1.000s |  All Task WaitReaderTime 6.259s | Percentage 100.00%
2022-10-23 00:25:24.955 [job-0] INFO  JobContainer - 
任务启动时刻                    : 2022-10-23 00:25:12
任务结束时刻                    : 2022-10-23 00:25:24
任务总计耗时                    :                 12s
任务平均流量                    :          910.40KB/s
记录写入速度                    :         100000rec/s
读出记录总数                    :             1000003
读写失败总数                    :                   0
```

## 使用 Ranger 和 Kerberos 场景下

在 Hadoop 权限体系中，认证由 Kerberos 提供，授权鉴权由 Ranger 负责。开启了 Ranger 和 Kerberos 后，使用 DataX 对接已开启元数据加速功能的存储桶的步骤大致和上述步骤一样，但有一些需要额外进行操作和配置。

1. 已开启元数据加速功能的存储桶支持腾讯云大数据权限管控方案 [COS Ranger Service](https://cloud.tencent.com/document/product/436/80261) （在 EMR 控制台购买 Ranger 和 cosranger 组件时会自动安装；如果自行安装，可参考 [CHDFS Ranger 权限体系解决方案](https://cloud.tencent.com/document/product/1105/53307)）。
2. 将 `cosn-ranger-interface-1.x.x-${version}.jar` 和 `hadoop-ranger-client-for-hadoop-${version}.jar` 这两个 jar 包拷贝到 Datax 解压路径 `plugin/reader/hdfsreader/libs/` 和 `plugin/writer/hdfswriter/libs/` 下。[单击前往 Github 下载](https://github.com/tencentyun/cos-ranger-service)
3. 进入已开启元数据加速功能的存储桶，在 **HDFS 鉴权模式**中，选择 **Ranger 鉴权**，配置 Ranger 地址（非 COS Ranger 地址）
![](https://qcloudimg.tencent-cloud.cn/raw/3c46123a755f685eaaf1f05a5ae05434.png)
4. 在 JSON 配置文件里配置 hdfsreader 和 hdfswriter。
```json
{
  "job": {
  "setting": {
    "speed": {
      "byte": 10485760
    },
    "errorLimit": {
      "record": 0,
      "percentage": 0.02
    }
  },
  "content": [{
    "reader": {
      "name": "hdfsreader",
      "parameter": {
        "path": "/test/",
        "defaultFS": "cosn://examplebucket1-1250000000/",
        "column": ["*"],
        "fileType": "text",
        "encoding": "UTF-8",
        "hadoopConfig": {
          "fs.cosn.impl": "org.apache.hadoop.fs.CosFileSystem",
          "fs.cosn.trsf.fs.ofs.bucket.region": "ap-guangzhou",
          "fs.cosn.bucket.region": "ap-guangzhou",
          "fs.cosn.tmp.dir": "/tmp/hadoop_cos",
          "fs.cosn.trsf.fs.ofs.tmp.cache.dir": "/tmp/",
          "fs.cosn.trsf.fs.ofs.user.appid": "1250000000",
          "fs.cosn.credentials.provider": "org.apache.hadoop.fs.auth.RangerCredentialsProvider",
          "qcloud.object.storage.zk.address": "172.16.0.30:2181",
          "qcloud.object.storage.ranger.service.address": "172.16.0.30:9999",
          "qcloud.object.storage.kerberos.principal": "hadoop/172.16.0.30@EMR-5IUR9VWW"
        },
        "haveKerberos": "true",
        "kerberosKeytabFilePath": "/var/krb5kdc/emr.keytab",
        "kerberosPrincipal": "hadoop/172.16.0.30@EMR-5IUR9VWW",
        "fieldDelimiter": ","
      }
    },
    "writer": {
      "name": "hdfswriter",
      "parameter": {
        "path": "/",
        "fileName": "hive.test",
        "defaultFS": "cosn://examplebucket2-1250000000/",
        "column": [
          {"name":"col1","type":"int"},
          {"name":"col2","type":"string"}
        ],
        "fileType": "text",
        "encoding": "UTF-8",
        "hadoopConfig": {
          "fs.cosn.impl": "org.apache.hadoop.fs.CosFileSystem",
          "fs.cosn.trsf.fs.ofs.bucket.region": "ap-guangzhou",
          "fs.cosn.bucket.region": "ap-guangzhou",
          "fs.cosn.tmp.dir": "/tmp/hadoop_cos",
          "fs.cosn.trsf.fs.ofs.tmp.cache.dir": "/tmp/",
          "fs.cosn.trsf.fs.ofs.user.appid": "1250000000",
          "fs.cosn.credentials.provider": "org.apache.hadoop.fs.auth.RangerCredentialsProvider",
          "qcloud.object.storage.zk.address": "172.16.0.30:2181",
          "qcloud.object.storage.ranger.service.address": "172.16.0.30:9999",
          "qcloud.object.storage.kerberos.principal": "hadoop/172.16.0.30@EMR-5IUR9VWW"
        },
        "haveKerberos": "true",
        "kerberosKeytabFilePath": "/var/krb5kdc/emr.keytab",
        "kerberosPrincipal": "hadoop/172.16.0.30@EMR-5IUR9VWW",
        "fieldDelimiter": ",",
        "writeMode": "append"
      }
    }
  }]
 }
}
```

新增配置说明如下：

- fs.cosn.credentials.provider 配置为 org.apache.hadoop.fs.auth.RangerCredentialsProvider ，使用 Ranger 鉴权。
- qcloud.object.storage.zk.address 配置 ZOOKEEPER 地址。
- qcloud.object.storage.ranger.service.address 配置 COS Ranger 地址。
- haveKerberos 配置为 true。
- qcloud.object.storage.kerberos.principal 和 kerberosPrincipal 配置为 Kerberos 认证 Principal 名（在开启了 kerboros 的 emr 环境中可从 core-site.xml 读取）。
- kerberosKeytabFilePath 配置为 keytab 认证文件的绝对路径（在开启了 kerboros 的 emr 环境中可从 ranger-admin-site.xml 读取）。

## 常见问题

### **报错 java.io.IOException: Permission denied: no access groups bound to this mountPoint examplebucket2-1250000000, access denied 或者 java.io.IOException: Permission denied: No access rules matched**，该如何处理？

检查存储桶的 **HDFS 权限配置**中的 VPC 网络配置，配置好运行机器的 ip 地址或网段，例如 emr 需要配置所有节点的 ip 地址。

### **报错 java. lang. RuntimeException: java. lang.ClassNotFoundException: Class org.apache.hadoop.fs.con.ranger.client.RangerQcloudObjectStorageClientImpl not found**，该如何处理？

检查是否将 `cosn-ranger-interface-1.x.x-${version}.jar` 和 `hadoop-ranger-client-for-hadoop-${version}.jar` 拷贝到 Datax 解压路径 `plugin/reader/hdfsreader/libs/` 以及 `plugin/writer/hdfswriter/libs/`  下。[单击前往 Github 下载](https://github.com/tencentyun/cos-ranger-service)

### **报错 java.io.IOException: Login failure for hadoop/_HOST@EMR-5IUR9VWW from keytab /var/krb5kdc/emr.keytab: javax.security.auth.login.LoginException: Unable to obtain password from user**，该如何处理？

检查 kerberosPrincipal 和 qcloud.object.storage.kerberos.principal 项，是否将 hadoop/172.16.0.30@EMR-5IUR9VWW 错误地设置为 `hadoop/_HOST@EMR-5IUR9VWW`。因为 datax 并不能解析 `_HOST` 域名，所以需要将 `_HOST` 换成 ip。可以使用 `klist -ket /var/krb5kdc/emr.keytab` 命令来查找合适的 Principal。

### **报错 java.io.IOException: init fs.cosn.ranger.plugin.client.impl failed**，该如何处理？

检查 json 文件中的 hadoopConfig 项是否没有配置 qcloud.object.storage.kerberos.principal。如是，则需要配置。
