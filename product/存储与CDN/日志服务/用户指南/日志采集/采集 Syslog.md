

## 使用场景

Syslog常被称为系统日志或系统记录，是一种用来在因特网协定的中传递记录档讯息的标准。网络中的路由器、交换机、防火墙、Unix/Linux 服务器等众多设备都支持它。syslog监控和管理对于每个组织来说都很重要，可以减少系统停机时间、提高网络性能并加强企业的安全策略。

## 使用前提

已部署好 rsyslog。
- 开通腾讯云日志服务。
- 在 rsyslog 目标 IP 的机器上已安装好 Loglistener 3.0.1.0 及以上版本。
- 当前控制台配置需要开白处理，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系 CLS 处理。

利用 rsyslog/etc/rsyslog.conf 配置开启 udp/tcp 开启转发：
![](https://qcloudimg.tencent-cloud.cn/raw/2dad44a1d89d9b0aabbb89ebd339805b.png)

>?安装 Loglistener 请参考 [Loglistener 安装指南](https://cloud.tencent.com/document/product/614/17414)。

## 操作流程


### 配置 rsyslog 转发
- 在 syslog 所在的服务器上修改 rsyslog 的配置文件 /etc/rsyslog.conf，在配置文件的最后添加一行转发规则。添加转发规则后，rsyslog 会将 syslog 转发至指定IP地址和端口上。如果通过当前服务器采集本机 syslog，配置转发地址为127.0.0.1，端口为任意非知名的空闲端口。
- 如果通过其他服务器采集本机 syslog，配置转发地址为其他服务器的公网 IP，端口为任意非知名的空闲端口。

例如以下配置表示将所有的日志都通过TCP转发至127.0.0.1:1000，配置文件详细说明请参见 [RSyslog Documentation](https://www.rsyslog.com/doc/v8-stable/configuration/index.html)。

```
*.* @@127.0.0.1:1000
```

执行以下命令重启rsyslog，使日志转发规则生效。
```
sudo service rsyslog restart
```

### 进入 CLS 控制台配置 syslog 采集规则

#### **步骤** 1 **：选择日志主题**
- 如果您想选择新的日志主题，可执行如下操作：登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
	1. 在左侧导航栏中，单击 **概览**，进入概览页面。
	2. 在其他日志栏下，找到syslog 采集，单击 **立即接入** 。
	![](https://qcloudimg.tencent-cloud.cn/raw/39076bfdb53332530e6dddf69e8ad44a.png)
	3. 在创建日志主题页面，根据实际需求，输入日志主题名称，配置日志保存时间等信息，单击 **下一步** 。
- 如果您想选择现有的日志主题，可执行如下操作：登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
  1. 在左侧导航栏中，单击 **日志主题**，选择需要投递的日志主题，进入日志主题管理页面。
  2. 选择 **采集配置** 页签，在 **Loglistener**采集配置栏下单击**新增**。
![](https://qcloudimg.tencent-cloud.cn/raw/2c6b184594228a2bbe545149b9bdf9c0.png)

#### **步骤** 2 **：机器组配置**

在"机器组管理"页面，勾选需要与当前日志主题进行绑定的机器组，单击**下一步**，即可进入采集配置阶段，更多详情请参阅 [管理机器组](https://cloud.tencent.com/document/product/614/17412)。
![](https://qcloudimg.tencent-cloud.cn/raw/f4d04ca9eaa15771befaf66764bacc61.png)

#### **步骤** 3 **：** syslog **采集配置**

在 syslog 采集配置页面，依次配置如下信息：

| **配置项** | **类型** | **说明** |
| --- | --- | --- |
| 采集规则名称 | 输入框 | 输入本条采集规则的名称 |
| 网络类型 | 单选框 | 指定syslog的传输协议，UDP/TCP |
| 解析协议 | 单选框 | 指定解析日志所使用的协议，默认为空，表示不解析。其中：rfc3164：指定使用RFC3164协议解析日志。rfc5424：指定使用RFC5424协议解析日志。auto：自动选择合适的解析协议。 |
| 输出源 | 输入框 | 指定loglistener监听的协议、地址和端口.格式为[tcp/udp]://[ip]:[port]。不配置时，默认为[tcp://127.0.0.1:](http://tcp://127.0.0.1:9999)10000。 |
| 解析失败上传 | 开关 | 指定解析失败后的操作，打开时表示如果解析失败，按照输入的key返回日志全文。配置为false ，表示解析失败时丢弃日志。 |
| 解析失败日志的键名称(Key) | 输入框 | 指定解析失败的 key 名 |

![](https://qcloudimg.tencent-cloud.cn/raw/4f3c692dc2803b5ae242f8d1b85c88af.png)

#### **步骤** 4 **：索引配置**

1. 在索引配置页面，配置如下信息：
![](https://qcloudimg.tencent-cloud.cn/raw/e71f7b32e963da0f87de75093287e92f.png)
 - 索引状态：确认是否开启。
 - 全文索引：确认是否需要设置大小写敏感。全文分词符：默认为"@&()='",;:\<\>[]{}/ \n\t\r"，确认是否需要修改。
 - 是否包含中文：确认是否开启。
 - 键值索引：默认关闭，您可根据 key 名按需进行字段类型、分词符以及是否开启统计分析的配置。若您需要开启键值索引，可打开开关。
>!
>- 检索必须开启索引配置，否则无法检索。
>- 索引规则编辑后仅对新写入的日志生效，已有数据不会更新。

2. 单击 **提交**，完成导入配置。

## 查看 syslog 日志
当前日志主题下配置完成 syslog 采集后，单击**检索**，进入**检索分析**页面查看 syslog。
![](https://qcloudimg.tencent-cloud.cn/raw/64a10cddd2abc70c44b1aa889eaf6d50.png)

| **字段** | **说明** |
| --- | --- |
| **HOSTNAME** | 主机名，如果日志中未提供则获取当前主机名。 |
| **program** | 协议中的 tag 字段。 |
| **priority** | 协议中的 priority 字段。 |
| **facility** | 协议中的 facility 字段。 |
| **severity** | 协议中的 severity 字段。 |
| **timestamp** | 日志对应的时间戳。 |
| **content** | 日志内容，如果解析失败的话，此字段包含未解析日志的所有内容。 |
| **SOURCE** | 当前主机的 IP 地址。 |
| **client\_ip** | 传输日志的客户端 IP 地址。 |
