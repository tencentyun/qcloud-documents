## StorageClass管理
### StorageClass 简介
StorageClass 描述了存储的类型，集群管理员可以为集群定义不同的存储类别，腾讯云TKE服务默认提供了块存储类型的StorageClass， 通过 StorageClass 配合 PersistentVolumeClaim 可以动态创建需要的存储资源。

### StorageClass 控制台操作指引
#### 创建 StorageClass
1. 点击需要创建 StorageClass 的集群ID，进入集群详情页面。
2. 点击 StorageClass 选项，选择新建 StorageClass
3. 根据指引设置 StorageClass 参数，完成创建。

![][createStorageClasse]

#### 创建PVC指定StorageClass
1. 点击需要创建 PersistentVolumeClaim 的集群ID，进入集群详情页面。
2. 点击 PersistentVolumeClaim 选项，选择新建 PersistentVolumeClaim
3. 根据指引设置 PersistentVolumeClaim StorageClass 和其他参数，完成创建。

![][createPersistentVolumeClaim]
#### 创建 StatefulSet 挂载自动创建PersistentVolumeClaim类型
1. 点击需要部署 StatefulSet 的集群ID，进入集群详情页面。
2. 点击 任意 StatefulSet 类型 ，选择新建。
3. 根据指引设置数据卷参数为使用新建PersistentVolumeClaim,并填写其他参数，配置挂载点，完成创建。

![][MountVolume]


### kubectl 操作 StorageClass 指引
以下仅提供示例文件，可直接通过Kubectl 进行创建操作。
#### 1. 创建 StorageClass

如果不创建 StorageClass， 集群内将默认存在 name 为 cbs 的 StorageClass。
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  # annotations:
  #   storageclass.beta.kubernetes.io/is-default-class: "true"
  #   如果有这一条，则会成为default-class，创建pvc时不指定类型则自动使用此类型
  name: cloud-premium
provisioner: cloud.tencent.com/qcloud-cbs ##tke集群自带的provisioner
parameters:
  type: CLOUD_PREMIUM
  # 支持 CLOUD_BASIC,CLOUD_PREMIUM,CLOUD_SSD  如果不识别则当做cloudBasic
  # zone:ap-shanghai-1
  # zone 支持指定zone，如果指定，则讲云盘创建到此zone，如果不指定，则拉取所有node的zone信息，随机挑选一个
  # paymode: PREPAID
  # paymode为云盘的计费模式，PREPAID模式（包年包月：仅支持Retain保留的回收策略），默认是POSTPAID（按量计费：支持Retain保留和Delete删除策略，Retain仅在高于1.8的集群版本生效）
  # aspid:asp-123
  # 支持指定快照策略，创建云盘后自动绑定此快照策略,绑定失败不影响创建

```
支持参数有：
- type：CLOUD_BASIC,CLOUD_PREMIUM,CLOUD_SSD
- zone: 支持指定zone，如果指定，则讲云盘创建到此zone，如果不指定，则拉取所有node的zone信息，随机挑选一个。 腾讯云个地域标识符  https://cloud.tencent.com/document/product/213/6091
- paymode:paymode为云盘的计费模式，PREPAID模式（包年包月：仅支持Retain保留的回收策略），默认是POSTPAID（按量计费：支持Retain保留和Delete删除策略，Retain仅在高于1.8的集群版本生效）
- aspid:支持指定快照ID，创建云盘后自动绑定此快照策略,绑定失败不影响创建

##### 2. 创建多实例 StatefulSet
使用云硬盘 CBS 创建多实例 StatefulSet：
``` yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:  # 自动创建pvc，进而自动创建pv
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      storageClassName: cloud-premium
      resources:
        requests:
          storage: 10Gi
```
[createStorageClasse]:https://main.qcloudimg.com/raw/f58ff199292aff6da3e95089271baa57.png
[createPersistentVolumeClaim]:https://main.qcloudimg.com/raw/3584c1853de78023225c208e7ba2a7dd.png
[MountVolume]:https://main.qcloudimg.com/raw/824f75660d02086f89e97d3a557d6248.png
