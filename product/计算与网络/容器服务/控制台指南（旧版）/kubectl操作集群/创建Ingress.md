## 创建公网 Ingress
使用以下命令创建 myingress.yaml 文件：
```shell
$ kubectl create -f myingress.yaml 
```
> myingress.yaml 文件内容如下：
``` yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: qcloud
  name: my-ingress
  namespace: default
spec:
  rules:
  - host: localhost
    http:
      paths:
      - backend:
          serviceName: non-service
          servicePort: 65535
        path: /
```

## 创建内网 Ingress
内网 Ingress 只需在 metadata 下的 annotations 中增加 **kubernetes.io/ingress.subnetId** 即可，即创建的内网 LB 所在子网的唯一 ID，此子网必须在集群 VPC下。
``` yaml
metadata:
  annotations:
    kubernetes.io/ingress.subnetId: subnet-xxxxxxxx
```

## 带宽上移用户
带宽上移用户在创建公网 Ingress 时需要指定如下两个 annotations 项：
- **kubernetes.io/ingress.internetChargeType**
公网带宽计费方式， 可选值有：TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费），BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）。
- **kubernetes.io/ingress.internetMaxBandwidthOut**
带宽上限，范围：[1,2000] Mbps。

创建命令如下：
``` yaml
metadata:
  annotations:
    kubernetes.io/ingress.internetChargeType: TRAFFIC_POSTPAID_BY_HOUR
    kubernetes.io/ingress.internetMaxBandwidthOut: "10"
```