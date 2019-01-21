为了更好的使用Kubernetes编排引擎，并使得Kubernetes编排引擎和腾讯云Iaas层的基础服务更好的结合。腾讯云容器服务在Kubernetes原生的编排语法的基础上，对编排的语法进行了扩展。下面将对扩展的语法进行介绍。

## 扩展语法---cbs盘使用

容器服务支持直接在服务实例上挂载CBS盘。具体的做法如下面的示例所示：

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    qcloud-app: cbs
  name: cbs
  namespace: default
spec:
  replicas: 1
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      qcloud-app: cbs
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        qcloud-app: cbs
    spec:
      containers:
      - args:
        - "360000"
        command:
        - sleep
        image: busybox:latest
        imagePullPolicy: Always
        name: busybox
        resources:
          requests:
            cpu: 200m
        securityContext:
          privileged: true
        volumeMounts:
        - mountPath: /mnt
          name: vol
      serviceAccountName: ""
      volumes:
      - name: vol
        qcloudCbs:
          cbsDiskId: 'disk_xxxxxxxx'
          fsType: ext4
```

在volume盘指定时，指定类型为qcloudCbs，并设置对应的cbsDiskId为需要挂载盘的instanceId。(Cbs盘的instanceId可以在[云硬盘页面][1]查看)。挂载点位置设定与其他类型的磁盘设置一样，如上例所示，将cbs盘挂载到容器的/mnt目录。

备注：由于一块cbs盘只能同时被挂载一次，所以如果在服务中使用了cbs盘则容器实例不能大于1，且不支持滚动更新。

## 扩展语法---VPC内负载均衡访问

在基础语法中，通过设置`Service` 中的`type`字段，能够设置服务的访问方式。在容器服务中定义`annotations`中`service.kubernetes.io/qcloud-loadbalancer-internal-subnetid`来区分是VPC内网访问负载均衡还是外网访问服务均衡。

如果设置了`service.kubernetes.io/qcloud-loadbalancer-internal-subnetid`这个`annotations`则认为是创建VPC内访问的负载均衡器，否则则认为是创建外网的负载均衡器。

具体示例如下所示：
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: 'subnet-xxxxxx'
  labels:
    qcloud-app: nginx
  name: nginx
spec:
  ports:
  - name: tcp-80-80-pfbp1
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    qcloud-app: nginx
  type: LoadBalancer
```
其中`subnet-xxxxxx`为集群节点所在VPC内的一个子网。

[1]: https://console.cloud.tencent.com/cvm/cbs




