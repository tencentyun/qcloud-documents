## 功能说明
使用 COSCMD 工具，用户可通过简单的命令行指令实现对对象（Object）的批量上传、下载、删除等操作。
## 使用限制
适用于 COS V4、V5 版本；针对 V3 迁移过来的用户也可以使用，但要用 V3 用户的 appid 才可以。
## 使用环境
### 系统环境
Windows 或 Linux 系统
### 软件依赖
Python 2.7 
并装有最新版本的 pip
#### 安装及配置
环境安装与配置详细操作请参考 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866)。
## 下载与安装
- **手动安装**
下载链接：[GitHub 链接](https://github.com/tencentyun/coscmd.git)
在该项目根目录下使用如下命令安装：
```
python setup.py install
```
- **pip 安装**
执行`pip`命令进行安装：
```
pip install coscmd
```
安装成功之后，用户可以通过`-v`或者`--version`命令查看当前的版本信息。
- **pip 更新**
执行`pip`命令进行更新：
```
pip install coscmd -U
```

> **注意：** 
不论是在 Linux 还是 Windows 环境下，都可以通过以上的方法安装或更新。

## 使用方法
### 查看 help
用户可通过`-h`或`--help`命令来查看工具的 help 信息。
```
coscmd -h  //查看当面版本信息
```
help 信息如下所示：
```
usage: coscmd [-h] [-d] [-b BUCKET] [-v]
              {config,upload,download,delete,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
              ...

an easy-to-use but powerful command-line tool. try 'coscmd -h' to get more
informations. try 'coscmd sub-command -h' to learn all command usage, likes
'coscmd upload -h'

positional arguments:
  {config,upload,download,delete,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
    config              config your information at first.
    upload              upload file or directory to COS.
    download            download file from COS to local.
    delete              delete file or files on COS
    list                list files on COS
    info                get the information of file on COS
    mget                download big file from COS to local(Recommand)
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
  -v, --version         show program's version number and exit
```
除此之外，用户还可以在每个命令后（不加参数）输入`-h`查看该命令的具体用法，例如：
```
coscmd upload -h  //查看 upload 命令使用方法
```
### 配置参数
COSCMD 工具在使用前需要进行参数配置。用户可以通过如下命令来配置：
```
coscmd config -a <secret_id> -s <secret_key> -b <bucket> -r <region> [-m <max_thread>] [-p <parts_size>]      
```
上述示例中使用"<>"的字段为必选参数，使用"[]"的字段为可选参数。其中：

| 名称         | 描述                                       | 有效值  |
| :---------| :---------------------------------------- | :---- |
| secret_id  | 必选参数，APPID 对应的密钥 ID，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/doc/product/436/6225)。 | 字符串  |
| secret_key | 必选参数，APPID 对应的密钥 Key，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/doc/product/436/6225)。 | 字符串  |
| bucket     | 必选参数，指定的存储桶名称，bucket的命名规则为{name}-{appid} ，参考 [创建存储桶](https://cloud.tencent.com/doc/product/436/6232)。 | 字符串  |
| region     | 必选参数，存储桶所在地域。参考 [可用地域](https://cloud.tencent.com/doc/product/436/6224)。 | 字符串  |
| max_thread | 可选参数，多线程上传时的最大线程数（默认为 5），有效值：1~10         | 数字   |
| parts_size | 可选参数，分块上传的单块大小（单位为 MB，默认为 1MB），有效值：1~10     | 数字   |

> **注意：** 
1. 可以直接编辑`~/.cos.conf`文件 （在 Windows 环境下，该文件是位于`我的文档`下的一个隐藏文件）。
配置完成之后的`.cos.conf`文件内容示例如下所示：
2. 可以在配置文件中增加`schema`项来选择`http / https`
```
 [common]
secret_id = AChT4ThiXAbpBDEFGhT4ThiXAbpHIJK
secret_key = WE54wreefvds3462refgwewerewr
bucket = ABC-1234567890
region = ap-guangzhou
max_thread = 5
part_size = 1
schema = https
```

### 指定 Bucket 的命令
-  通过`-b <bucket> 指定 Bucket`可以指定特定 Bucket。
- Bucket 的命名规则为`{name}-{appid}` ，此处填写的存储桶名称必须为此格式。
```
coscmd -b <bucket> method ...  //命令格式
coscmd -b AAA-12345567 upload a.txt b.txt  //操作示例-上传文件
coscmd -b AAA-12344567 createbucket  //操作示例-创建bucket
```

### 创建 Bucket
-  建议配合`-b <bucket> 指定 Bucket`使用。
```
coscmd -b <bucket> createbucket //命令格式
coscmd createbucket  //操作示例
coscmd -b AAA-12344567 createbucket  //操作示例
```

### 删除 Bucket
-  建议配合`-b <bucket> 指定 Bucket`使用。
```
coscmd -b <bucket> deletebucket //命令格式
coscmd createbucket  //操作示例
coscmd -b AAA-12344567 deletebucket  //操作示例
```
### 上传文件或文件夹
- 上传文件命令如下：
```
coscmd upload <localpath> <cospath>  //命令格式
coscmd upload /home/aaa/123.txt bbb/123.txt  //操作示例
coscmd upload /home/aaa/123.txt bbb/  //操作示例
```
- 上传文件夹命令如下：
```
coscmd upload -r <localpath> <cospath>  //命令格式
coscmd upload -r /home/aaa/ bbb/aaa  //操作示例
coscmd upload -r /home/aaa/ bbb/  //操作示例
coscmd upload -r /home/aaa/ /  //上传到bucket根目录
```

请将 "<>" 中的参数替换为您需要上传的本地文件路径（localpath），以及 COS 上存储的路径（cospath）。
> **注意：** 
* 上传文件时需要将cos上的路径包括文件(夹)的名字补全(参考例子)。
* COSCMD 支持大文件断点上传功能。当分片上传大文件失败时，重新上传该文件只会上传失败的分块，而不会从头开始（请保证重新上传的文件的目录以及内容和上传的目录保持一致）。
* COSCMD 分块上传时会对每一块进行 MD5 校验。

### 下载文件或文件夹
- 下载文件命令如下：
```
coscmd download <cospath> <localpath>  //命令格式
coscmd download bbb/123.txt /home/aaa/111.txt  //操作示例
coscmd download bbb/123.txt /home/aaa/  //操作示例
```
- 下载文件夹命令如下：
```
coscmd download-r <cospath> <localpath> //命令格式
coscmd download -r /home/aaa/ bbb/aaa  //操作示例
coscmd download -r /home/aaa/ bbb/  //操作示例
coscmd download -r / bbb/aaa  //下载当前bucket根目录下所有的文件
```
请将 "<>" 中的参数替换为您需要下载的 COS 上文件的路径（cospath），以及本地存储路径（localpath）。
> **注意：** 
* 若本地存在同名文件，则会下载失败。使用 `-f` 参数覆盖本地文件。
* 将以上命令中的 `download` 替换为 `mget`， 则可以使用分块下载，在带宽足够的条件下速度会提升 2 ~ 3 倍。

### 删除文件或文件夹
- 删除文件命令如下：
```
coscmd delete <cospath>  //命令格式
coscmd delete bbb/123.txt  //操作示例
```
- 删除文件夹命令如下：
```
coscmd delete -r <cospath>  //命令格式
coscmd delete -r bbb/  //操作示例
coscmd delete -r /  //操作示例
```

请将"<>"中的参数替换为您需要删除的 COS 上文件的路径（cospath）。工具会提示用户是否确认进行删除操作。
> **注意：** 
* 批量删除需要输入确定，使用 `-f` 参数跳过确认 。

### 复制文件
- 复制文件命令如下：
```
coscmd copy <sourcepath> <cospath>  //命令格式
coscmd copy bucket-appid.cos.ap-guangzhou.myqcloud.com/a.txt aaa/123.txt  //操作示例
```

请将"<>"中的参数替换为您需要复制的 COS 上文件的路径（sourcepath），和您需要复制到 COS 上文件的路径（cospath）。

> **注意：** 
sourcepath 的样式如下：```<bucketname>-<appid>.cos.<region>.myqcloud.com/<cospath>```

### 打印文件列表
- 打印命令如下：
```
coscmd list <cospath>  //命令格式
coscmd list -a //操作示例
coscmd list bbb/123.txt  -r -n 10 //操作示例
```
请将"<>"中的参数替换为您需要打印文件列表的 COS 上文件的路径（cospath）。
* 使用`-a`打印全部文件。
* 使用 `-r` 递归打印，并且会在末尾返回列出文件的数量和大小之和。
* 使用 `-n num` 设置打印数量的最大值。

> **注意：** 
`<cospath>`为空默认打印当前 Bucket 根目录。

### 显示文件信息
- 命令如下：
```
coscmd info <cospath>  //命令格式
coscmd info bbb/123.txt //操作示例
```
请将"<>"中的参数替换为您需要显示的 COS 上文件的路径（cospath）。

### 获取带签名的下载 URL
- 命令如下：
```
coscmd sigurl<cospath>  //命令格式
coscmd signurl bbb/123.txt //操作示例
coscmd signurl bbb/123.txt -t 100//操作示例
```
请将"<>"中的参数替换为您需要获取下载url的 COS 上文件的路径（cospath）。
使用 `-t time` 设置打印签名的有效时间（单位为秒）。

### 设置访问控制（ACL）
- 命令如下：
使用如下命令设置 Bucket 的访问控制：
```
coscmd putbucketacl [--grant-read GRANT_READ]  [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL] //命令格式
coscmd putbucketacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 //操作示例
```
使用如下命令设置 Object 的访问控制：
```
coscmd putbucketacl [--grant-read GRANT_READ] [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL] <cospath> //命令格式
coscmd putbucketacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 aaa/aaa.txt //操作示例
```

#### ACL 设置指南
> *  --grant-read 代表读的权限。
* --grant-write 代表写的权限。
* --grant-full-control 代表读写的权限。
* GRANT_READ / GRANT_WRITE / GRANT_FILL_CONTORL 代表被赋权的帐号。
* 若赋权根帐号，使用 rootid 的形式；
* 若赋权子账户，使用 rootid/subid 的形式；
* 若需要对所有人赋权，使用 anyone 的形式。
* 同时赋权的多个帐号用逗号`,`隔开。
* 请将参数替换为您所需要删除的 COS 上文件的路径（cospath）。

### 获取访问控制（ACL）
- 使用如下命令设置 Bucket 的访问控制：
```
coscmd getbucketacl //命令格式
coscmd getbucketacl //操作示例
```
- 使用如下命令设置 Object 的访问控制：
```
coscmd putbucketacl <cospath> //命令格式
coscmd getobjectacl aaa/aaa.txt //操作示例
```

### 恢复归档文件
- 命令如下：
```
coscmd restore <cospath>  //命令格式
coscmd restore a.txt -d 3 -t  Expedited//操作示例
coscmd restore a.txt -d 3 -t  Bulk///操作示例
```
请将"<>"中的参数替换为您需要打印文件列表的 COS 上文件的路径（cospath）。
* 使用 `-d day` 设置临时副本的过期时间；默认值：7。
* 使用 `-t tier` 具体复原过程类型，枚举值： Expedited ，Standard ，Bulk；默认值：Standard。

### Debug 模式执行命令
在各命令前加上`-d`或者`-debug`，在命令执行的过程中，会显示详细的操作信息 。示例如下：
```
//显示upload的详细操作信息
coscmd -d upload <localpath> <cospath>  //命令格式
coscmd -d upload /home/aaa/123.txt bbb/123.txt  //操作示例
```
