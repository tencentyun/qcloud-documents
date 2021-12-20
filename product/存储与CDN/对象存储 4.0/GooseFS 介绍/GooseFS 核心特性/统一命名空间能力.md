## 统一命名空间能力概述

GooseFS 统一命名空间（NameSpace）能力通过透明的命名机制，可以融合多种不同的底层存储系统访问语义，为用户提供了一个统一的数据管理交互视图。

GooseFS 通过统一命名空间能力对接不同的底层存储系统，如本地文件系统、腾讯云对象存储（Cloud Object Storage，COS）、腾讯云云 HDFS（Cloud HDFS，CHDFS）等，与这些底层存储系统进行通信，并为上层业务提供统一的访问接口和文件协议。业务侧只需使用 GooseFS 的访问接口，即可访问存储在不同底层存储系统中的数据。

![](https://main.qcloudimg.com/raw/6ef8e2899bbd704f7c05c7d0526624b1.png)

上图显示了统一命名空间的工作原理。您可以通过 GooseFS 创建命名空间的指令 create ns ，将 COS 和 云 HDFS 的指定文件目录挂载到 GooseFS 中，然后通过 gfs:// 的这一统一的 schema 访问数据。详细说明如下所示：

- COS 总共有3个存储桶，分别是 bucket-1、bucket-2、bucket-3，其中 bucket-1 有 BU_A 和  BU_B 两个目录，bucket-1 和 bucket-2 均挂载在 GooseFS 中。
- 云 HDFS 中有 BU_E、BU_F、BU_G 和 BU_H 共 4 个目录，其中除了 BU_H 其余目录均挂载到 GooseFS 上。
- 在 GooseFS 的文件操作中，如果以 gfs:// 这一统一的 schema 访问 BU_A 和 BU_E 这两个目录，均可正常访问，且文件缓存在 GooseFS 的本地文件系统中。
-  BU_A 和 BU_E 这两个存储在底层文件系统（COS、云 HDFS）中的目录已经挂载到 GooseFS 中，如果文件已经缓存在 GooseFS 的上，可以通过 gfs:// 这一统一的 schema 访问（例如 hadoop fs ls gfs://BU_A ）；也可以通过各个远端文件系统的命名空间访问（例如 hadoop fs ls cosn://bucket-1/BU_A ）。
- 如果文件未被缓存在 GooseFS 上，此时通过 gfs:// 这一形式访问则会失败，因为文件未被缓存在本地文件系统中，但仍然可以通过底层存储系统的命名空间访问。

## 使用统一命名空间能力

您可以通过 ns 操作在 GooseFS 中创建命名空间，并将底层存储系统映射到 GooseFS 上，目前支持的底层存储系统包括 COS、云 HDFS、本地 HDFS 等。创建命名空间的操作与 Linux 文件系统中挂载文件卷盘类似。创建命名空间后，GooseFS 可以为客户端提供一个具有统一访问语义的文件系统。目前 GooseFS 命名空间的操作指令集如下：

```plaintext
$ goosefs ns
Usage: goosefs ns [generic options]
         [create <namespace> <CosN/Chdfs path> <--wPolicy <1-6>> <--rPolicy <1-5>> [--readonly] [--shared] [--secret fs.cosn.userinfo.secretId=<AKIDxxxxxxx>] [--secret fs.cosn.userinfo.secretKey=<xxxxxxxxxx>] [--attribute fs.ofs.userinfo.appid=1200000000][--attribute fs.cosn.bucket.region=<ap-xxx>/fs.cosn.bucket.endpoint_suffix=<cos.ap-xxx.myqcloud.com>]]
         [delete <namespace>]                                      
         [help [<command>]]                                        
         [ls [-r|--sort=option|--timestamp=option]]                
         [setPolicy [--wPolicy <1-6>] [--rPolicy <1-5>] <namespace>]
         [setTtl [--action delete|free] <namespace> <time to live>]
         [stat <namespace>]                                        
         [unsetPolicy <namespace>]                                 
         [unsetTtl <namespace>] 
```
上述指令集中各项指令的能力简述如下：

| 指令        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| create      | 用于创建命名空间，将一个远端存储系统（UFS）映射到命名空间中；支持在创建命名空间时设置读写缓存策略；需要传入有权限的密钥信息（secretId、secretKey）。 |
| delete      | 用于删除指定命名空间。                                       |
| ls          | 用于列出指定命名空间的详细信息，例如挂载点、UFS 路径、创建时间、缓存策略、TTL 信息等。 |
| setPolicy   | 用于设置指定命名空间的缓存策略。                             |
| setTtl      | 用于设置指定命名空间的 TTL。                                 |
| stat        | 用于提供指定命名空间的描述性信息，例如挂载点、UFS 路径、创建时间、缓存策略、TTL  信息、持久化状态、用户组、ACL、最后一次访问时间、修改时间等。 |
| unsetPolicy | 用于重置指定命名空间的缓存策略。                             |
| unsetTtl    | 用于重置指定命名空间的 TTL。                                 |

### 创建和删除命名空间
通过 GooseFS 创建命名空间操作，可以将频繁访问的热数据从远端存储系统缓存到本地高性能存储节点中，为本地计算业务提供高性能的数据访问。如下指令展示了将 COS 中的存储桶 example-bucket、存储桶中的 example-prefix 目录以及云 HDFS 文件系统分别映射到 test_cos、test_cos_prefix 和 test_chdfs 等命名空间下。

```plaintext
# 将 COS 存储桶 example-bucket 映射到 test_cos 命名空间中
$ goosefs ns create test_cos cosn://example-bucket-1250000000/ --wPolicy 1 --rPolicy 1 --secret fs.cosn.userinfo.secretId=AKIDxxxxxxx --secret fs.cosn.userinfo.secretKey=xxxxxxxxxx --attribute fs.cosn.bucket.region=ap-guangzhou --attribute fs.cosn.bucket.endpoint_suffix=cos.ap-guangzhou.myqcloud.com 

# 将 COS 存储桶 example-bucket 的 example-prefix 目录映射到 test_cos_prefix 命名空间中
$ goosefs ns create test_cos_prefix cosn://example-bucket-1250000000/example-prefix/ --wPolicy 1 --rPolicy 1 --secret fs.cosn.userinfo.secretId=AKIDxxxxxxx --secret fs.cosn.userinfo.secretKey=xxxxxxxxxx --attribute fs.cosn.bucket.region=ap-guangzhou --attribute fs.cosn.bucket.endpoint_suffix=cos.ap-guangzhou.myqcloud.com

# 将 云HDFS 文件系统 f4ma0l3qabc-Xy3 映射到 test_chdfs 命名空间中
$ goosefs ns create test_chdfs ofs://f4ma0l3qabc-Xy3/ --wPolicy 1 --rPolicy 1 --attribute fs.ofs.userinfo.appid=1250000000
```

创建成功后，可以通过 goosefs fs ls 指令查看目录详情：
```plaintext
$ goosefs fs ls /test_cos
```

对于不需要使用的命名空间，可以通过 delete 指令来删除：

```plaintext
$ goosefs ns delete test_cos
Delete the namespace: test_cos
```

### 设置缓存策略
用户可通过 setPolicy 和 unsetPolicy 设置指定命名空间的缓存策略。设置缓存策略的指令集如下：
```plaintext
$goosefs ns setPolicy [--wPolicy <1-6>] [--rPolicy <1-5>] <namespace>
```
其中各项参数的含义如下：
- wPolicy：写缓存策略，支持6种写缓存策略。
- rPolicy：读缓存策略，支持5种读缓存策略。
- namespace：指定的命名空间。

目前 GooseFS 支持的读写缓存策略分别如下：

**写缓存策略**

| 策略名字      | 行为                                                         | 对应 Write_Type | 数据安全性 | 写效率 |
| :------------ | :---------------------------------- | :--------- | :-----  | :-----  |
| MUST_CACHE（1） | 数据仅存储在 GooseFS，不会写入远端存储系统中。 | MUST_CACHE | 不可靠     | 高     |
| TRY_CACHE（2） | 缓存有空间时就写入 GooseFS 中，缓存如果没空间则直接写入到底层存储中。 | TRY_CACHE | 不可靠 | 中 |
| CACHE_THROUGH（3） | 尽量缓存数据，同时同步写入远端存储系统。                    | CACHE_THROUGH | 可靠       | 低    |
| THROUGH（4）       | 数据不存储在 GooseFS，直接写远端存储系统。                   | THROUGH | 可靠       | 中     |
| ASYNC_THROUGH（5） | 数据写入 GooseFS 中，并异步刷新到远端存储系统。                 | ASYNC_THROUGH | 弱可靠     | 高     |

>? Write_Type：指用户调用 SDK 或者 API 向 GooseFS 中写入数据时指定的文件缓存策略，对单个文件生效。
> 

**读缓存策略**

| 策略名字                      | 行为                                                         | 元数据同步 | 对应 Read_Type | 数据一致性 | 读效率                  | 是否缓存数据 |
| :---------------------------- | :----------------------------------------------------------- | :--------- | ------------- | :--------- | :---------------------- | :----------- |
| NO_CACHE（1）                 | 不缓存数据，直接从远端存储系统中读数据。                     | NO         | NO_CACHE      | 强一致     | 低                      | 否           |
| CACHE（2）                    | <li>元数据访问行为：如果命中缓存时，元数据以 Master 中的为准，不会主动从底层同步元数据。</li><li>数据流访问行为：数据流的 ReadType 采用 CACHE 策略。</li> | Once       | CACHE         | 弱一致     | 命中：高<br/>未命中：低 | 是           |
| CACHE_PROMOTE（3）            | <li>元数据访问行为：与 CACHE 模式相同。</li><li>数据流访问行为：数据流的 ReadType 采用 CACHE_PROMOTE 策略。</li> | Once       | CACHE_PROMOTE | 弱一致     | 命中：高<br/>未命中：低 | 是           |
| CACHE_CONSISTENT_PROMOTE（4） | <li>元数据行为：每次读取操作前均先同步远端存储系统 UFS 上的元数据，如果 UFS 中不存在，则抛出异常 Not Exists。</li><li>数据流访问行为：数据流的 ReadType 采用 CACHE_PROMOTE 策略，命中以后，缓存到最热的缓存介质中。</li> | Always     | CACHE         | 强一致     | 命中：中<br/>未命中：低 | 是           |
| CACHE_CONSISTENT（5）         | <li>元数据行为：与 CACHE_CONSISTENT_PROMOTE  相同。</li><li>数据流访问行为：数据流的 ReadType 采用 CACHE 策略，即 CACHE 命中，不会在不同的介质层中移动数据。</li> | Always     | CACHE_PROMOTE | 强一致     | 命中：中<br/>未命中：低 | 是           |

>? Read_Type：指用户调用 SDK 或者 API 从 GooseFS 中读取数据时指定的文件缓存策略，对单个文件生效。
>  

结合目前大数据的业务实践，我们推荐的读写缓存策略组合主要如下：

| 写缓存策略                      | 读缓存策略                                                         | 策略组合表现 |
| :---------------------------- | :----------------------------------------------------------- | :--------- |
|CACHE_THROUGH（3）|CACHE_CONSISTENT（5）|缓存和远端存储系统数据强一致。|
|CACHE_THROUGH（3）|CACHE（2）|写强一致性，读最终一致性。|
|ASYNC_THROUGH（5）|CACHE_CONSISTENT（5）|写最终一致性，读强一致性。|
|ASYNC_THROUGH（5）|CACHE（2）|读写最终一致性。|
|MUST_CACHE（1）|CACHE（2）|只从缓存中读数据。|

如下示例展示了将指定命名空间 test_cos 的读写缓存策略分别设置为 CACHE_THROUGH 和 CACHE_CONSISTENT：
```plaintext
$ goosefs ns setPolicy --wPolicy 3 --rPolicy 5 test_cos
```

>!除了在创建命名空间时指定缓存策略，用户还可以通过在读写文件时，针对指定文件设置 ReadType 或者 Write_Type，或者通过 properties 配置文件配置全局缓存策略。多个策略同时存在的时候，优先级为用户自定义优先级 >  Namespace 读写策略 > 配置文件的全局缓存策略配置。其中，针对读策略会采用用户自定义 ReadType 和 Namespace 的 DirReadPolicy 的组合生效，即数据流读策略采用用户自定义 ReadType，元数据采用 Namespace 的策略。 
>
> 例如，GooseFS 中存在一个 COSN 命名空间，读策略为 CACHE_CONSISTENT；假设在该命名空间中存在一个 test.txt 的文件。客户端读取  test.txt  时，ReadType 指定了 CACHE_PROMOTE。那么整个读取行为就是同步元数据并且 CACHE_PROMOTE。

如果需要重置读写缓存策略，可以通过 unsetPolicy 指令实现，如下策略展示了重置 test_cos 命名空间的读写缓存策略：
```plaintext
$ goosefs ns unsetPolicy test_cos
```


### 设置 TTL

TTL 用于管理缓存在 GooseFS 本地节点的数据，配置 TTL 参数可以让缓存数据在指定的时间后执行指定的操作，例如 delete 或者 free 操作。目前设置 TTL 的操作指令如下：

```plaintext
$ goosefs ns setTtl [--action delete|free] <namespace> <time to live>
```

其中各项参数的含义如下：
- action：缓存时间到期后执行的操作，目前支持 delete 和 free 两种操作。delete 操作会删除缓存和 UFS 上的数据，free 操作只会删除缓存上的数据。
- namespace：指定的命名空间。
- time to live：数据缓存时间，单位毫秒。

如下示例展示了将指定命名空间 test_cos 的策略设置为60秒到期后删除：

```plaintext
$ goosefs ns setTtl --action free test_cos 60000
```

## 元数据信息管理

本小节介绍 GooseFS 如何管理元数据，包括元数据的同步、更新等内容。GooseFS 为用户提供了统一命名空间能力，用户可以通过统一的 gfs:// 的路径来访问不同底层存储系统上的文件，只需要指定好底层存储系统的路径即可。我们推荐您使用 GooseFS 作为统一的数据接入层，统一从 GooseFS 进行数据读写，保障元数据信息的一致性。

### 元数据同步概述

您可以通过在 conf/goosefs-site.properties 配置文件中修改元数据同步周期来管理元数据同步周期，配置参数如下：

```plaintext
goosefs.user.file.metadata.sync.interval=<INTERVAL>
```


同步周期支持如下3种入参：

- 入参数值为-1：代表元数据在首次加载到 GooseFS 中后就不再进行更新。
- 入参数值为0：代表 GooseFS 会在每次读写操作后都更新元数据。
- 入参数值为正整数：代表 GooseFS 会按照指定的时间间隔，周期性地更新元数据。

您可以综合考虑您的节点数量、GooseFS 集群和底层存储的 I/O 距离、底层存储类型等因素，选择合适的同步周期。通常：

- GooseFS 集群节点数量越多，元数据同步延迟越大。
- GooseFS 集群所处的机房和底层存储的物理距离越远，元数据同步延迟越大。
- 底层存储系统对元数据同步延迟的影响主要视系统请求 QPS 负载情况而定，QPS 负载越高则同步延迟相对更低。

### 元数据同步管理方式

#### 配置方式

1. 通过命令行配置
您可以通过命令行的方式设置元数据信息同步周期：
```plaintext
goosefs fs ls -R -Dgoosefs.user.file.metadata.sync.interval=0 <path to sync>
```
2. 通过配置文件配置
对于大规模的 Goosefs 集群而言，您可以通过 goosefs-site.properties 配置文件批量配置集群中 Master 节点的元数据信息同步周期，其他节点的同步周期会默认按照该周期值执行。
```plaintext
goosefs.user.file.metadata.sync.interval=1m
```

>! 很多业务会选择按照目录来区分数据的用途，不同目录的数据访问频次并不全部相同。元数据同步周期可以按照不同目录设置不同的周期值，对于一些经常变化的目录，可以将该目录的元数据同步周期设置为较短的时间（如5分钟），对于极少变化或者不变化的目录，可以将同步周期设置为-1，这样 GooseFS 不会自动同步该目录的元数据。
>

#### 推荐配置

根据业务访问模式的差异，您可以设置不同的元数据同步周期：

<table>
   <tr>
      <td colspan=2>访问模式</td>
      <td>元数据同步周期</td>
      <td>说明</td>
   </tr>
   <tr>
      <td colspan=2>所有文件请求都经过 GooseFS</td>
      <td>-1</td>
      <td>-</td>
   </tr>
   <tr>
      <td rowspan=2>绝大部分文件请求都经过 GooseFS</td>
      <td>使用 HDFS 作为 UFS</td>
      <td>推荐使用热更新或者按路径更新</td>
      <td>如果 HDFS 的更新特别频繁，推荐将更新周期设置为-1，禁止更新</td>
   </tr>
   <tr>
      <td>使用 COS 作为 UFS</td>
      <td>推荐按照路径配置更新周期</td>
      <td rowspan=3>按照不同目录配置不同的更新周期，可以缓解元数据同步的压力</td>
   </tr>
   <tr>
      <td rowspan=2>上传文件请求一般不经过 GooseFS</td>
      <td>使用 HDFS 作为 UFS</td>
      <td>推荐按照路径配置更新周期</td>
   </tr>
   <tr>
      <td>使用 COS 作为 UFS</td>
      <td>推荐按照路径配置更新周期</td>
   </tr>
</table>
