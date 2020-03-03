## 功能说明
本迁移工具支持从 AWS S3，阿里云 OSS 和七牛云等服务迁移文件到对象存储 COS；同时也支持文件列表迁移，即从一系列给定的 URL 中迁移文件到对象存储 COS。
## 使用限制
只适用于 COS V4 版本
## 使用环境
### 系统环境
Linux 或 Mac 系统
### 软件依赖
Python 2.7.x，同时应该安装 pip，gcc 与 python-dev。
#### 安装及配置
1. Python 2.7.x 安装请参考 [Python 安装与配置](https://cloud.tencent.com/document/product/436/10866)。
2. 安装 pip，gcc 与 python-dev：
```
sudo yum install python-pip python-devel gcc
```

## 使用方法
### 获取工具
[Github 地址](https://github.com/tencentyun/cos_migrate_tool) 
### 安装方法
推荐使用 pip 安装，安装 pip 的方法，可以参考 [ pip 官网](https://pip.pypa.io/en/latest/installing/) 或者使用 apt/yum 等包管理工具安装 python-pip 包。
```
 pip install -U cos_migrate_tool
```
![迁移工具1](//mc.qcloudimg.com/static/img/1b576204b2d16c368be9a6bca908b014/image.png)
执行完上述命令后，使用如下命令检测是否安装成功。
```
cos_migrate_tool -h
```
返回结果如下图所示，则表示已安装成功：
![迁移工具2](//mc.qcloudimg.com/static/img/04495932eebaae7e5099830cbe73f2e1/image.png)
<span id="配置文件"></span>
### 配置文件
配置文件模板（路径：`./cos_migrate_tool-master/conf`），配置内容举例如下：
假设用户迁移数据从 OSS 到 COS，common 部分配置基本信息，workspace 是工作目录。source 部分配置数据源的信息，配置 OSS 的属性。destination 部分配置 COS 属性。
**配置文件请删除注释文字，即 `# 注释` 部分，空白模板参考 [GitHub 页面](https://github.com/tencentyun/cos_migrate_tool/tree/master/conf)。**
#### 迁移 OSS 中文件
```
[common]
workspace=/tmp/tmp6

[source]
type=oss
accesskeyid=         # oss accesskey id
accesskeysecret=     # oss accesskey secret
bucket=              # 要迁移的bucket名
endpoint=            # oss 的endpoint，例如 oss-cn-beijing.aliyuncs.com

[destination]
type=cosv4
region=shanghai            # cos 的 region，如shanghai, guangzhou
accesskeyid=               # cos 的 accesskeyid
appid=                     # cos 的 appid
accesskeysecret=           # cos 的 accesskeysecret
bucket=sdktest             # cos 的 bucket
prefix_dir=/dir21          # cos 的目录，迁移的文件都会位于该目录下，不配置该项则迁移到根目录
```
#### 迁移七牛云中的文件
```
[common]
workspace=/tmp/tmp11


[source]
type=qiniu
accesskeyid=               # qiniu 的 accesskeyid
accesskeysecret=           # qiniu 的 accesskeysecret
bucket=                    # 要迁移的qiniu的bucket
domain_url=                # qiniu 的下载域名

[destination]
type=cosv4
region=shanghai            # cos 的 region，如shanghai, guangzhou
accesskeyid=               # cos 的 accesskeyid
appid=                     # cos 的 appid
accesskeysecret=           # cos 的 accesskeysecret
bucket=sdktest             # cos 的 bucket
prefix_dir=/dir21          # cos 的目录，迁移的文件都会位于该目录下，不配置该项则迁移到根目录
```
#### 迁移 S3 中的文件
```
[common]
workspace=/tmp/tmp21

[source]
type=s3
accesskeyid=               # s3 的 accesskey id
accesskeysecret=           # s3 的 accesskey secret
bucket=                    # s3 的要迁移的bucket名

[destination]
type=cosv4
region=shanghai
accesskeyid=
appid=
accesskeysecret=
bucket=
```
#### 迁移列表文件
```
[common]
workspace=

[source]
type=url
url_list_file=/tmp/urllist.txt   # 要迁移的文件url列表文件，文件每一行为一个完整的url
timeout=3                        # http请求的超时时间

[destination]
type=cosv4
region=
accesskeyid=
appid=
accesskeysecret=
bucket=
```
### 运行工具
在安装成功后，系统会有一个可执行命令 `cos_migrate_tool`，之后的迁移过程都是使用该命令。执行命令的方式如下：
```
cos_migrate_tool -c /path/to/your/conf
```
配置文件自行编写，模版参考 [配置文件](#配置文件)。在配置文件中，需要配置一个工作目录，之后迁移过程中产生的临时文件都在放置在该目录，请保证目录空间足够大，如果并行执行多个迁移任务，推荐使用不同的目录。
在迁移过程中，你可以查看你设定的工作目录下面的 fail_file.txt 来查看迁移失败的文件列表。
### 卸载方法
执行如下命令：
```
pip uninstall cos_migrate_tool
```
## 常见问题
1. pip 命令不存在。 
使用 `apt install python-pip` 或者 `yum install python-pip` 命令安装PIP。
2. 使用 pip 安装迁移工具不成功。
尝试执行`sudo pip install cos_migrate_tool`。
