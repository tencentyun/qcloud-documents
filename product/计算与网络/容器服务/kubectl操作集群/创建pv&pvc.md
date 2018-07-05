## 创建pv&pvc
当前仅支持CBS类型的PV&PVC， 敬请期待CFS和COS存储类型支持。
### 静态创建CBS类型PV
#### 第一步：通过已有CBS创建PV (可选)
若未通过本步骤创建PV,直接执行第二步将PVC自动创建对应的PV。
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

#### 第二步：创建PVC

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


# 普通云盘大小必须是10的倍数，最小为10，最大为4000
# 高效云盘最小为50G
# SSD云硬盘最小为200GB，具体策略见cbs文档

```

#### 使用PVC
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


### 动态创建CBS盘
#### 第一步：创建StorageClass
如果不创建StorageClass， 集群内默认存在name为cbs的StorageClass。

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  # annotations:
  #   storageclass.beta.kubernetes.io/is-default-class: "true"  
  #   如果有这一条，则会成为default-class，创建pvc时不指定类型则自动使用此类型
  name: cloud-premium
provisioner: cloud.tencent.com/qcloud-cbs
parameters:
  type: cloudPremium
  # 支持 cloudBasic,cloudPremium,cloudSSD  如果不识别则当做cloudBasic
  # zone:ap-shanghai-1
  # zone 支持指定zone，如果指定，则讲云盘创建到此zone，如果不指定，则拉取所有node的zone信息，随机挑选一个
  # aspid:asp-123
  # 支持指定快照策略，创建云盘后自动绑定此快照策略,绑定失败不影响创建
  
```


#### 使用腾讯云盘创建多实例StatefulSet
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

