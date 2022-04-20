## 操作背景 
HCCPNV4h 实例搭载了 A100 GPU 并支持 **NvLink & NvSwitch**，需额外安装与驱动版本对应的 nvidia-fabricmanager 服务使 GPU 卡间能够互联。若您使用该实例，请参考本文安装 nvidia-fabricmanager 服务，否则可能无法正常使用 GPU 实例。


## 操作步骤
本文以驱动版本 **470.103.01** 为例，您可参考以下步骤进行安装，可根据实际情况需要替换 `version` 后的驱动版本。
 
### 安装 nvidia-fabricmanager 服务
1. 登录实例，详情请参见 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)。
2. 不同操作系统版本安装方法不同，请您参考以下方式，执行对应命令进行安装。
<dx-tabs>
::: CentOS 7.x 镜像
```ruby
version=470.103.01
yum -y install yum-utils
yum-config-manager --add-repo https://developer.download.nvidia.com/compute/cuda/repos/rhel7/x86_64/cuda-rhel7.repo
yum install -y nvidia-fabric-manager-${version}-1
```
:::
::: Ubuntu 18.04 镜像
```ruby
version=470.103.01
main_version=$(echo $version | awk -F '.' '{print $1}')
apt-get update
apt-get -y install nvidia-fabricmanager-${main_version}=${version}-*
```
:::
</dx-tabs>


### 启动 nvidia-fabricmanager 服务
依次执行以下命令，启动服务。
```ruby
systemctl enable nvidia-fabricmanager
```
```ruby
systemctl start nvidia-fabricmanager
```

### 查看 nvidia-fabricmanager 服务状态
执行以下命令，查看服务状态。
```ruby
systemctl status nvidia-fabricmanager
```
若输出信息如下，则表示服务安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/3575a97948b57964dff2b922d15756a8.png)
