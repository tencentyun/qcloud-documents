## 环境依赖

- [CHDFS_JAR](https://github.com/tencentyun/chdfs-hadoop-plugin)。
- Druid 版本：Druid-0.12.1。

## 下载与安装

#### 获取 CHDFS JAR

在官方 Github 上下载 [CHDFS_JAR](https://github.com/tencentyun/chdfs-hadoop-plugin)。

#### 安装 CHDFS JAR

使用 CHDFS 作为 Druid 的 Deep Storage，需要借助 Druid-hdfs-extension 实现。
下载 CHDFS JAR 后，将`chdfs_hadoop_plugin_network-1.7.jar`拷贝到 Druid 安装路径`extensions/druid-hdfs-storage`以及`hadoop-dependencies/hadoop-client/2.x.x`下。

## 使用方法

#### 配置修改

1. 修改 Druid 安装路径的`conf/druid/_common/common.runtime.properties`文件，将 hdfs 的 extension 加入到`druid.extensions.loadList`中，同时指定 hdfs 为 Druid 的 deep storage，而路径则填写为 CHDFS 的路径：
```plaintext
properties
druid.extensions.loadList=["druid-hdfs-storage"]
druid.storage.type=hdfs
druid.storage.storageDirectory=ofs://<mountpoint>/<druid-path>
```
2. 在`conf/druid/_common/`这个目录下，新建一个 hdfs 的配置文件 hdfs-site.xml，填入 CHDFS 的配置信息等：
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
    <name>fs.AbstractFileSystem.ofs.impl</name>
    <value>com.qcloud.chdfs.fs.CHDFSDelegateFSAdapter</value>
 </property>
 <property>
    <name>fs.ofs.impl</name>
    <value>com.qcloud.chdfs.fs.CHDFSHadoopFileSystemAdapter</value>
 </property>
 <!--本地 cache 的临时目录, 对于读写数据, 当内存 cache 不足时会写入本地硬盘, 这个路径若不存在会自动创建-->
 <property>
    <name>fs.ofs.tmp.cache.dir</name>
    <value>/data/chdfs_tmp_cache</value>
 </property>
 <!--appId 用户需要换成自己的 appid，可前往 https://console.cloud.tencent.com/cam/capi 获取-->      
 <property>
    <name>fs.ofs.user.appid</name>
    <value>125000001</value>
 </property>
</configuration>
```
上述配置的支持项与 CHDFS 官网文档描述完全一致，详情可参见 [挂载 CHDFS](https://cloud.tencent.com/document/product/1105/36368) 文档。

#### 开始使用
依次启动 Druid 进程，Druid 数据就可加载到 CHDFS 中。

