## 操作场景

本文指导您使用 Winlogbeat 或者 Filebeat 采集 Windows 环境日志上传至 CLS。

## 前提条件

- 已开通日志服务（Cloud Log Service，CLS），并创建对应资源（如日志集和日志主题）。
- 已在 [腾讯云控制台](https://console.cloud.tencent.com/cam/capi) 获取到 SecretId 和 SecretKey。

## 操作步骤


### 使用 Winlogbeat 采集 Windows 事件日志上传 CLS

#### 安装 Winlogbeat

1. 前往 Winlogbeat 官网下载，您需要下载的版本。
本文以 Winlogbeat 7.6.2 版本为例，[点此前往下载](https://www.elastic.co/cn/downloads/past-releases/winlogbeat-7-6-2)。
2. 将已下载的压缩包解压缩至 C: 盘下。
建议在 Program Files 目录下新建一个 winlogbeat 文件夹，并解压缩至该文件夹下。
3. 以管理员身份打开 powershell，并执行如下命令。
```
cd C:\Program Files
cd .\winlogbeat-7.6.2-windows-x86_64
.\install-service-winlogbeat.ps1
```
执行过程中，如果报错，请输入`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`命令并选择`y`，然后重新输入以上命令。
执行命令后，如果返回下图结果则表示成功。
![](https://qcloudimg.tencent-cloud.cn/raw/68fa77d15c4198ce73f3b68bc543f041.png)
4. 执行如下命令，测试环境是否正常。
```
.\winlogbeat.exe test config -c .\winlogbeat.yml -e
```
如果返回 `config OK` 则表示成功。
5. 执行如下命令，启动程序。
```
Start-Service winlogbeat
```

#### 上传日志至 CLS

在 C:\Program Files\Winlogbeat\winlogbeat.yml 文件中，将 output.kafka 修改为如下内容，将日志发送到 CLS。
```
output.kafka:
  enabled: true
  hosts: ["${region}-producer.cls.tencentyun.com:9095"] # TODO 服务地址；外网端口9096，内网端口9095
  topic: "${topicID}" #  TODO topicID
  version: "0.11.0.2"
  compression: "${compress}"   # 配置压缩方式，支持gzip，snappy，lz4；例如"lz4"
  username: "${logsetID}"
  password: "${SecurityId}#${SecurityKey}"
```

| 参数 | 说明 |
|---------|---------|
| 链接类型 | 当前支持 SASL_PLAINTEXT。 |
| hosts | 初始连接的集群地址，详细请参见 [服务入口](#hosts)。 |
| topic | 配置为日志主题 ID，例如 76c63473-c496-466b-XXXX-XXXXXXXXXXXX。 |
| username | 配置为日志集 ID，例如 0f8e4b82-8adb-47b1-XXXX-XXXXXXXXXXXX。 |
| password | 格式为 ${SecurityId}#${SecurityKey}，例如 XXXXXXXXXXXXXX#YYYYYYYY。 |

### 使用 Filebeat 采集 Windows 文件日志

#### 安装 Filebeat

1. 前往 [官网](https://www.elastic.co/cn/downloads/past-releases#filebeat)，选择对应版本，下载安装包。
2. 将安装包上传至目标 Windows 主机某个盘的根目录，并解压缩。
3. 编辑 filebeat.yml 文件。
>? 路径符号，要用“/”而不是“\”。
>
4. 找到目标日志路径，编辑模块配置文件（这里以 mssql 为例）。
```
# Module: mssql
# Docs: https://www.elastic.co/guide/en/beats/filebeat/7.3/filebeat-module-mssql.html

- module: mssql
  # Fileset for native deployment
  log:
    enabled: true

    # Set custom paths for the log files. If left empty,
    # Filebeat will choose the paths depending on your OS.
    var.paths: ["D:/Program Files/Microsoft SQL Server/MSSQL10_50.MSSQLSERVER/MSSQL/Log/ERROR*"]
```
5. 以管理员身份打开 powershell，并执行如下命令。
```
#进入 filebeat 的路径,具体看你自己放在哪里
cd c:/filebeat

#执行安装脚本，安装 filebeat 服务
.\install-service-filebeat.ps1

#启动 mssql 模块
.\filebeat.exe modules enable mssql

#安装模板文件
.\filebeat.exe setup -e

#启动 filebeat 服务
start-service filebeat
```

#### 上传日志至 CLS

在 filebeat.yml 文件中，将 output.kafka 修改为如下内容，将日志发送到 CLS。

```
output.kafka:
  enabled: true
  hosts: ["${region}-producer.cls.tencentyun.com:9095"] # TODO 服务地址；外网端口9096，内网端口9095
  topic: "${topicID}" #  TODO topicID
  version: "0.11.0.2"
  compression: "${compress}"   # 配置压缩方式，支持gzip，snappy，lz4；例如"lz4"
  username: "${logsetID}"
  password: "${SecurityId}#${SecurityKey}"
```

| 参数 | 说明 |
|---------|---------|
| 链接类型 | 当前支持 SASL_PLAINTEXT。 |
| hosts | 初始连接的集群地址，详细请参见 [服务入口](#hosts)。 |
| topic | 配置为日志主题 ID，例如 76c63473-c496-466b-XXXX-XXXXXXXXXXXX。 |
| username | 配置为日志集 ID，例如 0f8e4b82-8adb-47b1-XXXX-XXXXXXXXXXXX。 |
| password | 格式为 ${SecurityId}#${SecurityKey}，例如 XXXXXXXXXXXXXX#YYYYYYYY。 |

<span id="hosts"></span>
## 服务入口 

<table>
	<tr><th>地域</th><th>网络类型</th><th>端口号</th><th>服务入口</th></tr>
	<tr><td rowspan=2>广州</td><td>内网</td><td>9095</td><td>gz-producer.cls.tencentyun.com:<b>9095</b></td></tr>
	<tr><td>外网</td><td>9096</td><td>gz-producer.cls.tencentcs.com:<b>9096</b></td></tr>
</table>

>! 本文档以广州地域为例，内外网域名需用不同端口标识，其他地域请替换地址前缀。详情请参考 [可用域名-Kafka上传日志](https://cloud.tencent.com/document/product/614/18940#Kafka)。
>
