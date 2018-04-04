# COS Migration 工具

## 功能说明

COS Migration是一个集成了有关COS数据迁移功能的一体化工具。通过简单的配置操作，用户可以将源地址数据快速迁移至COS中，它具有以下特点：



- 丰富的数据源：

    本地数据：将本地存储的数据迁移到COS

    其他云存储：目前支持AWS S3, 阿里云 OSS, 七牛存储迁移至COS，后续会不断扩展 

    URL列表：根据指定的URL下载列表进行下载迁移到COS
    
    Bucket相互复制：COS的Bucket数据相互复制, 支持跨账号跨地域的数据复制

- 断点续传

- 分块上传

- 并行上传

- 迁移校验



## 使用环境

###系统环境

 - Linux 或 Windows 环境

### 软件依赖
- JDK1.7或以上, 有关JDK的安装与配置请参考[JAVA安装与配置](https://cloud.tencent.com/document/product/436/10865)


## 使用方法
### 1. 获取工具

下载链接：[cos Migration 工具](https://github.com/tencentyun/cos_migrate_tool_v5)

### 2. 解压缩工具包
 - Windows：
  
    解压并保存到某个目录, 比如 `C:\Users\Administrator\Downloads\cos_migrate`
 - Linux：
  
    解压并保存到某个目录
    ```unzip cos_migrate_tool_v5-master.zip && cd cos_migrate_tool_v5-master```

- 迁移工具结构

 正确解压后的COS Migration工具目录结构如下所示：

    COS_Migrate_tool
    |——conf  #配置文件所在目录
    |   |——config.ini  #迁移配置文件
    |——db    #存储迁移成功的记录
    |——dep   #程序主逻辑编译生成的JAR包
    |——log   #工具执行中生成的日志
    |——opbin #用于编译的脚本
    |——src   #工具的源码
    |——pom.xml #项目配置文件
    |——README  #说明文档
    |——start_migrate.sh  #Linux 下迁移启动脚本
    |——start_migrate.bat #Windows 下迁移启动脚本

说明：

 - db目录主要记录工具迁移成功的文件标识，每次迁移任务会优先对比db中的记录，若当前文件标识已被记录，则会跳过当前文件，否则进行文件迁移
 - log目录记录着工具迁移时的所有日志，若在迁移过程中出现错误, 请先查看该目录下的error.log





### 3. 修改config.ini配置文件
在执行迁移启动脚本之前，需先进行config.ini配置文件修改（路径：./conf/config.ini），config.ini内容可以分为以下几部分：

####3.1 配置迁移类型

type表示迁移类型，用户根据迁移需求填写对应的标识。例如，需要将本地数据迁移至COS，则`[migrateType]`的配置内容是`type=migrateLocal`。

    [migrateType]
    type=migrateLocal

目前支持的迁移类型如下：

| migrateType | 描述 |
| ------| ------ |
| migrateLocal| 从本地迁移至cos |
| migrateAws| 从aws s3本地迁移至cos |
| migrateAli| 从阿里 oss 迁移至cos |
| migrateQiniu| 从七牛迁移至cos |
| migrateUrl| 下载url迁移到cos |
| migrateBucketCopy| 从源bucket复制到目标bucket|



#### 3.2 配置迁移任务

用户根据实际的迁移需求进行相关配置，主要包括迁移至目标cos信息配置及迁移任务相关配置

    # 迁移工具的公共配置分节，包含了要迁移到得目标COS的账户信息 
    [common]
    secretId=AKIDXXXXXXXXXXXXXXXXX
    secretKey=GYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
    bucketName=mybcket-1251668577
    region=ap-guangzhou
    storageClass=Standard
    cosPath=/
    https=off
    tmpFolder=/a/b/c/tmp
    smallFileThreshold=5242880
    smallFileExecutorNum=64
    bigFileExecutorNum=8
    entireFileMd5Attached=on
    daemonMode=off
    daemonModeInterVal=60



| 名称 | 描述 |默认值|
| ------| ------ |----- |
| secretId| 用户的秘钥 secret_id(可在[https://console.qcloud.com/capi](https://console.qcloud.com/capi) 查看) |-|
| secretKey| 用户的秘钥 secret_key(可在[https://console.qcloud.com/capi]( https://console.qcloud.com/capi) 查看)|-|
| bucketName| 目的Bucket的名称, 合法命名规则为{name}-{appid}，即bucket名必须包含appid, 例如movie-1251000000|-|
| region| 目的Bucket的region信息. COS地域的简称请参照[可用地域](https://www.qcloud.com/document/product/436/6224)|-|
| storageClass|存储类型：Standard - 标准存储, Standard_IA - 低频存储 |Standard|
| cosPath|要迁移到的cos路径, /表示迁移到bucket的根路径下, /aaa/bbb/表示要迁移到bucket的/aaa/bbb/下面, 如果/aaa/bbb/不存在,则会自动建立|/|
| https| 是否使用HTTPS传输：on - 开启，off - 关闭(开启传输速度较慢，适用于对传输安全要求高的场景)|off|
| tmpFolder|从其他云存储迁移至cos的过程中，用于存储临时文件的目录, 迁移完成后会删除（要求格式为绝对路径：Linux下分隔符为单斜杠，如/a/b/c； Windows下分隔符为两个反斜杠，如E:\\\a\\\b\\\c）|-|
| smallFileThreshold| 小文件阈值的字节，大于等于这个阈值使用分块上传，否则使用简单上传，默认5MB |5242880|
| smallFileExecutorNum|小文件(文件小于smallFileThreshold)的并发度，使用简单上传, 如果是通过外网来连接COS, 且带宽较小, 请减小改并发度|64|
| bigFileExecutorNum| 大文件(文件大于等于smallFileThreshold)的并发度，使用分块上传。如果是通过外网来连接COS, 且带宽较小, 请减小改并发度|8|
| entireFileMd5Attached|表示迁移工具将全文的MD5计算后，存入文件的自定义头部x-cos-meta-md5中, 用于后续的校验，因为COS的分块上传的大文件的etag不是全文的md5|on|
| daemonMode|是否启用damon模式：on - 开启，off - 关闭（damon表示程序会循环不停的去执行同步，每一轮同步的间隔由damonModeInterVal参数设置）|off|
| daemonModeInterVal|表示每一轮同步结束后，多久进行下一轮同步，单位为秒 |60|

#### 3.3 配置数据源信息
根据`[migrateType]`的迁移类型配置相应的分节。例如`[migrateType]`的配置内容是`type=migrateLocal`, 则用户只需配置`[migrateLocal]`分节即可。
#####3.3.1 配置本地数据源 migrateLocal
 
若从本地迁移至cos，则进行该部分配置，具体配置项及说明如下：

      # 从本地迁移到COS配置分节
      [migrateLocal]
      localPath=E:\\code\\java\\workspace\\cos_migrate_tool\\test_data
      exeludes=

| 名称 | 描述 |
| ------| ------ |
|localPath|本地路径，要求格式为绝对路径：Linux下分隔符为单斜杠，如/a/b/c； Windows下分隔符为两个反斜杠，如E:\\\a\\\b\\\c|
|exeludes| 要排除的目录或者文件的绝对路径, 表示将localPath下面某些目录或者文件不进行迁移，多个绝对路径之前用分号分割，不填表示localpath下面的全部迁移|


#####3.3.2 配置阿里oss数据源 migrateAli
若从阿里云oss迁移至cos，则进行该部分配置，具体配置项及说明如下：

    # 从阿里oss迁移到COS配置分节
      [migrateAli]
      bucket=mybucket-test
      accessKeyId=xxxxxxxxxx
      accessKeySecret=yyyyyyyyyyy
      endPoint=oss-cn-shenzhen.aliyuncs.com
      prefix=
      proxyHost=
      proxyPort=

| 名称 | 描述 |
| ------| ------ |
|bucket|阿里云oss Bucket名称|
|accessKeyId|用户的秘钥accessKeyId |
|accessKeySecret| 用户的秘钥accessKeySecret|
|endPoint|阿里云endpoint地址|
|prefix|要迁移的路径的前缀, 如果是迁移bucket下所有的数据, 则prefix为空|
|proxyHost|如果要使用代理进行访问，则填写代理IP地址|
|proxyPort|代理的端口|


#####3.3.3 配置AWS数据源 migrateAws
若从AWS迁移至cos，则进行该部分配置，具体配置项及说明如下：

    # 从AWS迁移到COS配置分节
      [migrateAws]
      bucket=aws-emr-test
      accessKeyId=xxxxxxxxxx
      accessKeySecret=yyyyyyyyyyyyyyyy
      endPoint=s3.us-east-1.amazonaws.com
      prefix=
      proxyHost=
      proxyPort=

| 名称 | 描述 |
| ------| ------ |
|bucket|AWS对象存储 Bucket名称|
|accessKeyId|用户的秘钥accessKeyId |
|accessKeySecret| 用户的秘钥accessKeySecret|
|endPoint|AWS的endpoint地址|
|prefix|要迁移的路径的前缀, 如果是迁移bucket下所有的数据, 则prefix为空|
|proxyHost|如果要使用代理进行访问，则填写代理IP地址|
|proxyPort|代理的端口|



#####3.3.4 配置七牛数据源 migrateQiniu
若从七牛迁移至cos，则进行该部分配置，具体配置项及说明如下：

    # 从七牛迁移到COS配置分节
      [migrateQiniu]
      bucket=mybuckettest
      accessKeyId=xxxxxxxxxx
      accessKeySecret=yyyyyyyyyyyyyyyy
      endPoint=wwww.bkt.clouddn.com
      prefix=
      proxyHost=
      proxyPort=

| 名称 | 描述 |
| ------| ------ |
|bucket|七牛对象存储 Bucket名称|
|accessKeyId|用户的秘钥accessKeyId |
|accessKeySecret| 用户的秘钥accessKeySecret|
|endPoint|七牛下载地址，对应downloadDomain|
|prefix|要迁移的路径的前缀, 如果是迁移bucket下所有的数据, 则prefix为空|
|proxyHost|如果要使用代理进行访问，则填写代理IP地址|
|proxyPort|代理的端口|


#####3.3.5 配置url列表数据源 migrateUrl
若从指定url列表迁移至cos，则进行该部分配置，具体配置项及说明如下：

    # 从url列表下载迁移到COS配置分节
      [migrateUrl]
      urllistPath=/data/mydata/url    

| 名称 | 描述 |
| ------| ------ |
|urllistPath|url列表项，要求格式为绝对路径：Linux下分隔符为单斜杠，如/a/b/c； Windows下分隔符为两个反斜杠，如E:\\\a\\\b\\\c。（如果填写的是目录，则会将该目录下的所有文件视为urllist文件去扫描迁移）|




#####3.3.6 配置Bucket相互复制 migrateBucketCopy
若从指定url列表迁移至cos，则进行该部分配置，具体配置项及说明如下：

    # 从源bucket迁移到目标bucket配置分节
      [migrateBucketCopy]
      srcRegion=ap-shanghai  
      srcBucketName=mysrcbucket-1251668555
      srcSecretId=xxxxxxxxxxx
      srcSecretKey=yyyyyyyyyyyyyyyy
      srcCosPath=/

| 名称 | 描述 |
| ------| ------ |
|srcRegion|源bucket的region信息，请参照[可用地域](https://www.qcloud.com/document/product/436/6224)|
|srcBucketName|源Bucket的名称, 合法命名规则为{name}-{appid}，即bucket名必须包含appid, 例如movie-1251000000|
|srcSecretId|源bucket隶属的用户的秘钥 secret_id(可在[https://console.qcloud.com/capi](https://console.qcloud.com/capi) 查看)。如果是同一用户的数据，则srcSecretId和common中的secretId相同，否则是跨账号bucket拷贝，srcSecretId和common中的secretId不同 |
|srcSecretKey|源bucket隶属的用户的秘钥 secret_key(可在[https://console.qcloud.com/capi](https://console.qcloud.com/capi) 查看)。如果是同一用户的数据，则srcSecretId和common中的secretId相同，否则是跨账号bucket拷贝，srcSecretId和common中的secretId不同|
|srcCosPath|要迁移的cos路径，表示该路径下的文件要迁移至目标bucket|


###4. 运行迁移工具
 - Windows：
 
    双击 start_migrate.bat 即可运行

 - Linux：

    1.从config.ini配置文件读入配置，运行命令为：
                  
    `sh start_migrate.sh`

    2.部分参数从命令行读入配置，运行命令为：

    `sh start_migrate.sh -Dcommon.cosPath=/savepoint0403_10/`

 - 特别说明

    1. 工具支持配置项读取方式有两种：命令行读取或配置文件读取。
    2. 命令行优先级高于配置文件，即相同配置选项会优先采用命令行里的参数。
    3. 命令行中读取配置项的形式方便用户同时运行不同的迁移任务，但前提是两次任务中的关键配置项不完全一样，比如bucket名称，cos路径, 要迁移的源路径等。因为不同的迁移任务写入的是不同的db目录，可以保证并发迁移. 请参照前文中的工具结构中的db信息。
    4. 配置项的形式为-D{sectionName}.{sectionKey}={sectionValue}的形式。其中sectionName是配置文件的分节名称，sectionKey表示分节中配置项名称，sectionValue表示分节中配置项值。如设置要迁移到的cos路径，则以-Dcommon.cosPath=/bbb/ddd表示。




## 迁移机制及流程
###迁移机制原理
COS迁移工具是有状态的，已经迁移成功的会记录在db目录下，以KV的形式存储在leveldb文件中。每次迁移前对要迁移的路径，先查找下DB中是否存在， 如果存在，且属性和db中存在的一致， 则跳过迁移，否则进行迁移。这里的属性根据迁移类型的不同而不同，对于本地迁移，会判断mtime。对于其他云存储迁移与bucket复制，会判断源文件的etag和长度是否与db一致。因此，我们参照的db中是否有过迁移成功的记录，而不是查找COS，如果绕过了迁移工具，通过别的方式(比如coscmd或者控制台)删除修改了文件，那么运行迁移工具由于不会察觉到这种变化，是不会重新迁移的



###迁移流程步骤

1. 读取配置文件，根据迁移type，读取响应的配置分节，并执行参数的检查。
2. 根据指定的迁移类型，扫描对比db下对所要迁移文件的标识，判断是否允许上传
3. 迁移执行过程中会打印执行结果，其中inprogress表示迁移中，skip表示跳过，fail表示失败，ok表示成功。失败的详细信息可以在log的error日志中查看。执行过程示意图如下图所示：

     ![](https://i.imgur.com/oojIbOm.png)

4. 整个迁移结束后会打印统计信息，包括累积的迁移成功量，失败量，跳过量，耗时。对于失败的情况，请查看error日志，或重新运行，因为迁移工具会跳过已迁移成功的，对未成功的会跳过。运行完成结果示意图如下图所示：

    ![](https://i.imgur.com/NkoddI5.png)


## 常见问题

1. 迁移工具中途异常退出怎么办？ 

    工具支持上传时断点续传, 对于一些大文件, 如果中途退出或者因为服务故障, 可重新运行工具, 会对未上传完的文件进行续传。

2. 对于迁移成功的文件，用户通过控制台或其他方式删除了COS上的文件，迁移工具会将这些文件进行重新上传吗？

    不会。原因是，所有迁移成功的文件会被记录在db中，迁移工具运行之前会先扫描db目录，对于已被记录的文件不会再次上传，具体原因请参照迁移机制说明。

3. 迁移失败，日志显示403 Access Deny，该怎么办？


    请确认秘钥信息，bucket信息，region信息是否正确，并且是否具有操作权限。如果是子账号，请让父账号授予相应的权限；如果是本地迁移和其他云存储迁移, 需要对bucket具有数据写入和读取权限；如果是bucket copy, 还需要对源bucket具有数据读取权限。

4. 迁移失败，日志显示503 Slow Down，该怎么办？


    这是触发频控所导致，COS目前对一个账号具有每秒800 QPS的操作限制。建议调小配置中小文件的并发度,，并重新运行工具，则会将失败的重新运行。

5. 迁移失败，日志显示404 NoSuchBucket，该怎么办？


    请确认你的秘钥信息，bucket信息，region信息是否正确。


6. 其他问题


    请重新运行迁移工具，若仍然失败的，请将配置信息(秘钥信息请隐藏)与log目录打包后。
   


     
