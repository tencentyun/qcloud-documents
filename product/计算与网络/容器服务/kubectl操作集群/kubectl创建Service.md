## kubectl创建Service

### 创建公网访问方式的服务
```shell
# mysvc.yaml文件见下文
$ kubectl create -f mysvc.yaml 
```
mysvc.yaml 文件内容如下：
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

### 创建VPC内网访问方式的服务
VPC内网访问方式的服务只需在metadata下的annotations中增加**service.kubernetes.io/qcloud-loadbalancer-internal-subnetid**即可，含义为创建的内网LB所在的子网唯一ID，此子网必须在集群VPC下。

``` yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx
```

### 带宽上移用户
带宽上移用户在创建公网访问方式的服务时需要指定如下两个annotations项

 - **service.kubernetes.io/qcloud-loadbalancer-internet-charge-type** :公网带宽计费方式， 可选值有：TRAFFIC_POSTPAID_BY_HOUR(按使用流量计费)，BANDWIDTH_POSTPAID_BY_HOUR(按带宽计费)
 - **service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out**: 带宽上限，范围[1,2000]Mbps

``` yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internet-charge-type: TRAFFIC_POSTPAID_BY_HOUR
    service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out: "10"
```
