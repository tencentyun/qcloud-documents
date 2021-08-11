## 安装使用流程

### 1. 创建命名空间

```shell
$ kubectl create ns fluid-system
```


### 2. 下载 fluid

下载 [fluid-0.6.0.tgz](https://cos-data-lake-release-1253960454.cos.ap-guangzhou.myqcloud.com/fluid.tgz) 安装包。

>!您也可以前往 Fluid 官方页面 [Fluid Releases](https://github.com/fluid-cloudnative/fluid/releases) 中下载最新版本，但一些机器从中国境内访问时可能存在网络问题。
>


### 3. 使用 Helm 安装 Fluid

```shell
$ helm install --set runtime.goosefs.enabled=true fluid fluid-0.6.0.tgz
```

### 4. 查看 Fluid 的运行状态

```shell
$ kubectl get pod -n fluid-system
NAME                                         READY   STATUS    RESTARTS   AGE
csi-nodeplugin-fluid-2mfcr                   2/2     Running   0          108s
csi-nodeplugin-fluid-l7lv6                   2/2     Running   0          108s
dataset-controller-5465c4bbf9-5ds5p          1/1     Running   0          108s
goosefsruntime-controller-654fb74447-cldsv     1/1     Running   0          108s
```

其中，csi-nodeplugin-fluid-xx 的数量应该与 k8s 集群中节点 node 的数量相同。

到此 Fluid 已成功安装，如需自定义镜像和升级系统 crd 请参考如下说明（可选）。

### 5. 自定义镜像

解压 `fluid-0.6.0.tgz`，修改默认`values.yaml`文件：
```yaml
runtime:
  mountRoot: /runtime-mnt
  goosefs:
    runtimeWorkers: 3
    portRange: 26000-32000
    enabled: false
    init:
      image: fluidcloudnative/init-users:v0.6.0-116a5be
    controller:
      image: fluidcloudnative/goosefsruntime-controller:v0.6.0-116a5be
    runtime:
      image: ccr.ccs.tencentyun.com/goosefs/goosefs:v1.0.1
    fuse:
      image: ccr.ccs.tencentyun.com/goosefs/goosefs-fuse:v1.0.1
```

您可以修改 `goosefs` 相关的默认 `image` 内容，如放到自己的 `repo` 上。待修改完成后，重新使用 `helm package fluid` 打包，并使用如下命令，更新`fluid`版本。
```shell
helm upgrade --install fluid fluid-0.6.0.tgz
```

### 6. 更新 crd

```shell
$ kubectl get crd      
NAME                                             CREATED AT
databackups.data.fluid.io                        2021-03-02T13:12:31Z
dataloads.data.fluid.io                          2021-04-14T11:14:58Z
datasets.data.fluid.io                           2021-03-02T13:12:31Z
goosefsruntimes.data.fluid.io                    2021-04-13T13:31:38Z
```

例如，更新系统中已有的 `goosefsruntime` 的 crd。

首先删除已有的 crd：

```shell
kubectl delete crd goosefsruntimes.data.fluid.io
```

然后解压 `fluid-0.6.0.tgz`：

```shell
$ ls -l fluid/
total 32
total 32
-rw-r--r--  1 xieydd  staff   489  5 15 16:14 CHANGELOG.md
-rw-r--r--  1 xieydd  staff  1061  7 22 00:08 Chart.yaml
-rw-r--r--  1 xieydd  staff  2560  5 15 16:14 VERSION
drwxr-xr-x  8 xieydd  staff   256  7 20 15:06 crds
drwxr-xr-x  7 xieydd  staff   224  5 24 14:18 templates
-rw-r--r--  1 xieydd  staff  1665  7 22 00:08 values.yaml
```

最后创建新的 crd：

```shell
kubectl apply -f crds/data.fluid.io_goosefsruntimes.yaml
```
