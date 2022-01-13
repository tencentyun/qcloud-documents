## 使用场景

为 EKS 集群挂载文件存储（Cloud File Storage，CFS）Turbo 类型存储，该组件基于私有协议将腾讯云 CFS Turbo 文件系统挂载到工作负载，目前仅支持静态配置。CFS 存储类型详情见 [文件存储类型及性能规格](https://cloud.tencent.com/document/product/582/38112)。

## 前提条件

已创建 EKS 集群且集群版本 >=1.14。

## 使用步骤 

### 创建文件系统

创建 CFS Turbo 文件系统，具体操作请参见 [创建文件系统](https://cloud.tencent.com/document/product/582/9132)。

>! 文件系统创建后，需将集群网络（vpc-xx）关联到文件系统的 [云联网](https://cloud.tencent.com/document/product/877/18747)（可在文件系统挂载点信息中查看）。
>

### 部署 Node Plugin

#### 步骤1：新建 csidriver.yaml 文件
csidriver.yaml 文件示例如下：
```yaml
apiVersion: storage.k8s.io/v1beta1
kind: CSIDriver
metadata:
  name: com.tencent.cloud.csi.cfsturbo
spec:
  attachRequired: false
  podInfoOnMount: false
```

#### 步骤2：创建 csidriver
执行以下命令创建 csidriver：
```sh
kubectl apply -f csidriver.yaml
```

### 创建 CFS Turbo 存储卷

#### 步骤1：使用以下模板创建 CFS Turbo 类型 PV[](id:step1)

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-cfsturbo
spec:
  accessModes:
  - ReadWriteMany
  capacity:
    storage: 10Gi
  csi:
    driver: com.tencent.cloud.csi.cfsturbo
    volumeHandle: pv-cfsturbo
    volumeAttributes: 
      host: *.*.*.*
      fsid: ********
  storageClassName: ""
```

参数说明：  
- **metadata.name**：创建 PV 名称。
- **spec.csi.volumeHandle**：与 PV 名称保持一致。  
- **spec.csi.volumeAttributes.host**：文件系统 ip 地址，可在文件系统挂载点信息中查看。  
- **spec.csi.volumeAttributes.fsid**：文件系统 fsid（非文件系统 id），可在文件系统挂载点信息中查看（挂载命令中 "tcp0:/" 与 "/cfs" 之间的字符串，如下图）。
![](https://qcloudimg.tencent-cloud.cn/raw/56b46e1e64fb2531f313da0a61485097.png)

#### 步骤2：使用以下模板创建 PVC 绑定 PV

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-cfsturbo
spec:
  storageClassName: ""
  volumeName: pv-cfsturbo
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Gi
```

参数说明：  
- **metadata.name**：创建 PVC 名称。
- **spec.volumeName**：与 [步骤1](#step1) 中创建 PV 名称保持一致。

### 使用 CFS Turbo 存储卷

使用以下模板创建 Pod 挂载 PVC。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx 
spec:
  containers:
  - image: ccr.ccs.tencentyun.com/qcloud/nginx:1.9
    imagePullPolicy: Always
    name: nginx
    ports:
    - containerPort: 80
      protocol: TCP
    volumeMounts:
      - mountPath: /var/www
        name: data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: pvc-cfsturbo
```

