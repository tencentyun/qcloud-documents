许多腾讯云产品服务已经支持在访问管理（CAM）进行权限管理，您可以在本文内详细查看已支持 CAM 的产品服务的相关信息，包括接入粒度，对云 API、控制台鉴权等是否支持，是否支持角色等。

对表中信息进行如下定义：
- 服务：支持 CAM 的云服务的名称，单击链接至对应产品服务文档方便您快速获取相关信息。
- 策略语法：当前服务是否支持通过策略语法进行权限管理，“✔”表示支持，“-”表示暂不支持。
- 云 API：当前服务是否支持通过云 API 进行权限管理，“✔”表示支持，“-”表示暂不支持。
- 控制台：当前服务是否支持在控制台进行权限管理，“✔”表示支持，“-”表示暂不支持。
- 授权粒度：当前服务提供的最小授权粒度。
- 临时证书（STS）：当前服务是否支持通过临时证书进行权限管理，“✔”表示支持，“-”表示暂不支持。
- 角色：当前服务是否支持角色，“✔”表示支持，“-”表示暂不支持。


>其中授权粒度按照粒度粗细分为服务级、操作级和资源级三个级别。
> - 服务级：定义对服务的整体是否拥有访问权限，分为允许对服务拥有全部操作权限或者拒绝对服务拥有全部操作权限。
> - 操作级：定义对服务的特定接口（API）是否拥有访问权限，例：授权某账号对云服务器服务进行只读操作。
> - 资源级：定义对特定资源是否有访问权限，这是最细的授权粒度，例：授权某账号仅读写操作某台云服务器。

## 支持 CAM 的云服务列表

| 服务                                                         | 策略语法 | 云 API | 控制台 | 授权粒度 | 临时证书 | 角色 |
| ------------------------------------------------------------ | -------- | ------ | ------ | -------- | -------- | ---- |
| [云服务器](https://cloud.tencent.com/document/product/213/10314) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| 安全组                                                       | ✔        | ✔      | ✔      | 资源级   | ✔        | -    |
| [黑石物理服务器](https://cloud.tencent.com/document/product/386/13245) | ✔        | ✔      | ✔      | 资源级   | ✔        | -    |
| [云硬盘](https://cloud.tencent.com/document/product/362)     | ✔        | ✔      | ✔      | 资源级   | ✔        | -    |
| [容器服务-集群](https://cloud.tencent.com/document/product/457/11542) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| [容器服务-镜像仓库](https://cloud.tencent.com/document/product/457/11527) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| [容器服务-持续集成](https://cloud.tencent.com/document/product/457/11542) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| [弹性伸缩](https://cloud.tencent.com/document/product/377)   | ✔        | ✔      | ✔      | 服务级   | -        | -    |
| [无服务器云函数](https://cloud.tencent.com/document/product/583/18014) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| [批量计算](https://cloud.tencent.com/document/product/599)   | ✔        | ✔      | ✔      | 资源级   | ✔        | -    |
| [对象存储](https://cloud.tencent.com/document/product/436/12469) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| [文件存储](https://cloud.tencent.com/document/product/582/14679) | ✔        | ✔      | -      | 服务级   | ✔        | -    |
| [归档存储](https://cloud.tencent.com/document/product/572)   | ✔        | ✔      | -      | 资源级   | ✔        | -    |
| [存储网关](https://cloud.tencent.com/document/product/581)   | ✔        | -      | ✔      | 服务级   | -        | -    |
| [日志服务](https://cloud.tencent.com/document/product/614)   | ✔        | -      | ✔      | 服务级   | -        |  ✔ |
| [云数据库 MySQL](https://cloud.tencent.com/document/product/236/14469) | ✔        | ✔      | ✔      | 资源级   | ✔        | - |
| [时序数据库](https://cloud.tencent.com/document/product/652) | ✔        | ✔      | -      | 操作级   | ✔        | - |
| [负载均衡](https://cloud.tencent.com/document/product/214/9779) | ✔        | ✔      | ✔      | 资源级   | ✔        |      |
| [私有网络](https://cloud.tencent.com/document/product/215/9510) | ✔        | ✔      | ✔      | 资源级   | ✔        | - |
| [黑石负载均衡](https://cloud.tencent.com/document/product/386/13351) | ✔        | ✔      | ✔      | 资源级   | ✔        | - |
| [黑石私有网络](https://cloud.tencent.com/document/product/386/13352) | ✔        | ✔      | ✔      | 资源级   | ✔        | - |
| [黑石弹性公网 IP](https://cloud.tencent.com/document/product/386/13350) | ✔        | ✔      | ✔      | 资源级   | ✔        | - |
| [内容分发网络](https://cloud.tencent.com/document/product/228/12722) | -        | ✔      | ✔      | 操作级   | ✔        | - |
| [动态加速网络](https://cloud.tencent.com/document/product/570) | ✔        | ✔      | ✔      | 服务级   | ✔        |      |
| [消息队列 CMQ](https://cloud.tencent.com/document/product/406/8621) | ✔        | ✔      | ✔      | 资源级   | ✔        | - |
| [消息队列 CKafka](https://cloud.tencent.com/document/product/597/17989) | ✔        | ✔      | ✔      | 资源级   | ✔        | ✔    |
| 消息订阅                                                     | ✔        | -      | ✔      | 服务级   | -        | - |
| [域名注册](https://cloud.tencent.com/document/product/242)   | ✔        | -      | ✔      | 服务级   | -        |      |
| [网站备案](https://cloud.tencent.com/document/product/243)   | ✔        | -      | ✔      | 服务级   | -        | - |
| [移动解析 HttpDNS](https://cloud.tencent.com/document/product/379) | ✔        | -      | ✔      | 服务级   | -        | - |
| [大禹网络安全](https://cloud.tencent.com/document/product/297) | ✔        | ✔      | ✔      | 服务级   | -        | - |
| [主机安全（云镜）](https://cloud.tencent.com/document/product/296) | ✔        | ✔      | ✔      | 操作级   | ✔        | - |
| [态势感知](https://cloud.tencent.com/document/product/664)   | ✔        | ✔      | ✔      | 服务级   | -        | - |
| [点播](https://cloud.tencent.com/document/product/266)       | ✔        | -      | ✔      | 服务级   | -        | - |
| [直播](https://cloud.tencent.com/document/product/267)       | ✔        | -      | ✔      | 服务级   | -        |      |
| [互动直播](https://cloud.tencent.com/document/product/268)   | ✔        | -      | ✔      | 服务级   | -        |      |
| [弹性 MapReduce](https://cloud.tencent.com/document/product/589/14625) | ✔        | ✔      | ✔      | 操作级   | ✔        | - |
| [Snova 数据仓库](https://cloud.tencent.com/document/product/878) | ✔        | ✔      | ✔      | 操作级   | ✔        | - |
| [流计算服务](https://cloud.tencent.com/document/product/849) | ✔        | ✔      | ✔      | 服务级   | ✔        |      |
| [数据工坊](https://cloud.tencent.com/document/product/564)   | ✔        | -      | ✔      | 服务级   | -        | - |
| [云搜](https://cloud.tencent.com/document/product/270)       | ✔        | -      | ✔      | 服务级   | -        | - |
| [智能语音服务](https://cloud.tencent.com/document/product/441) | ✔        | -      | ✔      | 服务级   | -        | - |
| [文智自然语言处理](https://cloud.tencent.com/document/product/271) | ✔        | -      | ✔      | 服务级   | -        | - |
| [机器翻译](https://cloud.tencent.com/document/product/551)   | ✔        | -      | ✔      | 服务级   | -        | - |
| [腾讯智能钛机器学习](https://cloud.tencent.com/document/product/851) | ✔        | -      | ✔      | 服务级   | -        |      |
| [腾讯云小微](https://cloud.tencent.com/document/product/645) | ✔        | -      | ✔      | 服务级   | -        | - |
| [测试服务 WeTest](https://cloud.tencent.com/product/MGCT)    | ✔        | -      | ✔      | 服务级   | -        |      |
| [云通信](https://cloud.tencent.com/document/product/269)     | ✔        | -      | ✔      | 服务级   | -        | - |
| [短信](https://cloud.tencent.com/document/product/382)       | ✔        | -      | ✔      | 服务级   | -        |      |
| [物联网通信](https://cloud.tencent.com/document/product/634) | ✔        | ✔      | ✔      | 服务级   | ✔        | ✔    |
| [TBaaS](https://cloud.tencent.com/document/product/663)      | ✔        | ✔      | ✔      | 操作级   | ✔        | ✔ |
| [云监控](https://cloud.tencent.com/document/product/248)     | ✔        | ✔      | ✔      | 操作级   | ✔        | - |
| [标签](https://cloud.tencent.com/document/product/651)       | ✔        | ✔      | ✔      | 操作级   | ✔        | - |
| [密钥管理服务](https://cloud.tencent.com/document/product/573) | ✔        | ✔      | ✔      | 资源级   | ✔        |      |
| [云拨测](https://cloud.tencent.com/document/product/280)     | ✔        | -      | ✔      | 服务级   | -        | - |
| [云审计](https://cloud.tencent.com/document/product/629)     | ✔        | ✔      | ✔      | 操作级   | ✔        | ✔    |
| [万象优图](https://cloud.tencent.com/document/product/460)   | ✔        | -      | ✔      | 服务级   | -        | - |
| [微信云支付](https://cloud.tencent.com/document/product/569) | ✔        | -      | ✔      | 服务级   | -        | - |
| [智能推荐](https://cloud.tencent.com/document/product/587) | ✔        | -      | ✔      | 服务级   | ✔        | - |
| [数字营销](https://cloud.tencent.com/document/product/588) | ✔        | -      | ✔      | 服务级   | ✔        | - |
| [云数据库 MongoDB](https://cloud.tencent.com/document/product/240)         |-        | -      | -      | -   | -        | ✔    |
| [腾讯云应用服务平台](https://cloud.tencent.com/document/product/876)     |-        | -      | -      | -   | -        | ✔    |
| [分布式服务框架](https://cloud.tencent.com/document/product/649)     |-        | -      | -      | -   | -        | ✔    |
| [织云](https://cloud.tencent.com/document/product/609)                |-        | -      | -      | -   | -        | ✔    |
| [宙斯盾安全防护](https://cloud.tencent.com/product/aegis)       |-        | -      | -      | -   | -        | ✔    |
| [API 网关](https://cloud.tencent.com/document/product/628)         |-        | -      | -      | -   | -        | ✔    |


 ## 支持 CAM 角色的第三方服务列表

| 服务                                           | 角色 |
| ---------------------------------------------- | ---- |
| [腾讯区块链开发平台](https://trustsql.qq.com/) |  ✔    |
