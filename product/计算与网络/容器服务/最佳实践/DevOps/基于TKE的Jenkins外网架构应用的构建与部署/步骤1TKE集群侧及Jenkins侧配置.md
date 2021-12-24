## TKE 集群侧配置

此步骤中介绍了通过在 [TKE 中自定义 RBAC 授权](https://cloud.tencent.com/document/product/457/51683) ServiceAccount ，以及获取配置 Jenkins 时所需的集群访问地址、token 及集群 CA 证书信息。

### 获取集群凭证[](id:proof)
>? 当前集群需要开启内网访问。详情见 [Service 控制台操作指引](https://cloud.tencent.com/document/product/457/45489#service-.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.93.8D.E4.BD.9C.E6.8C.87.E5.BC.95)。
>
1. 使用以下 Shell 脚本，创建测试命名空间 ci、ServiceAccount 类型的测试用户 jenkins 并获取集群访问凭证（token）认证。
```
# 创建测试命名空间ci
kubectl create namespace ci
# 创建测试 ServiceAccount 账户
kubectl create sa jenkins -n ci
# 获取 ServiceAccount 账户自动创建的 Secret token
kubectl get secret $(kubectl get sa jenkins -n ci -o jsonpath={.secrets[0].name}) -n ci -o jsonpath={.data.token} | base64 --decode
```

2. 在测试命名空间 ci 创建一个 Role 权限对象资源 jenkins-role.yaml 文件。示例如下：
```
kind: Role
apiVersion: rbac.authorization.k8s.io/v1beta1
metadata:
  name: jenkins
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["create","delete","get","list","patch","update","watch"]
- apiGroups: [""]
  resources: ["pods/exec"]
  verbs: ["create","delete","get","list","patch","update","watch"]
- apiGroups: [""]
  resources: ["pods/log"]
  verbs: ["get","list","watch"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get"]
```

3. 创建一个 RoleBinding 对象资源 jenkins-rolebinding.yaml 文件。如下权限绑定表示，添加 ServiceAccount 类型的 jenkins 用户在ci 命名空间具有 jenkins（Role 类型）的权限。示例如下：
```
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: RoleBinding
metadata:
  name: jenkins
  namespace: ci
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: jenkins
subjects:
- kind: ServiceAccount
  name: jenkins
```



### 获取集群 CA 证书[](id:getCA)
1. 参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录目标集群的 node 节点。
2. 执行以下命令，查看集群 CA 证书。
```
cat /etc/kubernetes/cluster-ca.crt
```
3. 请记录并保存查询所得证书信息。如下图所示：
![](https://main.qcloudimg.com/raw/9431bdeb070e4e2e382bf6ea628b1842.png)

### 授权 docker.sock 

TKE 集群中的每个 node 节点系统里都有一个 `docker.sock` 文件，slave pod 在执行 `docker build` 时将会连接该文件。在此之前，需逐个登录到每个节点上，依次执行以下命令对 `docker build` 进行授权：
```
chmod 666 /var/run/docker.sock
```
```
ls -l /var/run/docker.sock
```


## Jenkins 侧配置

### 添加 TKE 内网访问地址

1. 参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录 Jenkins Master 节点。
2. 执行以下命令，配置访问域名。
```
sudo sed -i '$a 10.x.x.x cls-ixxxelli.ccs.tencent-cloud.com' /etc/hosts
```
> ? 该命令可在集群开启内网访问后，从集群基本信息页面中的“集群APIServer” 中获取，详情请参见 [获取集群凭证](#proof)。 
> 
3. 执行以下命令，查看是否配置成功。
```
cat /etc/hosts
```
如下图所示即为配置成功：
![](https://main.qcloudimg.com/raw/2e1bd6f1df51f150e9064d68f01e1754.png)
               
### Jenkins 安装必备插件
1. 登录 Jenkins 后台，选择左侧导航栏中的**系统管理**。
2. 在打开的“管理Jenkins” 面板中，单击**插件管理**。
3. 选择插件管理页面中**可选插件**，勾选 Locale、Kubernetes、Git Parameter 和 Extended Choice Parameter。
 - **Locale**：汉化语言插件，安装该插件可使 Jenkins 界面默认设置为中文版。
 - **Kubernetes**：Kubernetes-plugin 插件。
 - **Git Parameter** 和 **Extended Choice Parameter**：用于构建打包时传参。
   以 Kubernetes 插件为例，如下图所示：
![](https://main.qcloudimg.com/raw/81941906a99def8fc11bfcc581af8183.png)
4. 勾选上述插件后单击**直接安装**，并重启 Jenkins 即可。

### 开启 jnlp 端口
1. 登录 Jenkins 后台，选择左侧导航栏中的**系统管理**。
2. 在打开的“管理Jenkins” 面板中，单击**全局安全配置**。
2. 在全局安全配置页中，设置入站代理的 TCP 端口为“指定端口 50000”。如下图所示：
![](https://main.qcloudimg.com/raw/78bcd4551ee5bd35bc92ea4ec5aca93e.png)
4. 其他配置项保持默认状态，并单击页面下方的**保存**。

### 添加 TKE 集群 token[](id:addToken)
1. 登录 Jenkins 后台，选择左侧导航栏中的**凭据** > **系统**。
2. 在打开的“系统”面板中，选择**全局凭据 (unrestricted)**。如下图所示：
![](https://main.qcloudimg.com/raw/bb761bc624d5e60462a57607ff6f88aa.png)
3. 在“全局凭据 (unrestricted)”页中，单击左侧菜单栏中的**添加凭据**，根据以下提示设置凭据基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/c32f572ba76674c09c6550c68f1835de.png)
  - **类型**：选择**Secret text**。
  - **范围**：默认为**全局（Jenkins,nodes,items,all child items,etc）**。
  - **Secret**：填写[ 获取集群凭证 ](#proof)步骤中获取的 ServiceAccount jenkins 的 **Token**。
  - **ID**：默认不填写。
  - **描述**：填写该凭据相关信息，该内容将被显示为凭据名称及描述信息，本文以 `tke-token` 为例。
3. 单击**确定**即可添加，添加成功后该凭据将显示在凭据列表中。如下图所示：
!![](https://main.qcloudimg.com/raw/7f5e00bb12c27c7efc085c8c94b5dc71.png)

### 添加 gitlab 认证[](id:addGitlab)
1. 在“全局凭据 (unrestricted)”页中，单击左侧菜单栏中的**添加凭据**，并根据以下提示设置凭据基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/ce8f9e2ca7f8d87d96c23f889ff72450.png)
 - **类型**：选择**Username with password**。
 - **范围**：默认为**全局（Jenkins,nodes,items,all child items,etc）**。
 - **用户名**：gitlab 用户名。
 - **密码**：gitlab 登录密码。
 - **ID**：默认不填写。
 - **描述**：填写该凭据相关信息，该内容将被显示为凭据名称及描述信息，本文以 `gitlab-password` 为例。
2. 单击**确定**即可添加成功。

### 配置 slave pod 模板[](id:PodTemplates)
1. 登录 Jenkins 后台，选择左侧导航栏中的**系统管理**。
2. 在打开的“管理Jenkins” 面板中，单击**系统配置**。
3. 在“系统配置”面板最下方，选择“云”模块下的**新增一个云** > **Kubernetes**。如下图所示：
![](https://main.qcloudimg.com/raw/f23401c33207fa861ce61b6544327662.png)
4. 单击**Kubernetes Cloud details...**，设置 Kubernetes 以下基本信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/35f184a46b1cded49ecef0d97c8cacf6.png)
主要参数配置如下，其余选项请保持默认设置：
    - **名称**：自定义，本文以 `kubernetes` 为例。
    - **Kubernetes 地址**：TKE 集群访问地址，可参考[ 获取集群凭证 ](#proof)步骤获取。
    - **Kubernetes 服务证书 Key**：集群 CA 证书，可参考 [获取集群 CA 证书](#getCA) 步骤获取。
    - **凭据**：选择[ 添加 TKE 集群 token ](#addToken)步骤中已创建的凭据 `tke-token`，并单击**连接测试**。若连接成功则会提示 Connection test succeessful。
    - **Jenkins 地址**：填写为 Jenkins 内网地址，例如`http://10.x.x.x:8080`。
5. 选择**Pod Templates** > **添加 Pod 模板** > **Pod Templates details...**，设置 Pod 模板基本信息。如下图所示：
![](https://main.qcloudimg.com/raw/084af569d140e04750b3c157835f6e31.png)
主要参数信息如下，其余选项请保持默认设置：
 - **名称**：自定义，本文以 `jnlp-agent` 为例。
 - **标签列表**：定义标签名称，构建时可根据该标签选择 Pod ，本文以 `jnlp-agent` 为例。
  - **用法**：选择**尽可能的使用这个节点**。
6. [](id:ContainerTemplate)在“容器列表”中，选择**添加容器** > **Container Template**，设置以下容器相关信息。如下图所示：
![](https://main.qcloudimg.com/raw/6a5e619f36709cc9af76ee555ee8e984.png)
    - **名称**：自定义容器名称，本文以 `jnlp-agent` 为例。
    - **Docker 镜像**：输入镜像地址 `jenkins/jnlp-slave:alpine`。
    - **工作目录**：保持默认设置，请记录工作目录，将用于 shell 脚本处构建打包。
    - 其余选项保持默认设置即可。
7. 在“卷”中按照以下步骤添加卷，为 slave pod 配置 docker 命令。如下图所示：
![](https://main.qcloudimg.com/raw/bd098fee9954a62c9c6e2328e9912314.png)
  1. 选择**添加卷** > **Host Path Volume**，主机和挂载路径均填写 `/usr/bin/docker`。
   2. 选择**添加卷** > **Host Path Volume**，主机和挂载路径均填写`/var/run/docker.sock`。
8. 单击页面下方的**保存**，即可完成 slave pod 模板配置。

## 下一步操作
请前往 [步骤2：Slave pod 构建配置](https://cloud.tencent.com/document/product/457/41397) 创建新任务及配置任务参数。
