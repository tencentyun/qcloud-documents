# 使用 Velero 跨云平台迁移集群资源到 TKE



## 概述

[Velero](https://velero.io/) 是一个非常强大的开源工具，可以安全地备份和还原，执行灾难恢复以及迁移Kubernetes群集资源和持久卷，可以在 TKE 平台上使用 Velero 备份、还原和迁移集群资源，关于如何使用请参阅 [使用对象存储 COS 作为 Velero 存储实现集群资源备份和还原](https://cloud.tencent.com/document/product/457/50122) 和 [在 TKE 中使用 Velero 迁移复制集群资源](https://cloud.tencent.com/document/product/457/50550)，本文将介绍如何使用 Velero 将自建或其他云平台 Kubernetes 集群无缝迁移到 TKE 平台。

## 迁移原理

架构原理与[使用 Velero 迁移复制集群资源 ](https://cloud.tencent.com/document/product/457/50550#.E8.BF.81.E7.A7.BB.E5.8E.9F.E7.90.86)过程的原理类似，迁移集群和被迁移集群都安装 Velero 实例，且指定同一个腾讯云 COS 后端存储，被迁移集群按需执行备份，目标集群按需还原集群资源实现资源迁移。不同的是，自建或其他云平台的集群资源迁移到 TKE 时，需要考虑和解决因跨平台导致集群环境差异问题，幸运的是，Velero 提供了很多实用的备份和还原策略帮助我们解决这些问题，后面的迁移示例会介绍如何更好的利用和使用它们。

## 环境准备

- 已有自建或其他云平台 Kubernetes 集群（以下称作集群 A ），且集群版本为 1.10 以上。
- 已创建迁移目标的 TKE 集群（以下称作集群 B ），创建 TKE 集群请参阅 [创建集群](https://cloud.tencent.com/document/product/457/32189)。
- 集群 A 和 集群 B 都需要安装 Velero 实例（1.5 版本以上），并且共用同一个腾讯云 COS 存储桶作为 Velero 后端存储，安装步骤请参阅 [配置存储和安装 Velero ](https://cloud.tencent.com/document/product/457/50122)。
- 确保镜像资源在迁移后可以正常拉取。
- 确保两个集群的 K8S 版本的 API 兼容，最好是相同版本。

## 迁移指导

在迁移工作进行前，首先应该理清迁移思路，制定详细的迁移计划，迁移过程大概需要考虑下面几点：

- **筛选分析需要迁移哪些集群资源，不需要迁移哪些集群资源**

  根据实际情况筛选分类出需要迁移资源清单和不需要迁移的资源清单。


- **根据业务场景考虑是否需要自定义一些 Hook 操作**

  需要考虑在备份集群资源时，是否需要在备份期间执行 [备份 Hooks](https://velero.io/docs/v1.5/backup-hooks/) ，比如需要将正在运行的应用的内存数据落盘场景。

  类似的，在还原（迁移）集群资源时，是否需要在还原期间执行 [还原 Hooks](https://velero.io/docs/v1.5/backup-hooks/) ，比如需要在还原前做一些初始化工作。

- **按需编写备份和还原的命令或资源清单**

  根据筛选归类的资源清单编写备份和还原策略，推荐在复杂场景下使用创建资源清单的方式来执行备份和还原， YAML 资源清单比较直观且方便维护，参数指定的方式可以在简单迁移场景或测试时使用。

- **处理跨云平台资源的差异性**

  由于是跨云平台，动态创建 PVC 的存储类等关系可能不同，需要提前规划动态 PVC/PV 存储类关系是否需要重新映射，需在在还原操作前，创建相关映射的 `ConfigMap` 配置。如果需要解决更加个性化的差异，可以手动修改备份后的资源清单解决。

- **操作完成后核查迁移资源**

  检查校验迁移的集群资源是否符合预期且数据完整可用。

## 操作步骤

接下来将演示将某云平台集群 A 中的资源迁移到 TKE 集群 B 中的操作步骤，其中涉及到 Velero  备份和还原实用基础知识，如不了解请先移步文章末尾【 Velero 备份/还原实用知识】 查看。

### 创建集群 A 示例资源

在集群 A 中部署 Velero 示例中含有 PVC 的 Nginx 工作负载，为了方便起见直接使用动态存储类来创建 PVC 和 PV ，首先查看当前集群支持的动态存储类信息：

```bash
# 获取当前集群支持的存储类信息
[root@iZj6c3vzs170hmeiu98h5aZ ~]# kubectl  get sc
NAME                       PROVISIONER                       RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
alicloud-disk-available    diskplugin.csi.alibabacloud.com   Delete          Immediate              true                   3d3h
...
```

这里使用集群中存储类名为 "alicloud-disk-available" 的存储类来动态创建 ，修改  [with-pv.yaml](https://github.com/vmware-tanzu/velero/blob/v1.5.1/examples/nginx-app/with-pv.yaml) 的 PVC 资源清单如下图：

```yaml
...
---
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: nginx-logs
  namespace: nginx-example
  labels:
    app: nginx
spec:
  # Optional: 修改PVC 的存储类的值为 alicloud-disk-available 
  storageClassName: alicloud-disk-available 
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi # 由于该云平台限制存储最小为20G，需要同步修改此值为20Gi
... 
```

修改完成后应用示例中的 YAML 创建下面的集群资源（nginx-example命名空间）：

```bash
[root@iZj6c3vzs170hmeiu98h5aZ nginx-app]# kubectl apply -f with-pv.yaml 
namespace/nginx-example created
persistentvolumeclaim/nginx-logs created
deployment.apps/nginx-deployment created
service/my-nginx created
```

创建出来的 PVC "nginx-logs"  已挂载给 nginx 容器的 `/var/log/nginx` 目录作为服务的日志存储，本示例在浏览器测试访问 Nginx 服务，给挂载的 PVC 生产一些日志数据。

```bash
# 查看测试产生的 Nginx 日志大小，当前为 84 K 
[root@iZj6c8ttj5dmmrs75yb7ybZ ~]# kubectl exec -it nginx-deployment-5ccc99bffb-6nm5w bash -n nginx-example
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl kubectl exec [POD] -- [COMMAND]
Defaulting container name to nginx.
Use 'kubectl describe pod/nginx-deployment-5ccc99bffb-6nm5w -n nginx-example' to see all of the containers in this pod 
root@nginx-deployment-5ccc99bffb-6nm5w:/# du -sh /var/log/nginx/
84K /var/log/nginx/
# 查看 accss.log 和 error.log 前两条日志（以便后续还原时做数据比对）
root@nginx-deployment-5ccc99bffb-6nm5w:/# head -n 2 /var/log/nginx/access.log 
192.168.0.73 - - [29/Dec/2020:03:02:31 +0000] "GET /?spm=5176.2020520152.0.0.22d016ddHXZumX HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
192.168.0.73 - - [29/Dec/2020:03:02:32 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://47.242.233.22/?spm=5176.2020520152.0.0.22d016ddHXZumX" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
root@nginx-deployment-5ccc99bffb-6nm5w:/# head -n 2 /var/log/nginx/error.log 
2020/12/29 03:02:32 [error] 6#6: *597 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.0.73, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "47.242.233.22", referrer: "http://47.242.233.22/?spm=5176.2020520152.0.0.22d016ddHXZumX"
2020/12/29 03:07:21 [error] 6#6: *1172 open() "/usr/share/nginx/html/0bef" failed (2: No such file or directory), client: 192.168.0.73, server: localhost, request: "GET /0bef HTTP/1.0"
```

### 确认需要迁移的资源清单

使用下面命令输出当前集群中所有的资源清单列表：

```yaml
kubectl api-resources --verbs=list -o name  | xargs -n 1 kubectl get --show-kind --ignore-not-found --all-namespaces
```

 也可以根据资源是否区分命名空间需要缩小输出的资源范围：

-   查看不区分命名空间的资源清单列表：

   ```yaml
   kubectl api-resources --namespaced=false --verbs=list -o name | xargs -n 1 kubectl get --show-kind --ignore-not-found
   ```

- 查看区分命名空间的资源清单列表：

   ```yaml
   kubectl api-resources --namespaced=true --verbs=list -o name | xargs -n 1 kubectl get --show-kind --ignore-not-found --all-namespaces
   ```


可以根据实际情况筛选出需要被迁移的资源清单，本示例将直接从某云平台迁移 "nginx-example" 命名空间下 Nginx 工作负载相关的资源到 TKE 平台，如下所示：

```bash
[root@iZj6c3vzs170hmeiu98h5aZ ~]# kubectl  get all -n nginx-example
NAME                                    READY   STATUS    RESTARTS   AGE
pod/nginx-deployment-5ccc99bffb-tn2sh   2/2     Running   0          2d19h

NAME               TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/my-nginx   LoadBalancer   172.21.1.185   x.x.x.x   80:31455/TCP   2d19h

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx-deployment   1/1     1            1           2d19h

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/nginx-deployment-5ccc99bffb   1         1         1       2d19h
[root@iZj6c3vzs170hmeiu98h5aZ ~]# kubectl  get pvc -n nginx-example
NAME         STATUS   VOLUME                   CAPACITY   ACCESS MODES   STORAGECLASS              AGE
nginx-logs   Bound    d-j6ccrq4k1moziu1l6l5r   20Gi       RWO            alicloud-disk-available   2d19h
[root@iZj6c3vzs170hmeiu98h5aZ ~]# kubectl  get pv
NAME                     CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                      STORAGECLASS              REASON   AGE
d-j6ccrq4k1moziu1l6l5r   20Gi       RWO            Delete           Bound    nginx-example/nginx-logs   alicloud-disk-available            2d19h
```

### 确认Hook 策略

本示例在 [with-pv.yaml](https://github.com/vmware-tanzu/velero/blob/v1.5.1/examples/nginx-app/with-pv.yaml) 中已经配置了在备份 Nginx 工作负载前将文件系统设置为只读，在备份后恢复读写的 Hook 策略，如下 YAML 所示：

```yaml
...
      annotations:
        # 备份 Hook 策略的注解表示：在开始备份之前将nginx日志目录设置为只读模式，备份完成后恢复读写模式
        pre.hook.backup.velero.io/container: fsfreeze
        pre.hook.backup.velero.io/command: '["/sbin/fsfreeze", "--freeze", "/var/log/nginx"]'
        post.hook.backup.velero.io/container: fsfreeze
        post.hook.backup.velero.io/command: '["/sbin/fsfreeze", "--unfreeze", "/var/log/nginx"]'
    spec:
      volumes:
        - name: nginx-logs
          persistentVolumeClaim:
           claimName: nginx-logs
      containers:
      - image: nginx:1.17.6
        name: nginx
        ports:
        - containerPort: 80
        volumeMounts:
          - mountPath: "/var/log/nginx"
            name: nginx-logs
            readOnly: false
      - image: ubuntu:bionic
        name: fsfreeze
        securityContext:
          privileged: true
        volumeMounts:
          - mountPath: "/var/log/nginx"
            name: nginx-logs
 ...
```



### 开始迁移操作

接下来根据实际情况编写备份和还原策略，开始对某云平台的 Nginx 工作负载资源进行迁移。

#### 在集群 A 执行备份

本示例创建如下 YAML 来备份想要迁移的资源：

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: migrate-backup
  # 必须得是 velero 安装的命名空间
  namespace: velero
spec:
  # 仅包含 nginx-example 命名空间的资源
  includedNamespaces:
   - nginx-example
  # 表示是否包含不区分命名空间的资源
  includeClusterResources: true
  # 备份数据存储位置指定
  storageLocation: default
  # 卷快照存储位置指定
  volumeSnapshotLocations:
    - default
  # 使用 restic 备份卷
  defaultVolumesToRestic: true

```

执行备份过程如下所示， 当备份状态为 "Completed" 且 errors 数为 0 时表示备份过程完整无误：

```bash
[root@iZj6c8ttj5dmmrs75yb7ybZ ~]# kubectl apply -f backup.yaml 
backup.velero.io/migrate-backup created
[root@iZj6c8ttj5dmmrs75yb7ybZ ~]# velero backup get 
NAME             STATUS      ERRORS   WARNINGS   CREATED                EXPIRES   STORAGE LOCATION   SELECTOR
migrate-backup   InProgress  0        0          2020-12-29 19:24:12 +0800 CST   29d    default     <none>
[rootftiZi6c8tti5dmmrs75yb7vbZ ~1# velero backup get 
NAME             STATUS      ERRORS   WARNINGS   CREATED                EXPIRES   STORAGE LOCATION   SELECTOR
migrate-backup   Completed   0        0          2020-12-29 19:24:28 +0800 CST   29d    default     <none>
```

备份完成后，临时将备份存储位置更新为只读模式（非必须，这可以防止在还原过程中 Velero 在备份存储位置中创建或删除备份对象）：

```bash
kubectl patch backupstoragelocation default --namespace velero \
    --type merge \
    --patch '{"spec":{"accessMode":"ReadOnly"}}'
```



#### 处理跨云平台资源的差异性

1. 由于使用的动态存储类有差异，这里应用如下所示的 ConfigMap  YAML 为持久卷 "nginx-logs"  创建动态存储类名映射：

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: change-storage-class-config
  namespace: velero
  labels:
    velero.io/plugin-config: ""
    velero.io/change-storage-class: RestoreItemAction
data:
  # 添加 PVC 存储类新名映射到腾讯云动态存储类 cbs
  alicloud-disk-available: cbs
```

```bash
[root@VM-20-5-tlinux ~]# kubectl  apply -f backup.yaml 
configmap/change-storage-class-config created
```

2. Velero 备份的资源清单 以 `json` 格式存放在对象存储中，如果有更加个性化的迁移需求，可以直接下载备份文件并自定义修改，本示例为 Nginx  的 Deployment 资源清单自定义添加一个注解 "jokey-test:jokey-test"。

```bash
jokey@JOKEYLI-MB0 Downloads % mkdir migrate-backup
# 解压备份文件
jokey@JOKEYLI-MB0 Downloads % tar -zxvf migrate-backup.tar.gz  -C migrate-backup
# 编辑修改想要自定义的资源, 本示例为 nginx 的 Deployment 资源添加 "jokey-test":"jokey-test" 的注解项
jokey@JOKEYLI-MB0 migrate-backup % cat  resources/deployments.apps/namespaces/nginx-example/nginx-deployment.json 
{"apiVersion":"apps/v1","kind":"Deployment","metadata":{"annotations":{"jokey-test":"jokey-test",...
# 重新打包修改后的备份文件
jokey@JOKEYLI-MB0 migrate-backup % tar -zcvf migrate-backup.tar.gz *
```

完成自定义修改并重新打包后上传替换原有备份文件：

![image-20210104171654052](https://main.qcloudimg.com/raw/d71c98bb81548f20538208f258a40fc3.png)

#### 在集群 B 执行还原

本示例应用如下所示的资源清单执行还原操作（迁移）：

```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: migrate-restore
  namespace: velero
spec:
  backupName: migrate-backup
  includedNamespaces:
    - nginx-example
  
  # 按需填写需要恢复的资源类型，nginx-example 命名空间下没有想要排除的资源，所以这里直接写 '*'
  includedResources:
    - '*'
  
  includeClusterResources: null
  
  # 还原时不包含的资源，由于 includeClusterResources 已配置 false，这里不需要再额外排除 storageclasses 资源类型。
  excludedResources:
    - storageclasses.storage.k8s.io
 
  # 使用 labelSelector 选择需要还原的资源，由于此示例中 Deployment 资源清单没有此label， 但需要还原，这里先注释。
  # labelSelector:
  #   matchLabels:
  #     app: nginx
  
  # 设置命名空间关系映射策略
  namespaceMapping:
    nginx-example: default
  restorePVs: true
```
执行还原过程如下所示， 当还原状态为 "Completed" 且 errors 数为 0 时表示还原过程完整无误：
```bash
[root@VM-20-5-tlinux ~]# kubectl  apply -f restore.yaml 
restore.velero.io/migrate-restore created
[root@VM-20-5-tlinux ~]# velero restore get
NAME              BACKUP           STATUS      STARTED                         COMPLETED                       ERRORS   WARNINGS   CREATED                         SELECTOR
migrate-restore   migrate-backup   Completed   2021-01-12 20:39:14 +0800 CST   2021-01-12 20:39:17 +0800 CST   0        0          2021-01-12 20:39:14 +0800 CST   <none>
```


### 迁移资源核查

1. 首先查看被迁移的资源的运行状态：

   ```bash
   # 在还原时指定了 "nginx-example" 命名空间映射到 "default" 命名空间，所以还原的资源将运行在 "default" 命名空间下 
   [root@VM-20-5-tlinux ~]# kubectl  get all -n default 
   NAME                                    READY   STATUS    RESTARTS   AGE
   pod/nginx-deployment-5ccc99bffb-6nm5w   2/2     Running   0          49s
   
   NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)         AGE
   service/kube-user    LoadBalancer   172.16.253.216   10.0.0.28        443:30060/TCP   8d
   service/kubernetes   ClusterIP      172.16.252.1     <none>           443/TCP         8d
   service/my-nginx     LoadBalancer   172.16.254.16    x.x.x.x          80:30840/TCP    49s
   
   NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/nginx-deployment   1/1     1            1           49s
   
   NAME                                          DESIRED   CURRENT   READY   AGE
   replicaset.apps/nginx-deployment-5ccc99bffb   1         1         1       49s
   ```

2. 从上面可以看出被迁移的资源的运行状态都是正常的，下来核查设置的还原策略是否生效：

   - 核查动态存储类名映射是否正确：

     ```bash
     # 可以看到 PVC/PV 的存储类已经是 "cbs" 了，说明映射成功
     [root@VM-20-5-tlinux ~]# kubectl  get pvc -n default 
     NAME         STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
     nginx-logs   Bound    pvc-bcc17ccd-ec3e-4d27-bec6-b0c8f1c2fa9c   20Gi       RWO            cbs            55s
     [root@VM-20-5-tlinux ~]# kubectl  get pv 
     NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                STORAGECLASS   REASON   AGE
     pvc-bcc17ccd-ec3e-4d27-bec6-b0c8f1c2fa9c   20Gi       RWO            Delete           Bound    default/nginx-logs   cbs                     57s
     ```

   - 在还原前自定义为 "deployment.apps/nginx-deployment" 添加的注解：

     ```bash
     # 获取注解"jokey-test"成功,说明自定义修改资源成功。
     [root@VM-20-5-tlinux ~]# kubectl  get deployment.apps/nginx-deployment -o custom-columns=annotations:.metadata.annotations.jokey-test
     annotations
     jokey-test
     ```

   - 从上述资源运行状态可以看出命名空间映射配置也是成功的。

3. 检查工作负载挂载的 PVC 数据是否成功迁移：

   ```bash
   # 查看挂载的 PVC 数据目录中的数据大小，显示为 88K 是因为 CLB 请求服务增加了健康检查日志。   
   [root@VM-20-5-tlinux ~]# kubectl  exec -it nginx-deployment-5ccc99bffb-6nm5w -n default -- bash
   Defaulting container name to nginx.
   Use 'kubectl describe pod/nginx-deployment-5ccc99bffb-6nm5w -n default' to see all of the containers in this pod.
   root@nginx-deployment-5ccc99bffb-6nm5w:/# du -sh /var/log/nginx 
   88K     /var/log/nginx
   # 查看前两条日志信息，和迁移前一致，说明 PVC 数据没丢失
   root@nginx-deployment-5ccc99bffb-6nm5w:/# head -n 2 /var/log/nginx/access.log 
   192.168.0.73 - - [29/Dec/2020:03:02:31 +0000] "GET /?spm=5176.2020520152.0.0.22d016ddHXZumX HTTP/1.1" 200 612 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
   192.168.0.73 - - [29/Dec/2020:03:02:32 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://47.242.233.22/?spm=5176.2020520152.0.0.22d016ddHXZumX" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36" "-"
   root@nginx-deployment-5ccc99bffb-6nm5w:/# head -n 2 /var/log/nginx/error.log 
   2020/12/29 03:02:32 [error] 6#6: *597 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), client: 192.168.0.73, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "47.242.233.22", referrer: "http://47.242.233.22/?spm=5176.2020520152.0.0.22d016ddHXZumX"
   2020/12/29 03:07:21 [error] 6#6: *1172 open() "/usr/share/nginx/html/0bef" failed (2: No such file or directory), client: 192.168.0.73, server: localhost, request: "GET /0bef HTTP/1.0"
   ```

综上所述，此示例中成功迁移了 "nginx-example" 命名空间下 Nginx 工作负载相关资源和数据到 "default" 命名空间。

## 总结

本示例讲解和演示了常见的集群资源迁移到 TKE 的思路和方法步骤，若在实际迁移过程中遇到未覆盖到的场景时，欢迎咨询和讨论迁移解决方案。



## Velero 备份/还原实用知识

velero 提供了许多非常实用的备份和还原策略，以下作简要梳理：

- 当不使用任何筛选选项时，Velero 会将所有对象包括在备份或还原操作中，在**备份和还原**时可以指定参数按需过滤资源：

  包含关系的过滤参数：

  - `--include-resources`：指定要包含的资源对象列表。

  - `--include-namespaces`：指定要包含的命名空间列表。

  - `--include-cluster-resources`：指定是否要包含集群的资源。

  - `--selector`：指定包含与标签选择器匹配的资源。

  不包含关系的过滤参数：

  - `--exclude-namespaces`：指定要排除的命名空间列表

  - `--exclude-resources`：指定要排除的资源对象列表。

  - `velero.io/exclude-from-backup=true`：此配置项为资源对象配置lable 属性，添加了此 label 配置项的资源对象将会排除在外。

  详情请参阅 [资源过滤]( https://velero.io/docs/v1.5/resource-filtering/)。

- 在**备份期间**执行一些 Hook 操作，比如需要在在备份前将内存数据落盘，详情请参阅 [备份 Hooks](https://velero.io/docs/v1.5/backup-hooks/) 。

- 在**还原期间**执行一些 Hook 操作，比如在还原前判断组件依赖是否可用，详情请参阅 [还原 Hooks](https://velero.io/docs/v1.5/backup-hooks/) 。

- 在**还原时**配置 PVC/PV 卷相关映射关系配置：

  - [配置 PV / PVC 存储类映射](https://velero.io/docs/v1.5/restore-reference/#changing-pvpvc-storage-classes)。

  - [配置 PVC 绑定节点映射](https://velero.io/docs/v1.5/restore-reference/#changing-pvc-selected-node)。

  详情请参阅 [还原参考](https://velero.io/docs/v1.5/restore-reference/)。

- Restic 备份卷配置

  从 1.5 版本开始，Velero 默认使用 Restic 备份所有pod卷，而不必单独注释每个pod，所以**推荐使用 Velero 1.5 以上版本**。

  *在 1.5 版本以前， Velero 使用 restic 在备份卷时， Restic 有两种方式发现需要备份的 Pod卷*：

  - *使用的Pod卷备份选择包含注解（默认）：*

    ```yaml
    kubectl -n <YOUR_POD_NAMESPACE> annotate <pod/YOUR_POD_NAME> backup.velero.io/backup-volumes=<YOUR_VOLUME_NAME_1,YOUR_VOLUME_NAME_2,...>
    ```

  - *使用的 Pod 卷备份选择不包含注解：*

    ```yaml
    kubectl -n <YOUR_POD_NAMESPACE> annotate <pod/YOUR_POD_NAME> backup.velero.io/backup-volumes-excludes=<YOUR_VOLUME_NAME_1,YOUR_VOLUME_NAME_2,...>
    ```

  备份完成后可以查看备份卷信息：

  ```yaml
  kubectl -n velero get podvolumebackups -l velero.io/backup-name=<YOUR_BACKUP_NAME> -o yaml
  ```

  还原完成后可以查看还原卷信息：

  ```yaml
  kubectl -n velero get podvolumerestores -l velero.io/restore-name=<YOUR_RESTORE_NAME> -o yaml
  ```

- 除了使用 Velero 命令执行备份操作，也可以通过**创建备份资源来触发（推荐）**，配置示例请参阅 [备份示例](https://velero.io/docs/v1.5/api-types/backup/#definition) ，API 详细字段定义可参考 [备份 API 定义]( https://github.com/vmware-tanzu/velero/blob/main/pkg/apis/velero/v1/backup.go)。

- 除了执行 Velero 命令执行还原操作，也可以通过**创建还原资源来触发（推荐）**，配置示例参参阅 [还原示例](https://velero.io/docs/v1.5/api-types/restore/#definition)，API 详细字段定义可参考 [还原 API 定义](https://github.com/vmware-tanzu/velero/blob/main/pkg/apis/velero/v1/restore.go)。

- 如有 annonations 、label 等其他个性化资源配置差异，可以在还原前手动编辑备份的 josn 资源清单文件。