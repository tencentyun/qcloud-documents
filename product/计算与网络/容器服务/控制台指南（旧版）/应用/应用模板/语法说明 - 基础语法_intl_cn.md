腾讯云容器服务底层基于Kubernetes编排引擎。在容器服务的应用模板中原生的支持Kubernetes的语法。本文将对Kubernetes的常用的语法做介绍。

## CPU/Memory限制设置
Kubernetes使用Limit和Request对容器使用的资源进行限制。更多详细内容可以参数[官方文档][1]。

对于CPU和内存的设置，示例如下：
```
        resources:
          limits:
            memory: 128Mi
            cpu: 0
          requests:
            cpu: 200m
            memory: 128Mi
```

在上面的示例中，通过设置resources中limits和requests参数中CPU和Memory的值，来限制容器CPU和memory的使用。上面的示例中，CPU在调度时被分配的CPU为0.2核，CPU限制使用的最大量无上限。内存在调度时被分配的128M，内存最大使用量被限制为128M。
在CPU资源的限制中，可以使用单位`m`,1m=0.001核。在内存的限制中，可以使用M，Mi，G，Gi。1M=1000*1000*Byte,1Mi=1024*1024*Byte,1G=1000*1000*1000*Byte,1Gi=1024*1024*1024*Byte。

## 命名空间设置

Kubernetes使用namespace参数来设置服务所在的命名空间。例如设置命名空间为wordpress

```
  namespace: wordpress
```

备注： 
1、在同一个服务不同资源下，命名空间必须设置成一样。同一个应用中不同服务，也必须设置成一样。
2、如果namespace参数不填写，会默认使用default命名空间。

关于更多关于namespace的作用可以参考[Namespace使用指引][2]

## 实例数设置
Kubernetes使用replicas参数来设置实例的数量，如下所示:

```
spec:
  replicas: 2
```

通过设置replicas参数，把容器示例数设置为2。

## 镜像参数设置

Kubernetes使用image参数来设置容器使用的镜像。指定使用容器镜像busybox，版本号为latest示例如下：

```
image: busybox:latest
```

备注：如果不指定镜像的版本，会默认使用latest作为镜像的版本

## 服务类型设置

Kubernetes支持多种不同的服务访问类型，常用的服务访问类型包括: 负载均衡访问，集群内访问，节点端口访问，不设置访问方式。对于负载均衡访问，在容器服务中又分为外网负载均衡访问和VPC内负载均衡访问。Kubernetes通过Service资源中的`type`参数来指定服务的访问类型。

**外网负载均衡访问**
```
apiVersion: v1
kind: Service
metadata:
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
如上面的例子所示，通过设置`type`为LoadBalancer将服务的访问类型指定为外网负载均衡访问。

**VPC内负载均衡访问**

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

VPC内访问的负载均衡，除了需要将通过设置`type`为LoadBalancer，还需要设置一个`service.kubernetes.io/qcloud-loadbalancer-internal-subnetid`的`annotations`，其值设置成负载均衡IP所在的子网(该子网必须在容器集群节点所在vpc内)。

**集群内访问**

```
apiVersion: v1
kind: Service
metadata:
  labels:
    qcloud-app: nginx
  name: nginx
spec:
  ports:
  - name: tcp-80-80-tlap9
    nodePort: 0
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    qcloud-app: nginx
  type: ClusterIP
```
如上面的例子所示，通过设置`type`为ClusterIP将服务的访问类型指定为集群内通过ClusterIP访问。对于外网负载均衡和内网负载均衡也会默认分配ClusterIP，也可以通过ClusterIP在集群内访问。

**不设定访问方式**

如果服务中没有`Service`资源，则不设定服务的访问方式。

备注： 容器服务中暂时未开放节点端口的这种访问方式，在外网负载均衡访问，VPC内负载均衡访问和集群内访问三种访问方式中都会默认为服务分配节点端口。在Ingress中也会通过注册配节点端口，来注册服务访问，如果Ingress中配置了对该服务的访问，将服务访问方式设定为"不设定访问方式"会到时候服务不可用。

更多关于服务访问方式的说明可以参考[kubernetes 官方文档][3]，也可以参考[服务访问方式设置][4]

## 磁盘挂载设置

Kubernetes支持挂载不类型的目录或者文件到容器指定的目录。其中涉及到两个步骤：挂载磁盘设置和挂载点设置。

例如挂载一个主机上的/home目录到容器中：

(1) 设置挂载的磁盘/home目录
```
      volumes:
      - hostPath:
          path: /home
        name: vol
```
(2) 将磁盘挂载到mnt目录
```
        volumeMounts:
        - mountPath: /mnt
          name: vol
```

详细的关于磁盘挂载的说明，可以参考[Kubernetes官方文档-volumes][5]

容器平台现还支持挂载CBS盘，NFS，和配置文件。对于不同类型磁盘的挂载，可以参考。

[扩展语法--CBS盘的使用][6]

[自定义变量--ReleaseConfig][7]

## 多容器服务

Kubernetes中支持在一个实例中包含多个容器，例如下面服务中一个实例包含一个nginx容器和一个busybox容器。

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    qcloud-app: nn
  name: nn
  namespace: default
spec:
  replicas: 1
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      qcloud-app: nn
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        qcloud-app: nn
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
      - args:
        - "36000"
        command:
        - sleep
        image: busybox:latest
        imagePullPolicy: Always
        name: busybox
        resources:
          requests:
            cpu: 200m
        securityContext:
          privileged: false
      serviceAccountName: ""
      volumes: null
status: {}
```

如上面的例子所示，在`containers`参数中设置不同的容器信息，可以使服务实例包含多个容器。

## Kubernetes基础编排语法

Kubernetes通过定义API结构体中的每一个参数，来定义编排的描述语言。关于Kubernetes API参数的详细说明可以参考：
[v1.7][9]
[v1.6][10]
[v1.5][11]

更多关于Kubernetes编排描述语言的说明，可以参考[API Overview][12]

  [1]: https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container/
  [2]: https://cloud.tencent.com/document/product/457/10177
  [3]: https://kubernetes.io/docs/concepts/services-networking/service/
  [4]: https://cloud.tencent.com/document/product/457/9098
  [5]: https://kubernetes.io/docs/concepts/storage/volumes/
  [6]: https://cloud.tencent.com/document/product/457/11958#.E6.89.A9.E5.B1.95.E8.AF.AD.E6.B3.95---cbs.E7.9B.98.E4.BD.BF.E7.94.A8
  [7]: https://cloud.tencent.com/document/product/457/11956#.E8.87.AA.E5.AE.9A.E4.B9.89.E5.8F.98.E9.87.8F--releaseconfig
  [8]: https://cloud.tencent.com/document/product/457/9112
  [9]: https://kubernetes.io/docs/api-reference/v1.7/
  [10]: https://kubernetes.io/docs/api-reference/v1.6/
  [11]: https://kubernetes.io/docs/api-reference/v1.5/
  [12]: https://kubernetes.io/docs/reference/api-overview/