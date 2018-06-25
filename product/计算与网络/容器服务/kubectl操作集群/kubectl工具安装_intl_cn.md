## 使用kubectl操作集群教程
### 安装kubectl工具

如果您已经安装有kubectl工具，请忽略本步骤。详细安装kubectl过程参考[Installing and Setting up kubectl](https://kubernetes.io/docs/user-guide/prereqs/)

下载kubectl（腾讯云主机内网下载）:
>注：腾讯云容器服务创建的云主机，默认已安装kubectl工具。

```shell
# Linux
curl -LO http://mirrors.tencentyun.com/install/ccs/v1.4.6/linux/amd64/kubectl 

# Windows
curl -LO http://mirrors.tencentyun.com/install/ccs/v1.4.6/windows/amd64/kubectl.exe
```
下载kubectl（公网下载）:
```shell
# OS X
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl

# Linux
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

# Windows
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/windows/amd64/kubectl.exe
```

添加执行权限
```shell
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
测试安装结果,输入以下命令，输出版本信息即安装成功
```shell
kubectl version
Client Version: version.Info{Major:"1", Minor:"5", GitVersion:"v1.5.2", GitCommit:"08e099554f3c31f6e6f07b448ab3ed78d0520507", GitTreeState:"clean", BuildDate:"2017-01-12T04:57:25Z", GoVersion:"go1.7.4", Compiler:"gc", Platform:"linux/amd64"}
```

### 获取集群账号密码以及证书信息
登录到容器服务TKE控制台，点击需要连接的集群，查看集群详情
![Alt text](https://mc.qcloudimg.com/static/img/b99b529c6e30983db14e6ec81605be27/Image+012.png)

点击集群凭证，查看用户名、密码和证书信息

![Alt text](https://mc.qcloudimg.com/static/img/1aac831641ccfc0b3becd0b38e2a9634/Image+014.png)

复制或下载证书文件到本地

![Alt text](https://mc.qcloudimg.com/static/img/0b74fedbf69a1ce31d8fcd0f3baff7e5/Image+015.png)

### 通过证书信息使用kubectl操作集群
#### 方法一：每次请求附带证书信息
请求方法：
kubectl 命令 -s "域名信息" --username=用户名 --password=密码 --certificate-authority=证书路径，如：
```shell
kubectl get node -s "https://cls-66668888.ccs.tencent-cloud.com" --username=admin --password=6666o9oIB2gHD88882quIfLMy6666 --certificate-authority=/etc/kubernetes/cluster-ca.crt
```

#### 方法二：修改kubectl配置文件  

设置kubectl配置,修改以下命令中的密码、证书信息
```shell
kubectl config set-credentials default-admin --username=admin --password=6666o9oIB2gHD88882quIfLMy6666
kubectl config set-cluster default-cluster --server=https://cls-66668888.ccs.tencent-cloud.com --certificate-authority=/etc/kubernetes/cluster-ca.crt
kubectl config set-context default-system --cluster=default-cluster --user=default-admin
kubectl config use-context default-system

```
配置完成，直接使用kubectl命令
```shell
kubectl get nodes
NAME        STATUS    AGE
10.0.0.61   Ready     10h
```

### 设置kubectl命令自动补全
您可以通过配置Kubectl自动补全，提高可使用性
```shell
source <(kubectl completion bash)
```