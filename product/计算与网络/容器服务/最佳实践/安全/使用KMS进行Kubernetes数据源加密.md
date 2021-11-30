## 操作场景

[腾讯云 TKE-KMS 插件](https://github.com/Tencent/tke-kms-plugin) 集成密钥管理系统（Key Management Service，KMS）丰富的密钥管理功能，针对 Kubernetes 集群中 Secret 提供强大的加密/解密能力。本文介绍如何通过 KMS 对 Kubernetes 集群进行数据加密。

## 基本概念

#### 密钥管理系统 KMS
[密钥管理系统（Key Management Service，KMS）](https://cloud.tencent.com/document/product/573/8780)是一款安全管理类服务，使用经过第三方认证的硬件安全模块 HSM（Hardware Security Module） 来生成和保护密钥。帮助用户轻松创建和管理密钥，满足用户多应用多业务的密钥管理需求，符合监管和合规要求。

## 前提条件
已创建符合以下条件的容器服务**独立集群**：
- Kubernetes 版本为1.10.0及以上。
- Etcd 版本为3.0及以上。
>?如需检查版本，可前往  “[集群管理](https://console.cloud.tencent.com/tke2/cluster)” 页面，选择集群 ID 并进入集群“基本信息”页面进行查看。


## 操作步骤

### 创建 KMS 密钥并获取 ID[](id:createKMS)

1. 登录 [密钥管理系统（合规）](https://console.cloud.tencent.com/kms2) 控制台，进入“用户密钥”页面。
2. 在“用户密钥”页面上方，选择需要创建密钥的区域并单击**新建**。
3. 在弹出的“新建密钥”窗口，参考以下信息进行配置。如下图所示：
![](https://main.qcloudimg.com/raw/2082bac6e37c381f6d14e1717fa6e401.png)
主要参数信息如下，其余参数请保持默认设置：
 - **密钥名称**：必填且在区域内唯一，密钥名称只能为字母、数字及字符`_`和`-`，且不能以 `KMS-` 开头。本文以 `tke-kms` 为例。
 - **描述信息**：选填，可用来说明计划保护的数据类型或计划与 CMK 配合使用的应用程序。
 - **密钥用途**：选择“对称加解密”。
 - **密钥材料来源**：提供 “KMS” 和“外部”两种选择，请根据实际需求进行选择。本文以选择 “KMS” 为例。
4. 单击**确定**后返回“用户密钥”页面，即可查看已成功创建的密钥。
5. 单击密钥 ID，进入密钥信息页，记录该密钥完整 ID。如下图所示：
![](https://main.qcloudimg.com/raw/ab708d6ade0bdd9dd12cd54e2cea35d9.png)

### 创建并获取访问密钥[](id:createCAM)
>?如已创建访问密钥，则请跳过此步骤。
>
1. 登录[ 访问管理控制台](https://console.cloud.tencent.com/cam/overview)，选择左侧导航栏中的**访问密钥** > **API密钥管理**，进入 “API密钥管理”页面。
2. 在 “API密钥管理”页面中，单击**新建密钥**并等待创建完成。
3. 创建完成即可在 “API密钥管理”页面查看该密钥信息，包含 `SecretId`、`SecretKey`。如下图所示：
![](https://main.qcloudimg.com/raw/106be1fd3e9f52f0d112b7f583b2d7df.png)

### 创建 DaemonSet 并部署 tke-kms-plugin

1. 登录[ 腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中**集群**。
2. 在“集群管理”页面中，选择符合条件的集群 ID，进入该集群详情页。
3. 选择该集群任意界面右上角**YAML创建资源**，进入 YAML 创建资源页，输入 `tke-kms-plugin.yaml` 内容。如下所示：
> ? 请根据实际情况替换以下参数：
> - `{{REGION}}`：KMS 密钥所在地域，有效值可参见 [地域列表](https://cloud.tencent.com/document/api/573/34406#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
> - `{{KEY_ID}}`：输入 [创建 KMS 密钥并获取 ID](#createKMS) 步骤中所获取的 KMS 密钥 ID。
> - `{{SECRET_ID}}` 和 `{{SECRET_KEY}}`：输入 [创建并获取访问密钥](#createCAM) 步骤中创建的 SecretID 和 SecretKey。
> - `images: ccr.ccs.tencentyun.com/tke-plugin/tke-kms-plugin:1.0.0`：tke-kms-plugin 镜像地址。当您需要使用自己制作的 tke-kms-plugin 镜像时，可自行进行更换。
> 
```
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: tke-kms-plugin
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: tke-kms-plugin
  template:
    metadata:
      labels:
        name: tke-kms-plugin
    spec:
      nodeSelector:
        node-role.kubernetes.io/master: "true"
      hostNetwork: true
      restartPolicy: Always
      volumes:
        - name: tke-kms-plugin-dir
          hostPath:
            path: /var/run/tke-kms-plugin
            type: DirectoryOrCreate
      tolerations:
        - key: node-role.kubernetes.io/master
          effect: NoSchedule
      containers:
        - name: tke-kms-plugin
          image: ccr.ccs.tencentyun.com/tke-plugin/tke-kms-plugin:1.0.0
          command:
            - /tke-kms-plugin
            - --region={{REGION}}
            - --key-id={{KEY_ID}}
            - --unix-socket=/var/run/tke-kms-plugin/server.sock
            - --v=2
          livenessProbe:
            exec:
              command:
                - /tke-kms-plugin
                - health-check
                - --unix-socket=/var/run/tke-kms-plugin/server.sock
            initialDelaySeconds: 5
            failureThreshold: 3
            timeoutSeconds: 5
            periodSeconds: 30
          env:
            - name: SECRET_ID
              value: {{SECRET_ID}}
            - name: SECRET_KEY
              value: {{SECRET_KEY}}
          volumeMounts:
            - name: tke-kms-plugin-dir
              mountPath: /var/run/tke-kms-plugin
              readOnly: false
```
4. 单击**完成**并等待 DaemonSet 创建成功即可。

### 配置 kube-apiserver
1. 参考 [使用标准方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，分别登录该集群每一个 Master 节点。
>?Master 节点安全组默认关闭22端口，执行登录节点操作前请首先前往其安全组界面打开22端口。详情请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。
>
2. 执行以下命令，新建并打开该 YAML 文件。
```
vim /etc/kubernetes/encryption-provider-config.yaml
```
3. 按 **i** 切换至编辑模式，对上述 YAML 文件进行编辑。对应实际使用的 K8S 版本，输入如下内容：
 -  K8S v1.13+：
```
   apiVersion: apiserver.config.k8s.io/v1
   kind: EncryptionConfiguration
   resources:
     - resources:
         - secrets
       providers:
         - kms:
             name: tke-kms-plugin
             timeout: 3s
             cachesize: 1000
             endpoint: unix:///var/run/tke-kms-plugin/server.sock
         - identity: {}
```
 - K8S v1.10 - v1.12：
```
   apiVersion: v1
   kind: EncryptionConfig
   resources:
     - resources:
         - secrets
       providers:
         - kms:
             name: tke-kms-plugin
             timeout: 3s
             cachesize: 1000
             endpoint: unix:///var/run/tke-kms-plugin/server.sock
         - identity: {}
```
4. 编辑完成后，按 **Esc**，输入 **:wq**，保存文件并返回。
5. 执行以下命令，对该 YAML 文件进行编辑。
```
vi /etc/kubernetes/manifests/kube-apiserver.yaml
```
6. 按 **i** 切换至编辑模式，对应实际使用的 K8S 版本，将以下内容添加至 `args`。
>?K8S v1.10.5 版本的独立集群，需要先将 `kube-apiserver.yaml`  移出 `/etc/kubernetes/manifests` 目录，编辑完成之后再移入。
>
 - K8S v1.13+：
```
 --encryption-provider-config=/etc/kubernetes/encryption-provider-config.yaml
```
 - K8S v1.10 - v1.12：
```
--experimental-encryption-provider-config=/etc/kubernetes/encryption-provider-config.yaml
```
7. 为 `/var/run/tke-kms-plugin/server.sock` 添加 Volume 指令，其中添加位置及内容如下所示：
> ?`/var/run/tke-kms-plugin/server.sock` 是 tke kms server 启动时监听的一个 unix socket，kube apiserver 会通过访问该 socket 来访问 tke kms server。
> 
 为 `volumeMounts:` 添加以下内容：
```
   - mountPath: /var/run/tke-kms-plugin
     name: tke-kms-plugin-dir
```
 为 `volume:` 添加以下内容：
```
   - hostPath:
       path: /var/run/tke-kms-plugin
     name: tke-kms-plugin-dir
```
8. 编辑完成后，按 **Esc**，输入 **:wq**，保存 `/etc/kubernetes/manifests/kube-apiserver.yaml` 文件，等待 kube-apiserver 重启完成。

### 验证

1. 登录该集群 Node 节点，执行以下命令新建 Secret。
```
kubectl create secret generic kms-secret -n default --from-literal=mykey=mydata
```
2. 执行以下命令，验证 Secret 是否已正确解密。
```
kubectl get secret kms-secret -o=jsonpath='{.data.mykey}' | base64 -d
```
3. 输出若为 `mydata`，即与创建 Secret 的值相同，则表示 Secret 已正确解密。如下图所示：
![](https://main.qcloudimg.com/raw/7d8980d32ee2b48cc30948152246fc29.png)

## 参考资料

有关 Kubernetes KMS 的更多信息，请参阅 [使用 KMS 提供程序进行数据加密](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)。
