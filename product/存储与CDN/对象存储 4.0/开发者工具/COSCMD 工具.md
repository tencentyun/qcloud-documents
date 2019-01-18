## 功能说明
使用 COSCMD 工具，用户可通过简单的命令行指令实现对对象（Object）的批量上传、下载、删除等操作。

## 使用环境

### 系统环境

Windows 或 Linux 系统。

>?请保证本地字符格式为 UTF-8，否则操作中文文件会出现异常。

### 软件依赖

- Python 2.7/3.5/3.6。
- 最新版本的 pip。

#### 安装及配置

环境安装与配置详细操作请参考 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866)。

## 下载与安装
安装 pip 有以下几种方式：

- **pip 安装**
  执行`pip`命令进行安装：
```sh
pip install coscmd
```

 安装成功之后，用户可以通过`-v`或者`--version`命令查看当前的版本信息。
- **pip 更新**
  执行`pip`命令进行更新：
```sh
pip install coscmd -U
```
>! 当 pip 版本大于等于10.0.0 时，升级或安装依赖库时可能会出现失败，建议使用 pip 版本 9.x（pip install pip==9.0.0）。

- **源码安装(不推荐)**
  下载链接：[GitHub 链接](https://github.com/tencentyun/coscmd.git)。
```shell
git clone https://github.com/tencentyun/coscmd.git
cd coscmd
python setup.py install
```
>!Python 版本为2.6时，pip 安装依赖库时容易失败，推荐使用该方法安装。

- **离线安装**
```sh
# 在有外网的机器下运行如下命令
mkdir coscmd-packages
pip download coscmd -d coscmd-packages
tar -czvf coscmd-packages.tar.gz coscmd-packages
```
>! 请确保两台机器的 python 版本保持一致，否则会出现安装失败的情况。
>```sh
># 将安装包拷贝到没有外网的机器后运行如下命令
>tar -xzvf coscmd-packages.tar.gz
>pip install coscmd --no-index -f coscmd-packages
```

## 使用方法

### 查看 help

用户可通过`-h`或`--help`命令来查看工具的 help 信息。
```shell
coscmd -h  //查看当面版本信息
```

help 信息如下所示：
```shell
usage: cos_cmd.py [-h] [-d] [-b BUCKET] [-r REGION] [-c CONFIG_PATH]
                  [-l LOG_PATH] [-v]
                  {config,upload,download,delete,copy,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
                  ...

an easy-to-use but powerful command-line tool. try 'coscmd -h' to get more
informations. try 'coscmd sub-command -h' to learn all command usage, likes
'coscmd upload -h'

positional arguments:
  {config,upload,download,delete,copy,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
    config              config your information at first.
    upload              upload file or directory to COS.
    download            download file from COS to local.
    delete              delete file or files on COS
    copy                copy file from COS to COS.
    list                list files on COS
    info                get the information of file on COS
    mget                download file from COS to local.
    restore             restore
    signurl             get download url
    createbucket        create bucket
    deletebucket        delete bucket
    putobjectacl        set object acl
    getobjectacl        get object acl
    putbucketacl        set bucket acl
    getbucketacl        get bucket acl

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           debug mode
  -b BUCKET, --bucket BUCKET
                        set bucket
  -r REGION, --region REGION
                        set region
  -c CONFIG_PATH, --config_path CONFIG_PATH
                        set config_path
  -l LOG_PATH, --log_path LOG_PATH
                        set log_path
  -v, --version         show program's version number and exit
```

除此之外，用户还可以在每个命令后（不加参数）输入`-h`查看该命令的具体用法，例如：
```shell
coscmd upload -h  //查看 upload 命令使用方法
```

### 配置参数

COSCMD 工具在使用前需要进行参数配置，用户可以通过如下命令来配置：
```shell
coscmd  config [-h] -a <SECRET_ID> -s <SECRET_KEY> -b <BUCKET>
                         (-r <REGION> | -e <ENDPOINT>) [-m <MAX_THREAD>]
                         [-p <PART_SIZE>] [-u <APPID>] [--do-not-use-ssl]
                         [--anonymous <ANONYMOUS>]      
```
上述示例中使用 "<>" 的字段为必选参数，使用 "[]" 的字段为可选参数，其中：

| 名称       | 描述                                                         | 有效值 |
| :--------- | :----------------------------------------------------------- | :----- |
| SECRET_ID  | 必选参数，APPID 对应的密钥 ID 可从 COS 控制台左侧栏【密钥管理】或 [云 API 密钥控制台]( https://console.cloud.tencent.com/cam/capi) 获取 | 字符串 |
| SECRET_KEY | 必选参数，APPID 对应的密钥 Key 可从 COS 控制台左侧栏【密钥管理】或 [云 API 密钥控制台]( https://console.cloud.tencent.com/cam/capi) 获取 | 字符串 |
| BUCKET     | 必选参数，指定的存储桶名称，bucket的命名规则为{name}-{appid} ，参考 [创建存储桶](https://cloud.tencent.com/doc/product/436/6232) | 字符串 |
| REGION     | 必选参数，存储桶所在地域，参考 [可用地域](https://cloud.tencent.com/doc/product/436/6224) | 字符串 |
| MAX_THREAD | 可选参数，多线程上传时的最大线程数（默认为5）               | 数字   |
| PART_SIZE  | 可选参数，分块上传的单块大小（单位MB，默认为1MB）        | 数字   |


>!
- 可以直接编辑`~/.cos.conf`文件 （在 Windows 环境下，该文件是位于**我的文档**下的一个隐藏文件），该文件初始时不存在，是通过`coscmd config`命令生成，用户也可以手动创建。
  配置完成之后的`.cos.conf`文件内容示例如下所示：
```shell
 [common]
secret_id = AChT4ThiXAbpBDEFGhT4ThiXAbpHIJK
secret_key = WE54wreefvds3462refgwewerewr
bucket = ABC-1234567890
region = ap-guangzhou
max_thread = 5
part_size = 1
schema = https
```
- 可以在配置文件中增加`schema`项来选择`http/https`，默认为`https`。
- 可以在`anonymous`项中选择`True/False`，来使用匿名模式，即签名保持为空。
- bucket 的命名规则为`{name}-{appid}`。


### 指定 Bucket 的命令
-  通过`-b <bucket> 指定 Bucket`， 可以指定特定的 Bucket。
-  Bucket 的命名规则为`{name}-{appid}`，此处填写的存储桶名称必须为此格式。
```sh
#命令格式
coscmd -b <bucket> method ...
#操作示例-上传文件
coscmd -b AAA-12345567 upload a.txt b.txt
#操作示例-创建bucket
coscmd -b AAA-12344567 createbucket
```

### 创建存储桶
-  建议配合`-b <bucket> 指定 Bucket`使用。
```sh
#命令格式
coscmd -b <bucket> createbucket
#操作示例
coscmd createbucket
coscmd -b AAA-12344567 createbucket
```

### 删除存储桶
-  建议配合`-b <bucket> 指定 Bucket`使用。
```sh
#命令格式
coscmd -b <bucket> deletebucket
#操作示例
coscmd deletebucket
coscmd -b AAA-12344567 deletebucket
coscmd -b AAA-12344567 deletebucket -f
```

- 使用 -f 参数则会强制删除该 bucket，包括所有文件、开启版本控制之后历史文件夹、上传产生的碎片。

### 上传文件或文件夹
- 上传文件命令如下：
```sh
#命令格式
coscmd upload <localpath> <cospath>
#操作示例
coscmd upload /home/aaa/123.txt bbb/123.txt
coscmd upload /home/aaa/123.txt bbb/
```
- 上传文件夹命令如下：
```sh
#命令格式
coscmd upload -r <localpath> <cospath>
#操作示例
coscmd upload -r /home/aaa/ bbb/aaa
coscmd upload -r /home/aaa/ bbb/
#该操作会在bbb/目录下新建一个aaa/文件夹
coscmd upload -r /home/aaa  bbb/
#上传到bucket根目录
coscmd upload -r /home/aaa/ /
#同步上传，跳过md5相同的文件
coscmd upload -rs /home/aaa/ /home/aaa
#忽略.txt和.doc的后缀文件
coscmd upload -rs /home/aaa/ /home/aaa --ignore *.txt,*.doc
```

 请将 "<>" 中的参数替换为您需要上传的本地文件路径（localpath），以及 COS 上存储的路径（cospath）。
 
 >!
 >  - 上传文件时需要将 COS 上的路径包括文件（文件夹）的名字补全（参考例子）。
 >  - COSCMD 支持大文件断点上传功能；当分片上传大文件失败时，重新上传该文件只会上传失败的分块，而不会从头开始（请保证重新上传的文件的目录以及内容和上传的目录保持一致）。
 >  - COSCMD 分块上传时会对每一块进行 MD5 校验。
 >  - COSCMD 上传默认会携带`x-cos-meta-md5`的头部，值为该文件的`md5`值。
 >  - 使用 -s 参数可以使用同步上传，跳过上传 md5 一致的文件（COS 上的原文件必须是由 1.8.3.2 之后的 COSCMD 上传的，默认带有 x-cos-meta-md5 的 header）。
 >  - 使用 -H 参数设置 HTTP header 时，请务必保证格式为 json，示例：`coscmd upload -H '{"Cache-Control":"max-age=31536000","Content-Language":"zh-CN"}' <localpath> <cospath>`。
 >  - 在上传文件夹时，使用 --ignore 参数可以忽略某一类文件，支持 shell 通配规则，支持多条规则，用逗号`,`分隔。当忽略一类后缀时，必须最后要输入`,` 或者加入`""`。
 >  - 目前只支持上传最大40TB的单一文件。

### 下载文件或文件夹
- 下载文件命令如下：
```sh
#命令格式
coscmd download <cospath> <localpath>
#操作示例
coscmd download bbb/123.txt /home/aaa/111.txt
coscmd download bbb/123.txt /home/aaa/
```
- 下载文件夹命令如下：
```sh
#命令格式
coscmd download -r <cospath> <localpath>
#操作示例
coscmd download -r /home/aaa/ bbb/aaa
coscmd download -r /home/aaa/ bbb/
#覆盖下载当前bucket根目录下所有的文件
coscmd download -rf / bbb/aaa
#同步下载当前bucket根目录下所有的文件，跳过md5校验相同的文件
coscmd download -rs / bbb/aaa
#忽略.txt和.doc的后缀文件
coscmd download -rs / bbb/aaa --ignore *.txt,*.doc 
```
请将 "<>" 中的参数替换为您需要下载的 COS 上文件的路径（cospath），以及本地存储路径（localpath）。
>!
> - 若本地存在同名文件，则会下载失败，使用`-f`参数覆盖本地文件。
> - `download`接口使用分块下载，老版本的`mget`接口已经废除，请使用`download`接口。
> - 使用`-s`或者`--sync`参数，可以在下载文件夹时跳过本地已存在的相同文件（前提是下载文件夹是通过`COSCMD`的`upload`接口上传的，文件携带有 `x-cos-meta-md5`头部）。
> - 在下载文件夹时，使用 --ignore 参数可以忽略某一类文件，支持 shell 通配规则，支持多条规则，用逗号`,`分隔。当忽略一类后缀时，必须最后要输入`,`或者加入`""`。

### 删除文件或文件夹
- 删除文件命令如下：
```sh
#命令格式
coscmd delete <cospath>
#操作示例
coscmd delete bbb/123.txt
```
- 删除文件夹命令如下：
```sh
#命令格式
coscmd delete -r <cospath>
#操作示例
coscmd delete -r bbb/
coscmd delete -r /
```

 请将"<>"中的参数替换为您需要删除的 COS 上文件的路径（cospath），工具会提示用户是否确认进行删除操作。

 >!批量删除需要输入确定，使用`-f`参数跳过确认。

### 清除上传文件碎片
- 命令如下：
```sh
#命令格式
coscmd abort
#操作示例
coscmd abort
```

### 复制文件或文件夹
- 复制文件命令如下：
```sh
#命令格式
coscmd copy <sourcepath> <cospath> 
#操作示例
coscmd copy bucket-appid.cos.ap-guangzhou.myqcloud.com/a.txt aaa/123.txt
```
- 复制文件夹命令如下：
```sh
#命令格式
coscmd copy -r <sourcepath> <cospath>
#操作示例
coscmd copy -r bucket-appid.cos.ap-guangzhou.myqcloud.com/coscmd/ aaa
coscmd copy -r bucket-appid.cos.ap-guangzhou.myqcloud.com/coscmd/ aaa/
```

 请将"<>"中的参数替换为您需要复制的 COS 上文件的路径（sourcepath），和您需要复制到 COS 上文件的路径（cospath）

 >!sourcepath 的样式如下：```<bucketname>-<appid>.cos.<region>.myqcloud.com/<cospath>```。

### 打印文件列表
打印命令如下：
```sh
#命令格式
coscmd list <cospath>

#操作示例
coscmd list -a
coscmd list bbb/123.txt  -r -n 10
```
请将"<>"中的参数替换为您需要打印文件列表的 COS 上文件的路径（cospath）。
 - 使用`-a`打印全部文件。
 - 使用 `-r` 递归打印，并且会在末尾返回列出文件的数量和大小之和。
 - 使用 `-n num` 设置打印数量的最大值。

>!`<cospath>`为空默认打印当前 Bucket 根目录。

### 显示文件信息
命令如下：
```sh
#命令格式
coscmd info <cospath> 

#操作示例
coscmd info bbb/123.txt
```
请将"<>"中的参数替换为您需要显示的 COS 上文件的路径（cospath）。

### 获取带签名的下载 URL
命令如下：
```sh
#命令格式
coscmd signurl <cospath>

#操作示例
coscmd signurl bbb/123.txt
coscmd signurl bbb/123.txt -t 100
```

请将 "<>" 中的参数替换为您需要获取下载 URL 的 COS 上文件的路径（cospath）
使用 `-t time` 设置打印签名的有效时间（单位为秒）

### 设置访问控制（ACL）
使用如下命令设置 Bucket 的访问控制：
```sh
#命令格式
coscmd putbucketacl [--grant-read GRANT_READ]  [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL]

#操作示例 
coscmd putbucketacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222
```

使用如下命令设置 Object 的访问控制：
```sh
#命令格式
coscmd putobjectacl [--grant-read GRANT_READ] [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL] <cospath> 

#操作示例
coscmd putobjectacl  --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 aaa/aaa.txt 
```

#### ACL 设置指南

- --grant-read 代表读的权限。
- --grant-write 代表写的权限。
- --grant-full-control 代表读写的权限。
- GRANT_READ / GRANT_WRITE / GRANT_FILL_CONTORL 代表被赋权的账号。
- 若赋权根账号，使用 rootid 的形式。
- 若赋权子账户，使用 rootid/subid 的形式。
- 若需要对所有人赋权，使用 anyone 的形式。
- 同时赋权的多个账号用逗号`,`隔开。
- 请将参数替换为您所需要删除的 COS 上文件的路径（cospath）。

### 获取访问控制（ACL）
- 使用如下命令设置 Bucket 的访问控制：
```sh
#命令格式
coscmd getbucketacl 
#操作示例
coscmd getbucketacl
```

- 使用如下命令设置 Object 的访问控制：
```sh
#命令格式
coscmd putbucketacl <cospath> 
#操作示例
coscmd getobjectacl aaa/aaa.txt 
```

### 开启关闭版本控制
命令如下：
```sh
#命令格式
coscmd putbucketversioning <status>

#开启版本控制
coscmd putbucketversioning Enabled

#关闭版本控制
coscmd putbucketversioning Suspended
```

请将 "<>" 中的参数替换为您需要版本控制状态（status）。
>!开启版本控制为不可逆过程，之后该 bucket 将无法使用 JSON API 接口（包括所有 JSON SDK），请慎重选择。

### 恢复归档文件
- 恢复归档文件命令如下：
```sh
#命令格式
coscmd restore <cospath>
#操作示例
coscmd restore -d 3 -t Expedited a.txt 
```
- 批量恢复归档文件命令如下：
```sh
#命令格式
coscmd restore -r <cospath>
#操作示例
coscmd restore -r -d 3 -t Bulk folder/
```

 请将 "<>" 中的参数替换为您需要打印文件列表的 COS 上文件的路径（cospath）。
 - 使用`-d day`设置临时副本的过期时间；默认值：7。
 - 使用`-t tier`具体复原过程类型，枚举值： Expedited ，Standard ，Bulk；默认值：Standard。

### Debug 模式执行命令
在各命令前加上`-d`或者`-debug`，在命令执行的过程中，会显示详细的操作信息 。示例如下：
```sh
#显示upload的详细操作信息，命令格式：
coscmd -d upload <localpath> <cospath>

#操作示例
coscmd -d upload /home/aaa/123.txt bbb/123.txt  
```

## 常见问题
如您在使用 COSCMD 工具过程中，有相关的疑问，请参阅 [COSCMD 工具类常见问题](https://cloud.tencent.com/document/product/436/30744)。
