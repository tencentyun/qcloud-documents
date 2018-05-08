## kubectl创建Ingress

### 创建公网Ingress
```shell
# myingress.yaml文件见下文
$ kubectl create -f myingress.yaml 
```
myingress.yaml 文件内容如下：
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

### 创建内网Ingress
内网Ingress只需在metadata下的annotations中增加**kubernetes.io/ingress.subnetId**即可，含义为创建的内网LB所在的子网唯一ID，此子网必须在集群VPC下。

``` yaml
metadata:
  annotations:
    kubernetes.io/ingress.subnetId: subnet-xxxxxxxx
```

### 带宽上移用户
带宽上移用户在创建公网Ingress时需要指定如下两个annotations项

 - **kubernetes.io/ingress.internetChargeType** :公网带宽计费方式， 可选值有：TRAFFIC_POSTPAID_BY_HOUR(按使用流量计费)，BANDWIDTH_POSTPAID_BY_HOUR(按带宽计费)
 - **kubernetes.io/ingress.internetMaxBandwidthOut**: 带宽上限，范围[1,2000]Mbps

``` yaml
metadata:
  annotations:
    kubernetes.io/ingress.internetChargeType: TRAFFIC_POSTPAID_BY_HOUR
    kubernetes.io/ingress.internetMaxBandwidthOut: "10"
```
