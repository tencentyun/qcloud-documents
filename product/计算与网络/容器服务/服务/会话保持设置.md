## 会话保持设置
### 集群内访问（ClusterIp）通过Service访问的会话保持
您可以通过指定Service的sessionAffinity属性设置Sevice的会话保持。
设置sessionAffinity仅保证Service到Pod的会话保持。
通过更改Service Yaml设置sessionAffinity：
```yaml
apiVersion: v1
kind: Service
metadata:
  annotations:
  labels:
    qcloud-app: nginx-service
  name: nginx-service
  namespace: default
spec:
  ports:
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    qcloud-app: nginx-service
  sessionAffinity: ClientIP   ### 设置基于客户端IP的会话保持
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800  ### 设置会话保持时间
  type: ClusterIP
status:
  loadBalancer: {}

```


### 集群通过负载均衡到Pod的会话保持
如需要通过设置负载均衡到Pod的会话保持，当前仅支持使用nginx-ingress。 
敬请期待腾讯云容器服务新网络方案实现外部负载均衡直通Pod(可实现基于Loadbalances模式的Service的会话保持)。

#### 通过nginx-ingress 实现会话保持
##### 使用nginx Ingress controller 替换腾讯云默认l7-lb-controller
__注：使用nginx Ingress controller替换默认的ingress contorller后，将无法使用腾讯云7层负载均衡器作为ingress载体，您需根据业务自行选择nginx Ingress controller和l7-lb-controller， 请谨慎操作。__

1.删除腾讯云容器服务l7-lb-controller
```shell
kubectl delete deployment l7-lb-controller -n kube-system
```

2.安装nginx Ingress controller 
```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml
```
![][1]
安装nginx Ingress controller即可正常使用nginx ingress.

点击查看[nignx ingress使用示例](https://kubernetes.github.io/ingress-nginx/examples/)

##### 示例验证nginx ingress会话保持
nginx ingress 支持设置以下字段
|名称|描述|值|
|nginx.ingress.kubernetes.io/affinity|设置关联类型|字符串|
|nginx.ingress.kubernetes.io/session-cookie-name|将使用的cookie的名称|字符串|
|nginx.ingress.kubernetes.io/session-cookie-hash|将在cookie值中使用的哈希类|sha1/md5/index|

1.提前创建ingress后端测试Sevice， 名称为http-svc
2.创建ingress.yaml
```shell
kubectl create -f ingress.yaml
```

示例：
```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: nginx-test
  annotations:
    nginx.ingress.kubernetes.io/affinity: "cookie"
    nginx.ingress.kubernetes.io/session-cookie-name: "route"
    nginx.ingress.kubernetes.io/session-cookie-hash: "sha1"

spec:
  rules:
  - host: stickyingress.example.com
    http:
      paths:
      - backend:
          serviceName: http-svc
          servicePort: 80
        path: /
```
3.创建ingress Nodeport访问入口
```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/baremetal/service-nodeport.yaml
```
4.测试客户端配置Host
集群内客户端：配置stickyingress.example.com host为第三步创建ingress-nginx的clusterIp
外部客户端：配置stickyingress.example.com host为第三步创建ingress-nginx的NodeIp
5.访问测试：

```shell
[root@VM_88_88_centos ~]# curl -I http://stickyingress.example.com
HTTP/1.1 200 OK
Server: nginx/1.13.12
Date: Sat, 11 Aug 2018 08:28:34 GMT
Content-Type: text/html
Content-Length: 612
Connection: keep-alive
Vary: Accept-Encoding
Set-Cookie: route=7695dac7197ddd90f512de075fef2ccb3fb4e5d3; Path=/; HttpOnly
Last-Modified: Tue, 24 Jul 2018 13:02:29 GMT
ETag: "5b572365-264"
Accept-Ranges: bytes

```

在上面的示例中，您可以看到包含“Set-Cookie：INGRESSCOOKIE”的行设置正确定义的粘性cookie。此cookie由NGINX创建，其中包含该请求中使用的上游的哈希值。如果用户更改此cookie，NGINX会创建一个新cookie并将用户重定向到另一个上游。

更多nginx ingress设置参考[nginx ingress官网](https://kubernetes.github.io/ingress-nginx/)

[1]:https://main.qcloudimg.com/raw/c77f47b9180990a3e1140a2dd07f4ce7.png



