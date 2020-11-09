## 操作场景
本文档介绍如何通过 Kubernetes 命令行工具 Kubectl 从本地客户端机器连接到弹性集群。


## 前提条件
- 请安装 curl 软件。
- 请根据操作系统的类型，选择获取 Kubectl 工具的方式：
>!请对应您实际使用版本，将命令行中的 `v1.14.5` 替换成业务所需的 Kubectl 版本。
>
 - **Mac OS 系统**
 在终端执行以下命令，获取 Kubectl 工具。
```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.14.5/bin/darwin/amd64/kubectl
```
 - **Linux 系统**
在终端执行以下命令，获取 Kubectl 工具。
```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.14.5/bin/linux/amd64/kubectl
```
 - **Windows 系统**
通过命令行工具执行以下命令，获取 Kubectl 工具。
```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.14.5/bin/windows/amd64/kubectl.exe
```

## 操作步骤

### 安装 Kubectl 工具

1. 参考 [Installing and Setting up kubectl](https://kubernetes.io/docs/user-guide/prereqs/)，安装 Kubectl 工具。
>?
>- 如果您已经安装 Kubectl 工具，请忽略本步骤。
>- 此步骤以 Linux 系统为例。
2. 依次执行以下命令，添加执行权限。
```shell
chmod +x ./kubectl
```
```
sudo mv ./kubectl /usr/local/bin/kubectl
```
3. 执行以下命令，测试安装结果。
```shell
kubectl version
```
如若输出类似以下版本信息，即表示安装成功。
```shell
Client Version: version.Info{Major:"1", Minor:"14", GitVersion:"v1.14.5", GitCommit:"0e9fcb426b100a2aea5ed5c25b3d8cfbb01a8acf", GitTreeState:"clean", BuildDate:"2019-08-05T09:21:30Z", GoVersion:"go1.12.5", Compiler:"gc", Platform:"windows/amd64"}
```

### 获取集群账号密码以及证书信息
1. 登录容器服务控制台，选择左侧导航栏中的【[弹性集群](https://console.cloud.tencent.com/tke2/ecluster)】。
2. 在“弹性集群”列表页面，单击需连接的集群 ID，进入该集群的管理页面。
3. 选择左侧导航栏中的【基本信息】，进入该集群“基础信息”页面。如下图所示：
![](https://main.qcloudimg.com/raw/498310beff5f0b8805cc99494ca5cce0.png)
4. 在“基本信息”中，单击 “集群凭证” 中的 【显示凭证】。
5. <span id="info"></span>在弹出的“集群凭证”窗口中，根据实际需求进行如下操作。
  - 获取用户名、密码和证书信息，单击【复制】或【下载】将集群 CA 证书保存到本地。
  - 开启外网或内网访问地址，并连接集群：
    - **集群内直接访问**：“外网访问地址”和“内网访问地址” 保持默认值，即关闭状态。您无须进行任何配置，即可直接在集群内的主机上执行 Kubectl 命令。
     - **获取公网访问入口**：将“外网访问地址”设置为【已开启】，可参考 [通过证书信息使用 Kubectl 操作集群](#TheCluster) 直接使用外网访问地址进行访问。
    - **获取 VPC 内网访问入口**：将“内网访问地址”设置为【已开启】，您需要指定 Apiserver 的内网访问子网，请确保选择的子网有剩余 IP。配置完成后，可参考 [通过证书信息使用 Kubectl 操作集群](#TheCluster) 直接使用内网访问地址进行访问。



### 通过证书信息使用 Kubectl 操作集群<span id="TheCluster"></span>

#### 单次 Kubectl 操作请求，附带证书信息
>?该方法适用于单次操作集群，无需将容器集群的证书信息长期保存到机器上。
>
**请求方法：**
Kubectl 命令参数格式如下所示：
```
-s "域名信息" --username=用户名 --password=密码 --certificate-authority=证书路径
```
 - **域名信息**：已获取的公网或 VPC 内网访问地址。
 - **用户名**：默认为 `admin`。
 - **密码**：“集群凭证”窗口中的 `token`，已在 [步骤5](#info) 中获取。
 - **证书路径**：“集群凭证”窗口中的 `集群CA证书`，已在 [步骤5](#info) 中获取。
 
**示例**
执行以下命令，获取集群 node 信息。
```shell
kubectl get node -s "https://xxx.xx.xx.xxx:443/" --username=admin --password=6666o9oIB2gHD88882quIfLMy6666 --certificate-authority=/etc/kubernetes/cluster-ca.crt
```

#### 修改 Kubectl 配置文件，长期有效
>?该方法适用于长期通过 Kubectl 操作集群，仅配置一次且无需修改文件，即可长期有效。
>
1. 参考以下命令，设置 Kubectl 配置文件中的密码、证书信息。
```shell
kubectl config set-credentials default-admin --username=admin --password=6666o9oIB2gHD88882quIfLMy6666
kubectl config set-cluster default-cluster --server=https://xxx.xx.xx.xxx:443/ --certificate-authority=/etc/kubernetes/cluster-ca.crt
kubectl config set-context default-system --cluster=default-cluster --user=default-admin
kubectl config use-context default-system
```
2. 配置完成后，执行以下命令，获取 node 节点信息。
```shell
kubectl get namespaces
```
返回类似以下信息，即表示配置成功。
```
NAME         STATUS    AGE
default      Active    11d
kube-system  Active    11d
```

<span id="setKubectlAutomaticComplete"></span>
### 设置 Kubectl 命令自动补全
您可以通过执行以下命令，配置 Kubectl 自动补全，提高可使用性。
```shell
source <(kubectl completion bash)
```

