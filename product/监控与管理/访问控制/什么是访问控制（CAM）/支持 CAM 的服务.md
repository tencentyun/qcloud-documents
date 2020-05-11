## 简介	

访问管理已经支持对多数腾讯云产品服务进行权限管理。本文主要介绍支持访问管理 CAM 的产品服务的相关信息。具体维度包括授权粒度、控制台、根据标签进行授权、参考文档等。
以下列表分别罗列了腾讯云平台各大产品类别下已支持 CAM 的服务。
对表中信息进行如下定义：

- 服务：支持 CAM 的云服务的名称，单击链接至对应产品服务文档，方便您快速获取相关信息。	
- 授权粒度：当前服务提供的最小授权粒度。

> ? 其中授权粒度按照粒度粗细分为服务级、操作级和资源级三个级别。	
>
> - 服务级：定义对服务的整体是否拥有访问权限，分为允许对服务拥有全部操作权限或者拒绝对服务拥有全部操作权限。
> - 操作级：定义对服务的特定接口（API）是否拥有访问权限，例如：授权某账号对云服务器服务进行只读操作。	
> - 资源级：定义对特定资源是否有访问权限，这是最细的授权粒度，例如：授权某账号仅读写操作某台云服务器。

- 控制台：是否支持子账号通过控制台访问当前服务，“&#10003;”表示支持，“-”表示暂不支持。	
- 根据标签进行授权：当前服务是否支持通过标签进行权限管理，“&#10003;”表示支持，“-”表示暂不支持。		
- [服务角色](https://cloud.tencent.com/document/product/598/19420)：当前服务是否支持作为角色载体进行跨服务授权访问其他服务，“&#10003;”表示支持，“-”表示暂不支持。	
- 参考文档：当前服务与 CAM 相关的文档链接，“-”表示暂无。

## 计算	

 | 服务                                                         | 授权粒度 | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |	
| ------------------------------------------------------------| ------ | -------- | ------- |  ---- |	---- |	
| [云服务器](https://cloud.tencent.com/document/product/213) <sup>1</sup> | 资源级  | &#10003;      |&#10003;    |  &#10003;  |	 [访问管理指南](https://cloud.tencent.com/document/product/213/10311)   |	
| [黑石物理服务器](https://cloud.tencent.com/document/product/386)  | 资源级   | &#10003;      | &#10003;   |-    |[	访问管理指南](https://cloud.tencent.com/document/product/386/13244)  |	
| [容器服务](https://cloud.tencent.com/document/product/457) | 资源级  | &#10003;       | - | &#10003;    |	[访问管理指南](https://cloud.tencent.com/document/product/457/11526)  |	
| [弹性伸缩](https://cloud.tencent.com/document/product/377) | 资源级   | &#10003;      | -  | &#10003;    |	-    |	
| [批量计算](https://cloud.tencent.com/document/product/599)  | 资源级 | &#10003;         |  -  | -    |[访问管理指南](https://cloud.tencent.com/document/product/599/40011)   |	
| [边缘计算机器](https://cloud.tencent.com/document/product/1108)  | 资源级 | &#10003;         |  -  | -    |-    |	
| [容器镜像服务](https://cloud.tencent.com/document/product/1141)  | 资源级 | &#10003;         |  -  | &#10003;     |[访问管理指南](https://cloud.tencent.com/document/product/1141/40718)    |	
> ?<sup>1</sup> 云服务器中 [GPU 服务器](https://cloud.tencent.com/document/product/560)、[ FPGA 云服务器](https://cloud.tencent.com/document/product/565)、[专用宿主机](https://cloud.tencent.com/document/product/416)  均已支持使用 CAM。

## 存储	

 | 服务                                                          | 授权粒度 | 控制台  | 根据标签进行授权 |  服务角色 |	参考文档 |	
| ------------------------------------------------------------ | ------ | --------  | ------- | ---- |	---- |	
| [对象存储](https://cloud.tencent.com/document/product/436) | 资源级 | &#10003;       | -  | &#10003;   |	[访问管理指南](https://cloud.tencent.com/document/product/436/12473)   |
| [文件存储](https://cloud.tencent.com/document/product/582) | 资源级 | &#10003;        | -  |  &#10003;    |[访问管理指南](https://cloud.tencent.com/document/product/582/14679)   |	
| [归档存储](https://cloud.tencent.com/document/product/572) | 资源级 | -        | -  |  -    |	-    |
| [云 HDFS](https://cloud.tencent.com/document/product/1105) | 资源级 |&#10003;       | -  | -    |	[访问管理指南](https://cloud.tencent.com/document/product/1105/37238)    |	
| [存储网关](https://cloud.tencent.com/document/product/581) | 服务级 |&#10003;       | -  | -    |	 - |	
| [云硬盘](https://cloud.tencent.com/document/product/362) | 资源级  | &#10003;       | &#10003;  |  -    |-    |	
| [云数据迁移](https://cloud.tencent.com/document/product/623)  | 服务级 | &#10003;        | -  |  - | - |	
| [日志服务](https://cloud.tencent.com/document/product/614)  | 资源级 | &#10003;        | -  | &#10003; |[访问管理指南](https://cloud.tencent.com/document/product/614/35564)    |	

## 网络	

 | 服务                                                       | 授权粒度 | 控制台 | 根据标签进行授权  |  服务角色 |	参考文档 |	
| ------------------------------------------------------------ | ------ | -------- | ------- | ---- |	 ---- |
| [负载均衡](https://cloud.tencent.com/document/product/214)   | 资源级  | &#10003;      | &#10003;    |    &#10003;  |	[访问管理指南](https://cloud.tencent.com/document/product/214/9776) |	
| [私有网络 VPC ](https://cloud.tencent.com/document/product/215)<sup>1</sup>  | 资源级 | &#10003;        | -     | - |	 [访问管理指南](https://cloud.tencent.com/document/product/215/20168) |	
| [专线接入](https://cloud.tencent.com/document/product/216) | 操作级   | &#10003;       | -       | -  |	 - |	
> ?<sup>1</sup> 私有网络 VPC 中 [弹性网卡](https://cloud.tencent.com/document/product/576)、[NAT 网关](https://cloud.tencent.com/document/product/552)、[对等连接](https://cloud.tencent.com/document/product/553)、[VPN 连接](https://cloud.tencent.com/document/product/554)、[网络流日志](https://cloud.tencent.com/document/product/682) 、[Anycast 公网加速](https://cloud.tencent.com/document/product/644)、[云联网](https://cloud.tencent.com/document/product/877)、[共享带宽包](https://cloud.tencent.com/document/product/684) 均已支持使用 CAM。

## CDN 与加速	

| 服务                                                      | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |	
| ------------------------------------------------------------| ------ | -------- | -------- |  ---- |	---- |	
| [全球应用加速](https://cloud.tencent.com/document/product/608)  | 资源级 | &#10003;  |  -   |  -  |-  |
| [全站加速网络](https://cloud.tencent.com/document/product/570)  | 资源级 | &#10003;  |  - | -  |[访问管理指南](https://cloud.tencent.com/document/product/570/42271)  |
| [内容分发网络](https://cloud.tencent.com/document/product/228)<sup>1</sup>| 资源级 | &#10003;   |  -   | &#10003; |[访问管理指南](https://cloud.tencent.com/document/product/228/12722)  |
> ?<sup>1</sup> 内容分发网络中 [安全加速](https://cloud.tencent.com/product/scdn) 已支持使用 CAM。

## 数据库	

 | 服务                                                         | 授权粒度 | 控制台   | 根据标签进行授权 | 服务角色 |	参考文档 |	
| ------------------------------------------------------------ | ------ | --------| --------- | ---- |	---- |
| [云数据库 MySQL](https://cloud.tencent.com/document/product/236)  | 资源级 | &#10003; | -  |  &#10003; |	[访问管理指南](https://cloud.tencent.com/document/product/236/14465) |	
| [云数据库 CynosDB](https://cloud.tencent.com/document/product/1003)  | 资源级 | &#10003; | -  |  - |	[访问管理指南](https://cloud.tencent.com/document/product/1003/38067) |	
| [云数据库 MariaDB](https://cloud.tencent.com/document/product/237)  |资源级 | &#10003;  | -    | &#10003;    |[访问管理指南](https://cloud.tencent.com/document/product/237/30940) |	
| [ 云数据库 SQL Server](https://cloud.tencent.com/document/product/238)  |资源级 | &#10003;  | -    | -     |[访问管理指南](https://cloud.tencent.com/document/product/238/38874) |	
| [分布式数据库 TDSQL](https://cloud.tencent.com/document/product/557)  |资源级 | &#10003;  | -    | -    |[访问管理指南](https://cloud.tencent.com/document/product/557/30965) |	
| [云数据库 Redis](https://cloud.tencent.com/document/product/239)   | 资源级| &#10003; | -  | - |[访问管理指南](https://cloud.tencent.com/document/product/239/38687) |	
| [云数据库 MongoDB](https://cloud.tencent.com/document/product/240) |资源级 | &#10003; | -   |&#10003;|[访问管理指南](https://cloud.tencent.com/document/product/240/38703) |	
| [云数据库 Memcached](https://cloud.tencent.com/document/product/241)  |资源级 | &#10003;  | -    | -    |[访问管理指南](https://cloud.tencent.com/document/product/241/38708) |	
| [时序数据库 CTSDB](https://cloud.tencent.com/document/product/652)  |资源级 | &#10003;  | -    | -    |[访问管理指南](https://cloud.tencent.com/document/product/652/42494) |	
| [游戏数据库 TcaplusDB](https://cloud.tencent.com/document/product/596)  |资源级 | &#10003;  | -    | -    |[访问管理指南](https://cloud.tencent.com/document/product/596/42901) |	
| [数据库智能管家 DBbrain](https://cloud.tencent.com/document/product/1130)  |资源级 | &#10003;  | -    | -    |[访问管理指南](https://cloud.tencent.com/document/product/1130/39344)|	
| [数据传输服务](https://cloud.tencent.com/document/product/571)  | 资源级 |  &#10003;  | -    | &#10003;    |[访问管理指南](https://cloud.tencent.com/document/product/571/38480)|	
| [分布式HTAP数据库 TBase](https://cloud.tencent.com/document/product/1129)  | 资源级 |  &#10003;  | -    | -   |[访问管理指南](https://cloud.tencent.com/document/product/1129/39783) |	

## Serverless	

| 服务                                                      | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |	
| ------------------------------------------------------------| ------ | -------- | -------- |  ---- |	---- |	
| [云函数](https://cloud.tencent.com/document/product/583)  | 资源级 | &#10003;        |  -  | &#10003;   |[访问管理指南](https://cloud.tencent.com/document/product/583/9203)  |	
| [Serverless Framework](https://cloud.tencent.com/document/product/1154)  | 资源级 | - |  -   |  &#10003;   |[访问管理指南](https://cloud.tencent.com/document/product/1154/41936)   |


## 中间件	

 | 服务                                                       | 授权粒度 | 控制台  | 根据标签进行授权 |  服务角色 |	参考文档 |
| ------------------------------------------------------------| ------ | -------- | -------- |  ---- |	 ---- |
| [消息队列 CMQ](https://cloud.tencent.com/document/product/406) | 资源级   | &#10003;  | - |  - |	[访问管理指南](https://cloud.tencent.com/document/product/406/8618) |
| [消息队列 CKafka](https://cloud.tencent.com/document/product/597) | 资源级 | &#10003; | - | &#10003;   |[访问管理指南](https://cloud.tencent.com/document/product/597/31528)|
| [API 网关](https://cloud.tencent.com/document/product/628)     | 资源级  | &#10003;  | -  | &#10003; |[访问管理指南](https://cloud.tencent.com/document/product/628/34267)|
| [腾讯微服务平台](https://cloud.tencent.com/document/product/649)  | 资源级  | &#10003;  | - |  &#10003; |[访问管理指南](https://cloud.tencent.com/document/product/649/38327) |

## 数据处理	

 | 服务                                                         | 授权粒度| 控制台 | 根据标签进行授权  |  服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | --------| ----- | ---- |	 ---- |	
| [数据万象](https://cloud.tencent.com/document/product/460)   | 资源级    | &#10003;   | -   | &#10003; |	[访问管理指南](https://cloud.tencent.com/document/product/460/36236) |

## 域名与网站	

 | 服务                                                         | 授权粒度| 控制台 | 根据标签进行授权  | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | --------| ----- | ---- |	---- |	
| [网站备案](https://cloud.tencent.com/document/product/243)   | 服务级    | &#10003;   | -   |  - |	- |	
| [SSL证书](https://cloud.tencent.com/document/product/400)   | 资源级    | &#10003;   | -   |  - |	[访问管理指南](https://cloud.tencent.com/document/product/400/40432) |	

## 网络安全	

 | 服务                                                          | 授权粒度 | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |
| ----------------------------------------------------------- | ------ | -------- | ----- | ---- | ---- |
| [DDOS 防护（大禹）](https://cloud.tencent.com/product/ddos)  <sup>1</sup>  | 服务级  | &#10003; | -   |  - | - |
| [样本智能分析平台](https://cloud.tencent.com/document/product/1012)  |资源级 | -   |  &#10003;   |  - |- |
| [云防火墙](https://cloud.tencent.com/document/product/1132)    | 操作级      |&#10003;    | -   |  &#10003;    |- |
| [宙斯盾安全防护](https://cloud.tencent.com/document/product/685)    | -      | -   | -   |  &#10003;    |- |
> ?<sup>1</sup> DDOS 防护（大禹）中 [DDoS 基础防护](https://cloud.tencent.com/document/product/1020)、 [BGP 高防包](https://cloud.tencent.com/document/product/1021)、[BGP 高防 IP](https://cloud.tencent.com/document/product/1014)、[高防 IP 专业版](https://cloud.tencent.com/document/product/1005)、 [棋牌盾](https://cloud.tencent.com/document/product/1022) 均已支持使用 CAM。

## 数据安全

 | 服务                                                         | 授权粒度  | 控制台  | 根据标签进行授权 | 服务角色 | 参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------- | ---- |  ---- | 
| [堡垒机](https://cloud.tencent.com/document/product/1025)    | 服务级  | &#10003; | &#10003;   | - | - |
| [数据安全审计](https://cloud.tencent.com/document/product/856)    | 服务级  | &#10003; | -  | - | - |
| [ 敏感数据处理](https://cloud.tencent.com/document/product/882)    | 服务级  | &#10003; | -  | - | - |
| [数据安全治理中心](https://cloud.tencent.com/document/product/1087)    | 操作级  | &#10003; | -   | &#10003; | - |
| [云加密机](https://cloud.tencent.com/document/product/639)    | 服务级  | &#10003; | -   | - | - |
| [密钥管理系统](https://cloud.tencent.com/document/product/573) | 资源级   | &#10003;  | -  |  -     |[访问管理指南](https://cloud.tencent.com/document/product/573/10126) |	
| [凭据管理系统](https://cloud.tencent.com/document/product/1140)    | 资源级  | &#10003; | -   | &#10003; | [访问管理指南](https://cloud.tencent.com/document/product/1140/40869)|

## 业务安全

 | 服务 | 授权粒度  | 控制台  | 根据标签进行授权 |  服务角色 | 参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------- | ---- |  ---- |
| [借贷反欺诈](https://cloud.tencent.com/document/product/668)  | 服务级  | &#10003; | -   |  - | - |
| [保险反欺诈](https://cloud.tencent.com/document/product/1030)  | 服务级  | - | -   |  - | - |
| [定制建模](https://cloud.tencent.com/document/product/1029)  | 服务级  | &#10003; | -   |  - | - |
| [天御业务安全防护](https://cloud.tencent.com/document/product/295)<sup>1</sup>    | 服务级  | &#10003; | -   |  - | - |
| [流量反欺诈](https://cloud.tencent.com/document/product/1031)| 操作级  | &#10003; | -   |  - | - |
| [内容安全](https://cloud.tencent.com/document/product/669) <sup>2</sup>   | 服务级  | &#10003; | -   |  - | - |
> ?<sup>1</sup> 天御业务安全防护中活动防刷、登录保护、注册保护、行业风险评估、置信度评分均已支持使用 CAM。
> <sup>2</sup> 内容安全中  [图片内容安全](https://cloud.tencent.com/document/product/1125)、 [文本内容安全](https://cloud.tencent.com/document/product/1124) 均已支持使用 CAM。

## 营销风控

 | 服务                                                         | 授权粒度  | 控制台  | 根据标签进行授权 | 服务角色 |  参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------- | ---- | ---- | 
| [验证码](https://cloud.tencent.com/document/product/1110)    | 服务级  | &#10003; | -   |  - | - |
| [营销号码安全](https://cloud.tencent.com/document/product/1127)    | 操作级  | - | -   |  - | - |

## 安全管理

 | 服务                                                         | 授权粒度  | 控制台  | 根据标签进行授权 | 服务角色 | 参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------- | ---- |  ---- | 
| [安全运营中心](https://cloud.tencent.com/document/product/664)    | 操作级  | &#10003; | -   | &#10003; |-  | 

## 应用安全

 | 服务                                                        | 授权粒度   | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------ |---- |	---- |	
| [Web 应用防火墙](https://cloud.tencent.com/document/product/627)  | 操作级 | &#10003;  | -  |  - |- |
| [漏洞扫描服务](https://cloud.tencent.com/document/product/692)  | 操作级 | &#10003;  | -  |  - |- |
| [网络资产风险监测系统](https://cloud.tencent.com/document/product/1088)  | 服务级 | &#10003;  | -  | &#10003; |- |

## 视频服务

 | 服务                                                         | 授权粒度 | 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	---- |	
| [实时音视频](https://cloud.tencent.com/document/product/647)   | 服务级| &#10003; | -  |  - |	-|	
| [云直播](https://cloud.tencent.com/document/product/267)   | 资源级| &#10003; | &#10003;  |  &#10003;  |	[访问管理指南](https://cloud.tencent.com/document/product/267/34301) |	
| [云点播](https://cloud.tencent.com/document/product/266)    | 资源级   | &#10003;  | -    |  -  |	[访问管理指南](https://cloud.tencent.com/document/product/266/39337)  |	
| [视频处理](https://cloud.tencent.com/document/product/862)    | 服务级   | &#10003;  | -    |   &#10003;   |	-  |	
| [互动直播](https://cloud.tencent.com/solution/ilvb) | 服务级  | &#10003;   | -   |  -   |	-  |	

## 视频智能
 | 服务                                                         | 授权粒度 | 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	---- |	
| [智能编辑](https://cloud.tencent.com/document/product/1186)   | 服务级| &#10003; | -  |  - |	-|	

## 移动开发
 | 服务                                                         | 授权粒度 | 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	---- |	
| [云开发](https://cloud.tencent.com/document/product/876)   |服务级  | &#10003; | -   | &#10003;  |	-   |

## 云智大数据平台

 | 服务                                                       | 授权粒度   | 控制台  | 根据标签进行授权 |  服务角色 |	参考文档 |
| ----------------------------------------------------------- | ------ | --------| ----- |  ---- |	 ---- |
| [弹性 MapReduce](https://cloud.tencent.com/document/product/589)   | 操作级 | &#10003;  | -   |  &#10003;  |	 [访问管理指南](https://cloud.tencent.com/document/product/589/14625) |
| [Snova 数据仓库](https://cloud.tencent.com/document/product/878) | 操作级  | &#10003;  | - |  - | [访问管理指南](https://cloud.tencent.com/document/product/878/20072) |
| [流计算服务](https://cloud.tencent.com/document/product/849)  | 服务级   | &#10003;     | -  | &#10003;  | [访问管理指南](https://cloud.tencent.com/document/product/849/38621) |
| [Elasticsearch Service](https://cloud.tencent.com/document/product/845)  | 操作级   | &#10003; | -   |  -  |	 [访问管理指南](https://cloud.tencent.com/document/product/845/19550) |

## 云智大数据可视化

 | 服务                                                         | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	 ---- |	
| [商业智能分析](https://cloud.tencent.com/document/product/590) | 服务级| &#10003;| -  |  - |	 [访问管理指南](https://cloud.tencent.com/document/product/590/19284) |	
| [腾讯云图](https://cloud.tencent.com/document/product/665) | 资源级| &#10003;| -  |  - |	 [访问管理指南](https://cloud.tencent.com/document/product/665/40956) |	

## 云智大数据应用

 | 服务                                                         | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	 ---- |	
| [智能推荐](https://cloud.tencent.com/document/product/587) | 服务级| &#10003;| -  |  - |	 - |	

## 文字识别

 | 服务                                                         | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	 ---- |	
| [文字识别](https://cloud.tencent.com/document/product/866) | 服务级| &#10003;| -  | - |	 - |	

## 图像识别

 | 服务                                                         | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | -------- | ---- |	 ---- |	
| [图像分析](https://cloud.tencent.com/document/product/865) | 服务级| -| -  | - |	 - |	
| [智能识图](https://cloud.tencent.com/document/product/1217) | 服务级| -| -  | - |	 - |	

## 人脸识别

 | 服务                                                         | 授权粒度  | 控制台 | 根据标签进行授权|  服务角色 |		参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------ |  ---- |	 ---- |	
| [人脸识别](https://cloud.tencent.com/document/product/867) | 服务级| &#10003; | -  |  &#10003; |	[访问管理指南](https://cloud.tencent.com/document/product/867/35076)  |
| [人脸核身](https://cloud.tencent.com/document/product/1007) | 服务级| &#10003; | -  |  - |	-  |

## 人脸特效

 | 服务                                                         | 授权粒度  | 控制台 | 根据标签进行授权|  服务角色 |		参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ------ |  ---- |	 ---- |	
| [人脸融合](https://cloud.tencent.com/document/product/670) | 服务级| &#10003; | -  |  - |	-  |
| [人脸试妆](https://cloud.tencent.com/document/product/1172) | 服务级| &#10003; | -  |  - |	-  |
| [人像变换](https://cloud.tencent.com/document/product/1202) | 服务级| &#10003; | -  |  - |	-  |

## 语音技术	

 | 服务                                                           | 授权粒度 | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |
| ------------------------------------------------------------| ------ | -------- | ------- | ---- |	---- |	
| [语音合成](https://cloud.tencent.com/document/product/1073)  | 操作级 |  &#10003; | -  |  - |	 - |	
| [语音识别](https://cloud.tencent.com/document/product/1093)  | 操作级 |  &#10003; | -  |  - |	 - |	

## 自然语言处理	

 | 服务                                                        | 授权粒度 | 控制台   | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------  | ------ | --------| -------  | ---- |	 ---- |
| [自然语言处理](https://cloud.tencent.com/document/product/271)  | 服务级 | &#10003;  | -   |   -|	-|	
| [机器翻译](https://cloud.tencent.com/document/product/551)  | 操作级 | &#10003;  | -   |   -|	-|	

## 企业通信	

 | 服务                                                        | 授权粒度 | 控制台   | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------  | ------ | --------| -------  | ---- |	 ---- |
| [云呼叫中心](https://cloud.tencent.com/document/product/679)  | 服务级 | &#10003;  | -   |   -|	-|	

## 办公协同	

 | 服务                                                        | 授权粒度 | 控制台   | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------  | ------ | --------| -------  | ---- |	 ---- |
| [云投屏](https://cloud.tencent.com/document/product/1001)  | 操作级 | &#10003;  | -   |   -|	-|	

## 金融服务

 | 服务                                                       | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ----- | ---- |	 ---- |	
| [金融联络机器人](https://cloud.tencent.com/document/product/656)  | 资源级 | &#10003; | -  |  - | - |
| [企业收付平台](https://cloud.tencent.com/document/product/1122)  | 操作级 | &#10003; | -  |  - | - |
| [云缴费平台](https://cloud.tencent.com/document/product/1097)  | 服务级 | &#10003; | -  |  - | - |

## 智能机器人	

 | 服务                                                         | 授权粒度 | 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ----- | ---- |	---- |
| [腾讯云小微](https://cloud.tencent.com/document/product/645)  | 服务级 | &#10003; | - |  - |- |

## AI 平台服务	

 | 服务                                                          | 授权粒度| 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| ---------------------------------------------------------| ------ | -------- | ------ | ---- |	 ---- |	
| [腾讯智能钛机器学习](https://cloud.tencent.com/document/product/851)  | -  | -   | -   |   &#10003;   |	  - |
| [ 智能钛弹性模型服务 ](https://cloud.tencent.com/document/product/1120)  | 服务级  | &#10003;   | -   |   &#10003;   |	  - |
| [智能对话平台 ](https://cloud.tencent.com/document/product/1060)  | 服务级  | &#10003;   | -   |  -  |	  - |

## 游戏服务

| 服务                                                        | 授权粒度 | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |
| ----------------------------------------------------------- | ------ | -------- | ----- |  ---- |	 ---- |	
| [小游戏联机对战引擎](https://cloud.tencent.com/document/product/1038)  | 资源级  | &#10003; | -   | &#10003;   | [访问管理指南](https://cloud.tencent.com/document/product/1038/38760)   |	
| [游戏多媒体引擎](https://cloud.tencent.com/document/product/607)  | 资源级 | &#10003;| -   |  -    |	 -   |

## 教育服务	

 | 服务 | 授权粒度  | 控制台 | 根据标签进行授权 | 服务角色 |		参考文档 |
| ------------------------------------------------------------  | ------ | -------- | -------- | ---- |	---- |	
| [智聆口语评测](https://cloud.tencent.com/document/product/884)   | 操作级 | &#10003;  | -   |  -  |	-  |	
| [ 数学作业批改](https://cloud.tencent.com/document/product/1004)   | 操作级 | &#10003; | -   |  -  |	-  |	
| [题目结构化归档](https://cloud.tencent.com/document/product/1085)   | 操作级 | - | -   |  -  |	-  |	
| [互动白板](https://cloud.tencent.com/document/product/1137)   | 操作级 | - | -   |  -  |	-  |	

## 移动服务	

 | 服务                                                        | 授权粒度  | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |
| ------------------------------------------------------------  | ------ | -------- | ------- | ---- |	---- |	
| [ 腾讯移动推送](https://cloud.tencent.com/document/product/548)   |资源级  | &#10003; | -   |  -   |	[访问管理指南](https://cloud.tencent.com/document/product/548/41370)   |
| [ 正版曲库直通车（版权音乐助手）](https://cloud.tencent.com/document/product/1155)   |服务级  | &#10003; | -   |  -   |	-   |

## 云通信	

 | 服务                                                         | 授权粒度 | 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------ | ------ | -------- | ----- | ---- |	---- |
| [即时通信](https://cloud.tencent.com/document/product/269)   | 服务级 | &#10003;   | -  |  - | - |
| [短信](https://cloud.tencent.com/document/product/382) | 操作级 | &#10003; | -   | -  |	-  |	
| [语音消息](https://cloud.tencent.com/document/product/1128) | 操作级 | &#10003; |-  | -  |	-  |	
| [号码保护](https://cloud.tencent.com/document/product/610) | 服务级 | - |-  | -  |	-  |	

## 物联网	

 | 服务                                                          | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| -------------------------------------------------------- | ------ | -------- | ------- | ---- |	---- |	
| [物联网通信](https://cloud.tencent.com/document/product/634)   | 服务级 | &#10003;   | -  |  &#10003; | [访问管理指南](https://cloud.tencent.com/document/product/634/14441)  |
| [物联网设备身份认证](https://cloud.tencent.com/document/product/1086)   | 服务级 | &#10003;   | -  |  - | -  |
| [ LPWA 物联网络](https://cloud.tencent.com/document/product/1023)   | 服务级 | &#10003;  | -  |  -  | -  |
| [物联网开发平台](https://cloud.tencent.com/document/product/1081)   | 服务级 | &#10003;  | -  |  -  | -  |
| [ 物联网智能视频服务](https://cloud.tencent.com/document/product/1131)   | 服务级  | &#10003;  | -  |  &#10003;  | -  |

## 区块链	

 | 服务                                                          | 授权粒度 | 控制台  | 根据标签进行授权  |服务角色 |	参考文档 |
| ----------------------------------------------------------- | ------ | -------- | ------ |  ---- |	 ---- |
| [腾讯云区块链服务 TBaaS](https://cloud.tencent.com/document/product/663) | 操作级   | &#10003; | -  | - |	[访问管理指南](https://cloud.tencent.com/document/product/663/38486)|	

## 企业应用	

 | 服务                                                          | 授权粒度 | 控制台  | 根据标签进行授权  |服务角色 |	参考文档 |
| ----------------------------------------------------------- | ------ | -------- | ------ |  ---- |	 ---- |
| [商标注册](https://cloud.tencent.com/document/product/1145) | 服务级   | &#10003; | -  | - |	-|	

## 云资源管理

 | 服务                                                         | 授权粒度  | 控制台 | 根据标签进行授权 |  服务角色 |	参考文档 |
| ----------------------------------------------------------- | ------ | -------- | ----- | ---- |	 ---- |	
| [标签](https://cloud.tencent.com/document/product/651) | 操作级 | &#10003;  | - |  - |	 - |	
| [资源编排 TIC](https://cloud.tencent.com/document/product/1213) | 服务级 | &#10003;  | - |  - |	 - |	

## 管理与审计

 | 服务                                                         | 授权粒度 | 控制台  | 根据标签进行授权 |  服务角色 |	参考文档 |
| ------------------------------------------------------------| ------ | --------| ----- |  ---- |		 ---- |
| [访问管理](https://cloud.tencent.com/document/product/598)  | 操作级  | &#10003; | -   | -    | [访问管理指南](https://cloud.tencent.com/document/product/598/10590)   |
| [云审计](https://cloud.tencent.com/document/product/629)  | 操作级  | &#10003; | -   | &#10003;    | -   |
| [企业组织](https://cloud.tencent.com/document/product/850) | 操作级 | &#10003; | -  |- | -   |
| [商业流程服务](https://cloud.tencent.com/document/product/1083)  | 操作级 | &#10003; | -   | &#10003;  | [访问管理指南](https://cloud.tencent.com/document/product/1083/34888)  |
| [身份管理服务](https://cloud.tencent.com/document/product/1106)  | - | - | -   |  &#10003;  | - |

## 监控与运维	

 | 服务                                                         | 授权粒度 | 控制台  | 根据标签进行授权 | 服务角色 |	参考文档 |
| ------------------------------------------------------------  | ------ | -------- | ----- | ---- |	---- |
| [云监控](https://cloud.tencent.com/document/product/248) | 操作级 | &#10003;  | -  |  &#10003; |	- |	
| [云拨测](https://cloud.tencent.com/document/product/280)  | 服务级   | &#10003; | -   |-     |	- |	
| [迁移服务平台](https://cloud.tencent.com/document/product/659)  | 服务级   | &#10003; | -   |&#10003;    |	- |	

## 解决方案	

 | 服务                                                          | 授权粒度 | 控制台 | 根据标签进行授权 | 服务角色 |	参考文档 |
| -------------------------------------------------------- | ------ | -------- | ------- | ---- |	 ---- |	
| [云支付](https://cloud.tencent.com/document/product/569)  | 服务级 | &#10003;   | -  |  - | - |
| [商业直播](https://cloud.tencent.com/document/product/1078)  | 操作级 | &#10003;   | -  |  - | - |
| [企业微信云](https://cloud.tencent.com/document/product/1119)  | 资源级 | &#10003;   | -  |  - |[访问管理指南](https://cloud.tencent.com/document/product/1119/38419) |
| [在线课堂](https://cloud.tencent.com/document/product/680)  | 服务级 | &#10003;  | -  |  - |- |
| [数字版权管理解决方案](https://cloud.tencent.com/document/product/1000)  | 操作级 | -  | -  |  - |- |

## 开发者工具

 | 服务                                                           | 授权粒度 | 控制台  | 根据标签进行授权 |  服务角色 |	参考文档 |
| --------------------------------------------------- | ------ | -------- | --------- |  ---- |	 ---- |
| [ CODING DevOps](https://cloud.tencent.com/product/coding)  <sup>1</sup> | 服务级 | &#10003;   | -   | &#10003;   |-    |
> ?<sup>1</sup> CODING DevOps 中 [代码托管](https://cloud.tencent.com/document/product/1112)、[项目管理](https://cloud.tencent.com/document/product/1113)、[测试管理](https://cloud.tencent.com/document/product/1114)、[持续集成](https://cloud.tencent.com/document/product/1115)、[制品库](https://cloud.tencent.com/document/product/1116) 、[持续部署](https://cloud.tencent.com/document/product/1159) 均已支持使用 CAM。


## 管理与支持

 | 服务                                                           | 授权粒度 | 控制台  | 根据标签进行授权 |  服务角色 |	参考文档 |
| --------------------------------------------------- | ------ | -------- | --------- |  ---- |	 ---- |
| [渠道合作伙伴](https://cloud.tencent.com/document/product/563)| 操作级  | &#10003;  | -    |-    |[访问管理指南](https://cloud.tencent.com/document/product/563/31828)   |	
| [开发者实验室](https://cloud.tencent.com/document/product/658/13897)   | -  | -   | -   | &#10003;   |	-    |	


## 第三方服务	

 | 服务                                                          | 服务角色 |	
| ------------------------------------------------------------ | ---- |	
| [腾讯区块链开发平台](https://trustsql.qq.com/)               | &#10003;    |





