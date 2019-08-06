当前仅支持 CBS 类型的 PV&PVC。

## 静态创建 CBS 类型 PV&PVC
### 1. 创建 PV（可选）
通过已有 CBS 创建 PV。若未通过本步骤创建 PV，直接执行步骤2时，创建 PVC 将自动创建对应的 PV。
```
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

### 2. 创建 PVC
创建命令如下：
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
- 普通云盘大小必须是10的倍数，最小为10，最大为4000。
- 高效云盘最小为50GB。
- SSD 云硬盘最小为200GB，具体策略见 [云硬盘文档](https://cloud.tencent.com/document/product/362)。

### 3. 使用 PVC
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

## 动态创建 CBS 类型 PV&PVC
### 1. 创建 StorageClass
如果不创建 StorageClass， 集群内将默认存在 name 为 CBS 的 StorageClass。
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  # annotations:
  #   storageclass.beta.kubernetes.io/is-default-class: "true"
  #   如果有这一条，则会成为 default-class，创建 PVC 时不指定类型则自动使用此类型
  name: cloud-premium
provisioner: cloud.tencent.com/qcloud-cbs ## TKE 集群自带的 provisioner
parameters:
  type: CLOUD_PREMIUM
  # 支持 CLOUD_BASIC,CLOUD_PREMIUM,CLOUD_SSD  如果不识别则当做 CLOUD_BASIC，注意全大写
  # paymode: PREPAID
  # paymode为云盘的计费模式，PREPAID模式（包年包月：仅支持Retain保留的回收策略），默认是 POSTPAID（按量计费：支持 Retain 保留和 Delete 删除策略，Retain 仅在高于1.8的集群版本生效）
  # aspid:asp-123
  # 支持指定快照策略，创建云盘后自动绑定此快照策略,绑定失败不影响创建
```

### 2. 创建多实例 StatefulSet
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
