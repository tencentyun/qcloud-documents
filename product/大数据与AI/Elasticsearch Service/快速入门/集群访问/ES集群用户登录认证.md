在了解如何访问 ES 集群前，您需要先了解 ES 集群用户登录认证。本文将为您介绍用户登录认证的相关内容。

## ES 集群用户登录认证（User authentication）
此功能用于提高 ES 集群的数据访问安全（可参阅 [保护您在 Elastic Stack 中的数据](https://www.elastic.co/what-is/elastic-stack-security)），用户必须通过用户名和密码认证，才被允许访问 ES 集群。无论是通过 Kibana、客户端或者 API 等方式访问集群都需要经过认证。详情请参考 [通过 API 访问集群](https://cloud.tencent.com/document/product/845/19540)、[通过客户端访问集群](https://cloud.tencent.com/document/product/845/19538)、[通过 Kibana 访问集群](https://cloud.tencent.com/document/product/845/19541)。

> ?在创建 ES 集群时会要求设置用户名和密码。
> - 对于未开启此功能的集群，用户名和密码仅用于 Kibana 的登录。
> - 对于已开启此功能的集群，用户名和密码可用于任何方式下的 ES 集群用户登录认证。

## 支持 ES 集群用户登录认证的 Elasticsearch 版本
并非所有的 Elasticsearch 版本都支持此功能，各版本情况如下：
- 开源版：不支持此功能。
- 基础版：从6.8版本开始，允许用户开启或关闭此功能，**6.8版本之前的版本不支持此功能**。
- 白金版：强制开启此功能，且不允许关闭。

## ES 集群开启用户登录认证注意事项

若 ES 集群未开启用户登录认证，需要通过升级或开启开关来开启用户登录认证时，应该先完成以下步骤：
- 提前修改业务代码，在调用 API 时传入用户名和密码，以便在开启此功能后可以正常访问集群。
- 根据 Elasticsearch 官方的设计要求，开启此功能需要全量重启集群，重启期间集群不可用，因此应谨慎选择合适的时机。

## 6.8及以上基础版如何开启和关闭 ES 集群用户认证
- 在创建集群时可以选择开启或关闭 ES 集群用户认证。
- 集群创建完成后，如果需要再次调整开关状态，可以到集群详情页进行操作。
![](https://main.qcloudimg.com/raw/b85a7b55378c7069de0a9d739122e6ea.png)

