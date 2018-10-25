In order to make better use of Kubernetes orchestration engine, and combine it with Tencent Cloud basic services at IaaS layer more effectively, Tencent TKE extends the Kubernetes native orchestration syntax. The following describes the extended syntax.

## Extended Syntax - Use of CBS Disk

In TKE, a CBS disk can be directly mounted to a service pod. You can proceed as follows:

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

Specify qcloudCbs for the volume type, and set the cbsDiskId as the instanceId of the disk to be mounted. (For the instanceId of CBS disk, please see [Cloud Block Storage][1]). You can set the mount point in the same way as setting that for other types of disks, as shown in the example above, to mount the CBS disk to the container's /mnt directory.

Note: CBS disk can only be mounted to one container at a time. Therefore, if a CBS disk is used in the service, the number of container pods cannot be greater than 1 and rolling update is not supported.

## Extended Syntax - VPC-based Load Balancer Access

In basic syntax, you can set the service access method by setting `type` field in `Service`. In TKE definition, `service.kubernetes.io/qcloud-loadbalancer-internal-subnetid` is defined in `annotations` to specify whether it is VPC-based load balancer access or public network-based load balancer access.

If `service.kubernetes.io/qcloud-loadbalancer-internal-subnetid` is set for the `annotations`, it is considered creating a load balancer that accesses the service within VPC. Otherwise, it is considered creating a load balancer in public network.

The example is as follows:
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
`Subnet-xxxxxx` represents a subnet of the VPC where the cluster nodes reside.

[1]: https://console.cloud.tencent.com/cvm/cbs





