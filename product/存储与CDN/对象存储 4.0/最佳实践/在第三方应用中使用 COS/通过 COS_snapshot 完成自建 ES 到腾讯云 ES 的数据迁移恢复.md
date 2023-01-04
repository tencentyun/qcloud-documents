
## 简介

腾讯云 Elasticsearch Service（ES）是基于开源搜索引擎 Elasticsearch 打造的高可用、可伸缩的云端全托管的 Elasticsearch 服务，包含 Kibana 及常用插件，并集成了安全、SQL、机器学习、告警、监控等高级特性（X-Pack）。使用腾讯云 ES，您可以快速部署、轻松管理、按需扩展您的集群，简化复杂运维操作，快速构建日志分析、异常监控、网站搜索、企业搜索、BI 分析等各类业务。 

腾讯云 ES 集成了腾讯云计算在计算、存储、安全等领域的领先技术优势，又保持了 Elasticsearch 本身的兼容与开放，拥有丰富的集群管理功能以及安全、弹性、高可用等特性，同时也集成了官方的高级商业特性（X-Pack），在开源的基础上，增加了权限管理、SQL、机器学习、告警等功能，可以帮助您简化集群部署、运营管理等基础运维工作，更加聚焦于业务本身。

通过腾讯云 ES，您可以快速构建海量数据存储搜索、实时日志分析等应用，例如网站搜索导航、企业级搜索、服务日志异常监控、点击流分析等。

ES 与 COS 之间的使用场景主要体现在数据迁移、数据恢复备份这几个方面。其原理就是通过 COS 将源 ES 数据中间存储，然后再将存储的数据进行目标 ES 集群异步恢复的过程。

## 准备工作

创建一个**公有读私有写**的存储桶，创建详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。

>!COS bucket 的地域一定要与 ES 在同一地域。

## 安装 COS 插件

腾讯云 ES 默认内部集成了这些插件，如果是用户自建的 ES 集群，并且需要使用 COS，那么需要安装针对用户对应的 ES 版本的 COS 插件。


### COS 插件的功能

可以直接将用户自建集群上将快照文件备份到 COS bucket 里，然后去对端执行恢复即可。

### 下载插件

前往 [Github](https://github.com/tencentyun/elasticsearch-repository-cos) 下载腾讯云 ES 推出的 COS 插件。


### 插件安装流程

1. 获取对应 ES 版本的插件。
2. 授权 ES 启动账号 elastic 对该插件文件的所有权限。
![](https://qcloudimg.tencent-cloud.cn/raw/ac4d492b482dc76cf851b770e111c22f.png)
3. 切换到普通用户下，安装插件，重启 ES 服务。注意：集群每个节点都要操作。执行命令如下：
```
bin/elasticsearch-plugin install file:///path/repository-cos.zip
```
如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/53a223c9d494fed3f7708c2f4adad419.png)
4. 执行完成后，可以在 kibana 上通过 `get _cat/plugins` 确认是否安装完成，得到如下结果则表示安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/d94b098c6e90f83cc8eb98009eeab5e1.png)

## 使用 COS 实现自建 ES 与腾讯云 ES 的数据迁移

1. 在本地集群上注册 COS 仓库：
```
PUT _snapshot/my_cos_backup
{
    "type": "cos",
    "settings": {
        "access_key_id": "xxxxxx",
        "access_key_secret": "xxxxxxx",
        "bucket": "不带appId后缀的bucket名",
        "region": "ap-guangzhou",
        "compress": true,
        "chunk_size": "500mb",
        "base_path": "/yourbasepath",
        "app_id": "xxxxxxx" 
    }
}
```

执行这条指令会在 COS 对应的 bucket 中的 base_path 目录下创建一个名为 my_cos_backup 的仓库。

参数说明如下：

| 参数名                           | 参数说明                                                     |
| -------------------------------- | ------------------------------------------------------------ |
| access_key_id，access_key_secret | 访问密钥信息，可前往 [云 API 密钥](https://console.cloud.tencent.com/capi) 中创建和获取。 |
| bucket                           | 存储桶名称，注意不要带 appid。                                        |
| app_id                           | APPID 是在成功申请腾讯云账户后，系统分配的账户标识之一，可通过 [腾讯云控制台](https://console.cloud.tencent.com/developer) 【账号信息】中查看。 |
| region                           | 桶所在的地域，COS 地域的简称请参照 [地域和访问域名](https://www.qcloud.com/document/product/436/6224)。 |
| base_path                        | 备份目录，形如/dir1/dir2/dir3，需要写最开头的`/`，目录最后不需要`/`。 |

2. 在本地仓库创建快照文件，快照文件会自动上传至 COS 的指定仓库中去，可以使用 `put _snapshot/仓库名/快照名` 的方式执行快照。
3. 在腾讯云 ES 上同样注册一个仓库，仓库名可以不一样。
```
PUT _snapshot/my_cos_backup
{
    "type": "cos",
    "settings": {
        "access_key_id": "xxxxxx",
        "access_key_secret": "xxxxxxx",
        "bucket": "不带appId后缀的bucket名",
        "region": "ap-guangzhou",
        "compress": true,
        "chunk_size": "500mb",
        "base_path": "/yourbasepath",
        "app_id": "xxxxxxx" 
    }
}
```
4. 在腾讯云 ES 上执行恢复，使用如下命令执行快照恢复：
```
POST _snapshot/仓库名/快照名/_restore
```
>!这里恢复的快照名是您之前在源集群创建的快照名。
>



## 结语

当然，COS 不仅提供以上应用和服务，还提供多款热门开源应用，并集成腾讯云 COS 插件，欢迎点击“[此处](https://cloud.tencent.com/act/pro/Ecological-aggregation?from=18406)”一键启动，立即使用！



