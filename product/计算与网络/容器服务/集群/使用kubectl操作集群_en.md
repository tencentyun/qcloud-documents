### Installing kubectl tool

If you have installed the kubectl tool, skip this step. For more information on how to install kubectl, please see [Installing and Setting up kubectl](https://kubernetes.io/docs/user-guide/prereqs/).

Download kubectl (from private network of Tencent Cloud CVM):
>Note: CVMs created by Tencent CCS are installed with Kubectl tool by default.

```shell
# Linux
curl -LO http://mirrors.tencentyun.com/install/ccs/v1.4.6/linux/amd64/kubectl 

# Windows
curl -LO http://mirrors.tencentyun.com/install/ccs/v1.4.6/windows/amd64/kubectl.exe
```
Download kubectl (from public network):
```shell
# OS X
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl

# Linux
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl

# Windows
curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/windows/amd64/kubectl.exe
```

Add execution permission
```shell
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```
Enter the following commands to test the installation. If the version information displays, kubectl is successfully installed.
```shell
kubectl version
Client Version: version.Info{Major:"1", Minor:"5", GitVersion:"v1.5.2", GitCommit:"08e099554f3c31f6e6f07b448ab3ed78d0520507", GitTreeState:"clean", BuildDate:"2017-01-12T04:57:25Z", GoVersion:"go1.7.4", Compiler:"gc", Platform:"linux/amd64"}
```

### Obtaining Account, Password, and Certificate of Cluster
Log in to the CCS Console, and click the appropriate cluster to view details.
![Alt text](https://mc.qcloudimg.com/static/img/b99b529c6e30983db14e6ec81605be27/Image+012.png)

Click the cluster credential to view the user name, password and certificate information.

![Alt text](https://mc.qcloudimg.com/static/img/1aac831641ccfc0b3becd0b38e2a9634/Image+014.png)

Copy or download the certificate to a local machine.

![Alt text](https://mc.qcloudimg.com/static/img/0b74fedbf69a1ce31d8fcd0f3baff7e5/Image+015.png)

### Using Certificate to Enable kubectl to Work with Clusters
#### Method 1: Supply certificate information for each request.
Request method:
kubectl command -s "Domain Name" --username=user name --password=password --certificate-authority=certificate path, for example:
```shell
kubectl get node -s "https://cls-66668888.ccs.tencent-cloud.com" --username=admin --password=6666o9oIB2gHD88882quIfLMy6666 --certificate-authority=/etc/kubernetes/cluster-ca.crt
```

#### Method 2: Modify the configuration file of kubectl. 

Set kubectl configuration, and modify the certification information and passwords of the following commands
```shell
kubectl config set-credentials default-admin --username=admin --password=6666o9oIB2gHD88882quIfLMy6666
kubectl config set-cluster default-cluster --server=https://cls-66668888.ccs.tencent-cloud.com --certificate-authority=/etc/kubernetes/cluster-ca.crt
kubectl config set-context default-system --cluster=default-cluster --user=default-admin
kubectl config use-context default-system

```
Directly use kubectl commands after configuration
```shell
kubectl get nodes
NAME        STATUS    AGE
10.0.0.61   Ready     10h
```

### Setting Auto Completion for kubectl Command
You can configure Kubectl auto completion to improve usability.
```shell
source <(kubectl completion bash)
```
