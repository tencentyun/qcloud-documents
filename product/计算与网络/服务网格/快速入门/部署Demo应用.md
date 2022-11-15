### Demo 应用概览
Demo 应用是一个电商网站，基于 Istio 社区的官方样例 [bookinfo](https://raw.githubusercontent.com/istio/istio/release-1.12/samples/bookinfo/platform/kube/bookinfo.yaml) 改造，由 6 个服务组成：

- **frontend**：网站前端，调用 user、product、cart、order 服务。
- **product**：商品服务，提供商品信息。product 包含两个版本，版本一没有顶部广告 banner；版本二有顶部广告 banner。
- **user**：用户登录服务，提供登录功能。
- **cart**：购物车服务，提供添加、查看购物车功能，调用库存服务提供库存告警功能，需要登录才可以下单。
- **order**：订单结算服务，登录后点击 checkout 后可发起结算，结算时需要调用 stock 库存服务查询库存情况，库存不足会下单失败。order 包含两个版本，版本一无积分抵扣运费的功能，版本二有积分抵扣运费的功能。
- **stock**：库存服务，为 order 购物车服务的库存告警功能和 order 订单结算服务的库存查询提供库存信息。

#### Demo 应用架构
![](https://qcloudimg.tencent-cloud.cn/raw/8752528907bffbb30f7a9823b39bdcd8.svg)
 
#### Demo 应用首页
![](https://qcloudimg.tencent-cloud.cn/raw/0e2a71adac0f270e5a92662b676e8c0a.png)
 

### 安装 Demo 应用
您可以在 [TCM Demo 仓库](https://github.com/Tencent-Cloud-Mesh/mesh-demo) 中获取 Demo 应用，由于 TCM 的 sidecar 自动注入需要标记 Istio 版本，您需要选择与您 Istio 版本一致的分支，或直接修改 master 分支，路径 mesh-demo/yamls/step01-apps-zone-a.yaml 中 base namespace 中的版本 label：
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: base
  labels:
    istio.io/rev: 1-10-3
spec:
  finalizers:
    - kubernetes
```
例如，您的 istio 版本为 1.8.1，则需要将 `istio.io/rev: 1-10-3` 修改为 `istio.io/rev: 1-8-1`，否则 sidecar 注入将会失败。

使用如下命令可快速部署 Demo 应用：
```
kubectl apply -f yamls/step01-apps-zone-a.yaml
```


您也可以前往 [容器服务控制台](https://console.cloud.tencent.com/tke2/cluster)，在**集群详情页 > 工作负载 > Deployment** 中，使用 **YAML 创建资源**，复制上述 yaml 内容，一键创建 Demo 应用相关资源。