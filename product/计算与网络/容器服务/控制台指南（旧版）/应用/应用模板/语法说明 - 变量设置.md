## 变量替换说明

应用模板中支持变量替换，变量的结构满足 `{{.}}`，在 `.` 后面加上对应的变量名。需要被替换的变量在模板解析时会被配置文件中配置项的值替换。例如在模板中定义 FRONTEND_REPLICAS：
```
spec:
 replicas: {{.FRONTEND_REPLICAS}}
```

在配置项中对变量 FRONTEND_REPLICAS 设定值：

```
FRONTEND_REPLICAS: 2
```
这样在模板解析时，模板文件中的 `{{.FRONTEND_REPLICAS}}` 会被替换成配置文件中的值"2"。

>? 变量名称满足正则表达式 "[A-Za-z\_][A-Za-z0-9_]\*"，最大长度为64个字符。

## 自定义变量--ReleaseCBS

在容器服务中，如果需要挂载 CBS 盘，指定的描述语言如下所示：
```
      volumes:
      - name: vol
        qcloudCbs:
          cbsDiskId: 'disk-pr47vtvt'
          fsType: ext4
```
```
        volumeMounts:
        - mountPath: /mnt
          name: vol
```
(上面这段描述语言表示：将 CBS 盘 disk-pr47vtvt 作为 vol 盘挂载，具体的挂载到容器的 /mnt 目录。)

由于 CBS 盘是不能重复挂载的，通过应用模板在不同环境部署应用时，需要指定不同的 CBS。所以容器服务提供 ReleaseCBS 变量来表示 CBS 盘。在应用部署时，会选择**应用可使用的**特定的 CBS 盘进行部署。具体示例如下：
```
      volumes:
      - name: vol
        qcloudCbs:
          cbsDiskId: '{{.ReleaseCBS_pr47vtvt}}'
          fsType: ext4
```

## 自定义变量--ReleaseSubnetId

在容器服务中，如果服务的访问方式选择为 VPC 内访问，则需要在描述文件中指定 LB 对应的 SubnetId，指定方式为，在 service 的描述文件中定义如下结果，其中 subnet-s1jz1ycx 为设定的 SubnetId。
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: 'subnet-s1jz1ycx'
```
由于 SubnetId 需要在集群所在的 VPC（私有网络）下，所以 SubnetId 在不同集群中很有可能是不相同的。为了方便在应用部署时设置 SubnetId，我们在模板中通过 ReleaseSubNetId 变量对需要设置的 subnetId 进行标识。下面是一个具体的示例：
```
apiVersion: v1
kind: Service
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: '{{.ReleaseSubnetId_XXXX}}'
```
在应用部署时，将在配置文件中为 ReleaseSubnetId_XXXX 变量指定对应的 subnetId。

>? 由于应用中的多个服务可能会设置不同的 subnetId，所有在 ReleaseSubnetId 名称后通过"\_"（下划线）和服务名称来区分不同服务的 subnetId。

## 自定义变量--ReleaseConfig

配置文件是程序运行很重要的一个部分，很多程序往往需要从磁盘的某个位置读取对应的配置文件，于是 Kubernetes 支持将通过 configmap 中的某个 key 挂载到容器指定的目录。更多关于 Kubernetes configmap 的说明可以参考 [Kubernetes官方文档](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)。

应用中包含一个属于应用的配置文件，通过自定义变量 ReleaseConfig 可以将应用的配置文件中 key 挂载到容器指定目录。
具体的使用示例如下：
```
      volumes:
      - configMap:
          Name: '{{.ReleaseConfig}}'
          items:
          - key: NAMESPCE
            mode: 511
            path: NAMESPCE
          - key: FRONTEND_REPLICAS
            mode: 511
            path: FRONTEND_REPLICAS
        name: data
```
挂载点的设置为：
```
        volumeMounts:
        - mountPath: /mnt
          name: data
```
应用的配置信息为：
```
NAMESPACE: default
FRONTEND_REPLICAS: 2
```

这样，配置文件中的 key：NAMESPACE 和 FRONTEND_REPLICAS 会被挂载到容器的 /mnt 目录，挂载的文件名称分别为 NAMESPACE 和 FRONTEND_REPLICAS。文件的内容为配置文件中相应的 key 所对应的内容。
