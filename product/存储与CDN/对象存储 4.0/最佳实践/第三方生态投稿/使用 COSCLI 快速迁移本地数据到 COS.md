## 背景
在 GitHub 或者 Gitee 等其他地方“白嫖“存储难免会遇到无法访问的时候，例如前段时间 jsDelivr 就因为被 DNS 污染导致无法访问、Gitee 公开仓库私有等问题。

遇到如上情况：
- 可以使用 git 获取到数据，能拉取到本地，对于有服务器的同学，重新放到本地，替换一下访问链接就可以继续访问了。
- 没有服务器或者没有任何备份程序的就很不友好了，可能会出现数据丢失的问题。

那么这个时候就推荐数据上云了，以腾讯云为例：可以将 [本地数据迁移](https://cloud.tencent.com/product/cdm?from=10680) 至 COS。
## 简介

[对象存储](https://cloud.tencent.com/product/cos?from=10680)（Cloud Object Storage，COS）是腾讯云提供的一种存储海量文件的分布式存储服务，具有高扩展性、低成本、可靠安全等优点。针对不同存储类型，腾讯云分别承诺标准存储服务可用性不低于 99.95%，低频存储可用性不低于 99.9%。

提到迁移，第一个想到的可能是 COS Migration 工具。COS Migration 是一个集成了 COS 数据迁移功能的一体化工具。通过简单的配置操作，用户可以将本地数据迁移至 COS 中，它具有以下特点：

- 断点续传：工具支持上传时断点续传。对于一些大文件，如果中途退出或者因为服务故障，可重新运行工具，会对未上传完成的文件进行续传。
- 分块上传：将对象按照分块的方式上传到 COS。
- 并行上传：支持多个对象同时上传。
- 迁移校验：对象迁移后的校验。

但是呢，这篇文章推荐使用 COSCLI 工具。COS Migration 是使用 Java 语言开发的，在使用时需要依赖 JDK，Linux 环境需要 IFUNC 支持，确保环境 binutils 版本大于 2.20，对于小白用户不太友好。而 COSCLI 是使用 Go 语言开发，部署方便，且支持跨桶操作。

除此之外，之前还介绍过 [COSCMD](https://qq52o.me/2755.html) 的用法，那么 COSCLI 工具与 COSCMD 工具有什么区别：
<table>
<thead>
<tr>
<th width=50%><a href="https://cloud.tencent.com/document/product/436/63143">COSCLI 工具</a></th>
<th width=50%><a href="https://cloud.tencent.com/document/product/436/10976">COSCMD 工具</a></th>
</tr>
</thead>
<tbody>
<tr>
<td>COSCLI 工具使用 golang 构建，直接发布编译后的二进制包，用户在安装部署时无需预先安装任何依赖，开箱即用。</td>
<td>COSCMD 工具使用 Python 构建，用户在安装时需先安装 Python 环境和依赖包。</td>
</tr>
<tr>
<td> COSCLI 工具支持设置存储桶别名，可以使用一个短字符串来代替 `<BucketName-APPID>`，方便用户使用。</td>
<td>COSCMD 工具不支持存储桶别名，用户需要输入 `<BucketName-APPID>` 来指定一个存储桶，命令繁琐且不易阅读。</td>
</tr>
<tr>
<td> COSCLI 工具支持在配置文件内配置多个存储桶，且支持跨桶操作。</td>
<td>COSCMD 工具在配置文件中只能配置一个存储桶，且跨桶操作命令过于冗长。</td>
</tr>
</tbody>
</table>

## 下载与安装配置
COSCLI 工具提供 Windows、Mac、Linux 操作系统的二进制包，通过简单的安装和配置后即可使用。

| GitHub 地址                                                                                         | 国内站点                                                                               |
| ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [Windows](https://github.com/tencentyun/coscli/releases/download/v0.11.1-beta/coscli-windows.exe) | [Windows](https://cosbrowser.cloud.tencent.com/software/coscli/coscli-windows.exe) |
| [Mac](https://github.com/tencentyun/coscli/releases/download/v0.11.1-beta/coscli-mac)             | [Mac](https://cosbrowser.cloud.tencent.com/software/coscli/coscli-mac)             |
| [Linux](https://github.com/tencentyun/coscli/releases/download/v0.11.1-beta/coscli-linux)         | [Linux](https://cosbrowser.cloud.tencent.com/software/coscli/coscli-linux)         |
>?当前版本号为 v0.11.1-beta，如需获取工具的最新版本、历史版本和更新日志，请前往 [GitHub](https://github.com/tencentyun/coscli/releases) 进行查看。

根据自己需要在什么环境下使用进行下载，这里以 macOS 为例，其他环境可以 [参考文档](https://cloud.tencent.com/document/product/436/63144?from=10680)。

1. 下载 COSCLI
```
wget https://cosbrowser.cloud.tencent.com/software/coscli/coscli-mac
```
2. 重命名并修改文件权限。
```
mv coscli-mac /usr/local/bin/coscli
chmod 755 /usr/local/bin/coscli
```
3. 查看版本号检查是否安装成功。
```
$ coscli -v
coscli version v0.11.1-beta
```
看到了 version 的输出表示安装成功。

在 macOS 系统下使用 COSCLI 时，若弹出无法打开“coscli”，因为无法验证开发者的提示，可以前往**设置** > **安全性与隐私** > **通用**中选择仍要打开 coscli，之后即可正常使用 COSCLI。

可以使用 coscli --help 命令来快速查看 COSCLI 的使用方法。在第一次使用时，执行 coscli 命令，会进行初始化配置，需要输入 Secret ID 等信息，按步骤填写完成后，COSCLI 会默认在~/.cos.yaml 的位置生成配置文件。
```
$ coscli
2022/08/06 17:11:46 Welcome to coscli!
When you use coscli for the first time, you need to input some necessary information to generate the default configuration file of coscli.
The path of the configuration file: /Users/lufei/.cos.yaml
Input Your Secret ID:
```

后期也可以使用 coscli config init 命令在其他位置为 COSCLI 交互式地生成配置文件，或者可以直接手动编写 COSCLI 的配置文件。

配置文件中各配置项的说明如下：

| 配置项           | 说明                                                                                                                                                                                                                                                                                                  |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Secret ID     | 密钥 ID，可从 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中创建并获取。                                                                                                                                                                                                                              |
| Secret Key    | 密钥 Key，可从 [访问管理控制台](https://console.cloud.tencent.com/cam/capi) 中创建并获取。                                                                                                                                                                                                                             |
| Session Token | 临时密钥 token，当使用临时密钥时需要配置，若不使用可以直接按 `Enter` 跳过。                                                                                                                                                                                                                                                       |
| APP ID        | APP ID 是您在成功申请腾讯云账户后所得到的账号，由系统自动分配，可从 [账号信息](https://console.cloud.tencent.com/developer) 中获取。一个存储桶的全称由 `Bucket Name` 和 `APP ID` 这两个元素组成，格式为 `<BucketName-APPID>`，详情请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。 |
| Bucket Name   | 存储桶名称，和 APP ID 一起构成存储桶全称，格式为 `<BucketName-APPID>`，详情请参见 [存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83)。                                                                                                             |
| Bucket Region | 存储桶所在地域，详情请参见 [地域与访问域名](https://cloud.tencent.com/document/product/436/6224)。                                                                                                                                                                                                                       |
| Bucket Alias  | 存储桶别名，配置后可以在使用时用 `BucketAlias` 代替 `BucketName-APPID`，减少所需输入的命令长度，如果不配置此项，`BucketAlias` 的值是 `BucketName-APPID` 的值。                                                                                                                                                                                         |


配置完成后可以查看~/.cos.yaml文件，可以看到类似如下内容：
```
$ cat ~/.cos.yaml
cos:
  base:
    secretid: xxxxx
    secretkey: xxxxx
    sessiontoken: xxxxx
    protocol: https
  buckets:
  - name: sy-records-85464277
    alias: sy-records-85464277
    region: ""
    endpoint: cos.ap-shanghai.myqcloud.com
```
>?secretid/secretkey/sessiontoken 均为加密后的字符串，不是明文配置的值。

如果需要支持多个存储桶，可以使用 coscli config add 命令添加存储桶配置。

## 使用
COSCLI 支持以下命令：
```
$ coscli --help
Welcome to use coscli!

Usage:
  coscli [flags]
  coscli [command]

Available Commands:
  abort          Abort parts
  bucket-tagging Modify bucket tagging
  config         Init or edit config file
  cp             Upload, download or copy objects
  du             Displays the size of a bucket or objects
  hash           Calculate local file's hash-code or show cos file's hash-code
  help           Help about any command
  ls             List buckets or objects
  lsparts        List multipart uploads
  mb             Create bucket
  rb             Remove bucket
  restore        Restore objects
  rm             Remove objects
  signurl        Gets the signed download URL
  sync           Synchronize objects

Flags:
  -c, --config-path string     config file path(default is $HOME/.cos.yaml)
  -e, --endpoint string        config endpoint
  -h, --help                   help for coscli
  -i, --secret-id string       config secretId
  -k, --secret-key string      config secretKey
  -t, --session-token string   config sessionToken
  -v, --version                version for coscli

Use "coscli [command] --help" for more information about a command.
```
这里介绍一下 cp 和 sync 命令：

- cp 命令用于上传、下载或拷贝文件。
- sync 命令用于同步上传、下载或拷贝文件。
- 与 cp 命令不同的是：sync 命令首先会对比同名文件的 crc64，如果 crc64 值相同则不进行传输。

这两个命令在上传和下载大文件时会自动启用并发上传/下载。当以分块形式上传/下载文件时，会默认开启断点续传。

以迁移 WordPress 为例，可以使用如下命令将 WordPress 的媒体库上传到 COS 中，其中 /yourpath/wp-content/uploads 就是您的 WordPress 站点目录本地的媒体库存储路径，而 wp-content/uploads 就是存放在 COS 中的路径。

### 首次上传
- 将本地 wp-content/uploads 文件夹下的所有文件上传至 bucket1 桶中的 wp-content/uploads 文件夹下
```
coscli cp /yourpath/wp-content/uploads/ cos://bucket1/wp-content/uploads/ -r
```
- 将本地 wp-content/uploads 文件夹下的所有 .mp4 类型文件上传至 bucket1 桶中的 wp-content/uploads 文件夹下
```
coscli cp /yourpath/wp-content/uploads/ cos://bucket1/wp-content/uploads/ -r --include .*.mp4
```
- 将本地 wp-content/uploads 文件夹下的所有非 .md 类型文件上传至 bucket1 桶中的 wp-content/uploads 文件夹下
```
coscli cp /yourpath/wp-content/uploads/ cos://bucket1/wp-content/uploads/ -r --exclude .*.md
```


### 二次上传
如果出现了某些异常，或者手动停止掉后，想要重新上传，可以使用 Sync，该命令会对比同名文件的 crc64，如果 crc64 值相同则不进行传输。
```
coscli sync /yourpath/wp-content/uploads/ cos://bucket1/wp-content/uploads/ -r
```

更多关于 COSCLI 的使用方法请参见 [官网文档介绍](https://cloud.tencent.com/document/product/436/63666?from=10680)。
