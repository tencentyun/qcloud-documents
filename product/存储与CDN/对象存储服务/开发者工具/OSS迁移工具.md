cos_migration 迁移工具可以将您在阿里云存储上的文件同步到腾讯云对象存储（COS）上。

## 功能说明

主要特性：

- 支持断点续传
- 支持并行数据下载/上传
- 支持自动同步增量数据

客户只需配置阿里云的存储信息以及腾讯云（COS）的账号信息，运行工具，即可自动迁移。迁移后，文件的名称、路径和数据源保持一致。

迁移效果示例：

``` 
数据源：aliyun
bucket：mytest
endpoint：oss-cn-shenzhen.aliyuncs.com
图片访问路径：http://mytest.oss-cn-shenzhen.aliyuncs.com/aa/bb/cc/gaoxiao.jpg

目的地：COS
appid：1000027
bucketname：new_laixin_test
数据迁移后，在COS的访问路径：
http://new_laixin_test-1000027.file.myqcloud.com/aa/bb/cc/gaoxiao.jpg
```

## 目录说明

``` 
├── bin    工具
├── code   源码
├── conf   配置
├── docs   文档
├── download 运行过程中存放下载文件存放处
├── output   日志等输出信息
└── tmp      运行过程中的临时文件存放处
```

## 使用环境

### 系统环境

cos_migration 迁移工具目前只支持 Linux 系统。

### 软件依赖

cos_migration 迁移工具会用到 php 和 php-curl 扩展，所以请先安装 php 和 php-curl。

安装 php 和 php-curl 的方法：

``` 
yum –y install php
yum -y install php-curl
```

## 使用方法

#### 获取软件

[点击这里](https://mc.qcloudimg.com/static/archive/1ce5a174bd3a7ec7cf44b7dbe45e90bf/cos_migration_tools.tar)下载最新版本的 cos_migration 迁移工具。

将安装包放置在存储空间较大的磁盘目录下，执行 tar 命令解压即可使用。

``` 
tar xvf cos_migration_tools.tar
```

#### 初级配置

配置文件 config.ini 位于工具 cos_migration_tools 目录的 conf 目录下，修改 config.ini 中的参数即可完成工具配置。

配置参数分为两方面内容：数据源信息设置 和 腾讯云 COS 信息设置。

##### 阿里云存储信息设置

``` 
[SrcStorageInfo]
SrcStorageBucket=阿里云的空间名称
SrcStorageAccessKey=阿里云的账号access key id
SrcStorageSecretKey=阿里云的账号access key secret
SrcStorageEndPoint=阿里云的endpoint
SrcStorageIsPrivateBucket=0 设置为1则表示的空间是私有空间，否则设为0表示公共空间
SrcStoragePrefix= 设置的迁移文件目录，如果有多个目录要迁移，可以用多台机器，分别迁移不同的目录的文件
```

##### 腾讯云 COS 信息设置

登录[腾讯云对象存储](https://console.cloud.tencent.com/cos)，默认项目会分配 APP ID、secretID、secretKey 如下图，如果新建项目，则会分配一套新的 APP ID、secretID、secretKey，每个项目下的 APP ID、secretID、secretKey 均不相同。

![image_1aog2g81ghgqmk210p4146c8tr9.png-23.6kB][1]

点击【获取 secretKey 按钮】，获取以下信息：

![image_1aog2gr3u2ek17a813gh8o1ts4m.png-30.1kB][2]

添加到如下配置中：

``` 
[CosInfo]
CosAppId=APPID
CosSecretId=secretID
CosSecretKey=secretKey
CosBucket=Bucket名称
```

##### 配置示例

以 aliyun 为例，迁移整个 bucket。

``` 
[ToolConfig]
Concurrency=10
TotalNum=

[SrcStorageInfo]
SrcStorageBucket=test
SrcStorageAccessKey=oEdafddccEPScbD
SrcStorageSecretKey=DkfgiG8nEntzFmOJpJ7CayLpa9SKL2b
SrcStorageEndPoint=oss-cn-shenzhen.aliyuncs.com
SrcStorageIsPrivateBucket=0
SrcStoragePrefix=

[CosInfo]
CosAppId=10234599
CosSecretId=fgvssa5a2DsULCp6MFa5bYs1CisMlEPf
CosSecretKey=ZjHRXsadfasdfaS5Mu3hB4nxVe5F2Ku
CosBucket=test
```

迁移文件夹 dir1

``` 
[ToolConfig]
Concurrency=10
TotalNum=

[SrcStorageInfo]
SrcStorageBucket=test
SrcStorageAccessKey=oEdafddccEPScbD
SrcStorageSecretKey=DkfgiG8nEntzFmOJpJ7CayLpa9SKL2b
SrcStorageEndPoint=oss-cn-shenzhen.aliyuncs.com
SrcStorageIsPrivateBucket=0
SrcStoragePrefix=dir1/

[CosInfo]
CosAppId=10234599
CosSecretId=fgvssa5a2DsULCp6MFa5bYs1CisMlEPf
CosSecretKey=ZjHRXsadfasdfaS5Mu3hB4nxVe5F2Ku
CosBucket=test
```

迁移文件 a.txt

***注意：这里是对文件名进行前缀匹配，如果有 a.txt2 这样的文件，会一并迁移。***

``` 
[ToolConfig]
Concurrency=10
TotalNum=

[SrcStorageInfo]
SrcStorageBucket=test
SrcStorageAccessKey=oEdafddccEPScbD
SrcStorageSecretKey=DkfgiG8nEntzFmOJpJ7CayLpa9SKL2b
SrcStorageEndPoint=oss-cn-shenzhen.aliyuncs.com
SrcStorageIsPrivateBucket=0
SrcStoragePrefix=a.txt

[CosInfo]
CosAppId=10234599
CosSecretId=fgvssa5a2DsULCp6MFa5bYs1CisMlEPf
CosSecretKey=ZjHRXsadfasdfaS5Mu3hB4nxVe5F2Ku
CosBucket=test
```

#### 高级配置

##### 并发配置

控制同时迁移的文件数，为了加快迁移速度、跑满带宽，可适当将该值调大，比如：若带宽为20Mb/s以上，可以将 Concurrency 的值设为100；若带宽较小，可以适当调小，以保证下载和上传的成功率。

``` 
[ToolConfig]
Concurrency=10
```

#### 启动迁移

所有工具都放置在工具包的 bin 目录下，所以，首先请进入 bin 目录

``` 
cd 到工具目录的存放目录
cd cos_migration_tools/bin
```

运行以下命令启动迁移：

``` 
./start.sh aliyun & 
```

由于在命令中指定了&符号，所以迁移任务会在后台运行。

迁移工具会首先从阿里云存储获取所有文件列表，然后按照配置的并发数，将任务拆分，并发执行下载和上传。任务拆分完，界面会输出：start task down. use ./stat.sh to see task status，注意，此条输出只表示任务启动完毕，此时迁移任务还很有可能正在进行。若想得知迁移是否完成，可以进一步使用【查看迁移进度】命令。

运行界面大致如下：

![image_1aogaou7ir6bud31svn1hg51vdh9.png-27kB][3]

#### 查看迁移进度

``` 
./stat.sh
```

会输出要迁移的文件总数，以及已经迁移成功和迁移失败的文件数。

若文件列表还没有拉取完毕，会每3秒输出一次当前已获取的文件数，输出为这样：

![image_1aogargqk618pnm122p24huegm.png-16.3kB][4]

当所有列表拉取完毕，开始执行下载和上传，会每3秒输出一次已上传成功的文件数和失败的文件数，类似这样：

![image_1aogat3gu1q2pmsvnlc1jos1k11g.png-200.3kB][5]

工具退出方法： ctrl-c

若输出异常可以使用【查看迁移进展详情】命令，查看具体情况。

若有失败的迁移文件，可以使用【获取失败文件信息】命令，查看失败原因，处理方法见【异常处理】。

#### 查看迁移进展详情

``` 
./stat_detail.sh
```

会输出迁移工具运行的详细情况。正常情况下，若开始进行上传下载，输出为这样：

![image_1aogav373v9l1d0c1hsp4dk2i21t.png-126.6kB][6]

迁移完后 工具会自动推出。

工具退出方法： kill 后台进程号。

#### 询问任务是否结束

``` 
./is_still_doing.sh
```

如果迁移已经完成会输出：no, task has been done

如果还在迁移会输出：yes, still doing download and upload...并且输出正在运行的进程信息

![image_1aogb0e231ti41h88osue0p3162a.png-54.8kB][7]

#### 停止迁移

``` 
./stop.sh
```

运行该脚本后，迁移任务就会停止，之后想再启动，可以重启迁移任务。

工具退出方法： kill 后台进程号。

#### 重启迁移任务

``` 
./stat.sh
```

如果有输出 has migrate[XX] files, will migrate[XX] files 的信息，如下图，说明文件列表已经获取完毕，可以不再拉取文件列表重启。

![image_1aogccamq1rq2f0fai461ctk82n.png-25.3kB][8]

如果没有输出，说明列表没有获取完毕，再次启动时，需要重新运行【启动迁移】命令。

#### 不再拉取文件列表重启

``` 
./restart_not_get_file_list.sh aliyun & 
```

#### 获取失败文件信息

``` 
./get_failed_info.sh 
```

可以获取失败文件的信息。

## 使用注意

1. 如果希望重新迁移已经迁移过的文件，则需要清空 output 文件夹中的文件。
2. 迁移的时候，把新拉取下来的文件，和之前迁移成功的文件去重，并生成形如 filelist.1470216681 的文件，这个文件内容是原始拉取下来的文件列表，而这个 filelist 文件是去重后的结果。

## 常见错误

#### 客户端异常

1. 未安装 php 时会报错：

   ![IMG of tool-cos_migration/PHP fail.png](https://mc.qcloudimg.com/static/img/694748c11829d1b6d15ab26a7a961b60/%7B24D8F2F9-496D-4115-AF95-E240F4040D2A%7D.png)

2. 未按照 php-curl 时会报错：

   ![](https://mc.qcloudimg.com/static/img/6c47948fa04f500a7681b47335ad53f9/%7BDA9F1329-7E87-4C42-AAE0-17A7E5205E32%7D.png)

#### 服务端异常

1.若中途异常，可以【停止迁移】，或者【查看迁移进展详情】。

2.若在【查看迁移进度】结果中有失败的迁移文件，例如下图：

![image_1aogd6r101ol91ulo13upqhn6t334.png-17.2kB][9]

此时不必紧张，等所有任务都跑完后（输入【询问任务是否结束】命令，显示任务已经结束），使用【不再拉取文件列表重启】命令，会把失败的任务重新执行，已成功的不会再执行。



[1]: http://static.zybuluo.com/kitman/vra14dp3li42tta0ed8hl2r8/image_1aog2g81ghgqmk210p4146c8tr9.png
[2]: http://static.zybuluo.com/kitman/96r1eb6are7a4p737jodmmkp/image_1aog2gr3u2ek17a813gh8o1ts4m.png
[3]: http://static.zybuluo.com/kitman/4wu3xtjfi8rvjl646wdjn2lq/image_1aogaou7ir6bud31svn1hg51vdh9.png
[4]: http://static.zybuluo.com/kitman/4jk4uzjbmr3j9wia8msmd7uf/image_1aogargqk618pnm122p24huegm.png
[5]: http://static.zybuluo.com/kitman/oz0v85p3ncihhnycj45ctrtx/image_1aogat3gu1q2pmsvnlc1jos1k11g.png
[6]: http://static.zybuluo.com/kitman/1o0uy9q8o6bxa8a2206n8n9c/image_1aogav373v9l1d0c1hsp4dk2i21t.png
[7]: http://static.zybuluo.com/kitman/nqpfhcfkptl1ouyqe14grw7r/image_1aogb0e231ti41h88osue0p3162a.png
[8]: http://static.zybuluo.com/kitman/pwfj0l4trr5wtzbwinrqwwle/image_1aogccamq1rq2f0fai461ctk82n.png
[9]: http://static.zybuluo.com/kitman/y3951vvy960s7rr5t55xrdux/image_1aogd6r101ol91ulo13upqhn6t334.png
