LogListener 是腾讯云日志服务（Cloud Log Service，CLS）所提供的专用日志采集器，将它安装部署到服务器上，可快速采集日志到日志服务。

## 安装环境

LogListener 仅支持64位 Linux 操作系统环境（暂不支持 Windows），并适配主流 Linux 操作系统版本，若其他版本环境若安装异常，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。

| 操作系统类别&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 确定可安装环境                                               |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| CentOS（64位）                                               | CentOS_6.8_64位、CentOS_6.9_64位、CentOS_7.2_64位、CentOS_7.3_64位、CentOS_7.4_64位、CentOS_7.5_64位、CentOS_7.6_64位、CentOS_8.0_64位 |
| Ubuntu（64位）                                               | Ubuntu Server_14.04.1_LTS_64位、Ubuntu Server_16.04.1_LTS_64位、Ubuntu Server_18.04.1_LTS_64位 |
| Debian（64位）                                               | Debian_8.2_64位、Debian_9.0_64位                             |
| openSUSE（64位）                                             | openSUSE_42.3_64位                                           |

## 支持功能

LogListener 版本支持新功能如下：

| LogListener 版本 | 支持功能                    | 功能说明                                                     | 相关文档                                                     |
| --------------- | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| v2.5.4          | 支持 LogListener 服务日志功能 | LogListener 服务日志功能支持记录 LogListener 端运行状态和采集监控的日志数据并配置可视化视图，提供重要指标数据。 | [LogListener 服务日志](https://cloud.tencent.com/document/product/614/55281) |
| v2.5.2          | 支持上传解析失败日志        | 所有解析失败的日志，均以 LogParseFailure 作为键名称（Key），原始日志内容作为值（Value）进行上传。 | -                                                            |
| v2.5.0          | 支持 LogListener 自动升级功能 | 支持用户在控制台预设时间段指定机器组进行 agent 自动升级，也可对目标机器实行手动升级。 | [LogListener 升级指南](https://cloud.tencent.com/document/product/614/55468) |
| v2.4.5          | 支持多行-完全正则采集模式   | LogListener 采集配置规则新增【多行-完全正则】提取模式采集日志。 | [完全正则（多行）](https://cloud.tencent.com/document/product/614/52366) |



## 安装启动

### 1. 下载安装 LogListener

LogListener 最新版本下载地址：[公网下载 LogListener](https://mirrors.tencent.com/install/cls/loglistener-linux-x64-2.6.5.tar.gz)、[内网下载 LogListener](http://mirrors.tencentyun.com/install/cls/loglistener-linux-x64-2.6.5.tar.gz)

以安装路径`/usr/local/`为例： 下载 LogListener 安装包并解压，解压路径为`/usr/local/` ，解压完成后进入 LogListener 目录`loglistener/tools`，执行安装命令 。
- 公网环境下，操作命令如下：
```plaintext
wget https://mirrors.tencent.com/install/cls/loglistener-linux-x64-2.6.5.tar.gz  && tar -zxvf loglistener-linux-x64-2.6.5.tar.gz -C /usr/local && cd /usr/local/loglistener-2.6.5/tools && ./loglistener.sh install
```
- 内网环境下，操作命令如下：
```plaintext
wget http://mirrors.tencentyun.com/install/cls/loglistener-linux-x64-2.6.5.tar.gz  && tar -zxvf loglistener-linux-x64-2.6.5.tar.gz -C /usr/local && cd /usr/local/loglistener-2.6.5/tools && ./loglistener.sh install
```

### 2. 初始化 LogListener

在`loglistener/tools`路径下，以 root 权限执行 LogListener 初始化命令（默认使用内网方式访问服务），初始化命令如下：
```shell
./loglistener.sh init -secretid AKIDPEtPyKabfW8Z3Uspdz83xxxxxxxxxxx -secretkey whHwQfjdLnzzCE1jIf09xxxxxxxxxxxx -region ap-xxxxxx
```
>?初始化命令中 **-secretid**、**-secretkey**、**-region**、**-network** 为需要自主填写的参数，详细介绍请见如下 [参数说明](#parameterdescription)。

<span id="parameterdescription"></span>

#### 参数说明

| 参数名    | 类型描述                                                     |
| --------- | ------------------------------------------------------------ |
| secretid  | [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 的一部分，SecretId 用于标识 API 调用者身份 |
| secretkey | [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 的一部分，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥 |
| region    | region 表示日志服务所在的 [地域](https://cloud.tencent.com/document/product/614/18940)，此处填写域名简称，例如 ap-beijing、ap-guangzhou 等 |
| network   | 表示 loglistener 通过哪种方式访问服务域名，取值：intra 内网访问（默认），internet 外网访问 |
| ip        | 机器的 IP 标识。若不填写，loglistener 会自动获取本机的 IP 地址 |
| label     | 机器组标示，标示机器组需要填写标示信息，多个标示按逗号分隔 |

默认使用内网域名：

![](https://main.qcloudimg.com/raw/ea417c6d60ab21e52984d04c1364b30d.png)

如果需要通过外网方式访问服务域名，需要显式设置网络参数`internet`，执行如下命令：

```plaintext
./loglistener.sh init -secretid AKIDPEtPyKabfW8Z3Uspdz83xxxxxxxxxxxx -secretkey whHwQfjdLnzzCE1jIf0xxxxxxxxxxxx -region ap-xxxxxx -network internet
```

![](https://main.qcloudimg.com/raw/653ebe0400dca5b21b3e25d01f93cb5b.png)
> ?
> - 若主账号已授权协作者日志服务的读写权限，建议使用协作者密钥。
> - region 为您所使用的日志服务区域，而非您的业务机器所处的区域。
> - 云服务器与日志集同地域的情况下，建议使用内网方式访问服务域名。云服务器与日志集在不同地域的情况下，建议使用外网方式访问服务域名。
> - 关于日志采集权限详情，可参考 [授权子账号对 CLS 某个日志主题具有日志采集权限](https://cloud.tencent.com/document/product/614/50498) 文档。
> 

### 3. 启动 LogListener

成功安装后，执行 LogListener 启动命令：
```plaintext
/etc/init.d/loglistenerd start
```
![](https://main.qcloudimg.com/raw/184d6cc3308206b14288372da59a99a0.png)

## LogListener 常用操作

>? 本文档示例的操作命令说明仅适用于 LogListener-2.2.4 及以上版本，低版本操作命令请参见 [低版本 LogListener 安装指南](https://cloud.tencent.com/document/product/614/39211)。
>

### 1. 查看 LogListener 版本

```plaintext
/etc/init.d/loglistenerd -v
```

### 2. 查看 LogListener 帮助文档

```plaintext
/etc/init.d/loglistenerd -h
```

### 3. LogListener 进程管理

```plaintext
/etc/init.d/loglistenerd (start|restart|stop) # 启动、重启、停止
```

### 4. 查看 LogListener 进程状态

```plaintext
/etc/init.d/loglistenerd status
```

LogListener 正常情况会运行两个进程：
![](https://main.qcloudimg.com/raw/e28d0d88d14a65567ce46794979dfc94.png)

### 5. 检查 LogListener 心跳及配置

```plaintext
/etc/init.d/loglistenerd check
```

![](https://main.qcloudimg.com/raw/82430a9cb1aa364d2abfbc47ebae5ef5.png)


## 卸载 LogListener

以管理员权限执行 `loglistener/tools` 目录下的卸载命令：

```plaintext
./loglistener.sh uninstall
```

## 手动更新 LogListener

#### 复用断点文件（不会重复采集日志）：

1. 使用停止命令停止运行旧版本的 LogListener。
2. 备份旧版本中的断点文件目录（`loglistener/data`）。例如，将旧版的断点文件备份至`/tmp/loglistener-backup`目录下。
<dx-codeblock>
:::  plaintext
cp -r loglistener-2.2.3/data /tmp/loglistener-backup/
:::
</dx-codeblock>
3. 使用卸载命令卸载旧版本的 LogListener。
4. 下载最新版本的 LogListener，并使用相关命令安装和初始化新版本 LogListener。
5. 复制所备份的断点文件目录（步骤2）到新版本 LogListener 目录下。
```plaintext
cp -r /tmp/loglistener-backup/data loglistener-<version>/
```
 请根据实际情况替换 `<version>`，例如：
```plaintext
cp -r /tmp/loglistener-backup/data loglistener-2.2.8/
```
6. 使用启动命令启动运行新版本 LogListener。



#### 不复用断点文件（可能会重复采集日志）：

1. 使用停止命令停止运行旧版本的 LogListener。
2. 使用卸载命令卸载旧版本的 LogListener。
3. 下载最新版本的 LogListener，并使用相关命令安装和初始化新版本 LogListener。
4. 使用启动命令启动运行新版本 LogListener。
