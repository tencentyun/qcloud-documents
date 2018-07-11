## 安装 kubectl 工具
如果您已经安装 kubectl 工具，请忽略本步骤。详细安装 kubectl 过程参考 [Installing and Setting up kubectl](https://kubernetes.io/docs/user-guide/prereqs/)。

### 下载 kubectl
#### 腾讯云服务器内网下载
>注：腾讯云容器服务创建的云服务器，默认已安装 kubectl 工具。

- Linux 系统
```shell
curl -LO http://mirrors.tencentyun.com/install/ccs/v1.4.6/linux/amd64/kubectl 
```
- Windows 系统
```shell
curl -LO http://mirrors.tencentyun.com/install/ccs/v1.4.6/windows/amd64/kubectl.exe
```

#### 公网下载
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

### 添加执行权限
使用以下命令添加执行权限：
```shell
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
### 测试
测试安装结果，输入以下命令，输出版本信息即安装成功。
```shell
kubectl version
Client Version: version.Info{Major:"1", Minor:"5", GitVersion:"v1.5.2", GitCommit:"08e099554f3c31f6e6f07b448ab3ed78d0520507", GitTreeState:"clean", BuildDate:"2017-01-12T04:57:25Z", GoVersion:"go1.7.4", Compiler:"gc", Platform:"linux/amd64"}
```

## 获取集群账号密码以及证书信息
1. 登录 [容器服务控制台 > 集群](https://console.cloud.tencent.com/ccs)，单击需要连接的集群 ID/名称，查看集群详情。

2. 在集群信息页，单击【显示凭证】，查看用户名、密码和证书信息。

3. 复制或下载证书文件到本地。

## 通过证书信息使用 kubectl 操作集群
### 单次 kubectl 操作请求，附带证书信息
该方法适用于单次操作集群，不将容器集群的证书信息保存到机器上。
请求方法，kubectl 命令格式：
```
-s "域名信息" --username=用户名 --password=密码 --certificate-authority=证书路径
```
示例：
```shell
kubectl get node -s "https://cls-66668888.ccs.tencent-cloud.com" --username=admin --password=6666o9oIB2gHD88882quIfLMy6666 --certificate-authority=/etc/kubernetes/cluster-ca.crt
```

### 修改 kubectl 配置文件，长期有效
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