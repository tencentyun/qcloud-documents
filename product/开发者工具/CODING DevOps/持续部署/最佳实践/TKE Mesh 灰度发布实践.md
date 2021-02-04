本文为您详细介绍如何使用 CODING 持续部署配合 TKE 实践灰度发布。

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击页面右上角的 <img src ="https://main.qcloudimg.com/raw/d94a8e60dd3a41d0af07d72ae0e9d70e.png" style ="margin:0">，进入项目列表页面，单击项目图标进入目标项目。
3. 选择左侧菜单【持续部署】。

灰度发布（又名金丝雀发布）可实现业务从老版本到新版本的平滑过渡，并且避免升级过程中出现的问题对用户造成的影响。在云原生的背景下，像 Kubernetes 这样的平台可实现简单的灰度发布，但其功能非常有限，只能通过控制 pod 副本比例管理流量，并且不支持根据特定规则将请求路由到灰度版本。

但使用 isito，副本部署和流量管理是两个完全独立的功能，服务的 pod 数量可以根据流量负载灵活伸缩，与版本流量路由的控制完全正交；基于 istio，可以轻松实现细粒度控制流量百分比（例如，路由 1％ 的流量到灰度版本），当然也可以使用其他规则（如：url、headers 等）来控制流量。

TKE Mesh（腾讯云服务网格） 基于 istio，在开源版本的基础上优化了 envoy 的转发性能，并实现控制面托管/多活以及多集群网格产品化。灰度发布流程涉及多个微服务部署、人工审核、灰度比例控制等步骤，基于 CODING CD（持续部署），可以实现灰度发布流程的灵活编排，在关键节点进行人工审核、动态指定灰度比例，使用表达式控制分支流程等特性。

接下来我们将结合 CODING CD 和 TKE Mesh 演示灰度发布流程。

## 灰度发布 Bookinfo 应用演示

我们以 istio 官方的 Bookinfo 示例项目作为 demo，并在它的基础上做了 yaml 配置优化，更符合 CODING + TKE Mesh 灰度发布的 Demo 演示。对于不熟悉  istio 的同学，有必要对 Bookinfo 应用做简单的介绍。

Bookinfo 应用由四个单独的微服务构成。 这个应用模仿在线书店的一个分类，显示一本书的信息。 页面上会显示一本书的描述，书籍的细节（ISBN、页数等），以及关于这本书的一些评论。

Bookinfo 应用分为四个单独的微服务：

-   `productpage`.  这个微服务会调用 `details` 和 `reviews` 两个微服务，用来生成页面。
-   `details`.  这个微服务中包含了书籍的信息。
-   `reviews`.  这个微服务中包含了书籍相关的评论。它还会调用 `ratings` 微服务。
-   `ratings`.  这个微服务中包含了由书籍评价组成的评级信息。

`reviews` 微服务有 3 个版本：

-   v1 版本不会调用 `ratings` 服务。
-   v2 版本会调用 `ratings` 服务，并使用 1 到 5 个黑色星形图标来显示评分信息。
-   v3 版本会调用 `ratings` 服务，并使用 1 到 5 个红色星形图标来显示评分信息。

下图展示了这个应用的端到端架构。

![](https://help-assets.codehub.cn/enterprise/20200727172325.png)

Bookinfo 应用中的几个微服务是由不同的语言编写的。 这些服务对 Istio 并无依赖，但是构成了一个有代表性的服务网格的例子：它由多个服务、多个语言构成，并且 `reviews` 服务具有多个版本。

*阅读更多：[Bookinfo 应用](https://istio.io/latest/zh/docs/examples/bookinfo/)*

基于 Bookinfo 应用，我们将演示如下的灰度发布效果：

1.  部署 bookinfo 应用的基准版本（v1），即四个微服务 `productpage`、`details`、`reviews`和 `ratings`都是 v1 版本
2.  腾讯云 TKE Mesh（服务网格） 控制台查看网格拓扑
3.  部署 reviews 服务的灰度版本（v2）
4.  设置灰度比例
5.  人工确认是否全量发布
6.  将所有流量切换到灰度版本（v2）

### 部署基准版本（v1）

在 CODING 持续部署（CD）提交发布单，部署基准版本（v1）。`配置制品`处分别选择应用、Ingress Gateway、Destination Rule 和 VirtualServices 对应的 yaml 文件。

![](https://help-assets.codehub.cn/enterprise/20200727172714.gif)

部署完成后，在 TKE Mesh（服务网格）控制台查看生成的网络拓扑（网格拓扑中看不到 `ratings-v1`是因为`reviews-v1`没有调用`ratings-v1`）。

![](https://help-assets.codehub.cn/enterprise/20200727172738.png)

查看 Gateway 的信息，根据外网 IP 访问 bookinfo 服务。

![](https://help-assets.codehub.cn/enterprise/20200727172755.png)

浏览器打开示例网址浏览 bookinfo 应用的 Web 页面，无论怎么刷新页面都发现 reviews 服务只有 v1 版本的效果（没有红色或黑色的星形）。

![](https://help-assets.codehub.cn/enterprise/20200727172828.png)

### 灰度发布（v2）

在 CODING CD 提交发布单，执行灰度发布流程。

`配置制品`处填写 `reviews v2` yaml 文件的路径（`platform/kube/bookinfo-reviews-v2.yaml`）和分支；`reviews` 服务增加灰度版本后，需要更新 Destination Rule（包含 v1 和 v2 的配置），填写 Destination Rule 的路径（`networking/destination-rule-v1-v2.yaml`）和分支。

`启动参数`指定基准版本和灰度版本（即 v1 和 v2）。

![](https://help-assets.codehub.cn/enterprise/20200727173028.gif)

设置灰度比例为 50% 。

![](https://help-assets.codehub.cn/enterprise/20200727173235.png)

在 TKE Mesh 控制台查看网络拓扑已更新（`productpage-v1` 的请求会被转发到 `reviews-v1`或 `reviews-v2`）。

![](https://help-assets.codehub.cn/enterprise/20200727173253.png)

执行完下一阶段，灰度比例生效后，访问 `http://49.233.239.50/productpage` 会发现 `reviews` 服务的 v1 和 v2 版本流量各占 50%（黑色星形和没有星形交替出现）。

![](https://help-assets.codehub.cn/enterprise/20200727173455.gif)

当确认灰度版本（v2）版本稳定后，选择全量发布，将所有流量切换到灰度版本（v2）。

![](https://help-assets.codehub.cn/enterprise/20200727173618.png)

在 TKE Mesh 控制台查看网络拓扑已更新（没有 reviews-v1）。

![](https://help-assets.codehub.cn/enterprise/20200727173639.png)

访问 `http://49.233.239.50/productpage` 会发现 `reviews` 服务所有流量都发送到 v2 版本。即无论怎么刷新页面都发现 reviews 服务只有 v2 版本的效果（只显示黑色星形）。

![](https://help-assets.codehub.cn/enterprise/20200727173700.png)

## 配置过程

具体是如何实现上述的灰度发布效果呢，接下来跟着本教程动手实践。

### TKE 集群

使用腾讯云 TKE 创建一个 [Kubernetes 集群](https://cloud.tencent.com/document/product/457/11741)

### TKE Mesh

在 TKE 控制台创建服务网格实例，在`服务发现`处选择上一步骤创建的 TKE 集群；并开启 `default` 命名空间的 sidecar 自动注入功能。

![](https://help-assets.codehub.cn/enterprise/20200727173817.png)

### CODING DevOps

如果你没有 CODING DevOps 账号，请在腾讯云控制台访问 [CODING DevOps](https://cloud.tencent.com/product/coding)，根据提示开通即可。

### 代码仓库

克隆源代码并推送到自己的 CODING 代码库。

```sh
git clone https://ci-cd.coding.net/public/bookinfo/bookinfo/git
git remote remove origin
git remote add origin 你的 CODING 代码库地址
git push origin master
```

### 添加云账号

在 CODING 持续部署添加 TKE 集群。

![](https://help-assets.codehub.cn/enterprise/20200727174033.png)

### 创建应用并配置部署流程

进入 CODING 持续部署控制台创建名为 `bookinfo` 的应用，然后配置部署流程。

**部署基准版本（v1）**

![](https://help-assets.codehub.cn/enterprise/20200727174050.png)

配置了 4 个启动所需制品分别是：

*   `platform/kube/bookinfo-reviews-v1.yaml`：部署 bookinfo 四个微服务的 v1 版本。
*   `networking/bookinfo-gateway.yaml`：部署具有外网 IP 的 Ingress Gateway，通过此 Gateway 访问 bookinfo 应用的 Web 页面。
*   `networking/destination-rule-all-reviews-v1.yaml`：部署四个微服务 v1 版本的 Destination Rule。
*   `networking/virtual-service-all-v1.yaml`：部署四个微服务 v1 版本的 Virtual Services。

*在第二个阶段`部署 Ingress 网关` 执行完成后，就可以通过 Gateway 的外网 IP 访问 bookinfo 应用。后续两个阶段的作用是使用 Tke Mesh 对 bookinfo 进行流量管理。*

### reviews 灰度发布

![](https://help-assets.codehub.cn/enterprise/20200727174242.png)

配置了两个启动所需制品分别是：
*   `canary-reviews-deployment`：reviews 服务灰度版本的 Deployment 内容，在此 demo 中将会使用文件 `platform/kube/bookinfo-reviews-v2.yaml`。
*   `canary-reviews-destination-rule`：包含 v1 和 v2 的 subset 配置，在此 demo 中将会使用文件 `networking/destination-rule-v1-v2.yaml`。

「设置灰度比例」是一个人工确认阶段，通过参数 `canary-ratio` 指定灰度比例。

![](https://help-assets.codehub.cn/enterprise/20200727174307.png)

「灰度比例生效」是一个 Virtual Service 模板，可根据部署流程启动参数和上一阶段的 `canary-ratio` 参数对 reviews 服务的流量进行动态管理。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: reviews
spec:
  hosts:
    -   reviews
  http:
    -   route:
        -   destination:
            host: reviews
            subset: '${parameters.base_version}'
          weight: >-
            ${100 -
            #toInt(#stage("设置灰度比例")["context"]["customParams"]["canary_ratio"])}
        -   destination:
            host: reviews
            subset: '${parameters.canary_version}'
          weight: >-
            ${#toInt(#stage("设置灰度比例")["context"]["customParams"]["canary_ratio"])}

```

最后两个阶段可以根据「是否全量发布」阶段的确认选项（通过「#judgment('是否全量发布')」表达式获取上一阶段的确认选项），判断全量发布灰度版本或直接结束部署流程。

![](https://help-assets.codehub.cn/enterprise/20200727174344.png)

*以上两个部署流程的 json 配置存放在 bookinfo 代码仓库的 `coding-cd-template` 目录中，可直接导入 CODING CD 快速创建部署流程。*

### 将应用关联到项目（在项目内提交发布单）

部署流程配置完成后，将应用关联到项目，即可在项目内提交发布单，实现「reviews」服务的灰度发布。

![](https://help-assets.codehub.cn/enterprise/20200727174613.png)

## 小结

本文主要聚焦基于 CODING CD + TKE Mesh 的灰度发布实践，没有涉及更多 CODING DevOps 的能力。除了以上的灰度发布 Demo，你可以基于 CODING 平台实现一站式 DevOps 研发实践。具体来说，上述的灰度发布 Demo 可以结合 CODING 持续集成、制品库；实现代码提交后，自动构建 bookinfo 各微服务的 Docker 镜像上传到制品库，推送完成后自动触发灰度发布的流水线执行。

此外，结合 CODING CD + TKE Mesh，还可以拓展更多的微服务治理和发布能力，比如：

*   通过全链路跟踪系统进行服务性能分析。
*   通过丰富的路由规则、重试、故障转移和故障注入对流量行为进行细粒度控制。
*   基于 TKE Mesh（istio） 的熔断和限流能力，通过 CODING CD 联动监控系统（如腾讯云监控），实现业务系统压力较大时自动触发熔断和限流的部署流程，保证业务稳定。

## 公开资源和参考资料

*   [腾讯云 TKE 和 TKE Mesh](https://cloud.tencent.com/product/tke)
*   [CODING 持续部署](https://coding.net/products/cd)
*   [Bookinfo Demo 的 CODING 代码库地址](https://ci-cd.coding.net/public/bookinfo/bookinfo/git)
*   [istio 官方文档](https://istio.io/latest)