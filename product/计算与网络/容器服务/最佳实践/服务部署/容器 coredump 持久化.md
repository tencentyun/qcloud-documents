## 操作场景
容器有时会在发生异常后挂掉，业务日志中若无足够的信息来定位挂掉的原因，则需要结合 coredump 来进一步分析，本文将介绍如何使容器产生 coredump 并保存。

>! 本文仅适用于容器服务 TKE 集群。

## 前提条件 
已登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。

## 操作步骤
### 开启 coredump
1. 执行以下命令，为节点设置 core 文件的存放路径格式：
``` bash
# 在节点上执行
echo "/tmp/cores/core.%h.%e.%p.%t" > /proc/sys/kernel/core_pattern
``` 
主要参数信息如下：
**%h**：主机名（在 Pod 内主机名即 Pod 的名称），推荐。
**%e**：程序文件名，推荐。
**%p**：进程 ID，可选。
**%t**：coredump 的时间，可选。
最终生成的 core 文件完整路径如下所示：
```
/tmp/cores/core.nginx-7855fc5b44-p2rzt.bash.36.1602488967
```
2. 节点上执行后，容器无需更改配置，将自动生效（继承），如果需要在多个节点上批量执行，则分为以下两种情况：
 - 对于存量节点，请参见 [使用 Ansible 批量操作 TKE 节点](https://cloud.tencent.com/document/product/457/48973)。
 - 对于增量节点，请参见 [设置节点的启动脚本](https://cloud.tencent.com/document/product/457/32206)。

### 启用 COS 扩展组件
为了避免容器重启后丢失 core 文件，需要为容器挂载 volume。由于为每个 Pod 单独挂载云盘的成本太高，所以将组件挂载至 COS 对象存储。具体操作步骤请参见 [安装 COS 扩展组件](https://cloud.tencent.com/document/product/457/40934#.E5.AE.89.E8.A3.85-cos-.E6.89.A9.E5.B1.95.E7.BB.84.E4.BB.B6)。

### 创建存储桶

登录 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket)，手动创建 COS 存储桶，用于存储容器 coredump 生成的 core 文件。具体操作步骤请参见 [创建存储桶](https://cloud.tencent.com/document/product/457/44232#.E5.88.9B.E5.BB.BA.E5.AD.98.E5.82.A8.E6.A1.B6.3Cspan-id.3D.22creatbucket.22.3E.3C.2Fspan.3E)。如下图所示：
![](https://main.qcloudimg.com/raw/a981dcd8f35dcd94f7e20ea8f67a0a6d.png)


### 创建 Secret<span id="secret"></span>
- 若通过控制台使用对象存储，可参见 [创建可以访问对象存储的 Secret](https://cloud.tencent.com/document/product/457/44232#.E9.80.9A.E8.BF.87.E6.8E.A7.E5.88.B6.E5.8F.B0.E4.BD.BF.E7.94.A8.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8)。
- 若通过 YAML 文件使用对象存储，可参见 [创建可以访问对象存储的 Secret](https://cloud.tencent.com/document/product/457/44232#.E9.80.9A.E8.BF.87-yaml-.E6.96.87.E4.BB.B6.E4.BD.BF.E7.94.A8.E5.AF.B9.E8.B1.A1.E5.AD.98.E5.82.A8)。
- 若使用 kubectl 命令行工具创建 Secret，可参考以下代码片段：
``` bash
kubectl create secret generic cos-secret -n kube-system  --from-literal=SecretId=AKI*****************lV --from-literal=SecretKey=paQ9***************sZF
```
>! 注意替换 SecretId、SecretKey 以及命名空间。

### 创建 PV 和 PVC

使用 COS 插件需要手动创建 PV 和创建 PVC，并完成绑定。
#### 创建 PV<span id="pv"></span>
1. 在目标集群详情页面，选择左侧菜单栏中的【存储】>【PersistentVolume】，进入 “PersistentVolume” 页面。
2. 单击【新建】进入“新建PersistentVolume” 页面，参考以下信息创建 PV。如下图所示：
![](https://main.qcloudimg.com/raw/d2301b77ad197f86f9131656d5e5339b.png)
主要参数信息如下：
 - **来源设置**：选择【静态创建】。
 - **Secret**：选择已在 [创建 Secret](#secret) 中创建的 Secret，本文以 cos-secret 为例（kube-system 命名空间下）。
 - **存储桶列表**：选中已创建的用于存储 coredump 文件的存储桶。
 - **存储桶子目录**：此处指定根目录，如果需要指定子目录，请提前在存储桶中创建。
3. 单击【创建PersistentVolume】即可。


#### 创建 PVC<span id="pvc"></span>
1. 在目标集群详情页，选择左侧菜单栏中的【存储】>【PersistentVolumeClaim】，进入 “PersistentVolumeClaim” 页面。
2. 单击【新建】进入“新建PersistentVolumeClaim” 页面，参考以下信息创建 PVC。如下图所示：
![](https://main.qcloudimg.com/raw/b8e1a09f37a34264a8b251c0362d43a8.png)
主要参数信息如下：
 - **命名空间**：要与需要挂载存储 COS 的 PVC 的容器所在命名空间相同，如果有多个命名空间，可以创建多对 PV 与 PVC。
 - **PersistentVolume**：选择在 [创建 PV](#pv) 中已创建的 PV 的名称。
3. 单击【创建PersistentVolumeClaim】即可。


### 挂载 COS 存储
#### 通过控制台创建 Pod 使用 PVC
1. 在目标集群详情页，选择左侧菜单栏中的【工作负载】>【Deployment】，进入 “Deployment” 页面。
2. 单击【新建】进入“新建Workload” 页面，参考 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 进行创建，并设置数据卷挂载。如下图所示：
![](https://main.qcloudimg.com/raw/f63720106568c9eff4a263e4572ae9d9.png)
主要参数信息如下：
 - **数据卷**：添加在 [创建 PVC](#pvc) 中已创建的 PVC。
 - **挂载点**：单击【添加挂载点】，进行挂载点设置。选择为该步骤中所添加的数据卷 “core”。引用**数据卷**中声明的 PVC，挂载至目标路径，本文以 `/tmp/cores` 为例。
3. 单击【创建Workload】即可。


#### 通过 YAML 创建 Pod 使用 PVC
通过 YAML 创建 Pod，模版如下：
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

## 相关文档

- [使用对象存储 COS](https://cloud.tencent.com/document/product/457/44232)
