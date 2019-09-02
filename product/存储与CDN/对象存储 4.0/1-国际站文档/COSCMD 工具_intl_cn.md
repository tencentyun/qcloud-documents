## 功能说明
使用 COSCMD 工具，用户可通过简单的命令行指令实现对对象（Object）的批量上传、下载、删除、列表等操作。支持对对象进行信息查询、获取下载URL等操作。
## 使用限制
适用于 COS V4、V5 版本；

## 使用环境
### 系统环境
Windows 或 Linux 系统
### 软件依赖
Python 2.7.x
#### 安装及配置
环境安装与配置详细操作请参考 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866)。
## 下载与安装
- **手动安装**
下载链接：[GitHub 链接](https://github.com/tencentyun/coscmd.git)
- **pip 安装**
在该项目根目录下执行`pip`命令进行安装：
```
sudo pip install coscmd
```
安装成功之后，用户可以通过`-v`或者`--version`命令查看当前的版本信息。如下图所示：
![微信图片_20170817111542](//mc.qcloudimg.com/static/img/3ba7db584152f03ad5d1848058c35743/image.png)

## 使用方法
### 查看 help
用户可通过`-h`或`--help`命令来查看工具的 help 信息。
```
coscmd -h  //查看当前版本信息
```
help 信息如下图所示：
![微信图片_20170817111432](//mc.qcloudimg.com/static/img/d7d49135c1f3064e4d1be3c210192143/image.png)
除此之外，用户还可以在每个命令后（不加参数）输入`-h`查看该命令的具体用法，例如：
```
coscmd upload -h  //查看 upload 命令使用方法
```
### 配置参数
COSCMD 工具在使用前需要进行参数配置。用户可以直接编辑`~/.cos.conf`文件，也可以通过如下命令来配置：
```
coscmd config -a <access_id> -s <secret_key> -u <appid> -b <bucketname> -r <region> [-m <max_thread>] [-p <parts_size>]      
```
上述示例中使用"<>"的字段为必选参数，使用"[]"的字段为可选参数。其中：

| 名称         | 描述                                       | 有效值  |
| --------- | ---------------------------------------- | ---- |
| access_id  | 必选参数，APPID 对应的密钥 ID，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/document/product/436/6225)。 | 字符串  |
| secret_key | 必选参数，APPID 对应的密钥 Key，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/document/product/436/6225)。 | 字符串  |
| appid      | 必选参数，需要进行操作的 APPID，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/document/product/436/6225)。 | 数字   |
| bucketname     | 必选参数，指定的存储桶名称， 需要提前在控制台建立，参考 [创建存储桶](https://cloud.tencent.com/document/product/436/6232)。 | 字符串  |
| region     | 必选参数，存储桶所在地域，枚举值为 [可用地域](https://cloud.tencent.com/document/product/436/6224) 中适用于 XML API 的地域简称，如：ap-guangzhou 、eu-frankfurt 等。 | 字符串  |
| max_thread | 可选参数，多线程上传时的最大线程数（默认为 5），有效值：1~10         | 数字   |
| parts_size | 可选参数，分块上传的单块大小（单位为 M，默认为 1M），有效值：1~10     | 数字   |

配置完成之后的`.cos.conf`文件内容示例如下所示：
```
 [common]
access_id = AChT4ThiXAbpBDEFGhT4ThiXAbpHIJK
secret_key = WE54wreefvds3462refgwewerewr
appid = 1234567890
bucket = ABC
region = ap-guangzhou
max_thread = 5
part_size = 1
```
### 上传文件或文件夹
- 上传文件命令如下：
```
coscmd upload <localpath> <cospath>  //命令格式
coscmd upload /home/aaa/123.txt bbb/123.txt  //操作示例
```
- 上传文件夹命令如下：
```
coscmd upload -r <localpath> <cospath>  //命令格式
coscmd upload -r /home/aaa/ bbb/  //操作示例
```

请将 "<>" 中的参数替换为您需要上传的本地文件路径（localpath），以及 COS 上存储的路径（cospath）。
<font color="#0000cc">**注意：** </font>
COSCMD 支持大文件断点上传功能。当分片上传大文件失败时，重新上传该文件只会上传失败的分块，而不会从头开始（请保证重新上传的文件的目录以及内容和上传的目录保持一致）。

### 下载文件或文件夹
- 下载文件命令如下：
```
coscmd download <cospath> <localpath>  //命令格式
coscmd download bbb/123.txt /home/aaa/111.txt  //操作示例
```
- 下载文件夹命令如下：
```
coscmd download -r <cospath> <localpath>  //命令格式
coscmd download -r bbb/ /home/aaa/  //操作示例
```

请将 "<>" 中的参数替换为您需要下载的 COS 上文件的路径（cospath），以及本地存储路径（localpath）。
<font color="#0000cc">**注意：** </font>
COSCMD 使用-f覆盖本地的同名文件。

### 删除文件或文件夹
- 删除文命令如下：
```
coscmd delete <cospath>  //命令格式
coscmd delete bbb/123.txt  //操作示例
```
- 如下删除文件夹命令如下：
```
coscmd delete -r <cospath>  //命令格式
coscmd delete -r bbb/  //操作示例
```

请将"<>"中的参数替换为您需要删除的 COS 上文件的路径（cospath）。工具会提示用户是否确认进行删除操作。

### debug 模式执行命令
在各命令前加上`-d`或者`-debug`，在命令执行的过程中，会显示详细的操作信息 。示例如下：
```
//显示upload的详细操作信息
coscmd -d upload <localpath> <cospath>  //命令格式
coscmd -d upload /home/aaa/123.txt bbb/123.txt  //操作示例
```
