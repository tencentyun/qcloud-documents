## 功能说明

使用 COSCMD 工具，用户可通过简单的命令行指令实现对对象（Object）的批量上传、下载、删除等操作。

> !使用该工具上传同名文件，会覆盖较旧的同名文件，不支持校对是否存在同名文件的功能。

## 使用环境

#### 系统环境

支持 Windows、Linux 和 macOS 系统。

> ?
>
> - 请保证本地字符格式为 UTF-8，否则操作中文文件会出现异常。
> - 请确保本机时间已经与国际标准时间校准，如误差过大，将导致无法正常使用。

#### 软件依赖

- Python 2.7/3.5/3.6。
- 最新版本的 pip。

#### 安装及配置

- 环境安装与配置详细操作请参见 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866)。
- pip 环境安装与配置详细操作请参见 [官网 pip 安装说明](https://pip.pypa.io/en/stable/installing/)。

## 下载与安装

#### pip 安装

执行`pip`命令进行安装：

```shell
pip install coscmd
```

 安装成功之后，用户可以通过`-v`或者`--version`命令查看当前的版本信息。

#### pip 更新

执行`pip`命令进行更新：

```sh
pip install coscmd -U
```

> ! 当 pip 版本号大于等于10.0.0 时，升级或安装依赖库时可能会出现失败，建议使用 pip 版本 9.x（pip install pip==9.0.0）。

#### 源码安装（不推荐）

源码下载地址：[单击此处](https://github.com/tencentyun/coscmd.git)。

```shell
git clone https://github.com/tencentyun/coscmd.git
cd coscmd
python setup.py install
```

> !Python 版本为2.6时，pip 安装依赖库时容易失败，推荐使用该方法安装。

#### 离线安装

> ! 请确保两台机器的 Python 版本保持一致，否则会出现安装失败的情况。

```sh
# 在有外网的机器下运行如下命令
mkdir coscmd-packages
pip download coscmd -d coscmd-packages
tar -czvf coscmd-packages.tar.gz coscmd-packages

# 将安装包拷贝到没有外网的机器后运行如下命令
tar -xzvf coscmd-packages.tar.gz
pip install coscmd --no-index -f coscmd-packages
```

## 使用方法

### 查看 help

用户可通过`-h`或`--help`命令来查看工具的 help 信息。

```shell
coscmd -h  //查看当面版本信息
```

help 信息如下所示：

```shell
usage: coscmd [-h] [-d] [-b BUCKET] [-r REGION] [-c CONFIG_PATH] [-l LOG_PATH]
              [-v]
              
              {info,restore,createbucket,signurl,listparts,mget,list,upload,deletebucket,abort,getbucketversioning,putbucketacl,getobjectacl,download,putobjectacl,copy,config,putbucketversioning,getbucketacl,delete}
              ...

an easy-to-use but powerful command-line tool. try 'coscmd -h' to get more
informations. try 'coscmd sub-command -h' to learn all command usage, likes
'coscmd upload -h'

positional arguments:
  {info,restore,createbucket,signurl,listparts,mget,list,upload,deletebucket,abort,getbucketversioning,putbucketacl,getobjectacl,download,putobjectacl,copy,config,putbucketversioning,getbucketacl,delete}
    config              Config your information at first
    upload              Upload file or directory to COS
    download            Download file from COS to local
    delete              Delete file or files on COS
    abort               Aborts upload parts on COS
    copy                Copy file from COS to COS
    list                List files on COS
    listparts           List upload parts
    info                Get the information of file on COS
    mget                Download file from COS to local
    restore             Restore
    signurl             Get download url
    createbucket        Create bucket
    deletebucket        Delete bucket
    putobjectacl        Set object acl
    getobjectacl        Get object acl
    putbucketacl        Set bucket acl
    getbucketacl        Get bucket acl
    putbucketversioning
                        Set the versioning state
    getbucketversioning
                        Get the versioning state

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Debug mode
  -b BUCKET, --bucket BUCKET
                        Specify bucket
  -r REGION, --region REGION
                        Specify region
  -c CONFIG_PATH, --config_path CONFIG_PATH
                        Specify config_path
  -l LOG_PATH, --log_path LOG_PATH
                        Specify log_path
  -v, --version         show program's version number and exit
```

除此之外，用户还可以在每个命令后（不加参数）输入`-h`查看该命令的具体用法，例如：

```shell
coscmd upload -h  //查看 upload 命令使用方法
```

### 配置参数

COSCMD 工具在使用前需要进行参数配置，用户可以通过如下命令来配置：

```shell
coscmd config [OPTION]...<FILE>...
			  [-h] --help
			  [-a] <SECRET_ID>
			  [-s] <SECRET_KEY>
			  [-t] <TOKEN>
			  [-b] <BucketName-APPID>
              [-r] <REGION> | [-e] <ENDPOINT>
              [-m] <MAX_THREAD>
              [-p] <PART_SIZE>
              [--do-not-use-ssl]
              [--anonymous]   
```

通常情况下，如您只需要进行简单的配置，可参照如下操作示例配置即可：

```shell
coscmd config -a AChT4ThiXAbpBDEFGhT4ThiXAbp**** -s WE54wreefvds3462refgwewe**** -b examplebucket-1250000000 -r ap-beijing
```

> ?其中 "[]" 中的字段为选项， "<>" 的字段为需要填写的参数。

参数配置说明如下：

| 选项             | 参数说明                                                     | 是否必选 | 有效值 |
| :--------------- | :----------------------------------------------------------- | -------- | ------ |
| -a               | 密钥 ID 请前往 [API 密钥控制台](https://console.cloud.tencent.com/cam/capi) 获取 | 是       | 字符串 |
| -s               | 密钥 Key 请前往 [API 密钥控制台](https://console.cloud.tencent.com/cam/capi) 获取 | 是       | 字符串 |
| -t               | 临时密钥 token，当使用临时密钥时需要配置，设置 x-cos-security-token 头部 | 否       | 字符串 |
| -b               | 指定的存储桶名称，存储桶的命名格式为 BucketName-APPID，请参见 [命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) | 是       | 字符串 |
| -r               | 存储桶所在地域，请参见 [地域和访问域名](https://cloud.tencent.com/doc/product/436/6224) | 是       | 字符串 |
| -e               | 设置请求的 ENDPOINT，设置 ENDPOINT 参数后，REGION 参数会失效 | 否       | 字符串 |
| -m               | 多线程操作的最大线程数（默认为5，范围为1 - 30）              | 否       | 数字   |
| -p               | 分块操作的单块大小（单位MB，默认为1MB，范围为1 - 1000）      | 否       | 数字   |
| --do-not-use-ssl | 使用 HTTP 协议，而不使用 HTTPS                               | 否       | 字符串 |
| --anonymous      | 匿名操作（不携带签名）                                       | 否       | 字符串 |

> ?
1. 可以直接编辑`~/.cos.conf`文件 （在 Windows 环境下，该文件是位于【我的文档】下的一个隐藏文件），该文件初始时不存在，是通过`coscmd config`命令生成，用户也可以手动创建。
配置完成之后的`.cos.conf`文件内容示例如下所示：
```shell
 [common]
secret_id = AChT4ThiXAbpBDEFGhT4ThiXAbp****
secret_key = WE54wreefvds3462refgwewe****
bucket = examplebucket-1250000000
region = ap-beijing
max_thread = 5
part_size = 1
schema = https
```
> 2. 可以在配置文件中增加`schema` 项来选择`http/https`，默认为`https`。
> 3. 可以在 `anonymous` 项中选择`True/False`，来使用匿名模式，即签名保持为空。



### 指定 Bucket 和 Region 的命令

- 通过`-b <BucketName-APPID>`指定 Bucket， 可以指定特定的 Bucket。
- 存储桶的命名格式为 BucketName-APPID，此处填写的存储桶名称必须为此格式。
- 通过`-r <region>`指定 Region， 可以指定特定的 Region。

```shell
#命令格式
coscmd -b <BucketName-APPID> -r <region> <action> ...
#操作示例-创建bucket
coscmd -b examplebucket-1250000000 -r ap-beijing createbucket
#操作示例-上传文件
coscmd -b examplebucket-1250000000 -r ap-beijing upload exampleobject exampleobject

```

### 创建存储桶

- 建议配合`-b <BucketName-APPID>`指定 Bucket 和`-r <region>`指定 Region 使用。

```shell
#命令格式
coscmd -b <BucketName-APPID> createbucket
#操作示例
coscmd createbucket
coscmd -b examplebucket-1250000000 -r ap-beijing createbucket

```

### 删除存储桶

- 建议配合`-b <BucketName-APPID>`指定 Bucket 和`-r <region>`指定 Region 使用。

```shell
#命令格式
coscmd -b <BucketName-APPID> deletebucket
#操作示例
coscmd deletebucket
coscmd -b examplebucket-1250000000 -r ap-beijing deletebucket
coscmd -b examplebucket-1250000000 -r ap-beijing deletebucket -f

```

- 使用`-f`参数则会强制删除该存储桶，包括所有文件、开启版本控制之后历史文件夹、上传产生的碎片。

### 上传文件或文件夹

- 上传文件命令如下：

```shell
#命令格式
coscmd upload <localpath> <cospath>
#操作示例
#将本地的 /data/exampleobject 文件上传到 cos 的 data/exampleobject 路径下
coscmd upload /data/exampleobject data/exampleobject 
coscmd upload /data/exampleobject data/
#指定头部上传文件
#指定对象类型，上传一个归档的文件
coscmd upload /data/exampleobject data/exampleobject -H "{'x-cos-storage-class':'Archive'}"
#设置 meta 元属性
coscmd upload /data/exampleobject data/exampleobject -H "{'x-cos-meta-example':'example'}"

```

- 上传文件夹命令如下：

```shell
#命令格式
coscmd upload -r <localpath> <cospath>
#操作示例
coscmd upload -r /data/examplefolder data/examplefolder
coscmd upload -r /data/examplefolder data/examplefolder
#cos上的存储路径为 examplefolder2/examplefolder
coscmd upload -r /data/examplefolder examplefolder2/
#上传到 bucket 根目录
coscmd upload -r /data/examplefolder/ /
#同步上传，跳过md5相同的文件
coscmd upload -rs /data/examplefolder data/examplefolder
#忽略 .txt 和 .doc 的后缀文件
coscmd upload -rs /data/examplefolder data/examplefolder --ignore *.txt,*.doc

```

 请将 "<>" 中的参数替换为您需要上传的本地文件路径（localpath），以及 COS 上存储的路径（cospath）。

> !
>
> - 上传文件时需要将 COS 上的路径包括文件（文件夹）的名字补全（参考例子）。
> - COSCMD 支持大文件断点上传功能；当分片上传大文件失败时，重新上传该文件只会上传失败的分块，而不会从头开始（请保证重新上传的文件的目录以及内容和上传的目录保持一致）。
> - COSCMD 分块上传时会对每一块进行 MD5 校验。
> - COSCMD 上传默认会携带 `x-cos-meta-md5` 的头部，值为该文件的 md5 值。
> - 使用 -s 参数可以使用同步上传，跳过上传 md5 一致的文件（COS 上的原文件必须是由 1.8.3.2 之后的 COSCMD 上传的，默认带有 x-cos-meta-md5 的 header）。
> - 使用 -H 参数设置 HTTP header 时，请务必保证格式为 JSON，示例：`coscmd upload -H "{'x-cos-storage-class':'Archive','Content-Language':'zh-CN'}" <localpath> <cospath>`。更多头部可参见 [PUT Object](https://cloud.tencent.com/document/product/436/7749) 文档。
> - 在上传文件夹时，使用`--ignore`参数可以忽略某一类文件，支持 shell 通配规则，支持多条规则，用逗号`,`分隔。当忽略一类后缀时，必须最后要输入`,` 或者加入`""`。
> - 目前只支持上传最大40TB的单一文件。

### 下载文件或文件夹

- 下载文件命令如下：

```shell
#命令格式
coscmd download <cospath> <localpath>
#操作示例
coscmd download data/exampleobject /data/exampleobject
coscmd download data/exampleobject /data/

```

- 下载文件夹命令如下：

```shell
#命令格式
coscmd download -r <cospath> <localpath>
#操作示例
coscmd download -r data/examplefolder/ /data/examplefolder
coscmd download -r data/examplefolder/ /data/
#覆盖下载当前bucket根目录下所有的文件
coscmd download -rf / /data/examplefolder
#同步下载当前 bucket 根目录下所有的文件，跳过 md5校验相同的文件
coscmd download -rs / /data/examplefolder
#忽略 .txt 和 .doc 的后缀文件
coscmd download -rs / /data/examplefolder --ignore *.txt,*.doc 

```

请将 "<>" 中的参数替换为您需要下载的 COS 上文件的路径（cospath），以及本地存储路径（localpath）。

> !
>
> - 老版本的 mget 接口已经废除，download 接口使用分块下载，请使用 download 接口。
> - 若本地存在同名文件，则会下载失败，需要使用`-f`参数覆盖本地文件。
> - 使用 `-s` 或者 `--sync` 参数，可以在下载文件夹时跳过本地已存在的相同文件（前提是下载的文件是通过 COSCMD 的 upload 接口上传的，文件携带有 `x-cos-meta-md5` 头部）。
> - 在下载文件夹时，使用`--ignore`参数可以忽略某一类文件，支持 shell 通配规则，支持多条规则，用逗号`,`分隔。当忽略一类后缀时，必须最后要输入`,`或者加入`""`。

### 删除文件或文件夹

- 删除文件命令如下：

```shell
#命令格式
coscmd delete <cospath>
#操作示例
coscmd delete data/exampleobject

```

- 删除文件夹命令如下：

```shell
#命令格式
coscmd delete -r <cospath>
#操作示例
coscmd delete -r /data/examplefolder/
coscmd delete -r /
```

 请将"<>"中的参数替换为您需要删除的 COS 上文件的路径（cospath），工具会提示用户是否确认进行删除操作。

> !批量删除需要输`y`入确定，使用`-f`参数则可以跳过确认直接删除。

### 查询分块上传文件碎片

- 命令如下：

```shell
#命令格式
coscmd listparts <cospath>
#操作示例
coscmd listparts examplefolder/
```

### 清除分块上传文件碎片

- 命令如下：

```shell
#命令格式
coscmd abort
#操作示例
coscmd abort
```

### 复制文件或文件夹

- 复制文件命令如下：

```shell
#命令格式
coscmd copy <sourcepath> <cospath> 
#操作示例
#复制 examplebucket2-1250000000 存储桶下的 data/exampleobject 对象到 examplebucket1-1250000000 存储桶的 data/examplefolder/exampleobject
coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy examplebucket2-1250000000.ap-beijing.myqcloud.com/data/exampleobject data/examplefolder/exampleobject
#修改存储类型，将文件类型改为低频
coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy examplebucket2-1250000000.ap-beijing.myqcloud.com/data/exampleobject data/examplefolder/exampleobject -H "{'x-cos-storage-class':'STANDARD_IA'}"
#修改存储类型，将文件类型改为归档
coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy examplebucket2-1250000000.ap-beijing.myqcloud.com/data/exampleobject data/examplefolder/exampleobject -H "{'x-cos-storage-class':'Archive'}"
```

- 复制文件夹命令如下：

```shell
#命令格式
coscmd copy -r <sourcepath> <cospath>
#操作示例
#复制 examplebucket2-1250000000 存储桶下的 examplefolder 目录到 examplebucket1-1250000000 存储桶的 examplefolder 目录
coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy -r examplebucket2-1250000000.cos.ap-guangzhou.myqcloud.com/examplefolder/ examplefolder
coscmd -b examplebucket1-1250000000 -r ap-guangzhou copy -r examplebucket2-1250000000.cos.ap-guangzhou.myqcloud.com/examplefolder/ examplefolder/

```

请将"<>"中的参数替换为您需要复制的 COS 上文件的路径（sourcepath），和您需要复制到 COS 上文件的路径（cospath）。

> ?
>
> - sourcepath 的格式为：`<BucketName-APPID>.cos.<region>.myqcloud.com/<cospath>`。
> - 使用 -d 参数可以设置 `x-cos-metadata-directive` 参数，可选值为 Copy 和 Replaced，默认为 Copy。
> - 使用 -H 参数设置 HTTP header 时，请务必保证格式为 JSON，示例：`coscmd copy -H -d Replaced "{'x-cos-storage-class':'Archive','Content-Language':'zh-CN'}" <localpath> <cospath>`。更多头部请参见 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 文档。

### 查询文件列表

查询命令如下：

```shell
#命令格式
coscmd list <cospath>

#操作示例
#递归查询该存储桶下所有的文件列表
coscmd list -ar
#递归查询 examplefolder 前缀的所有文件列表
coscmd list examplefolder/  -ar
```

请将"<>"中的参数替换为您需要查询文件列表的 COS 上文件的路径（cospath）。

- 使用`-a`查询全部文件。
- 使用`-r`递归查询，并且会在末尾返回列出文件的数量和大小之和。
- 使用`-n num`设置查询数量的最大值。

>?`<cospath>`为空默认查询当前存储桶根目录。

### 显示文件信息

命令如下：

```shell
#命令格式
coscmd info <cospath> 

#操作示例
coscmd info exampleobject
```

请将"<>"中的参数替换为您需要显示的 COS 上文件的路径（cospath）。

### 获取带签名的下载 URL

命令如下：

```shell
#命令格式
coscmd signurl <cospath>

#操作示例
coscmd signurl exampleobject
coscmd signurl exampleobject -t 100
```

请将 "<>" 中的参数替换为您需要获取下载 URL 的 COS 上文件的路径（cospath）。
使用`-t time`设置查询签名的有效时间（单位为秒）。

### 开启/暂停版本控制

命令如下：

```shell
#命令格式
coscmd putbucketversioning <status>

#开启版本控制
coscmd putbucketversioning Enabled

#暂停版本控制
coscmd putbucketversioning Suspended
```

请将 "<>" 中的参数替换为您需要版本控制状态（status）。

> !一旦您对存储桶启用了版本控制，它将无法返回到未启用版本控制状态（初始状态）。但是，您可以对该存储桶暂停版本控制，这样后续上传的对象将不会产生多个版本。

### 恢复归档文件

- 恢复归档文件命令如下：

```shell
#命令格式
coscmd restore <cospath>
#操作示例
coscmd restore -d 3 -t Expedited exampleobject
```

- 批量恢复归档文件命令如下：

```shell
#命令格式
coscmd restore -r <cospath>
#操作示例
coscmd restore -r -d 3 -t Expedited examplefolder/
```

 请将 "<>" 中的参数替换为您需要查询文件列表的 COS 上文件的路径（cospath）。

- 使用`-d day`设置临时副本的过期时间，默认值：7。
- 使用`-t tier`具体复原过程类型，枚举值： Expedited （极速模式） ，Standard （标准模式），Bulk（批量模式），默认值：Standard。

### Debug 模式执行命令

在各命令前加上`-d`或者`-debug`，在命令执行的过程中，会显示详细的操作信息 。示例如下：

```shell
#显示 upload 的详细操作信息，命令格式：
coscmd -d upload <localpath> <cospath>

#操作示例
coscmd -d upload exampleobject exampleobject
```

## 常见问题

如您在使用 COSCMD 工具过程中，有相关的疑问，请参见 [COSCMD 工具类常见问题](https://cloud.tencent.com/document/product/436/30744)。
