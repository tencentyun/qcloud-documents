### 日志主题

日志主题（Topic）是日志数据在日志服务（Cloud Log Service，CLS）平台进行采集、存储、检索和分析的基本单元，采集到的海量日志以日志主题为单元进行管理，包括采集规则配置、保存时间配置、日志检索分析以及日志下载/消费/投递等。

一个日志主题通常对应某一个应用/服务，建议将同一个应用/服务在不同机器上的同类日志采集到同一个日志主题。例如，某支付服务（payService）部署在数十台机器上，包含访问日志（access_log）和错误日志（error_log）两类日志。可创建 payService_access_log_topic 和 payService_error_log_topic 两个日志主题，分别对应这数十台机器上的两类日志，通过这两个日志主题即可完成数十台机器上的所有日志的集中检索和分析。

日志主题与应用/服务之间并非严格的一一对应关系，如果两个服务之间的日志结构相似度较高，且经常需要集中分析日志，也可以将这两个服务的日志上报至同一日志主题下。



### 日志集

日志集（Logset）是对日志主题的分类，一个日志集可包含多个日志主题。日志集本身不存储任何日志数据，仅方便用户管理日志主题。

一个日志集通常对应公司内的某一个项目/业务，建议将某个项目/业务下的多个应用/服务的日志主题归属到同一个日志集下。例如，公司某电商项目下包含多个服务（支付服务 payService、用户服务 userService、库存管理服务 stockService 等），可创建一个日志集  e_commerce_logset，将这些服务的日志主题均归属至该日志集下。这样当公司有多个项目时，具体的项目人员只需要查看所属项目对应的日志集下的日志主题即可，其它项目的日志主题不会对其产生干扰。

>! 新建日志主题时可指定其归属的日志集，保存后不能再变更。
>

## 场景示例

![](https://qcloudimg.tencent-cloud.cn/raw/4e25a8a18a2a9e3f8cbe885b963e62db.png)

如上图，该公司有两个部门：

- 部门 A 有一个电商项目，采用微服务架构，每个服务均包含访问日志（access_log）和错误日志（error_log）两类日志。
- 部门 B 有两个项目，分别为小程序游戏项目和小程序社交项目，技术架构比较简单，均各有一个 Nginx 的访问日志（nginx_log）。

使用 CLS 监控上述这些应用日志时，可创建如下的日志集及日志主题：

| 日志集              | 日志主题                      | 标签       |
| ------------------- | ----------------------------- | ---------- |
| e_commerce_logset   | payService_access_log_topic   | 部门:部门A |
| e_commerce_logset   | payService_error_log_topic    | 部门:部门A |
| e_commerce_logset   | userService_access_log_topic  | 部门:部门A |
| e_commerce_logset   | userService_error_log_topic   | 部门:部门A |
| e_commerce_logset   | stockService_access_log_topic | 部门:部门A |
| e_commerce_logset   | stockService_error_log_topic  | 部门:部门A |
| e_commerce_logset   | ......                        | 部门:部门A |
| gameApplet_logset   | gameApplet_nginx_log_topic    | 部门:部门B |
| socialApplet_logset | socialApplet_nginx_log_topic  | 部门:部门B |

其中的标签用来区分日志集及日志主题归属的部门，结合权限策略还可以控制每个部门的人员仅可查看所属部门的数据。
对于部门 A，e_commerce_logset 日志集涵盖了其电商业务下的所有服务的日志主题，后续如果新增其他的项目，新建一个日志集即可。
对于部门 B，虽然目前的技术架构比较简单，总共只有两类日志，但却创建了两个日志集，每个日志集只有一个日志主题，是出于如下目的：
- 支持后续架构扩展：如果业务规模上升，技术架构也演变为微服务架构后，可继续沿用当前的日志集，在当前日志集下新增日志主题即可，不同的项目之间互不影响
- 灵活应对项目调整：如果把整个部门作为一个日志集，当其中的某个项目需要独立为一个部门，或需调整至另一个部门时，由于日志主题不能直接变更其归属的日志集，调整将变得非常麻烦，可能需要重新采集日志。而每个项目分别对应一个日志集时，则不存在该情况，只需调整日志集和日志主题对应的标签即可。
