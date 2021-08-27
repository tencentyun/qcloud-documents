
## 通过Kubectl连接集群

您可以通过kubernetes 命令行工具kubectl 从本地客户端机器连接到TKE集群。

### 第一步:安装 kubectl 工具
如果您已经安装 kubectl 工具，请忽略本步骤。详细安装 kubectl 过程参考 [Installing and Setting up kubectl](https://kubernetes.io/docs/user-guide/prereqs/)。

#### 下载kubectl 工具
- MAC OS X 系统
```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl
```
- Linux 系统
```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
```
- Windows 系统
```shell
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/windows/amd64/kubectl.exe
```

#### 添加执行权限
使用以下命令添加执行权限：

```shell
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

#### 测试安装结果
测试安装结果，输入以下命令，输出版本信息即安装成功。
```shell
kubectl version
Client Version: version.Info{Major:"1", Minor:"5", GitVersion:"v1.5.2", GitCommit:"08e099554f3c31f6e6f07b448ab3ed78d0520507", GitTreeState:"clean", BuildDate:"2017-01-12T04:57:25Z", GoVersion:"go1.7.4", Compiler:"gc", Platform:"linux/amd64"}
```

### 第二步：获取集群账号密码以及证书信息

1. 登录 [容器服务控制台 > 集群](https://console.cloud.tencent.com/ccs)，单击需要连接的集群 ID/名称，查看集群详情。

2. 在集群信息页，单击**显示凭证**，查看用户名、密码和证书信息。

3. 复制或下载证书文件到本地。

4. 获取访问入口

#### 获取公网访问入口

开启公网访问地址后可直接参考第三步直接使用。
#### 获取VPC内网访问入口

目前暂不支持内网**`DNS`**解析，因此需要指定客户端主机的**`hosts`**，来支持域名解析。即：在**`/etc/hosts`**文件后追加内网返回的**`IP`**和域名。用户可以参考下面的代码，也可以手动设置。 
<pre><code>sudo sed -i '$a **IP地址** **域名**' /etc/hosts</code></pre>
配置完成后，可参考第三步使用内网访问地址域名来访问。  

注：若集群无可用节点（包括节点异常,已封锁等状态），内网访问将在集群内有可用节点时生效。
#### 集群内直接访问：无须任何配置，可直接在集群内的主机上执行kubectl命令。

### 第三步：通过证书信息使用 kubectl 操作集群
#### 单次 kubectl 操作请求，附带证书信息
该方法适用于单次操作集群，不将容器集群的证书信息保存到机器上。
请求方法，kubectl 命令格式：
```
-s "域名信息" --username=用户名 --password=密码 --certificate-authority=证书路径
```
示例：
```shell
kubectl get node -s "https://cls-66668888.ccs.tencent-cloud.com" --username=admin --password=6666o9oIB2gHD88882quIfLMy6666 --certificate-authority=/etc/kubernetes/cluster-ca.crt
```

#### 修改 kubectl 配置文件，长期有效
该方法适用于长期通过 kubectl 操作集群， 一次配置，只要文件不修改就长期有效。
设置 kubectl 配置，修改以下命令中的密码、证书信息。
```shell
kubectl config set-credentials default-admin --username=admin --password=6666o9oIB2gHD88882quIfLMy6666
kubectl config set-cluster default-cluster --server=https://cls-66668888.ccs.tencent-cloud.com --certificate-authority=/etc/kubernetes/cluster-ca.crt
kubectl config set-context default-system --cluster=default-cluster --user=default-admin
kubectl config use-context default-system

```
配置完成，直接使用 kubectl 命令：
```shell
kubectl get nodes
NAME        STATUS    AGE
10.0.0.61   Ready     10h
```

## 设置 kubectl 命令自动补全
您可以通过配置 kubectl 自动补全，提高可使用性。
```shell
source <(kubectl completion bash)
```