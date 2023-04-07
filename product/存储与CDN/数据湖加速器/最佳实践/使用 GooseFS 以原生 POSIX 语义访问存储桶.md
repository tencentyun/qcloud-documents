## 背景

对象存储服务通过 [元数据加速能力](https://cloud.tencent.com/document/product/436/56971) 提供了原生的 POSIX 语义接口，支持用户通过文件系统语义访问对象存储服务，提供原生的元数据操作能力。系统设计指标可以达到 Gb 级单链接带宽、10万级 QPS 以及 ms 级延迟。启用元数据加速功能后，可以提升集群对元数据的操作性能，例如 List、Rename 等操作，并且支持原生的 Append、Truncate 操作，可以广泛应用于大数据、高性能计算、机器学习、AI 等场景。

GooseFS 在 GooseFS V1.3+ 版本集成了最新版本的 COSN interface（COSN V8.14+ 版本），支持了原生 POSIX 语义访问对象存储服务。整体的文件读写流程框架如下：

![](https://qcloudimg.tencent-cloud.cn/raw/99e322492b183c88c06b553dbb1fbc9b.png)

区别于原生 COS 协议，通过原生 POSIX 语义访问存储桶具有如下优势：

1.  更全面的 POSIX 语义兼容，提供原生的 Append 、Truncate 操作支持；
2.  更高性能的文件元数据操作，支持 10 万级的List/Rename QPS；
3.  更低延迟的文件数据操作，大数据场景下，能有效降低大文件的读写延迟。

>! GooseFS 暂时不支持通过 Append、Truncate 接口操作对象存储服务，GooseFS-Lite 客户端支持。如有需要，可下载使用。
>

## 前提条件

通过 GooseFS 以原生 POSIX 语义访问对象存储服务的前提条件如下：

1. 在 COS 服务上创建一个存储桶以作为远端存储，操作指引请参见 [控制台快速入门](https://cloud.tencent.com/document/product/436/38484)。
2. 确保您的存储桶已开启元数据加速服务能力，元数据加速能力只能在创建存储桶时开启。可参见 [使用 HDFS 协议访问已开启元数据加速器的存储桶](https://cloud.tencent.com/document/product/436/68700)。
3. 安装 GooseFS V1.3+ 以上版本的 GooseFS 客户端和服务端安装包。可前往 [产品动态](https://cloud.tencent.com/document/product/1424/68331) 下载最新版本的 GooseFS 软件。
 - 安装 GooseFS 前，必须先安装 [Java 8 或者更高的版本](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)。
 - 安装 GooseFS 前，必须先安装 [SSH](https://www.ssh.com/ssh/)，确保能通过 SSH 连接到 LocalHost，并远程登录。
4. 安装完成后，在 `core-site.properties` 文件中修改访问协议的配置，即可通过原生的 POSIX 协议访问指定存储桶。

## 操作步骤


<span id="1"></span>
### 创建存储桶并配置 HDFS 协议

1. 创建 COS 存储桶，并且开启元数据加速器。如下图所示：
![开启元数据加速能力](https://qcloudimg.tencent-cloud.cn/raw/148ce1336e35c53d3f7ef4cd95e2a35c.png)
当存储桶创建完成后，进入存储桶的**文件列表**页面，您可在该页面进行文件上传和下载操作。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bc79bd567aa0c59aa1c2ad9090470247.png)
2. 在左侧菜单栏中，单击**性能配置 > 元数据加速能力**，可以看到元数据加速能力已开启。
如果是第一次创建**需开启元数据加速**的存储桶，需要按照提示进行相应的**授权**操作，单击授权完成后，将自动开启 HDFS 协议，并且看到默认的存储桶挂载点信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8911a046375d13102a5d7faf8084f931.png)
>? 如果提示未找到对应的 HDFS 文件系统，请单击 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们获取帮助。
>
3. 在 HDFS 权限配置栏中，单击**新增权限配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/b1708a946fae9c4722e1c809770ee26b.png)
4. 在 VPC 网络名称列选择计算集群所在的 VPC 网络地址，在节点 IP 地址列填写 VPC 网段下需要放通的 IP 地址或者 IP 段，访问类型选择读写或者只读，配置完成后，单击**保存**即可。
>? HDFS 权限配置与原生 COS 权限体系存在差异。当您使用 HDFS 协议访问时，推荐通过配置 HDFS 权限授权指定 VPC 内机器访问 COS 存储桶，以便获取和原生 HDFS 一致的权限体验。
>


### 下载并安装好 GooseFS

1. 务必按照上方的**前提条件**，安装好对应的 JDK、SSH 以及依赖的 JAR 包。
JAR 包需要放到各节点 classpath 下保证任务启动能正常加载，例如 `$HADOOP_HOME/share/hadoop/common/lib/`下。
2. 可参见 [产品动态](https://cloud.tencent.com/document/product/1424/68331)，从官方仓库下载 GooseFS 安装包到本地。
3. 执行如下命令，对安装包进行解压。
```
$ tar -zxvf goosefs-1.3.0-bin.tar.gz
$ cd goosefs-1.3.0
```
解压后，得到 goosefs-1.3.0，即 GooseFS 的主目录。下文将以 `${GOOSEFS_HOME}` 代指该目录的绝对路径。
4. 在 `${GOOSEFS_HOME}/conf` 的目录下，创建 `conf/goosefs-site.properties` 的配置文件。可以使用内置的配置模板：
```
$ cp conf/goosefs-site.properties.template conf/goosefs-site.properties
```
5. 在配置文件 `conf/goosefs-site.properties` 中，将 `goosefs.master.hostname` 设置为 `localhost`：
```
$ echo  "goosefs.master.hostname=localhost">> conf/goosefs-site.properties
```

### 修改配置文件以支持通过 POSIX 语义访问 COS

1. 在完成 GooseFS 初步安装后，编辑 `core-site.xml` 文件，新增以下基本配置：
>!
>- 建议用户尽量避免在配置中使用永久密钥，采取配置子账号密钥或者临时密钥的方式有助于提升业务安全性。为子账号授权时建议按需授权子账号可执行的操作和资源，避免发生预期外的数据泄露。
>- 如果您一定要使用永久密钥，建议对永久密钥的权限范围进行限制，可通过限制永久密钥的可执行操作、资源范围和条件（访问 IP 等），提升使用安全性。
>
```
<!--账户的 API 密钥信息。可登录 [访问管理控制台](https://console.cloud.tencent.com/capi) 查看云 API 密钥。-->
<!--建议使用子账号密钥或者临时密钥的方式完成配置，提升配置安全性。为子账号授权时建议按需授权子账号可执行的操作和资源-->
<property>
         <name>fs.cosn.userinfo.secretId/secretKey</name>
         <value>AKIDxxxxxxxxxxxxxxxxxxxxx</value>
</property>

<!--cosn 的实现类-->
<property>
         <name>fs.AbstractFileSystem.cosn.impl</name>
         <value>org.apache.hadoop.fs.CosN</value>
</property>

<!--cosn 的实现类-->
<property>
         <name>fs.cosn.impl</name>
         <value>org.apache.hadoop.fs.CosFileSystem</value>
</property>

<!--用户存储桶的地域信息，格式形如 ap-guangzhou-->      
<property>
         <name>fs.cosn.bucket.region</name>
         <value>ap-guangzhou</value>
</property>

<!--本地临时目录，用于存放运行过程中产生的临时文件->      
<property>
         <name>fs.cosn.tmp.dir</name>
         <value>/tmp/hadoop_cos</value>
</property>
```
2. 将 ` core-site.xml` 同步到所有 `hadoop` 节点上。
完成这一步骤后，即可通过 POSIX 语义访问 COS 存储桶。

