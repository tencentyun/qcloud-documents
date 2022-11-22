## 操作场景

本文通过一个 demo 进行 Golang 应用接入微服务引擎托管的 PolarisMesh 治理中心的全流程操作演示，帮助您快速了解如何在 Kubernetest 中使用 DNS 协议来体验使用北极星网格的就近路由能力。

## 前提条件

- 已创建 PolarisMesh 北极星网格，请参见 [创建 PolarisMesh 治理中心](https://cloud.tencent.com/document/product/1364/65866)。
- 已准备好业务部署的容器资源。
  - 创建 TKE 容器集群，请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/32189)。
- 下载 Github 的 [demo 源码](https://github.com/polarismesh/polaris-go/tree/main/examples/route/nearby/k8s) 到本地。

## 操作步骤

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**北极星网格**下的 **polarismesh** 页面，单击页面左上方下拉列表，选择目标地域。
3. 单击目标引擎的“ID”，进入基本信息页面。
4. 查看访问地址，Golang 应用访问使用 gRPC 端口（8091）：
![](https://qcloudimg.tencent-cloud.cn/raw/e7dc5ac5f7c76a316ae68b667d8a365f.png)
5. 将北极星网格和 Kubernetes 集群进行关联，请参见 [关联 K8s 集群](https://cloud.tencent.com/document/product/1364/65869)。
6. 开启 polaris-sidecar 的注入能力。
<dx-codeblock>
:::  shell
# 对于 default 命名空间开启注入能力
kubectl label namespace default polaris-injection=enabled
# 对于注入的 polaris-sidecar 运行模式设置为 dns 模式
kubectl label namespace default polaris-sidecar-mode=dns
:::
</dx-codeblock>
7. 修改 demo 中的注册中心地址：
 1. 在下载到本地的 [demo 源码](https://github.com/polarismesh/polaris-go/tree/main/examples/route/nearby/k8s) 目录下，找到`configmap-provider.yaml`文件。
 - 添加微服务引擎北极星网格地址到项目配置文件中（这里已`configmap-provider.yaml`为例）。
 - 修改位置信息获取插件名称到项目配置文件中（这里已`configmap-provider.yaml`为例）。
<dx-codeblock>
:::  yaml
apiVersion: v1
data:
  polaris.yaml: |-
    global:
      serverConnector:
        addresses:
          - 10.0.4.6:8091
      location:
        # 设置 polaris-go 进程地理信息的提供插件
        provider: qcloud
    consumer:
      serviceRouter:
        plugin:
          nearbyBasedRouter:
            #描述:就近路由的最小匹配级别
            #范围:region(大区)、zone(区域)、campus(园区)
            matchLevel: campus
kind: ConfigMap
metadata:
  name: polaris-consumer-config
  namespace: default
:::
</dx-codeblock>
8. 将 demo 部署至 TKE 集群中。
<dx-codeblock>
:::  shell
kubectl apply -f ./
:::
</dx-codeblock>
9. 确认部署结果：
 1. 进入前面提到的微北极星网格实例页面。
 - 选择**服务管理** > **服务列表**，查看微服务 RouteNearbyEchoServer 的实例数量。
    - 若实例数量值不为0，则表示已经成功接入微服务引擎。
    - 若实例数量为0，或者找不到 RouteNearbyEchoServer 服务名，则表示微服务应用接入微服务引擎失败。
![](https://qcloudimg.tencent-cloud.cn/raw/7f46cd9aabfbfba93ac3e8bc7bbfbe4b.png)
 - 开启 RouteNearbyEchoServer 的就近路由。
![](https://qcloudimg.tencent-cloud.cn/raw/91ff51daff64a22a9d47261c096ccbe8.png)
10. 为 RouteNearbyEchoServer 创建服务别名 routenearby.echoserver。
![](https://qcloudimg.tencent-cloud.cn/raw/3d542768f5d3e89396c6ac679604dc5f.png)
11. 调用 provider 的 HTTP 接口，执行 http 调用，其中`${app.port}`替换为 provider 的监听端口（默认为28080），`${add.address}`则替换为 provider 的域名信息。
<dx-codeblock>
:::  shell
   curl -L -X GET 'http://routenearby.echoserver.default.svc.polaris:28080/echo'
   预期返回值：Hello, I'm RouteNearbyEchoServer Provider, MyLocInfo's : xxx, host : xxx:xxx
:::
</dx-codeblock>  

