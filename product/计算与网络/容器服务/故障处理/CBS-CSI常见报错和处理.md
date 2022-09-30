
## cbs 盘创建相关问题

###  1. no available storage in zone
**现象：**kubectl describe pvc 发现类型为 ProvisioningFailed 的事件，内容包含 `no available storage in zone`。
**原因：**资源售罄或者该 zone 不支持这种类型的 cbs 盘。
**解决措施：**用户可切换到有资源的 region/zone，或联系 cbs 售后提供资源。

###  2. disk is sold out
**现象：**cbs 插件报错 `disk is sold out`。
**原因：**cbs 磁盘售罄。
**解决措施：**联系 cbs 售后上架资源后重建 Pod。

###  3. InvalidParameter
**现象 1：**pvc 一直处于 pending 状态，pv 无法被创建出来，插件报错 `Key start with a word that is reserved for the system`。
**原因：**cbs 插件在创建云硬盘时，会将集群的云标签集成到云硬盘上。而当云标签 key 中带有 qcloud. tencent 或 project 字段时，会导致云硬盘创建失败。
**解决措施：**修改相关集群云标签，避免在标签 key 中出现 qcloud. tencent 或 project 字段。
```
[TencentCloudSDKError] Code=InvalidParameter, Message=(16ab33025ebd)Key (tencentCloudPorject) start with a word that is reserved for the system
```

**现象 2：**pvc 一直处于 pending 状态，pv 无法被创建出来，插件报错 `tag value contains illegal characters`。
**原因：**cbs 插件在创建云硬盘时，会将集群的云标签继承到云硬盘上。当云标签 value 为空值时，会导致云硬盘创建失败。
**解决措施：**修改相关集群云标签，避免将标签 value 配置为空。

```
[TencentCloudSDKError] Code=InvalidParameter, Message=(ec82d0f8807c)tag value contains illegal characters. Supports UTF-8-encoded characters, digits, spaces, and special characters (+-=._:/@()[]（）【】),
```

 ###  4. disk size is invalid
**现象：** describe pvc 或查看插件日志可以看到报错 `disk size is invalid`。
**原因：**用户配置的 cbs 盘大小不符合规范导致买盘失败，不同类型的 cbs 盘，支持大小区间不同，具体查看 [云硬盘类型文档](https://cloud.tencent.com/document/product/362/2353)。
**解决措施：**修改 pvc 容量大小，使其处于 cbs 支持区间范围内。

### 5. WaitForFirstConsumer 挂载模式下创盘失败
**现象：**StorageClass 中选择 WaitForFirstConsumer 的挂载模式，在 workload 中配置了 nodeName 参数，上述情况下会创盘失败。
**原因：**WaitForFirstConsumer 挂载模式依赖调度器触发云硬盘创建，而指定了 nodeName 参数会导致 Pod 在调度时跳过调度器，从而无法通知插件进行云硬盘创建。
**解决措施：**使用 nodeSelector 方式替换 nodeName 参数，或在 sc 中直接指定 Immediate 的挂载模式，如有需要也可以在 sc 参数中指定可用区。
   
### 6. 服务端返回 InternalError
**现象：**插件报错 `InternalError` 。
**原因：**一般为 cbs 服务端问题。
**解决措施：**联系 cbs 售后确定是否 cbs 服务问题，待恢复后即可正常买盘。

```
[TencentCioudSDKError] Code=InternalError, Message=内部服务错误，请稍后重试。
```

### 7. 服务端返回 UnauthorizedOperation.NotHavePaymentRight
**现象：**创建包年包月云硬盘失败，插件报错 `UnauthorizedOperation.NotHavePaymentRight`。
**原因：**TKE_QCSRole 角色没有关联策略 QcloudCVMFinanceAccess。
**解决措施：**请参考 [指引文档](https://cloud.tencent.com/document/product/457/43416#.E9.A2.84.E8.AE.BE.E7.AD.96.E7.95.A5-qcloudcvmfinanceaccess.3Ca-id.3D.22qcloudcvmfinanceaccess.22.3E.3C.2Fa.3E) 给角色关联策略添加权限。

## cbs 盘 attach 相关问题
#### 基本概念
**attach**：将 cbs 盘关联到 Pod 将被调度运行的 node 上面。

### 1. 黑石机器 attach 失败
**原因：**黑石机器默认不支持挂载 cbs 盘。

### 2. attach 云盘太慢（超过 10 分钟）
**现象：**pvc/pv 对象创建都比较及时，但是 volumeattachment 对象的创建延迟了6分钟甚至更近，导致 csi 组件 attach 也延迟。查看 kcm 日志，发现请求延迟很大。
**原因：**kcm 每一分钟就全量 Get 所有的 volumeattachment，当集群内 volumeattachment 对象数较多时会触发请求限频。
**解决措施：**让 kcm 全量 Get 所有 volumeattachment 的时间间隔变长，避免被限频，可申请修改 kcm 相关参数。

### 3. exceed max volume count
**现象：**业务 Pod 处于 Pending 状态，无法完成调度，Describe Pod 有告警 `node(s) exceed max volume count`
**原因：**单个 CVM 默认只支持 attach 20 块云硬盘，cbs 组件在除去系统盘和数据盘后，默认只支持再挂载 18 块云硬盘。

## cbs 盘 mount 相关问题

### 1. 插件注册到 kubelet 失败
**现象：**Describe Pod 或在 kubelet 日志中有如下报错。

```
MountVolume.MountDevice，driver name com.tencent.cloud.csi.cbs not found in the list of registered CSI drivers
```
**原因：**
1. 用户删除了集群中的 cbs 组件。
2. kubelet 的 rootdir 变更了，默认值为 /var/lib/kubelet。
3. csi-cbs-node 获取节点 instanceid 为空。

**排查思路：**
1. 登录集群，通过 `kubectl get pod -nkube-system |grep cbs` 查看是否已安装 cbs 组件。
2. 查看报错的 Pod 位置，登录节点，通过 `ps -ef |grep kubelet ` 查看 kubelet 进程有无 rootdir 参数，有且不为默认值，则为原因 2。
3. csi-cbs-node driver-registrar 容器日志中查看 driverNodeID must not be empty 报错信息。

**解决措施：**
1. 控制台安装 cbs 组件。
2. 控制台修改组件配置，将 rootdir 参数指定为正确的值。
3. 控制台升级 cbs 组件。

### 2. /dev/vd* is already mounted
**现象：**业务 Pod 挂载 cbs 失败，插件报错如下信息。

```
mount failed: exit status 32
Mounting command: mount
Mounting arguments: -t ext4 -o defaults /dev/vd* /var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-***/globalmount
Output: mount: /dev/vd* is already mounted or /var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-***/globalmount busy
```

**原因：**旧版本组件 globalmount 目录存在重复挂载问题。
**解决措施：**控制台升级 cbs 组件。

### 3. mounting failed: Invalid argument
**现象：**业务 Pod 挂载 cbs 失败，插件报错如下信息。

```
mount failed: exit status 255
Mounting command: mount
Mounting arguments: -t ext4 -o defaults /dev/vd* /var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-***/globalmount
Output: mount: mounting /dev/vd* on /var/lib/kubelet/plugins/kubernetes.io/csi/pv/pvc-***/globalmount failed: Invalid argument
```
**原因：**cbs 盘已格式化为 gpt 格式，无法通过 cbs 组件来挂载。
![](https://qcloudimg.tencent-cloud.cn/raw/2fdbe6dd6f3d1150a5d4c2100cd1c550.png)
**解决措施：**将盘直接格式化为 ext4，或通过 pvc 新建未格式化的云盘，并将业务 pod 指向新建的 pvc。

### 4. 业务 Pod 启动时间较长
**现象：**挂载 cbs 的业务 Pod 启动时间较长，kubelet 包含如下日志。

```
Setting volume ownership for %s and fsGroup set. If the volume has a lot of files then setting volume ownership could be slow, see https://github.com/kubernetes/kubernetes/issues/69699
```
**原因：**业务负载中指定了 fsGroup 参数，导致 kubelet 在完成 cbs 挂载后，会把挂载目录下所有文件进行一次权限修改，修改为 fsGroup 指定权限。若挂载目录下文件很多，kubelet 存储准备工作就会长时间卡在权限修改这一步，直到挂载目录下所有文件权限修改完成。
**解决措施：**
方案一：不指定 fsgroup 参数，用户需自行确保权限匹配。
方案二：在 Pod template 中配置 `spec.securityContext.fsGroupChangePolicy` 参数为 `OnRootMismatch`，只要目录下文件权限已匹配就不会去刷权限（集群版本需不小于 1.20）。
