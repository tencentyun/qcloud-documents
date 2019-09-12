## 环境依赖

- [HADOOP-COS](https://github.com/tencentyun/hadoop-cos) 与 Hadoop-COS-Java-SDK（包含在 HADOOP-COS 的 dep 目录下）。
- Druid 版本：Druid-0.12.1。

## 下载与安装

#### 获取 HADOOP-COS 

在官方 Github 上下载 [HADOOP-COS](https://github.com/tencentyun/hadoop-cos)。

#### 安装 HADOOP-COS
Druid 使用 COS 作为 Deep Storage，需要借助 Druid-hdfs-extension 实现：
下载 HADOOP-COS 后，将 dep 目录下的`hadoop-cos-2.x.x.jar`以及`cos_hadoop_api-5.2.6.jar`拷贝到 Druid 安装路径`extensions/druid-hdfs-storage`以及`hadoop-dependencies/hadoop-client/2.x.x`下。


## 使用方法
#### 配置修改

1. 修改 Druid 安装路径的`conf/druid/_common/common.runtime.properties`文件，将 hdfs 的 extension 加入到`druid.extensions.loadList`中，同时指定 hdfs 为 Druid 的 deep storage，而路径则填写为 cosn 的路径：
```shell
properties
druid.extensions.loadList=["druid-hdfs-storage"]
druid.storage.type=hdfs
druid.storage.storageDirectory=cosn://bucket-appid/<druid-path>
```
2. 在`conf/druid/_common/`这个目录下，新建一个 hdfs 的配置文件 hdfs-site.xml，填入 COS 的密钥信息等：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<!--
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License. See accompanying LICENSE file.
-->
<!-- Put site-specific property overrides in this file. -->
<configuration>
    <property>
        <name>fs.cosn.userinfo.secretId</name>
        <value>xxxxxxxxxxxxxxxxxxxxxxx</value>
    </property>
    <property>
        <name>fs.cosn.userinfo.secretKey</name>
        <value>xxxxxxxxxxxxxxx</value>
    </property>
    <property>
        <name>fs.cosn.impl</name>
        <value>org.apache.hadoop.fs.CosFileSystem</value>
    </property>
    <property>
        <name>fs.cosn.userinfo.region</name>
        <value>ap-xxxx</value>
    </property>
    <property>
        <name>fs.cosn.tmp.dir</name>
        <value>/tmp/hadoop_cos</value>
    </property>
</configuration>
```

上述配置的支持项与 HADOOP-COS 官网文档描述完全一致，详情请查见 [Hadoop 工具](https://cloud.tencent.com/document/product/436/6884) 文档。

#### 开始使用

依次启动 Druid 进程，Druid 数据就可加载到 COS 中。
