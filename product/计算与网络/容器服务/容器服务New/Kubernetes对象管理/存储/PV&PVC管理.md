## PV&PVC管理
### PV&PVC简介
PersistentVolume（PV）：集群内的存储资源， 如节点是集群的资源， PV独立于Pod的生命周期，根据不同的StorageClass类型创建不同类型的PV。
PersistentVolumeClaim（PVC）：集群内的存储请求，如果把PV比作Pod使用节点资源, PVC声明使用PV资源, PV资源不足时，PVC也可以动态创建PV。

#### 注意事项
1. CBS盘不支持跨可用区挂载， 故若挂载了CBS类型PV的Pod迁移到其他可用区会导致挂载失败。
2. TKE控制台不支持CBS盘扩缩容，请自行前往CBS控制台执行操作。


### PV&PVC 控制台操作指引
#### 静态创建PV
静态创建PV试用于已有存量云盘希望在集群内复用的场景。
1. 点击需要创建 PersistentVolume 的集群ID，进入集群详情页面。
2. 点击 PersistentVolume 选项，选择新建 PersistentVolume
3. 根据指引设置 PersistentVolume 参数，完成创建。


![][createPersistentVolume]

#### 创建pvc
1. 点击需要创建 PersistentVolumeClaim 的集群ID，进入集群详情页面。
2. 点击 PersistentVolumeClaim 选项，选择新建 PersistentVolumeClaim
3. 根据指引设置 PersistentVolumeClaim 参数，完成创建。
4. 在使用PVC时，若已有PV不足，将自动创建新的PV。


![][createPersistentVolumeClaim]

#### 创建Workload使用PVC数据卷
1. 点击需要部署 workloads 的集群ID，进入集群详情页面。
2. 点击 任意workloads类型 ，选择新建。
3. 根据指引设置数据卷参数为使用已有PersistentVolumeClaim,并填写其他参数，配置挂载点，完成创建。


![][MountVolume]


### kubectl 操作 PV&PVC 指引
当前仅支持 CBS 类型的 PV&PVC， 敬请期待 CFS 和 COS 存储类型支持。可通过[StorageClass]()指定PV绑定的云盘的类型。 以下仅提供示例文件，可直接通过Kubectl 进行创建操作。
#### 1. 创建 PV（可选）
通过已有 CBS 创建 PV。若未通过本步骤创建 PV，直接执行步骤 2 时，创建 PVC 将自动创建对应的 PV。
```Yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nginx-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteOnce
  qcloudCbs:
      cbsDiskId: disk-xxxxxxx ## 指定已有的CBS id
      fsType: ext4
  storageClassName: cbs
```

#### 2. 创建 PVC
示例如下：
```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: nginx-pv-claim
spec:
  storageClassName: cbs
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
```
- 普通云盘大小必须是 10 的倍数，最小为 10。
- 高效云盘最小为 50 GB。
- SSD 云硬盘最小为 200 GB，具体策略见 [云硬盘文档](https://cloud.tencent.com/document/product/362)。

#### 3. 使用 PVC
```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      qcloud-app: nginx-deployment
  template:
    metadata:
      labels:
        qcloud-app: nginx-deployment
    spec:
      containers:
      - image: nginx
        imagePullPolicy: Always
        name: nginx
        volumeMounts:
        - mountPath: "/opt/"
          name: pvc-test
      volumes:
      - name: pvc-test
        persistentVolumeClaim:
          claimName: nginx-pv-claim # 已经创建好的pvc
```


[createPersistentVolume]:https://main.qcloudimg.com/raw/7bcc6e2668c1f57f3abbc06b5c79da4d.png
[createPersistentVolumeClaim]:https://main.qcloudimg.com/raw/26f206e24d70852c68c0c5df1af04d1c.png
[MountVolume]:https://main.qcloudimg.com/raw/824f75660d02086f89e97d3a557d6248.png
