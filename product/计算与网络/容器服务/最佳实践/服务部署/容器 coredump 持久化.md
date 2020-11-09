## 操作场景

有时候容器发生异常然后挂掉，我们的业务日志可能无法足够的信息来定位挂掉的原因，需要结合 coredump 来进一步分析，本文将介绍如何让容器产生 coredump 并保存下来。

>! 本文仅适用于 TKE 集群

## 操作步骤
### 开启 coredump

首先要为节点设置 core 文件的存放路径格式:
``` bash
# 在节点上执行
echo "/tmp/cores/core.%h.%e.%p.%t" > /proc/sys/kernel/core_pattern
```

有几点需要说明：
* `%h`: 主机名，在 Pod 内，主机名就是 Pod 的名称，推荐。
* `%e`: 程序文件名，推荐。
* `%p`: 进程 ID，可选。
* `%t`: coredump 的时间，可选。

最终生成的 core 文件完整路径示例:  

```
/tmp/cores/core.nginx-7855fc5b44-p2rzt.bash.36.1602488967
```

节点上执行后，容器无需更改配置，自动生效(继承)，如果需要在许多节点上批量执行:

* 对于存量节点，参考 [使用 Ansible 批量操作 TKE 节点](https://cloud.tencent.com/document/product/457/48973)。

* 对于增量节点，参考 [设置节点的启动脚本](https://cloud.tencent.com/document/product/457/32206)。

### 启用 COS 扩展组件

我们需要为容器挂载 volume，不然容器重启后将会丢失 core 文件，存储在什么地方呢？一般不会为每个 Pod 单独挂载云盘，这样成本太高，我们可以挂载 COS 对象存储。

进入集群，点击【组件管理】-【新建】，勾选 【COS】，点完成:

![](https://main.qcloudimg.com/raw/f93686594dee1d137a747f7de85c72dd.png)

### 创建存储桶

接下来，手动创建一个 COS 存储桶，用于存储容器 coredump 生成的 core 文件。

在 [对象存储页面](https://console.cloud.tencent.com/cos5/bucket) 操作:

![](https://main.qcloudimg.com/raw/d8190e5495757da27f729319c4981e4b.png)

>! 注意地域要与 TKE 集群所在地域相同

### 创建 Secret

在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 里拿到你的 SecretId 和 SecretKey，如果没有可以新建一个，然后开始创建 Secret。

如果使用 kubectl 命令行工具，可以这样做:

``` bash
kubectl create secret generic cos-secret -n kube-system  --from-literal=SecretId=AKI*****************lV --from-literal=SecretKey=paQ9***************sZF
```

如果用 TKE 控制台，可以点击右上角 【YAML 创建资源】，输入:

``` yaml
apiVersion: v1
kind: Secret
type: Opaque
metadata:
  name: cos-secret
  # Replaced by your secret namespace.
  namespace: kube-system
stringData:
  # 替换成你的 SecretId 和 SecretKey，不需要 base64 加密
  SecretId: AKI*****************lV
  SecretKey: paQ9***************sZF
```

>! 注意替换 SecretId 、 SecretKey 以及命名空间

### 创建 PV 和 PVC

目前 COS 插件只支持静态方式创建 PV，也就是需要手动创建 PV，然后再创建 PVC 并完成绑定。

首先创建 PV，在控制台点击 【存储】-【PersistentVolume】-【新建】:

![](https://main.qcloudimg.com/raw/a0537e5d6d558a3861a205e84b9add84.png)

有几点需要注意:

* **来源设置** 固定为静态创建，因为目前还不支持动态创建。
* **Secret** 选择上一步中创建的 (kube-system 命名空间下)。
* **存储桶列表** 选中前面创建的用于存储 coredump 文件的存储桶。
* **存储桶子目录** 这里指定的根目录，如果需要指定子目录，请提前在存储桶中创建好。

最后点击 【创建PersistentVolume】即可完成创建，接下来创建 PVC，在控制台点击 【存储】-【PersistentVolumeClaim】-【新建】:

![](https://main.qcloudimg.com/raw/c3fd441fcbb9516091114925d91f59fd.png)

有几点需要注意:

* **命名空间** 要与需要挂载存储 COS 的 PVC 的容器所在命名空间相同，如果有多个命名空间都需要，可以创建多对 PV 与 PVC。
* **PersistentVolume** 选择前面创建好的 PV 的名称。

最后点击 【创建PersistentVolumeClaim】即可完成创建。

### 挂载 COS 存储

如果用 TKE 控制台创建工作负载，可参考下图挂载 PVC:

![](https://main.qcloudimg.com/raw/f63720106568c9eff4a263e4572ae9d9.png)

* **数据卷** 添加一个前面创建的 PVC。
* **挂载点** 添加一个，引用 **数据卷** 中声明的 PVC，挂载到 `/tmp/cores` 路径下。

如果使用 YAML创建，可参考下面的片段:

``` yaml
  containers:
  - name: pod-cos
    command: ["tail", "-f", "/etc/hosts"]
    image: "centos:latest"
    volumeMounts:
    - mountPath: /tmp/cores
      name: core
  volumes:
  - name: core
    persistentVolumeClaim:
      # Replaced by your pvc name.
      claimName: coredump
```

## 参考资料

* [使用对象存储 COS](https://cloud.tencent.com/document/product/457/44232)