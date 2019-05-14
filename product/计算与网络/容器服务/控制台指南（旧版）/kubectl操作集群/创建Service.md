## 创建公网服务
使用以下命令创建 mysvc.yaml 文件：
```shell
$ kubectl create -f mysvc.yaml 
```
> mysvc.yaml 文件内容如下：
``` yaml
kind: Service
apiVersion: v1
metadata:
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

## 创建内网服务
创建通过 VPC 内网访问的服务，只需在 metadata 下的 annotations 中增加 **service.kubernetes.io/qcloud-loadbalancer-internal-subnetid** 即可，即创建的内网 LB 所在子网的唯一 ID，此子网必须在集群 VPC 下。
命令如下：
``` yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx
```

## 指定 Loadbalance 只绑定指定节点
当您的集群规模较大时， 入口类型的应用设置亲和性调度到部分节点，你可以配置 Servce 的 Loadbalance 只绑定指定节点，annotations 如下：
```yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-backends-label: key in (value1, value2)  ## LabelSelector 格式
```

1. 建议配合工作负载的亲和性调度使用。
2. 前提条件是 Node 已根据业务需求设置 Label。
3. 采用原生LabelSelector格式如：
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1=values1, key2=values2
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1 in (value1),key2 in (value2)
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key in (value1, value2)
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1, key2 notin (value2)
4. 增量的节点若匹配，将自动绑定到该 Loadbalance。

## 带宽上移用户
带宽上移用户在创建公网访问方式的服务时需要指定如下两个 annotations 项：
- **service.kubernetes.io/qcloud-loadbalancer-internet-charge-type**
公网带宽计费方式， 可选值有：TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费），BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）。
- **service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out**
带宽上限，范围：[1,2000] Mbps。

创建命令：
``` yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internet-charge-type: TRAFFIC_POSTPAID_BY_HOUR
    service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out: "10"
```
