## 背景

TKE 支持安装 Nginx Ingress 扩展组件，使用 Nginx Ingress 来接入 Ingress 流量，更多请参考 [Nginx-ingress 说明](https://cloud.tencent.com/document/product/457/51260)，本文将给出这个组件的一些最佳实践指引。

## 为集群暴露多个 Nginx Ingress 流量入口

Nginx Ingress 的扩展组件安装好后，在 `kube-system` 下会有个 nginx ingress 的 operator 组件，它可以为我们创建多个 nginx ingress 实例，每个 nginx ingress 实例都使用不同的 ingressClass，且使用不同的 CLB 作为流量入口，从而可以实现不同 Ingress 绑定到不同流量入口。

我们可以根据需求，为集群创建多个 nginx ingress 实例，在【组件管理】里找到安装好的 nginx ingress 扩展组件，点进去:

![](https://main.qcloudimg.com/raw/7605a808c6116286593bae4323a04dbf.png)

然后点击 【新增Nginx Ingress实例】:

![](https://main.qcloudimg.com/raw/58750dcc07cf87284573355ed905e0b4.png)

根据需求配置 Nginx Ingress 实例即可，每个实例指定不同的 ingressClass 名称:

![](https://main.qcloudimg.com/raw/f4c859abc629f7a62aa659194da9fb3a.png)

后续在控制台创建 Ingress 时可指定具体的 ingressClass 来将 Ingress 绑定到具体的 Nginx Ingress 实例上:

![](https://main.qcloudimg.com/raw/9c00f36caddb98064359fccdcd61e5d4.png)

若使用 yaml 创建 Ingress，则需指定下 ingressClass 的 annotation (`kubernetes.io/ingress.class`):

![](https://main.qcloudimg.com/raw/e4ee61dd452ccc512ba8fc5b85ab5714.png)

## 性能优化

### LB 直通 Pod

如果是 Global Router 网络模式的集群，默认是没有开启 LB 直通 Pod 的，可以为集群启用 VPC-CNI，并且在创建 Nginx Ingress 实例时，勾选 `使用CLB直连Pod模式`:

![](https://main.qcloudimg.com/raw/b920ef483e80e83d2080910471f7de4c.png)

这样可以让流量绕过 NodePort，直达 Pod，以此来提升性能。

### 提升 LB 带宽上限

LB 作为流量入口，若需要较高的并发或吞吐，在创建 Nginx Ingress 示例时，可根据实际需求规划一下带宽上限，指定给 Nginx Ingress:

![](https://main.qcloudimg.com/raw/0a59544d930800c1bebf734da4d1ba6b.png)

若账号为非带宽上移类型(参考 [区分账户类型](https://cloud.tencent.com/document/product/684/39903))，带宽上限就取决于节点的带宽，可根据情况调整节点的带宽上限:

1. 若启用了 LB 直通 Pod，LB 总带宽为 Nginx Ingress 实例 Pod 所在节点的带宽之和，建议专门规划一些高外网带宽节点部署 Nginx Ingress 实例(指定节点池DaemonSet部署)。
2. 若没有使用 LB 直通 Pod，LB 总带宽为所有节点的外网带宽之和。

### 优化 Nginx Ingress 参数

Nginx Ingress 实例已经默认做了内核参数与 nginx ingress 自身的配置优化，参考 [Nginx Ingress 高并发实践](https://cloud.tencent.com/document/product/457/48142)。如果还需自定义，可自行修改。

**修改内核参数:**

直接编辑部署好的 nginx-ingress-conntroller 的 daemonset 或 deployment (取决于实例部署选项)，修改 initContainers (使用 kubectl 修改，控制台禁止修改 kube-system 下的资源):

![](https://main.qcloudimg.com/raw/821faeb4970ddebe190577d1ca213b84.png)

**修改 nginx ingress 自身配置:**

在【Nginx配置】中选中对应的实例，再点【编辑YAML】即可修改 Nginx Ingress 实例的 ConfigMap 配置:

![](https://main.qcloudimg.com/raw/1ab145284ec2ca208cdd2f665d092edf.png)

具体配置项参考 [官方文档](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/configmap/)。

## 提升 Nginx Ingress 可观测性

### 开启监控与日志

创建好 Nginx Ingress 实例后，在【日志/监控】里可以为实例开启日志与监控，方便查看实例各项状态指标与问题排查:

![](https://main.qcloudimg.com/raw/c4aeaeeb1cc54906846960baed374c3c.png)

监控依赖 [云原生监控](https://cloud.tencent.com/document/product/457/49889)，日志依赖 [日志服务](https://cloud.tencent.com/document/product/614)，强烈建议都开启。

### 查看监控大盘

开启监控后，点击实例的【前往Prometheus查看监控】跳转到云原生监控:

![](https://main.qcloudimg.com/raw/80d6e42319b6ff0c7a9cac49fe92e31f.png)

再进入 Grafana 面板，切换到 `NGINX Ingress controller` 的大盘，即可查看监控视图:

![](https://main.qcloudimg.com/raw/82ae23289f21bdd5d0bc9cdf3a8b8ed7.png)

### 日志检索与日志仪表盘

开启日志后，点击实例的【前往CLS查看访问日志】跳转到日志服务，到【检索分析】里选中实例对应的日志集与主题，即可查看 Nginx Ingress 的访问与错误日志；点击【查看访问日志仪表盘】可以直接跳转到根据 Nginx Ingress 日志数据来展示统计信息的仪表盘。

![](https://main.qcloudimg.com/raw/72bea519f45db00aee35620651d7f1fc.png)