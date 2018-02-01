## kubectl 命令行介绍
kubectl 是一个用于对 Kubernetes 集群操作命令行工具。 本文涵盖 kubectl 语法，常见命令操作，并提供常见示例。 有关每个命令（包括所有主命令和子命令）的详细信息，请参阅 [kubectl 参考文档](https://kubernetes.io/docs/reference/generated/kubectl/kubectl/) 或使用 kubectl help 命令查看详细帮助，有关安装说明，请参阅 [安装 kubectl](https://cloud.tencent.com/document/product/457/8438)。

## 语法
使用以下语法，通过 kubectl 从终端窗口运行命令：
```shell
kubectl [command] [TYPE] [NAME] [flags]
```

其中`command`，`TYPE`，`NAME`，和`flags`分别是：

- `command`：指定要在一个或多个资源进行操作，例如`create`，`get`，`describe`，`delete`。
- `TYPE`：指定资源类型。资源类型是区分大小写的，您可以指定单数，复数或缩写形式。例如，以下命令产生相同的输出：

```shell
$ kubectl get pod pod1
$ kubectl get pods pod1
$ kubectl get po pod1
```

- `NAME`:指定资源的名称。名称区分大小写。如果省略名称，则显示所有资源的详细信息
在多个资源上执行操作时，可以按类型和名称指定每个资源，或者指定一个或多个文件：
可按类型和名称指定资源：
例：`$ kubectl get pod example-pod1 example-pod2`
可分别指定多个资源类型：。
例：`$ kubectl get pod/example-pod1 replicationcontroller/example-rc1`
可用一个或多个文件指定资源：
例：`$ kubectl get pod -f ./pod.yaml`

- `flags`：指定可选标志。例如，您可以使用`-s`或`--server`标志来指定 Kubernetes API 服务器的地址和端口。

## nginx示例：常用操作
使用以下一组示例来帮助您熟悉运行常用 kubectl 操作：
### kubectl create
从文件或标准输入创建资源。

```shell
$ kubectl create -f nginx.yaml
```
yaml文件如下：

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx
  labels:
    qcloud-app: nginx
spec:
  replicas: 1
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      qcloud-app: nginx
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        qcloud-app: nginx
    spec:
      containers:
      - image: nginx:latest
        imagePullPolicy: Always
        name: nginx
        resources:
          requests:
            cpu: 200m
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
  name: nginx
  labels:
    qcloud-app: nginx
spec:
  ports:
  - name: tcp-80-80-ogxxh
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    qcloud-app: nginx
  type: LoadBalancer
status:
  loadBalancer: {}
```

![Alt text][create]

### kubectl get 
列出一个或多个资源。
```shell
// List all pod
$ kubectl get pods

// List the Deployment 
$ kubectl get deployment nginx

// List all deployment and services together 
$ kubectl get dp,services
```

通过kubectl get services 获取外网访问地址, 在浏览器上输入该IP， 便可直接访问nginx服务。
![Alt text][get]
![Alt text][show]
### kubectl describe
显示一个或多个资源的详细状态，默认情况下包括未初始化的资源。
```shell
// Display the details of the node with name <node-name>.
$ kubectl describe nodes <node-name>

// Display the details of the pod with name <pod-name>.
$ kubectl describe pods/<pod-name>
```

### kubectl logs
在容器中打印容器的日志。
```shell
// Return a snapshot of the logs from pod <pod-name>.
$ kubectl logs <pod-name>
```

### kubectl delete
从文件，stdin或指定标签选择器，名称，资源选择器或资源中删除资源。
```shell
// Delete a pod using the type and name specified in the pod.yaml file.
$ kubectl delete -f nginx.yaml

```


[create]:https://mc.qcloudimg.com/static/img/2624efeb9c11b4dc51ae166d4eed034a/image.png
[get]:https://mc.qcloudimg.com/static/img/fb095179d54e49e0287ba3020f7835cf/image.png

[show]:https://mc.qcloudimg.com/static/img/e09ab193d3f1732cc435ba53235094c1/image.png