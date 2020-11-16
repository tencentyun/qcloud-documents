## 操作场景

原生 LoadBalancer 模式 Servcie 可自动创建负载均衡（CLB），并通过集群的 Nodeport 转发至集群内， 再通过 iptable 或 ipvs 进行二次转发。该模式下的 Service 能满足大部分使用场景，但在以下场景中更推荐使用**直连 Pod 模式 Service**：

- 有获取来源 IP 需求时（非直连模式必须另外开启 Local 转发）。
- 要求具备更高转发性能时（非直连模式下 CLB 和 Service 本身存在两层 CLB， 性能有一定损失）。
- 需使用完整的健康检查和会话保持到 Pod 层级时（非直连模式下 CLB 和 Service 本身存在两层 CLB，健康检查及会话保持功能较难配置）。

## 使用限制

- 集群 Kubernetes 版本需要高于 1.12。
- 集群网络模式必须开启 VPC-CNI 弹性网卡模式。
- 直连模式 Service 使用的工作负载需使用 VPC-CNI 弹性网卡模式。
- 满足 CLB 本身绑定弹性网卡的功能限制，详情请参见 [绑定弹性网卡](https://cloud.tencent.com/document/product/214/36538)。
- 开启直连 Pod 模式的工作负载更新时，将会根据 CLB 的健康检查状态进行滚动更新，会对更新速度造成一定影响。

## 操作步骤

### 控制台操作指引

1.  登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2.  参考 [控制台创建 Service](https://cloud.tencent.com/document/product/457/45489#.E5.88.9B.E5.BB.BA-service) 步骤，进入 “新建Service” 页面，根据实际需求设置 Service 参数。
其中，部分关键参数信息需进行如下设置，如下图所示：
![](https://main.qcloudimg.com/raw/1e52f535cd9eb5712ddf6c4760952e70.png)
	- **服务访问方式**：选择为【提供公网访问】或【VPC内网访问】。
	- **网络模式**：勾选【采用负载均衡直连Pod模式】。
	- **Workload绑定**：选择【引用Workload】，并在弹出窗口中选择 VPC-CNI 模式的后端工作负载。
3. 单击【创建服务】，完成创建。

### YAML 操作指引

#### YAML 示例
直连 Pod 模式 Service 的 YAML 配置与普通 Service YAML 配置相同，示例中的 annotation 即代表是否开启直连 Pod 模式。
```
kind: Service
apiVersion: v1
metadata:
  annotations:
	service.cloud.tencent.com/direct-access: true ##开启直连 Pod 模式
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
  type: LoadBalancer
```



####  annotation 扩展
负载均衡 CLB 的相关配置，建议您参考 [TKEServiceConfig 介绍](https://cloud.tencent.com/document/product/457/41895) 进行设置。其中相关 annotation 配置如下：
```
service.cloud.tencent.com/tke-service-config: [tke-service-configName]
```
