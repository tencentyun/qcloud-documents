## kubectl 命令行介绍
kubectl 是一个用于对 Kubernetes 集群操作命令行工具。 本文涵盖 kubectl 语法，常见命令操作，并提供常见示例。 有关每个命令（包括所有主命令和子命令）的详细信息，请参阅 [kubectl 参考文档](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/) 或使用 kubectl help 命令查看详细帮助，有关安装说明，请参阅 [安装 kubectl](https://cloud.tencent.com/document/product/457/8438)。

## 通过 kubectl 创建 Nginx
以下示例帮助您熟悉运行常用 kubectl 操作：
### kubectl create
由于 Nginx 名称容易冲突，从文件或标准输入创建资源。
```shell
$ kubectl create -f nginx.yaml # nginx-test.yaml文件见下
```
nginx-test.yaml 文件如下：
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-test
  labels:
    qcloud-app: nginx-test
spec:
  replicas: 1
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      qcloud-app: nginx-test
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        qcloud-app: nginx-test
    spec:
      containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: nginx-test
        resources:
          limits:
            cpu: 200m
            memory: 128Mi
          requests:
            cpu: 200m
            memory: 128Mi
        securityContext:
          privileged: false
      serviceAccountName: ""
      volumes: null
      imagePullSecrets:
      - name: qcloudregistrykey
status: {}
---
apiVersion: v1
kind: Service
metadata:
  name: nginx-test
  labels:
    qcloud-app: nginx-test
spec:
  ports:
  - name: tcp-80-80-ogxxh
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    qcloud-app: nginx-test
  type: LoadBalancer
status:
  loadBalancer: {}
```
![Alt text][create]
通过以下命令获取外网访问地址：
```
kubectl get services
```
![Alt text][get]
在浏览器上输入该 IP， 便可直接访问 nginx 服务。
![Alt text][show]

### kubectl logs
在容器中打印容器的日志。
```shell
// Return a snapshot of the logs from pod <pod-name>.
$ kubectl logs <pod-name>
```
![Alt text][logs]


[create]:https://mc.qcloudimg.com/static/img/a33b8f47e796374d5c457542c1569a9c/image.png
[get]:https://main.qcloudimg.com/raw/364d4b12fa90db3f6cbf663eb5406a8f.png

[show]:https://mc.qcloudimg.com/static/img/e09ab193d3f1732cc435ba53235094c1/image.png
[logs]:https://main.qcloudimg.com/raw/f9db9c5e098b2cf5359688bead0c7f7b.png