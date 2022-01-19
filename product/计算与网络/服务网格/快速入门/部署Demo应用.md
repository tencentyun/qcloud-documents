### Demo应用概览
Demo应用是一个电商网站，基于Istio社区的官方样例[bookinfo](https://raw.githubusercontent.com/istio/istio/release-1.12/samples/bookinfo/platform/kube/bookinfo.yaml)改造，由6个服务组成：

- **frontend**：网站前端，调用user、product、cart、order服务
- **product**：商品服务，提供商品信息。 product包含两个版本，版本一没有顶部广告banner；版本二有顶部广告banner
- **user**：用户登陆服务，提供登陆功能
- **cart**：购物车服务，提供添加、查看购物车功能，调用库存服务提供库存告警功能，需要登陆才可以下单
- **order**：订单结算服务，登陆后点击checkout后可发起结算，结算时需要调用stock库存服务查询库存情况，库存不足会下单失败。order包含两个版本，版本一无积分抵扣运费的功能，版本二有积分抵扣运费的功能
- **stock**：库存服务，为order购物车服务的库存告警功能和order订单结算服务的库存查询提供库存信息

![](https://qcloudimg.tencent-cloud.cn/raw/8752528907bffbb30f7a9823b39bdcd8.svg)
<center>Demo应用架构</center>


![](https://qcloudimg.tencent-cloud.cn/raw/0e2a71adac0f270e5a92662b676e8c0a.png)
<center>Demo应用首页</center>

### 安装Demo应用
您可以在[TCM Demo仓库](https://github.com/Tencent-Cloud-Mesh/mesh-demo)中获取Demo应用，由于TCM的sidecar自动注入需要标记Istio版本，您需要选择与您Istio版本一致的分支，或直接修改 master分支，路径mesh-demo/yamls/step01-apps-zone-a.yaml 中 base namespace中的版本label：
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
例如，您的istio版本为1.8.1，则需要将：istio.io/rev: 1-10-3 修改为 istio.io/rev: 1-8-1，否则sidecar注入将会失败。

使用如下命令可快速部署Demo应用，
```
kubectl apply -f yamls/step01-apps-zone-a.yaml
```
您也可以直接在TKE控制台，使用【YAML】创建资源，贴入上述yaml内容，一键创建Demo应用相关资源。