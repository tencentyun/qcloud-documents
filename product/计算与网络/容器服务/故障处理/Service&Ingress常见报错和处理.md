


Kuberentes 通过声明式的方式管理资源，声明式 API 只需要声明一个期望的状态，系统就会自行调节以满足该状态。但声明式 API 也引入新的问题：无法感知资源当前状态信息，对任务的流程把握不够清晰。

为了保证负载均衡实例配置信息的一致性，整个 Service/Ingress 是作为一个资源整体进行同步的。若 CLB 类型的 Service/Ingress 有任何监听器级别的配置错误问题，会导致整个负载均衡同步失败，并以 Event 的形式反馈问题让用户进行处理。资源同步正确时，也会有该资源正常完成同步的 Event 更新。

Service/Ingress 作为用户直接对外提供服务的资源对象，如果异常将导致服务不可用，影响服务质量。本文提供了常见的 Service/Ingress 报错原因和处理办法。

## 如何查看 Service/Ingress Event 的报错信息？
<dx-tabs>
::: 通过控制台
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**集群**。
2. 在“集群管理”页面中，选择需要更新 YAML 的集群 ID，进入集群基本信息页面。
3. 选择**服务与路由** > **Service** 或 **Ingress**，进入 Service 或 Ingress 信息页面。
4. 单击某个具体的 Service 或 Ingress 名称。
5. 在“事件”页签，可查看当前 Service 或 Ingress 的事件信息。如下图所示，可以查看当前 Service/Ingress 的 Event 报错代码。
![](https://qcloudimg.tencent-cloud.cn/raw/4043c4e9101bfbe3a95ec0c0e361f62e.png)
>! 资源事件只保存最近 1 小时内发生的事件，请尽快查阅。
:::
::: 通过命令行
- 获取异常 Ingress 资源列表和报错信息：
```
kubectl get event | grep ingress  
```
- 获取异常 Service 资源列表和报错信息：
```
kubectl get event | grep service  
```
:::
</dx-tabs>
 

## Service Event 报错原因和处理办法

| 错误码 | 错误内容                                   | 解决方案                                                     | 不修改可能存在的风险                                       |
| ------ | ------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- |
| E4001  | TKE_QCSRoles 授权                           |登录访问管理控制台，检查 TKE 服务账户授权，并重新添加授权。详情可参见 [服务授权相关角色权限说明](https://cloud.tencent.com/document/product/457/43416)。| 集群维度，组件不能正常工作                                 |
| E4004  | 负载均衡数量超出上线                       | [提交工单](https://console.cloud.tencent.com/workorder/category) 申请负载均衡数量 Quota。 | 新增资源没有流量接入                                       |
| E4005  | 负载均衡创建参数错误                       | 检查创建参数：service.kubernetes.io/service.extensiveParameters，详情可参见 [Service Annotation 说明](https://cloud.tencent.com/document/product/457/51258#service.kubernetes.io.2Fservice.extensiveparameters)。 | 新增资源没有流量接入                                       |
| E4008  | 子网 IP 不足                                 | 三种方案：<br />1. 更换其他有足够 IP 的子网新建子网。<br />2. 更新 Service 注解使用新的子网 ID。<br />3. 改为使用公网类型的负载均衡。 | 新增资源没有流量接入                                       |
| E4009  | 欠费                                       | 您需要充值帐户。                                              | 新增资源没有流量接入                                       |
| E4011  | 使用已有负载均衡不存在                     | 登录负载均衡控制台，找到与当前集群相同的 VPC 下的负载均衡实例，确认负载均衡 ID，使用一个真实有效负载均衡 ID，详情可参见 [Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491)。 | 新增资源没有流量接入                                       |
| E4012  | 使用已有负载均衡是其他 TKE 管理的资源      | 使用已有负载均衡必须是用户自己在负载均衡控制台新建的，详情可参见 [Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491)。 | 新增资源没有流量接入                                       |
| E4013  | 使用已有负载均衡是其他集群使用的资源       | 不支持夸集群使用负载均衡，使用其他负载均衡或者删除该资源。详情可参见 [多 Service 复用 CLB](https://cloud.tencent.com/document/product/457/46370)。 | 新增资源没有流量接入                                       |
| E4014  | 使用已有负载均衡存在端口冲突               | 多个 Service 声明使用了同一个端口，修改报错 Service 的端口声明，使用其他端口避免冲突，详情可参见 [Service 使用已有 CLB](https://cloud.tencent.com/document/product/457/45491)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4016  | 用户未开通复用功能                         | 申请开白 Service 复用能力，详情可参见 [多 Service 复用 CLB](https://cloud.tencent.com/document/product/457/46370)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4026  | 外挂配置未找到                             | 不阻塞用户配置，详情可参见 [Service 负载均衡配置](https://cloud.tencent.com/document/product/457/45490)，有两种方案：<br />1. 删除 Service 中该外挂配置功能。<br />2. 注解添加对应名称的 TkeServiceConfig 资源。 | 暂无                                                       |
| E4033  | 开启直连，但是没有工作负载后端支持直连接入 | 工作负载使用弹性网卡网络模式，并且关闭 HostNetwork 删除直连注解，使用 NodePort 接入，直连 Service 使用说明请参见 [使用 LoadBalancer 直连 Pod 模式 Service](https://cloud.tencent.com/document/product/457/41897)。 | 后端更新可能失败，用户滚动更新时可能导致断流               |
| E4036  | 后端四元组冲突                             | 负载均衡 VIP、监听器端口、后端 IP、后端端口，四元组必须保持唯一。负载均衡限制，用户需要在 Pod 上监听多个端口，分别进行绑定解决这个问题。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4037  | 子网不存在                                 | 三种方案：<br />1. 更换其他有足够 IP 的子网新建子网。<br />2. 更新 Service 注解使用新的子网 ID。<br />3. 改为使用公网类型的负载均衡。 | 新增资源没有流量接入                                       |
| E4062  | 证书过期                                   | 证书服务添加新的证书，并更新扩展协议注解中声明的 Secret 资源内容，按照文档格式填写证书 ID，详情可参见 [Service 扩展协议](https://cloud.tencent.com/document/product/457/51259)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4075  | 跨地域功能，地域 ID 错误                     | 检查 Service 中的跨地域注解，地域  ID 可参见 [地域与可用区](https://cloud.tencent.com/document/product/215/20057)。 | 新增资源没有流量接入                                       |

## Ingress Event 报错原因和处理办法

| 错误码 | 错误内容                                                     | 解决方案                                                     | 不修改可能存在的风险                                       |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------- |
| E4003  | 负载均衡数量到上限                                           | [提交工单](https://console.cloud.tencent.com/workorder/category) 申请负载均衡数量 Quota。 | 新增资源没有流量接入                                       |
| E4005  | 转发规则数量到上限                                           | [提交工单](https://console.cloud.tencent.com/workorder/category) 申请负载均衡数量 Quota。 | 新增资源没有流量接入                                       |
| E4008  | TKE_QCSRole 授权被删除                                       | 登录访问管理控制台，检查 TKE 服务账户授权，并重新添加授权。详情可参见 [服务授权相关角色权限说明](https://cloud.tencent.com/document/product/457/43416)。 | 集群维度，组件不能正常工作                                 |
| E4009  | TLS 字段未配置 Secret 名称                                   | 若您需要 HTTPS 协议的转发规则，则需要修改 Ingress 里的 TLS 字段，配置 HTTPS 监听器需要的证书。详情可参见 [Ingress 证书配置](https://cloud.tencent.com/document/product/457/45738)。若您不需要 HTTPS 协议的转发规则，删除 TLS 字段，使用 HTTP 协议进行服务暴露。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4010  | TLS 字段配置 Secret 无法找到                                 | 新建 Ingress 中声明的 Secret 资源，并按照文档格式填写证书 ID，详情可参见 [Ingress 证书配置](https://cloud.tencent.com/document/product/457/45738)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4011  | TLS 字段配置 Secret 内容错误，没有证书 ID                        | 更新 TLS 中声明的 Secret 资源内容，按照文档格式填写证书 ID，详情可参见 [Ingress 证书配置](https://cloud.tencent.com/document/product/457/45738)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4012  | 证书状态异常                                                 | 证书服务添加新的证书，并更新 TLS 中声明的 Secret 资源内容，按照文档格式填写证书 ID，详情可参见 [Ingress 证书配置](https://cloud.tencent.com/document/product/457/45738)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4018  | 指定已有负载均衡不存在                                       | 到负载均衡控制台找到与当前集群相同的 VPC 下的 负载均衡实例，确认负载均衡 ID，使用一个真实有效负载均衡 ID，详情可参见 [Ingress 使用已有 CLB](https://cloud.tencent.com/document/product/457/45686)。 | 新增资源没有流量接入                                       |
| E4019  | 指定已有负载均衡是 TKE 创建的                                  | 使用已有负载均衡必须是用户自己在负载均衡控制台新建的，详情可参见 [Ingress 使用已有 CLB](https://cloud.tencent.com/document/product/457/45686)。 | 新增资源没有流量接入                                       |
| E4020  | 指定已有负载均衡是其他 Ingress 使用的                          | 使用已有负载均衡必须是用户自己在负载均衡控制台新建的，详情可参见 [Ingress 使用已有 CLB](https://cloud.tencent.com/document/product/457/45686)。 | 新增资源没有流量接入                                       |
| E4021  | 指定已有负载均衡监听器未排空                                 | 登录负载均衡控制台，删除该负载均衡所有的监听器。                 | 新增资源没有流量接入                                       |
| E4022  | kubernetes.io/ingress.http-rules，注解格式不正确             | 参考 [Ingress Annotation 说明](https://cloud.tencent.com/document/product/457/56112)，确认注解内容是否合法，建议使用控制台对资源进行更新。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4023  | kubernetes.io/ingress.https-rules，注解格式不正确            | 参考 [Ingress Annotation 说明](https://cloud.tencent.com/document/product/457/56112)，确认注解内容是否合法，建议使用控制台对资源进行更新。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4027  | 账户欠费                                                     | 您需要充值帐户。                                               | 新增资源没有流量接入                                       |
| E4031  | 转发规则存在不合法字符                                       | 修改转发规则 Rule 字段。负载均衡转发路径不支持正则。         | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4034  | IPv6 CLB，未声明 host 字段。（IPv4 可以不填 Host，默认为 VIP，IPv6 不支持） | 补充 Ingress 中所有 Host 字段，不能留空。                      | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4035  | 证书 ID 格式错误                                             | 更新 TLS 中声明的 Secret 资源内容，按照文档格式填写证书 ID，详情可参见 [Ingress 证书配置](https://cloud.tencent.com/document/product/457/45738)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4039  | 证书过期                                                     | 证书服务添加新的证书，并更新 TLS 中声明的 Secret 资源内容，按照文档格式填写证书 ID，详情可参见 [为 TKE Ingress 证书续期](https://cloud.tencent.com/document/product/457/49099)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4040  | Ingress 存在域名没有声明对应证书。                              | 修改 TLS 字段， 配置 HTTPS 监听器需要的证书，详情可参见 [Ingress 证书配置](https://cloud.tencent.com/document/product/457/45738)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4041  | Ingress 中转发规则指定的 Service 不存在。                      | 如果您的 Service 确实不存在，需要删除 Ingress 中使用该 Service 的转发规则如果您需要使用该 Service，则在与 Ingress 相同的命名空间下，新建该名称 Service 资源。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4042  | Ingress 中转发规则指定的 Service 不存在对应转发端口             | 如果您的 Service 确实不存在这样的端口，需要删除 Ingress 中使用该 Service 的转发规则如果是端口配置问题，需要更新成新端口。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4043  | Ingress 指定绑定的 TkeServiceConfig 资源不存在                 | 不阻塞用户配置，详情可参见 [Ingress 使用 TkeServiceConfig 配置 CLB](https://cloud.tencent.com/document/product/457/45700)，有两种方案：删除 Service 中该外挂配置功能注解添加对应名称的 TkeServiceConfig 资源。 | 暂无                                                       |
| E4044  | kubernetes.io/ingress.rule-mix，填了非合法值                 | 改成 true 或 false，详情可参见 [Ingress 混合使用 HTTP 及 HTTPS 协议](https://cloud.tencent.com/document/product/457/45693)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4046  | 资源带宽注解配置错误，格式错误或带宽范围错误                 | 带宽合法值 1-2048                                            | 新增资源没有流量接入                                       |
| E4047  | Ingress 中转发规则指定的 Service 为 ClusterIP 类型，没有转发端口接入 | 修改报错 Service 为 NodePort 类型                            | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4048  | Ingress 存在域名声明了多个默认证书                            | TLS 字段中声明了多个没有 Host 配置的 Secret。删除至只剩一个。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4049  | Ingress 存在某个固定域名声明了多个证书                        | TLS 字段中有一个域名声明了多个 Secret。删除至只剩一个。      | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4051  | 用户手动外挂配置指定了系统自动化生成的配置                   | 详情可参见 [Ingress 使用 TkeServiceConfig 配置 CLB](https://cloud.tencent.com/document/product/457/45700)，改用其他名称的资源。 | 暂无                                                       |
| E4052  | Ingress 中转发规则指定的域名不符合正则要求                   | 检查并修改错误域名一般错误原因域名不带"."，如 Host: test 域名用大写，如 Host: Test.com 正则：`(\*\|[a-z0-9]([-a-z0-9]*[a-z0-9])?)(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)+ `| 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4053  | 子网 IP 用尽，无法创建负载均衡                                 | 三种方案：<br />1. 更换其他有足够 IP 的子网新建子网。<br />2. 更新 Service 注解使用新的子网 ID。<br />3. 改为使用公网类型的负载均衡。 | 新增资源没有流量接入                                       |
| E4054  | 后端数量达到上限                                             | [提交工单](https://console.cloud.tencent.com/workorder/category) 申请负载均衡后端数量 Quota。 | 后端更新可能失败，用户滚动更新时可能导致断流               |
| E4055  | 子网不存在或格式错误，无法创建负载均衡                       | 三种方案：<br />1. 更换其他有足够 IP 的子网新建子网。<br />2. 更新 Service 注解使用新的子网 ID。<br />3. 改为使用公网类型的负载均衡。 | 新增资源没有流量接入                                       |
| E4060  | 账户未开白，无法为用户开启 SNAT Pro 功能                       | [提交工单](https://console.cloud.tencent.com/workorder/category) 申请负载均衡开白 SNAT Pro 能力。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4066  | 集群初始化失败，CRD 无法创建                                  | 用户集群存在问题，需要 [提交工单](https://console.cloud.tencent.com/workorder/category)。                               | 集群维度，组件不能正常工作                                 |
| E4068  | 自动重定向规则和用户其他声明规则冲突                         | 使用自动重定向功能建议不要再声明其他转发规则，详情可参见 [Ingress 重定向](https://cloud.tencent.com/document/product/457/59096)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4071  | 跨地域配置错误，CLB 所在 VPC 和当前集群所在 VPC 不在同一个云联网中 | 使用云联网关联两个 VPC 更换其他云联网内的 VPC 详情可参见 [Ingress 跨域绑定](https://cloud.tencent.com/document/product/457/59095)。 | 新增资源没有流量接入                                       |
| E4074  | 节点欠费可能，后端绑定失败                                   | CLB 后端绑定问题，可能节点遭到封锁。                           | 后端更新可能失败，用户滚动更新时可能导致断流               |
| E4081  | kubernetes.io/ingress.https-rules，注解格式不正确（配置冲突） | 建议通过控制台修改配置，详情可参见 [Ingress Annotation 说明](https://cloud.tencent.com/document/product/457/56112)。 | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4082  | NoSelector Service 不支持绑定，Ingress 在直连场景下，声明使用了类似资源 | NoSelector Service 后端不支持直连接入，需要改用 NodePort。   | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4084  | 跨域绑定 1.0 方案下，不能使用 SNAT Pro 功能                    | 系统限制，需要调整技术方案。                                   | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
| E4098  | 指定已有负载均衡，负载均衡 ID 格式错误                         | 登录负载均衡控制台找到与当前集群相同的 VPC 下的负载均衡实例，确认负载均衡 ID，使用一个真实有效负载均衡 ID，详情可参见 [Ingress 使用已有 CLB](https://cloud.tencent.com/document/product/457/45686)。 | 新增资源没有流量接入                                       |
| E4101  | 指定已有负载均衡监听器存在冲突                               | 检查 80/443 端口是否已经被其他资源占用。                         | 资源同步被阻塞，用户更新可能导致负载均衡后端不能正常更新。 |
