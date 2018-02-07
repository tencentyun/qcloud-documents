## kubectl 命令行介绍
kubectl 是一个用于对 Kubernetes 集群操作命令行工具。 本文涵盖 kubectl 语法，常见命令操作，并提供常见示例。 有关每个命令（包括所有主命令和子命令）的详细信息，请参阅 [kubectl 参考文档](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/) 或使用 kubectl help 命令查看详细帮助，有关安装说明，请参阅 [安装 kubectl](https://cloud.tencent.com/document/product/457/8438)。

## 通过kubectl创建nginx
使用以下一组示例来帮助您熟悉运行常用 kubectl 操作：
### kubectl create
从文件或标准输入创建资源。
> 由于nginx名称容易冲突， 

```shell
$ kubectl create -f nginx.yaml # nginx-test.yaml文件见下
```
nginx-test.yaml文件如下：

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



通过kubectl get services 获取外网访问地址, 在浏览器上输入该IP， 便可直接访问nginx服务。
![Alt text][get]
![Alt text][show]

### kubectl logs
在容器中打印容器的日志。
```shell
// Return a snapshot of the logs from pod <pod-name>.
$ kubectl logs <pod-name>
```
![Alt text][logs]



[create]:https://mc.qcloudimg.com/static/img/a33b8f47e796374d5c457542c1569a9c/image.png
[get]:https://mc.qcloudimg.com/static/img/fb095179d54e49e0287ba3020f7835cf/image.png

[show]:https://mc.qcloudimg.com/static/img/e09ab193d3f1732cc435ba53235094c1/image.png
[logs]:https://mc.qcloudimg.com/static/img/2c34aca3e996296742e6fa9a9be77432/image.png