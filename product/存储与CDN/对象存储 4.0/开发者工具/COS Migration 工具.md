
## 功能说明
COS Migration 是一个集成了 COS 数据迁移功能的一体化工具。通过简单的配置操作，用户可以将源地址数据快速迁移至 COS 中，它具有以下特点：
- 丰富的数据源：
   - 本地数据：将本地存储的数据迁移到 COS。
   - 其他云存储：目前支持 AWS S3，阿里云 OSS，七牛存储迁移至 COS，后续会不断扩展。
   - URL 列表：根据指定的 URL 下载列表进行下载迁移到 COS。
   - Bucket 相互复制：COS 的 Bucket 数据相互复制，支持跨账号跨地域的数据复制。
- 断点续传：工具支持上传时断点续传。对于一些大文件，如果中途退出或者因为服务故障，可重新运行工具，会对未上传完成的文件进行续传。
- 分块上传：将对象按照分块的方式上传到 COS。
- 并行上传：支持多个对象同时上传。
- 迁移校验：对象迁移后的校验。

>!
>- COS Migration 的编码格式只支持 UTF-8 格式。
>- 使用该工具上传同名文件，默认会覆盖较旧的同名文件，需要额外设置以跳过同名文件。

## 使用环境
#### 系统环境
Windows、Linux 和 macOS 系统。

#### 软件依赖
- JDK 1.8 X64或以上，有关 JDK 的安装与配置请参见 [Java 安装与配置](https://cloud.tencent.com/document/product/436/10865)。
- Linux 环境需要 IFUNC 支持，确保环境 binutils 版本大于 2.20 。

## 使用方法
### 1. 获取工具
前往下载 [COS Migration 工具](https://github.com/tencentyun/cos_migrate_tool_v5)。

### 2. 解压缩工具包
#### Windows
解压并保存到某个目录，例如：
```plaintext
C:\Users\Administrator\Downloads\cos_migrate
```

#### Linux
解压并保存到某个目录：
```plaintext
unzip cos_migrate_tool_v5-master.zip && cd cos_migrate_tool_v5-master
```

#### 迁移工具结构
正确解压后的 COS Migration 工具目录结构如下所示：
```plaintext
COS_Migrate_tool
|——conf  #配置文件所在目录
|   |——config.ini  #迁移配置文件
|——db    #存储迁移成功的记录
|——dep   #程序主逻辑编译生成的JAR包
|——log   #工具执行中生成的日志
|——opbin #用于编译的脚本
|——src   #工具的源码
|——tmp   #临时文件存储目录
|——pom.xml #项目配置文件
|——README  #说明文档
|——start_migrate.sh  #Linux 下迁移启动脚本
|——start_migrate.bat #Windows 下迁移启动脚本
```

>?
 - db 目录主要记录工具迁移成功的文件标识，每次迁移任务会优先对比 db 中的记录，若当前文件标识已被记录，则会跳过当前文件，否则进行文件迁移。
 - log 目录记录着工具迁移时的所有日志，若在迁移过程中出现错误，请先查看该目录下的 error.log。

### 3. 修改 config.ini 配置文件
在执行迁移启动脚本之前，需先进行 config.ini 配置文件修改（路径：`./conf/config.ini`），config.ini 内容可以分为以下几部分：

#### 3.1 配置迁移类型
type 表示迁移类型，用户根据迁移需求填写对应的标识。例如，需要将本地数据迁移至 COS，则`[migrateType]`的配置内容是`type=migrateLocal`。
```plaintext
[migrateType]
type=migrateLocal
```

目前支持的迁移类型如下：

| migrateType | 描述 |
| ------| ------ |
| migrateLocal| 从本地迁移至 COS |
| migrateAws| 从 AWS S3 迁移至 COS |
| migrateAli| 从阿里  OSS  迁移至 COS |
| migrateQiniu| 从七牛迁移至 COS |
| migrateUrl| 下载 URL 迁移到 COS |
| migrateBucketCopy| 从源 Bucket 复制到目标 Bucket|
|migrateUpyun  | 从又拍云迁移到 COS |

>? 如果想从上述未提及的源站进行迁移，若源站兼容 AWS S3 的API，即可使用 AWS 的配置进行迁移。
>

#### 3.2 配置迁移任务
用户根据实际的迁移需求进行相关配置，主要包括迁移至目标 COS 信息配置及迁移任务相关配置。
```plaintext
# 迁移工具的公共配置分节，包含了需要迁移到目标 COS 的账户信息。
[common]
secretId=COS_SECRETID
secretKey=COS_SECRETKEY
bucketName=examplebucket-1250000000
region=ap-guangzhou
storageClass=Standard
cosPath=/
https=off
tmpFolder=./tmp
smallFileThreshold=5242880
smallFileExecutorNum=64
bigFileExecutorNum=8
entireFileMd5Attached=on
daemonMode=off
daemonModeInterVal=60
executeTimeWindow=00:00,24:00
outputFinishedFileFolder=./result
resume=false
skipSamePath=false
```

| 名称 | 描述 |默认值|
| ------| ------ |----- |
| secretId| 用户密钥 SecretId，请将`COS_SECRETID`替换为您的真实密钥信息。可前往 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中的云 API 密钥页面查看获取 |-|
| secretKey| 用户密钥 SecretKey，请将`COS_SECRETKEY`替换为您的真实密钥信息。可前往 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中的云 API 密钥页面查看获取|-|
| bucketName| 目的 Bucket 的名称, 命名格式为 `<BucketName-APPID>`，即 Bucket 名必须包含 APPID，例如 examplebucket-1250000000 |  -  |
| region| 目的 Bucket 的 Region 信息。COS 的地域简称请参照 [地域和访问域名](https://cloud.tencent.com/document/product/436/6224) |-|
| storageClass|   数据迁移后的存储类型，可选值为 Standard（标准存储）、Standard_IA（低频存储）、Archive（归档存储）、Maz_Standard（标准存储多 AZ）、Maz_Standard_IA（低频存储多 AZ），相关介绍请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417)    |Standard|
| cosPath|要迁移到的 COS 路径。`/`表示迁移到 Bucket 的根路径下，`/folder/doc/` 表示要迁移到 Bucket的`/folder/doc/` 下，若 `/folder/doc/` 不存在，则会自动创建路径|/|
| https| 是否使用 HTTPS 传输：on 表示开启，off 表示关闭。开启传输速度较慢，适用于对传输安全要求高的场景|off|
| tmpFolder|从其他云存储迁移至 COS 的过程中，用于存储临时文件的目录，迁移完成后会删除。要求格式为绝对路径：<br>Linux 下分隔符为单斜杠，例如`/a/b/c` <br>Windows 下分隔符为两个反斜杠，例如`E:\\a\\b\\c`<br>默认为工具所在路径下的 tmp 目录|./tmp|
| smallFileThreshold| 小文件阈值的字节，大于等于这个阈值使用分块上传，否则使用简单上传，默认5MB |5242880|
| smallFileExecutorNum|小文件（文件小于 smallFileThreshold）的并发度，使用简单上传。如果是通过外网来连接 COS，且带宽较小，请减小该并发度|64|
| bigFileExecutorNum| 大文件（文件大于等于 smallFileThreshold）的并发度，使用分块上传。如果是通过外网来连接 COS，且带宽较小，请减小该并发度|8|
| entireFileMd5Attached|表示迁移工具将全文的 MD5 计算后，存入文件的自定义头部 x-cos-meta-md5 中，用于后续的校验，因为 COS 的分块上传的大文件的 etag 不是全文的 MD5|on|
| daemonMode|是否启用 daemon 模式：on 表示开启，off 表示关闭。daemon 表示程序会循环不停的去执行同步，每一轮同步的间隔由 daemonModeInterVal 参数设置|off|
| daemonModeInterVal|表示每一轮同步结束后，多久进行下一轮同步，单位为秒 |60|
| executeTimeWindow|执行时间窗口，时刻粒度为分钟，该参数定义迁移工具每天执行的时间段。例如：<br>参数 03:30,21:00，表示在凌晨 03:30 到晚上 21:00 之间执行任务，其他时间则会进入休眠状态，休眠态暂停迁移并会保留迁移进度, 直到下一个时间窗口自动继续执行|00:00,24:00|
| outputFinishedFileFolder  | 这个目录保存迁移成功的结果，结果文件会按照日期命名，例如`./result/2021-05-27.out`，其中./result 为已创建的目录。文件内容每一行的格式为：绝对路径\t文件大小\t最后修改时间。设置为空，则不输出结果。| ./result |
| resume | 是否接着最后一次运行的结果，继续往下遍历源的文件列表。默认从头开始。 | false |
| skipSamePath | 如果 COS 上已经有相同的文件名，是否直接跳过。默认不跳过，即覆盖原有文件。| false |

#### 3.3 配置数据源信息
根据`[migrateType]`的迁移类型配置相应的分节。例如`[migrateType]`的配置内容是`type=migrateLocal`, 则用户只需配置`[migrateLocal]`分节即可。

**3.3.1 配置本地数据源 migrateLocal**

若从本地迁移至 COS，则进行该部分配置，具体配置项及说明如下：
```plaintext
# 从本地迁移到 COS 配置分节
[migrateLocal]
localPath=E:\\code\\java\\workspace\\cos_migrate_tool\\test_data
excludes=
ignoreModifiedTimeLessThanSeconds=
```

| 配置项 | 描述 |
| ------| ------ |
|localPath|本地目录，要求格式为绝对路径：<ul  style="margin: 0;"><li>Linux 下分隔符为单斜杠，例如`/a/b/c` </li><li>Windows 下分隔符为两个反斜杠，例如`E:\\a\\b\\c`</li></ul>|
|excludes| 要排除的目录或者文件的绝对路径，表示将 localPath 下面某些目录或者文件不进行迁移，多个绝对路径之前用分号分割，不填表示 localPath 下面的全部迁移|
|ignoreModifiedTimeLessThanSeconds| 排除更新时间与当前时间相差不足一定时间段的文件，单位为秒，默认不设置，表示不根据 lastmodified 时间进行筛选，适用于客户在更新文件的同时又在运行迁移工具，并要求不把正在更新的文件迁移上传到 COS，例如设置为300，表示只上传更新了5分钟以上的文件|

**3.3.2 配置阿里 OSS 数据源 migrateAli**

若从阿里云 OSS 迁移至 COS，则进行该部分配置，具体配置项及说明如下：
```plaintext
# 从阿里 OSS 迁移到 COS 配置分节
[migrateAli]
bucket=bucket-aliyun
accessKeyId=yourAccessKeyId
accessKeySecret=yourAccessKeySecret
endPoint= oss-cn-hangzhou.aliyuncs.com
prefix=
proxyHost=
proxyPort=
```

| 配置项 | 描述 |
| ------| ------ |
|bucket|阿里云 OSS  Bucket 名称|
|accessKeyId|将 yourAccessKeyId 替换为用户的密钥 |
|accessKeySecret| 将 yourAccessKeySecret 替换为用户的密钥|
|endPoint|阿里云 endpoint 地址|
|prefix|要迁移的路径的前缀，如果是迁移 Bucket 下所有的数据, 则 prefix 为空|
|proxyHost|如果要使用代理进行访问，则填写代理 IP 地址|
|proxyPort|代理的端口|

**3.3.3 配置 AWS 数据源 migrateAws**

若从 AWS 迁移至 COS，则进行该部分配置，具体配置项及说明如下：
```plaintext
# 从 AWS 迁移到 COS 配置分节
[migrateAws]
bucket=bucket-aws
accessKeyId=AccessKeyId
accessKeySecret=SecretAccessKey
endPoint=s3.us-east-1.amazonaws.com
prefix=
proxyHost=
proxyPort=
```

| 配置项 | 描述 |
| ------| ------ |
|bucket| AWS 对象存储 Bucket 名称|
|accessKeyId|将 AccessKeyId 替换为用户的密钥|
|accessKeySecret| 将 SecretAccessKey 替换为用户的密钥|
|endPoint|AWS 的 endpoint 地址，必须使用域名，不能使用 region|
|prefix|要迁移的路径的前缀，如果是迁移 Bucket 下所有的数据，则 prefix 为空|
|proxyHost|如果要使用代理进行访问，则填写代理 IP 地址|
|proxyPort|代理的端口|

 
**3.3.4 配置七牛数据源 migrateQiniu**

若从七牛迁移至 COS，则进行该部分配置，具体配置项及说明如下：
```plaintext
# 从七牛迁移到COS配置分节
[migrateQiniu]
bucket=bucket-qiniu
accessKeyId=AccessKey
accessKeySecret=SecretKey
endPoint=www.bkt.clouddn.com
prefix=
proxyHost=
proxyPort=
```

| 配置项 | 描述 |
| ------| ------ |
|bucket|七牛对象存储 Bucket 名称|
|accessKeyId|将 AccessKey 替换为用户的密钥 |
|accessKeySecret| 将 SecretKey 替换为用户的密钥|
|endPoint|七牛下载地址，对应 downloadDomain|
|prefix|要迁移的路径的前缀，如果是迁移 Bucket 下所有的数据，则 prefix 为空|
|proxyHost|如果要使用代理进行访问，则填写代理 IP 地址|
|proxyPort|代理的端口|

 
**3.3.5 配置 URL 列表数据源 migrateUrl**

若从指定 URL 列表迁移至 COS，则进行该部分配置，具体配置项及说明如下：
```plaintext
# 从 URL 列表下载迁移到 COS 配置分节
[migrateUrl]
urllistPath=D:\\folder\\urllist.txt
```
     
| 配置项 | 描述 |
| ------| ------ |
|urllistPath|URL 列表的地址，内容为 URL 文本，一行一条 URL 原始地址（例如`http://aaa.bbb.com/yyy/zzz.txt`，无需添加任何双引号或其他符号）。URL 列表的地址要求为绝对路径：<ul  style="margin: 0;"><li>Linux 下分隔符为单斜杠，例如`/a/b/c.txt` </li><li>Windows  下分隔符为两个反斜杠，例如`E:\\a\\b\\c.txt`<br>如果填写的是目录，则会将该目录下的所有文件视为 urllist 文件去扫描迁移</li></ul>|

 
**3.3.6 配置 Bucket 相互复制 migrateBucketCopy**

若从 COS 的一个指定 Bucket 迁移至另一个 Bucket，则进行该部分配置，具体配置项及说明如下：
>!发起迁移的账号，需具备源读权限、目的写权限。

```plaintext
# 从源 Bucket 迁移到目标 Bucket 配置分节
[migrateBucketCopy]
srcRegion=ap-shanghai
srcBucketName=examplebucket-1250000000
srcSecretId=COS_SECRETID
srcSecretKey=COS_SECRETKEY
srcCosPath=/
```

| 配置项 | 描述 |
| ------| ------ |
|srcRegion|源 Bucket 的 Region 信息，请参照 [可用地域](https://cloud.tencent.com/document/product/436/6224)|
|srcBucketName|源 Bucket 的名称，命名格式为 `<BucketName-APPID>`，即 Bucket 名必须包含 APPID，例如 examplebucket-1250000000|
|srcSecretId|源 Bucket 隶属的用户的密钥 SecretId，可在 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 查看。如果是同一用户的数据，则 srcSecretId 和 common 中的 SecretId 相同，否则是跨账号 Bucket 拷贝|
|srcSecretKey|源 Bucket 隶属的用户的密钥 secret_key，可在 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 查看。如果是同一用户的数据，则 srcSecretKey 和 common 中的 secretKey 相同，否则是跨账号 Bucket 拷贝|
|srcCosPath|要迁移的 COS 路径，表示该路径下的文件要迁移至目标 Bucket|

**3.3.7 配置又拍云数据源 migrateUpyun**
若从又拍云迁移至 COS，则进行该部分配置，具体配置项及说明如下：

```plaintext
[migrateUpyun]
# 从又拍迁移
bucket=xxx
#又拍云操作员的 ID
accessKeyId=xxx
#又拍云操作员的密码     
accessKeySecret=xxx       
prefix=

#又拍云 sdk 限制，这个 proxy 会被设置成全局的 proxy
proxyHost=
proxyPort=
```

| 配置项 | 描述 |
| ------| ------ |
|bucket|又拍云 USS Bucket 名称|
|accessKeyId|替换为又拍云操作员的 ID|
|accessKeySecret| 替换为又拍云操作员的密码|
|prefix|要迁移的路径的前缀，如果是迁移 Bucket 下所有的数据，则 prefix 为空|
|proxyHost|如果要使用代理进行访问，则填写代理 IP 地址|
|proxyPort|代理的端口|

### 4. 运行迁移工具
#### Windows
双击 **start_migrate.bat** 即可运行。

#### Linux
1.从 config.ini 配置文件读入配置，运行命令为：
```plaintext
sh start_migrate.sh
```
2.部分参数从命令行读入配置，运行命令为：
```plaintext
sh start_migrate.sh -Dcommon.cosPath=/savepoint0403_10/
```

>?
> - 工具支持配置项读取方式有两种：命令行读取或配置文件读取。
> - 命令行优先级高于配置文件，即相同配置选项会优先采用命令行里的参数。
> - 命令行中读取配置项的形式方便用户同时运行不同的迁移任务，但前提是两次任务中的关键配置项不完全一样，例如 Bucket 名称，COS 路径，要迁移的源路径等。因为不同的迁移任务写入的是不同的 db 目录，可以保证并发迁移。请参照前文中的工具结构中的 db 信息。
> - 配置项的形式为 **-D{sectionName}.{sectionKey}={sectionValue}** 的形式。其中 sectionName 是配置文件的分节名称，sectionKey 表示分节中配置项名称，sectionValue 表示分节中配置项值。如设置要迁移到的 COS 路径，则以 **-Dcommon.cosPath=/bbb/ddd** 表示。
> 

## 迁移机制及流程
### 迁移机制原理

COS 迁移工具是有状态的，已经迁移成功的会记录在 db 目录下，以 KV 的形式存储在 leveldb 文件中。每次迁移前对要迁移的路径，先查找下 db 中是否存在， 如果存在，且属性和 db 中存在的一致， 则跳过迁移，否则进行迁移。这里的属性根据迁移类型的不同而不同，对于本地迁移，会判断 mtime。对于其他云存储迁移与 Bucket 复制，会判断源文件的 etag 和长度是否与 db 一致。因此，我们参照 db 中是否有过迁移成功的记录，而不是查找 COS，如果绕过了迁移工具，通过别的方式（如 COSCMD 或者控制台）删除修改了文件，那么运行迁移工具由于不会察觉到这种变化，是不会重新迁移的。

### 迁移流程步骤

1. 读取配置文件，根据迁移 type，读取相应的配置分节，并执行参数的检查。
2. 根据指定的迁移类型，扫描对比 db 下对所要迁移文件的标识，判断是否允许上传。
3. 迁移执行过程中会打印执行结果，其中 inprogress 表示迁移中，skip 表示跳过，fail 表示失败，ok 表示成功， condition_not_match 表示因为表示因不满足迁移条件而跳过的文件（如 lastmodifed 和 excludes）。失败的详细信息可以在 log 的 error 日志中查看。执行过程示意图如下图所示：
 ![](https://main.qcloudimg.com/raw/7561d07ea315c9bacbb228b36d6ad6d6.png)
4. 整个迁移结束后会打印统计信息，包括累积的迁移成功量，失败量，跳过量，耗时。对于失败的情况，请查看 error 日志，或重新运行，因为迁移工具会跳过已迁移成功的，对未成功的会重新迁移。运行完成结果示意图如下图所示：
![](https://main.qcloudimg.com/raw/2534fd390218db29bb03f301ed2620c8.png)

## 常见问题
如您在使用 COS Migration 工具过程中，遇到迁移失败、运行报错等异常情况，请参阅 [COS Migration 工具类常见问题](https://cloud.tencent.com/document/product/436/30745) 寻求解决。

