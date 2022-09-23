### 原始数据非 HDFS 数据
如果您的原始数据不是 HDFS 数据而是其他形式的文件数据，可以通过 COS 的 web 控制台或者 COS 提供的 API 来把数据传入到 COS，然后在 EMR 集群中进行分析，COS 传输数据请查看资料。

### 原始数据在 HDFS 的数据迁移
1. 获取 COS 迁移工具
[获取迁移工具](https://github.com/tencentyun/hdfs_to_cos_tools)，更多迁移工具请参考 [工具概览](https://cloud.tencent.com/document/product/436/6242)。
2. 工具配置
配置文件统一放在工具目录里的 conf 目录，将需要同步的 HDFS 集群的 core-site.xml 拷贝到 conf 中，其中包含了 NameNode 的配置信息，编辑配置文件 cos_info.conf，包括 appid、bucket、region 以及密钥信息。
3. 命令参数说明
```
 -ak <ak>                                the cos secret id
 -appid,--appid <appid>                  the cos appid
-bucket,--bucket <bucket_name>          the cos bucket name
-cos_info_file,--cos_info_file <arg>    the cos user info config default is ./conf/cos_info.conf
-cos_path,--cos_path <cos_path>         the absolute cos folder path
-h,--help                               print help message
-hdfs_conf_file,--hdfs_conf_file <arg>  the hdfs info config default is ./conf/core-site.xml
-hdfs_path,--hdfs_path <hdfs_path>      the hdfs path
-region,--region <region>               the cos region. legal value cn-south, cn-east, cn-north, sg
-sk <sk>                                the cos secret key
-skip_if_len_match,--skip_if_len_match  skip upload if hadoop file length match cos
```
4. 执行迁移 
```shell
# 所有操作都要在工具目录下。如果同时设置了配置文件和命令行参数，以命令行参数为准
./hdfs_to_cos_cmd -h
# 从 HDFS 拷贝到 COS（如果 COS 上已存在文件，则会覆盖）
./hdfs_to_cos_cmd --hdfs_path=/tmp/hive --cos_path=/hdfs/20170224/
# 从 HDFS 拷贝到 COS，同时要拷贝的文件和 COS 的长度一致，则忽略上传（适用于拷贝一次后，重新拷贝）
# 这里只做长度的判断，因为如果将 Hadoop 上的文件摘要算出，开销较大
./hdfs_to_cos_cmd --hdfs_path=/tmp/hive --cos_path=/hdfs/20170224/ -skip_if_len_match
# 完全通过命令行设置参数
./hdfs_to_cos_cmd -appid 1252xxxxxx -ak
      AKIDVt55xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -sk
      KS08jDVbVElxxxxxxxxxxxxxxxxxxxxxxxxxx -bucket test -cos_path /hdfs
      -hdfs_path /data/data -region cn-south -hdfs_conf_file
/home/hadoop/hadoop-2.8.1/etc/hadoop/core-site.xml
```
5. 验证运行命令后，输出如下日志
```
[Folder Operation Result : [ 53(sum)/ 53(ok) / 0(fail)]]
[File Operation Result: [22(sum)/ 22(ok) / 0(fail) / 0(skip)]]
[Used Time: 3 s]
```
 - sum 表示总共需要迁移的文件数。
 - ok 表示成功迁移的文件数。
 - fail 表示迁移失败的文件数。
 - skip 表示在添加 skip_if_len_match 参数后，由于上传文件和同名文件具有相同长度的文件，则跳过的数量。

您也可以登录 COS 控制台查看数据是否已经正确迁移过来。

### 常见问题  
- 请确保填写的配置信息，包括 appID、密钥信息、bucket 和 region 信息正确，以及机器的时间和北京时间一致（如相差1分钟左右是正常的），如果相差较大，请设置机器时间。  
- 请保证对于 DateNode，拷贝程序所在的机器也可以连接。因 NameNode 有外网 IP 可以连接，但获取的 block 所在的 DateNode 机器是内网 IP，无法连接上，因此建议同步程序放在 Hadoop 的某个节点上执行，保证对 NameNode 和 DateNode 皆可访问。
- 权限问题，用当前账户使用 Hadoop 命令下载文件，看是否正常，再使用同步工具同步 Hadoop 上的数据。    
- 对于 COS 上已存在的文件，默认进行重传覆盖，除非用户明确的指定 -skip_if_len_match，当文件长度一致时则跳过上传。    
- cos path 都认为是目录，最终从 HDFS 上拷贝的文件都会存放在该目录下。
