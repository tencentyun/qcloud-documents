## 功能说明
将本地目录下的子文件和子目录同步到 COS 上。
### 实现机制
COS 本地同步工具会获取用户本地的文件列表，执行上传并将上传的结果记录在本地。每次运行工具都会重新拉取本地文件列表，并与已成功的本地数据库进行比对和同步（上传或删除）。
## 使用限制
只适用于 COS V4 版本
## 使用环境
### 系统环境
Linux 或 Windows 系统
### 软件依赖
JDK 1.7 或 1.8  
#### 安装与配置
具体安装与配置说明请参考 [Java 安装与配置](/doc/product/436/10865)。
## 使用方法
### 获取工具包
下载链接：[本地同步工具](https://mc.qcloudimg.com/static/archive/ebda1aaa8fe077ae98bc0de7591b686f/cos_sync.zip)

解压缩工具包并进入工具包路径：
- **Windows：** 
解压并保存到 `C:\Users\Administrator\Downloads\cos_sync`
- **Linux:**
```
unzip cos_sync.zip && cd cos_sync
```

<span id="配置说明"></span>
### 配置说明
**Windows:** 
配置文件位于  `C:\Users\Administrator\Downloads\cos_sync\conf\config.json`

**Linux:** 配置文件位于工具包目录 `conf/config.json`

```
{
    "appid"            : "xxxxxx",
    "secret_id"        : "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "secret_key"       : "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "bucket"           : "xxxxxx",
    "timeout"          : "60",
    "thread_num"       : "20",
    "delete_sync"      : "1", 
    "daemon_mode"      : "0",
    "daemon_interval"  : "60", 
    "enable_https"     : "0",
    "region"           : "gz",

    "local_path"       : "/home/test/data",
    "cos_path"         : "/mysyncfolder/"
}
```
配置信息说明：

| 名称              | 描述                                       | 有效值      |
| --------------- | ---------------------------------------- | -------- |
| appid          | 需要进行操作的 APPID，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/document/product/436/6225) | APPID 数字 |
| secret_id       | APPID 对应的秘钥 ID，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/document/product/436/6225) | 字符串      |
| secret_key      | APPID 对应的秘钥 Key，可从控制台获取，参考 [基本概念](https://cloud.tencent.com/document/product/436/6225) | 字符串      |
| bucket          | 指定要同步的存储桶名称， 需要提前在控制台建立，参考 [创建存储桶](https://cloud.tencent.com/doc/api/436/6232) | 字符串      |
| timeout         | 连接 COS 的超时时间，在网络状况不佳的情况下可以增大该值。单位: 秒     | 数字       |
| thread_num      | 并发的线程数，表示同时上传的文件，对于大量的小文件(如图片类) 可以增大改值（如 50），提高上传速度。对于大文件，建议设置较小值（如 5，取决于文件大小)，否则有可能引起内存溢出 OOM | 数字       |
| delete_sync     | 删除本地文件时同步删除 COS 文件。 1：本地不存在的文件从 COS 上删除，建议谨慎使用；0：忽略本地已删除文件 | 数字       |
| daemon_mode     | 后台进程模式运行。1：循环运行同步工具； 0：运行一次后退出          | 数字       |
| daemon_interval | 后台进程模式下，检查本地文件变化的时间间隔。单位：秒               | 数字       |
| enable_https    | 启用 https 进行传输。1：使用 https；0：使用 http    | 数字       |
| region          | 存储桶所属地域。枚举值为 [可用地域](https://cloud.tencent.com/document/product/436/6224) 中适用于 JSON API 的地域简称，如 sh, gz, sgp 等。 | 字符串      |
| local_path      | 需要同步的本地绝对路径。Windows 路径需用双斜线 “\\\” 分割。<br>Linux 范例：/home/user/dir；Windows 范例：C:\\\document\\\dir | 字符串      |
| cos_path        | 同步到 COS 的目的路径，需以 / 为结尾以表示目录，根目录为 /      | 字符串      |
> <font color="#0000cc">**注意：** </font>
Windows 路径使用“\\\”进行分割。 因为如果使用“\”，配置文件中某些特殊字符会被当做被转义，整个文件不是一个有效的 json。

### 使用软件
执行同步工具：
 **Windows：** 请双击 【start_cos_sync.bat】。
**Linux:**
```
sh start_cos_sync.sh
```
执行完成后，会输出创建和删除成功与失败的统计，以及全部执行的时间。

## 问题与帮助
### 常见问题
**同步完成后，在 COS 上不小心删除了文件，再运行工具会上传吗？**
不会。工具对于已同步的文件列表是记录在本地的，不会从 COS 拉取文件列表。

**已同步记录的数据库保存在哪？删除了再运行工具会发生什么？**
同步结果记录会保存在 db 目录下的数据文件里。如果删除了再运行工具，工具会试图将本地文件全量再上传到 COS，如果 COS 上已存在文件则会进行覆盖。

**是否支持中文文件名和目录？**
支持。目前支持所有 UTF-8 编码的路径或文件。

### 常见错误
如果发生同步失败的情况，请先查看 cos_sync 工具文件包下 log 目录下的 error 日志。常见的错误返回码如下所示。
**code: -3, connection timeout**
说明：连接到 COS 服务超时，请检查解析和端口是否正常。
> 检查 DNS 方法：如 region 为 sh, 则本地执行 `dig sh.file.myqcloud.com` 查看获取到的 IP 是否为腾讯云的 IP，可以通过外部 ping 工具验证（例如 [站长工具 - Ping](http://ping.chinaz.com/)）。如果为腾讯云机房，应当解析为 10. * . *.*   的地址。其他region地区同理。
>
> 检查端口方法：在 IP 解析正确的情况下，执行 `telnet sh.file.myqcloud.com 80` 查看是否会返回 `Escape character is '^]'.`，如果无返回请检查本地防火墙配置以及网络是否通畅。

**code: -133, ERROR_CMD_BUCKET_NOTEXIST**
请确认配置文件中 region 是否设置正确。区域与配置的对应关系请参照 [配置说明](#配置说明)。

**code: -96, ERROR_PROXY_AUTH_EXPIRED**
首先请确认签名是否过期，如无问题，在 Linux 下执行 `date`命令确认系统时间设置是否正确，若不正确，请更新时间重试。

**config file is invalid json**
通常发生在 Windows 环境下，请注意 Windows 系统中对路径`local_path`的描述，需用双斜线 \\\ 分割，范例：C:\\\document\\\dir 。

### 其他错误
请 [提交工单](https://console.cloud.tencent.com/workorder/category)。并告知同步工具的 config.json 相关配置(不用提供密钥) 以及打包的 log 目录。
