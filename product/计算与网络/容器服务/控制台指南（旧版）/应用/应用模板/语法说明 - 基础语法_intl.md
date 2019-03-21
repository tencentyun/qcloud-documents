Tencent Cloud TKE is based on Kubernetes orchestration engine. Kubernetes syntax is natively supported in TKE application templates. This document describes the common syntax of Kubernetes.

## Set CPU/Memory Limits
Kubernetes uses `Limit` and `Request` to limit the resources used by a container. For more information, please see [here][1].

The limits of CPU and memory are configured as follows:
```
        resources:
          limits:
            memory: 128Mi
            cpu: 0
          requests:
            cpu: 200m
            memory: 128Mi
```

In the example above, the usage of container CPU and memory is limited by setting the values of CPU and Memory in the parameters `limits` and `requests` under `resources`. 0.2-core CPU is allocated during scheduling and there is no limit on the maximum CPU usage. 128-MB memory is allocated during scheduling and the maximum memory usage is 128 MB.
The unit `m` can be used for the limit of CPU resource (1m=0.001 core). The units of M, Mi, G and Gi can be used for the limit of memory. 1M=1000*1000*Byte, 1Mi=1024*1024*Byte, 1G=1000*1000*1000*Byte, 1Gi=1024*1024*1024*Byte.

## Set Namespace

Kubernetes uses the parameter `namespace` to set the namespace where the service resides. For example, set the `namespace` to `wordpress`.

```
  namespace: wordpress
```

Note: 
1. The namespace must be set to the same value for different resources under the same service. It must also be set to the same value for different services in the same application.
2. If parameter `namespace` is left empty, `default` namespace is used.

For more information on namespace, please see [Namespace Usage Guide][2]

## Set Number of Pods
Kubernetes uses the parameter `replicas` to set the number of pods, as shown below:

```
spec:
  replicas: 2
```

Set the number of container pods to 2 in the parameter `replicas`.

## Set Image Parameter

Kubernetes uses the parameter `image` to set the image used by the container. In the example below, container image is specified as "busybox" and tag as `latest`:

```
image: busybox:latest
```

Note: If you do not specify an image tag, `latest` is used as the image tag by default.

## Set Service Type

Kubernetes supports many service access types. Common service access types include: Load balancer access, in-cluster access, node port access, and "Do not set access mothod". In TKE, load balancer access is divided into public network-based load balancer access and VPC-based load balancer access. Kubernetes specifies the service access type with the parameter `type` in the Service resource.

**Public network-based load balancer access**
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
As shown in the example, the service access type is set to public network-based load balancer access by setting `type` to `LoadBalancer`.

**VPC-based load balancer access**

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

For VPC-based load balancer access, in addition to setting `type` to LoadBalancer, you need to set `service.kubernetes.io/qcloud-loadbalancer-internal-subnetid` for `annotations`. Its value represents the subnet where the load balancer IP resides (the subnet must be in the VPC where the container cluster nodes reside).

**In-cluster access**

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
As shown in the example, the service access type is set to access via ClusterIP by setting `type` to `ClusterIP`. For public network-based and VPC-based load balancers, ClusterIP is also assigned by default and the service can be also be accessed within the `cluster` via `ClusterIP`.

**Do not set access method**

If the service does not have a `Service` resource, service access method is not set.

Note: Node port access is unavailable in TKE. A node port will be assigned to the service by default in public network-based load balancer access, VPC-based load balancer access and in-cluster access. In Ingress, service access is also registered by registering a node port. If the access to the service is configured in the Ingress, setting the service access method to "Do not set access method" can make the service unavailable.

For more information on service access, please see [Kubernetes official documents][3], or [Set Service Access Method][4].

## Disk Mounting

Kubernetes supports mounting various directories or files to the container's specified directory. This involves two steps: setting disk mounting and setting mount point.

For example, to mount the /home directory on a server to a container:

(1) Set the disk/home directory to be mounted;
```
      volumes:
      - hostPath:
          path: /home
        name: vol
```
(2) Mount the disk to the mnt directory.
```
        volumeMounts:
        - mountPath: /mnt
          name: vol
```

For more information on disk mounting, please see [Kubernetes official documents - Volumes][5]

The container platform also supports mounting CBS disks, NFS and configuration files. For more information on mounting different types of disks, pleas see:

[Extended Syntax - Use of CBS Disk][6]

[Custom Variables - ReleaseConfig][7]

## Multi-Container Service

In Kubernetes, a pod can contain multiple containers. For example, in the following service, a pod contains an `nginx` container and a `busybox` container.

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

As shown in the example, setting different container information in the parameter `containers` makes the service pod contain multiple containers.

## Kubernetes Basic Orchestration Syntax

Kubernetes defines the orchestration description language by defining each parameter in the API structure. For more information on Kubernetes API parameters, please see:
[v1.7][9]
[v1.6][10]
[v1.5][11]

For more information on Kubernetes orchestration description language, please see [API Overview][12].

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
