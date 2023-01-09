
<dx-alert infotype="explain" title="">
本文来自 [GPU 云服务器用户实践征文](https://cloud.tencent.com/document/product/855/71869)，仅供学习和参考。
</dx-alert>


## 操作场景
本文介绍如何使用 GPU 云服务器实现边云协同处理。

## 配置环境
<table>
<tr>
<th>主机名</th>
<th>角色</th>
<th>IP 地址</th>
<th>服务</th>
<th>配置</th>
</tr>
<tr>
<td>VM-0-9-centos</td>
<td>云端</td>
<td>
VM-0-9-centos 内网 IP<br>
VM-0-9-centos 公网 IP
</td>
<td>kuberbetes、docker、cloudcore</td>
<td>操作系统：Centos 7.4<br>
CPU：Intel Xeon Cascade Lake(2.5 GHz)<br>
RAM：80GB<br>
GPU：NVIDIA T4
</td>
</tr>
<tr>
<td>berbai02</td>
<td>边端</td>
<td>berbai02 内网 IP</td>
<td>docker、edgecore</td>
<td rowspan=2>
操作系统：Ubuntu 18.04.6 LTS<br>
CPU：ARMv8 Processor rev 1 (v8l)<br>
RAM：4G<br>
GPU：128CUDA core Maxwell
</td>
</tr>
<tr>
<td>demo</td>
<td>边端</td>
<td>demo 内网 IP</td>
<td>docker、edgecore</td>
</tr>
</table>


## 操作步骤

### 安装驱动

#### 安装依赖包
1. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录 GPU 云服务器。
2. 执行以下命令，安装 dkms 依赖包。
```shellsession
sudo yum install -y dkms gcc kernel-devel yum-utils
```
3. 安装完成后，依次执行以下命令进行检查。
```shellsession
# 检查是否已经安装dkms
rpm -qa | grep -i dkms
```
```shellsession
# 检查是否安装kernel-devel
rpm -qa | grep kernel-devel
```
```shellsession
# 检查是否安装GCC
rpm -qa | grep gcc
```
```shellsession
# 检查是否安装yum-utils
rpm -qa | grep yum-utils
```
返回结果如下图所示，表示已成功安装依赖包。
![](https://qcloudimg.tencent-cloud.cn/raw/45871d2f93ad3c4e3071c60c405b5715.png)



#### 下载驱动
1. 前往 [NVIDIA Driver Downloads](https://www.nvidia.com/Download/Find.aspx)，根据实际配置查找对应版本驱动。本文选择驱动版本如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c1763383ae1d397718f3316efd38bb99.png)
2. 选择驱动进入下载页面，单击**DOWNLOAD**。
3. [](id:Step3)在 “Download” 页面，右键单击 **AGREE & DOWNLOAD**，并在弹出的菜单中选择**复制链接地址**。如下图所示：
![](https://main.qcloudimg.com/raw/e0412e1a06eb06ad9f98e7f6a2d5a026.png)
4. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录 GPU 云服务器。
5. 使用 `wget` 命令，粘贴 [步骤3](#Step3) 中已获取的驱动下载链接，下载驱动。命令如下：
```shellsession
wget https://us.download.nvidia.com/tesla/510.47.03/NVIDIA-Linux-x86_64-510.47.03.run
```
若您需将驱动下载至本地再上传至 GPU 云服务器，则可参考 [如何将本地文件拷贝到云服务器](https://cloud.tencent.com/document/product/213/39138)。


#### 安装驱动
1. 执行以下命令，添加执行权限。
```shellsession
chmod +x NVIDIA-Linux-x86_64-510.47.03.run
```
2. 执行以下命令，安装驱动。
```shellsession
sudo sh  NVIDIA-Linux-x86_64-510.47.03.run
```
3. 执行以下命令，验证驱动是否安装成功。
```shellsession
nvidia-smi
```
返回结果如下图所示，说明驱动已安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/52384af1a4bbf98490b28698501a06e9.png)




### 安装 KubeEdge


#### 安装前准备
1. 关闭防火墙
依次执行以下命令，关闭防火墙及自启动。
```shellsession
systemctl stop firewalld
```
```shellsession
systemctl disable firewalld
```
关闭后，可执行以下命令检查。
```shellsession
systemctl status firewalld
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/248938b102550b87abf693cc41538ecd.png)
2. 禁用 SELINUX
执行以下命令，编辑 `/etc/selinux/config` 配置文件。
```shellsession
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```
3. 关闭 swap
安装 Kubernetes 需关闭 swap，执行以下命令，修改 `/etc/fstab` 文件中的 swap 配置。
```shellsession
sed -ri 's/.*swap.*/#&/' /etc/fstab
```
4. 重启系统
执行以下命令，重启系统，使配置生效。
```shellsession
reboot
```


#### 安装 Docker
1. 执行以下命令，设置镜像仓库。
```shellsession
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```
2. 执行以下命令，更新 yum 软件包索引。
```shellsession
yum makecache fast
```
3. 执行以下命令，安装 Docker CE。
```shellsession
yum install docker-ce docker-ce-cli containerd.io
```
4. 依次执行以下命令，启动 Docker 并设置自启动。
```shellsession
systemctl start docker
```
```shellsession
systemctl enable docker
```
5. 依次执行以下命令，测试 Docker 安装是否成功。
```shellsession
docker version
```
```shellsession
docker run hello-world
```
```shellsession
docker images
```
返回结果如下图所示，表示 Docker 已安装成功。
![](https://qcloudimg.tencent-cloud.cn/raw/5e1437a1363b5a8cecbcbd68a3975be6.png)


#### 部署 Kubernetes
1. 执行以下命令，配置 yum 源。
```shellsession
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
       http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```
2. 依次执行以下命令，安装 kubeadm 及 kubectl。
```shellsession
yum makecache
```
```shellsession
yum install -y kubelet kubeadm kubectl ipvsadm
```
```shellsession
yum install kubelet-1.17.0-0.x86_64 kubeadm-1.17.0-0.x86_64 kubectl-1.17.0-0.x86_64
```
3. 依次执行以下命令，配置内核参数。
```shellsession
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
vm.swappiness=0
EOF
```
```shellsession
# 加载所有的 sysctl 配置
sysctl --system
modprobe br_netfilter
sysctl -p /etc/sysctl.d/k8s.conf
```
```shellsession
# 加载ipvs相关内核模块
# 如果重新开机，需要重新加载（可以写在 /etc/rc.local 中开机自动加载）
modprobe ip_vs
modprobe ip_vs_rr
modprobe ip_vs_wrr
modprobe ip_vs_sh
modprobe nf_conntrack_ipv4
```
```shellsession
# 查看是否加载成功
lsmod | grep ip_vs
```
4. 执行以下命令，查看 kubeadm 对应的 k8s 组件镜像版本。
```shellsession
kubeadm config images list
```
返回如下结果，以下镜像都需下载。
```shellsession
k8s.gcr.io/kube-apiserver:v1.23.5
k8s.gcr.io/kube-controller-manager:v1.23.5
k8s.gcr.io/kube-scheduler:v1.23.5
k8s.gcr.io/kube-proxy:v1.23.5
k8s.gcr.io/pause:3.6
k8s.gcr.io/etcd:3.5.1-0
k8s.gcr.io/coredns/coredns:v1.8.6
```
5. 执行以下命令，拉取上述镜像。
```shellsession
kubeadm config images pull
```
拉取完成后，执行以下命令，查看镜像。
```shellsession
docker images
```
返回结果如下：
```shellsession
[root@VM-0-9-centos ~]# docker images
REPOSITORY                           TAG       IMAGE ID       CREATED        SIZE
k8s.gcr.io/kube-apiserver            v1.23.5   3fc1d62d6587   4 weeks ago    135MB
k8s.gcr.io/kube-proxy                v1.23.5   3c53fa8541f9   4 weeks ago    112MB
k8s.gcr.io/kube-controller-manager   v1.23.5   b0c9e5e4dbb1   4 weeks ago    125MB
k8s.gcr.io/kube-scheduler            v1.23.5   884d49d6d8c9   4 weeks ago    53.5MB
k8s.gcr.io/etcd                      3.5.1-0   25f8c7f3da61   5 months ago   293MB
k8s.gcr.io/coredns                   1.8.6     a4ca41631cc7   6 months ago   46.8MB
hello-world                          latest    feb5d9fea6a5   6 months ago   13.3kB
k8s.gcr.io/pause                     3.6       6270bb605e12   7 months ago   683kB
```


#### 配置 Kubelet（可选）
您可参考以下步骤，在云中心配置 Kubelet，验证 K8s 集群的部署是否正确。

1. 执行以下命令，获取 Docker 的 cgroups。
```shellsession
DOCKER_CGROUPS=$(docker info | grep 'Cgroup' | cut -d' ' -f4)
echo $DOCKER_CGROUPS
```
2. 执行以下命令，配置 kubelet 的 cgroups。
```shellsession
cat >/etc/sysconfig/kubelet<<EOF
KUBELET_EXTRA_ARGS="--cgroup-driver=$DOCKER_CGROUPS --pod-infra-container-image=k8s.gcr.io/pause:3.1"
EOF
```
3. 依次执行以下命令，启动 kubelet。
```shellsession
systemctl daemon-reload
```
```shellsession
systemctl enable kubelet && systemctl start kubelet
```
<dx-alert infotype="explain" title="">
可通过 `systemctl status kubelet` 查看报错信息，该错误在运行 kubeadm init 生成 CA 证书后会被自动解决，此处可先忽略。
</dx-alert>



#### 初始化集群
使用 `kubeadm init` 命令初始化集群，参数说明如下表：
<table>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
<tr>
<td><code>--apiserver-advertise-address</code></td>
<td>master 和 worker 间能互相通信的 IP</td>
</tr>
<tr>
<td><code>--kubernetes-version</code></td>
<td>指定版本</td>
</tr>
<tr>
<td><code>--token-ttl=0</code></td>
<td>token 永不过期</td>
</tr>
<tr>
<td><code>--apiserver-cert-extra-sans</code></td>
<td>节点验证证书阶段忽略错误</td>
</tr>
</table>




<dx-alert infotype="notice" title="">
 - 初始化完成后需记录返回信息最后的 node 节点添加到集群的命令。同时支持使用 `kubeadm token create --print-join-command` 进行查看。
 - 若您使用了云服务器，则可删除 `--apiserver-advertise-address` 配置。
</dx-alert>

成功初始化过程如下所示：
```shellsession
kubeadm init --kubernetes-version=v1.23.5 \
                      --pod-network-cidr=10.244.0.0/16 \
                      --apiserver-advertise-address= <VM-0-9-centos 内网 IP> \
                      --ignore-preflight-errors=Swap

[root@VM-0-9-centos ~]# kubeadm init --kubernetes-version=v1.23.5 \
>                       --pod-network-cidr=10.244.0.0/16 \
>                       --ignore-preflight-errors=Swap
[init] Using Kubernetes version: v1.23.5

...

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join <VM-0-9-centos 内网 IP>:6443 --token 1tyany.dxr5ymxu2g3j0dzl \
        --discovery-token-ca-cert-hash sha256:a63bd724813ebe0c4aabadb8cc8c747b6c84c474b80d4104497542ec265ec36a
```

#### 配置 kubectl
依次执行以下命令，进一步配置 kubectl，完成 master 节点安装。
```shellsession
rm -rf $HOME/.kube
```
```shellsession
mkdir -p $HOME/.kube
```
```shellsession
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
```
```shellsession
chown $(id -u):$(id -g) $HOME/.kube/config
```


#### 查看 node 节点
执行以下命令，查看 node 节点。
```shellsession
kubectl get node
```
返回结果如下所示：
```shellsession
NAME            STATUS     ROLES                  AGE   VERSION
vm-0-9-centos   NotReady   control-plane,master   21m   v1.23.5
```


#### 配置网络插件 flannel（可选）
Kubernetes v1.17及以上版本，可使用以下命令安装 flannel。如需了解更多关于 flannel 信息，请参见 [flannel Github](https://github.com/flannel-io/flannel)。
```shellsession
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```
配置完成后，可依次执行以下命令进行查看。
```shellsession
kubectl get node -owide
```
```shellsession
kubectl get pods -n kube-system
```
```shellsession
kubectl get svc
```
返回结果如下所示：
```shellsession
[root@VM-0-9-centos ~]# kubectl get node -owide
NAME            STATUS     ROLES                  AGE   VERSION
vm-0-9-centos   NotReady   control-plane,master   31m   v1.23.5
[root@VM-0-9-centos ~]# kubectl get pods -n kube-system
NAME                                    READY   STATUS                  RESTARTS   AGE
coredns-64897985d-9hfz2                 0/1     Pending                 0          31m
coredns-64897985d-9hr2z                 0/1     Pending                 0          31m
etcd-vm-0-9-centos                      1/1     Running                 0          31m
kube-apiserver-vm-0-9-centos            1/1     Running                 0          31m
kube-controller-manager-vm-0-9-centos   1/1     Running                 3          31m
kube-flannel-ds-t4k2w                   0/1     Init:ImagePullBackOff   0          50s
kube-proxy-c6mck                        1/1     Running                 0          31m
kube-scheduler-vm-0-9-centos            1/1     Running                 4          31m
[root@VM-0-9-centos ~]# kubectl get svc
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   32m
```
<dx-alert infotype="explain" title="">
网络插件安装配置完成后，请等待几分钟，node 才会显示为 ready 状态。
</dx-alert>



#### 配置 iptables 转发 IP
由于在初始化时删除了 `--apiserver-advertise-address` 参数，返回的节点加入集群命令为内网 IP，而本文中使用的云服务器内网不互通，故需配置 iptables 进行 IP 转发，将主节点公网 IP 转发至内网 IP，及配置 node 节点将主节点的内网 IP 转发至主节点的公网 IP。步骤如下：
1. 在主节点 master 上，执行以下命令。
```shellsession
sudo iptables -t nat -A OUTPUT -d <主节点公网IP> -j DNAT --to-destination <主节点内网IP>
```
结合本文示例环境，则执行以下命令：
```shellsession
# cloud
sudo iptables -t nat -A OUTPUT -d <VM-0-9-centos 公网 IP> -j DNAT --to-destination <VM-0-9-centos 内网 IP>
```
2. 在 node 节点上，执行以下命令。
```shellsession
sudo iptables -t nat -A OUTPUT -d <VM-0-9-centos 内网 IP> -j DNAT --to-destination <VM-0-9-centos 公网 IP>
```
结合本文示例环境，则执行以下命令：
```shellsession
# edge
sudo iptables -t nat -A OUTPUT -d <VM-0-9-centos 内网 IP> -j DNAT --to-destination <VM-0-9-centos 公网 IP>
```


### 安装 KubeEdge

#### 配置 Cloud
Cloud 端负责编译 KubeEdge 的相关组件与运行 cloudcore。配置步骤如下：
1. 安装 golang
依次执行以下命令，下载并解压 golang 安装包。
```shellsession
wget https://golang.google.cn/dl/go1.18.1.linux-amd64.tar.gz
```
```shellsession
tar -zxvf go1.18.1.linux-amd64.tar.gz -C /usr/local
```
依次执行以下命令，修改 `/etc/profile` 文件配置 golang 环境。
```shellsession
cat >> /etc/profile << EOF
# golang env
export GOROOT=/usr/local/go
export GOPATH=/data/gopath
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
EOF
```
```shellsession
mkdir -p /data/gopath && cd /data/gopath
```
```shellsession
mkdir -p src pkg bin
```
执行以下命令，使配置生效。
```shellsession
source /etc/profile
```
2. 执行以下命令，安装 Git。
```shellsession
yum install git
```
3. 执行以下命令，下载 KudeEdge 源码。
```shellsession
git clone https://github.com/kubeedge/kubeedge $GOPATH/src/github.com/kubeedge/kubeedge
```


#### 部署 cloudcore
1. 依次执行以下命令，编译 kubeadm。
```shellsession
cd $GOPATH/src/github.com/kubeedge/kubeedge
```
```shellsession
make all WHAT=keadm
```
2. 执行以下命令，进入编译后的二进制文件目录 `./_output/local/bin`。
```shellsession
cd ./_output/local/bin
```
3. 执行以下命令，创建 cloud 节点。
```shellsession
./keadm init --advertise-address="<VM-0-9-centos 内网 IP>"
```
返回结果如下所示：
```shellsession
[root@VM-0-9-centos kubeedge]# ./keadm init --advertise-address="<VM-0-9-centos 内网 IP>"
Kubernetes version verification passed, KubeEdge installation will start...

...

KubeEdge cloudcore is running, For logs visit:  /var/log/kubeedge/cloudcore.log
CloudCore started
```
4. 执行以下命令，查看 cloudcore 状态。
```shellsession
systemctl status cloudcore.service
```


#### 配置 Edge
Edge 端也可以通过 keadm 进行配置，可以将 cloud 端编译生成的二进制可执行文件通过 scp 命令复制到 edge 端。步骤如下：

1. 安装必要环境
  1. 执行以下命令，查看操作系统版本。
```shellsession
uname -a
```
  2. 依次执行以下命令，树莓派需配置 ARMv6 版本的 golang 环境。
```shellsession
wget https://golang.google.cn/dl/go1.18.1.linux-armv6l.tar.gz
```
```shellsession
tar -zxvf go1.18.1.linux-armv6l.tar.gz -C /usr/local
```
  3. 执行以下命令，配置环境变量。
```shellsession
cat >> /home/pi/.bashrc << EOF
# golang env
export GOROOT=/usr/local/go
export GOPATH=/data/gopath
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
EOF
```
  4. 执行以下命令，使配置生效。
```shellsession
source /home/pi/.bashrc
```
  5. 执行以下命令，安装 Git。
```shellsession
yum install git
```
  6. 执行以下命令，下载 KudeEdge 源码。
```shellsession
git clone https://github.com/kubeedge/kubeedge $GOPATH/src/github.com/kubeedge/kubeedge
```
2. 执行以下命令，在云端获取 token 令牌。token 令牌在加入边缘节点时使用。
```shellsession
./keadm gettoken
```
返回结果如下所示：
```shellsession
b6107885645ec34725a76e7cf3fd9d8bf130dfa5e6f37d4c51b6bc1bee49cd48.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTA2MjE0MDR9.ZMtQnF_oWYG4pijYO-SaxVtUYhHQSuCIauf5iWFkNMY
```
3. 部署 edgecore
依次执行以下命令，编译 keadm。
```shellsession
cd $GOPATH/src/github.com/kubeedge/kubeedge
```
```shellsession
make all WHAT=keadm
```
```shellsession
cd ./_output/local/bin
```
通过 `keadm join` 命令安装 edgecore 和 mqtt。它还提供了一个标志，通过它可以设置特定的版本。
```shellsession
./keadm join --cloudcore-ipport=<VM-0-9-centos 内网 IP>:10000 --token=9c71cbbb512afd65da8813fba9a48d19ab8602aa27555af7a07cd44b508858ae.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NTA3MDgwNjN9.-S0YBgSSAz6loQsi0XaTgFeWyHsHDm8E2SAefluVTJA
Host has /usr/sbin/mosquitto already installed and running. Hence skipping the installation steps !!!

...

KubeEdge edgecore is running, For logs visit: journalctl -u edgecore.service -xe
```
<dx-alert infotype="notice" title="">
- `--cloudcore-ipport` 标志是强制性标志。
- `--token` 会自动为边缘节点应用证书。
- 云和边缘端使用的 kubeEdge 版本应相同。
</dx-alert>
4. 验证
边缘端在启动 edgecore 后，会与云端的 cloudcore 进行通信，K8s 进而会将边缘端作为一个 node 纳入 K8s 的管控。结果如下所示：
```shellsession
[root@VM-0-9-centos bin]# kubectl get node
NAME            STATUS   ROLES                  AGE   VERSION
berbai02        Ready    agent,edge             32m   v1.22.6-kubeedge-v1.10.0
demo            Ready    agent,edge             34m   v1.22.6-kubeedge-v1.10.0
vm-0-9-centos   Ready    control-plane,master   27h   v1.23.5
[root@VM-0-9-centos bin]# kubectl get pods -n kube-system
NAME                                    READY   STATUS              RESTARTS         AGE
coredns-64897985d-9hfz2                 1/1     Running             2 (69m ago)      27h
coredns-64897985d-9hr2z                 1/1     Running             2 (69m ago)      27h
etcd-vm-0-9-centos                      1/1     Running             2 (69m ago)      27h
kube-apiserver-vm-0-9-centos            1/1     Running             2 (69m ago)      27h
kube-controller-manager-vm-0-9-centos   1/1     Running             13 (69m ago)     27h
kube-flannel-ds-hsss5                   0/1     Error               10 (2m23s ago)   34m
kube-flannel-ds-qp6xj                   0/1     Error               9 (4m46s ago)    36m
kube-flannel-ds-t4k2w                   1/1     Running             2 (69m ago)      27h
kube-proxy-6qcfb                        0/1     ContainerCreating   0                34m
kube-proxy-c6mck                        1/1     Running             2 (69m ago)      27h
kube-proxy-hvpz9                        1/1     Running             0                36m
kube-scheduler-vm-0-9-centos            1/1     Running             14 (69m ago)     27h
```
<dx-alert infotype="explain" title="">
若您在 K8s 集群中配置了 flannel 网络插件，则由于 edge 节点未部署 kubelet，调度到 edge 节点上的 flannel pod 会创建失败。这不影响 KubeEdge 的使用，可忽略该问题。
</dx-alert>




### 云边协同实例
KubeEdge Counter Demo 计数器是一个伪设备，用户无需任何额外的物理设备即可运行此演示。计数器在边缘侧运行，用户可以从云侧在 Web 中对其进行控制，也可以从云侧在 Web 中获得计数器值。

1. 执行以下命令，下载源码。
```shellsession
git clone https://github.com/kubeedge/examples.git $GOPATH/src/github.com/kubeedge/examples
```
2. 依次执行以下命令，创建 device model。
```shellsession
cd $GOPATH/src/github.com/kubeedge/examples/kubeedge-counter-demo/crds
```
```shellsession
kubectl create -f kubeedge-counter-model.yaml
```
3. 依次执行以下命令，创建 device，并根据实际情况修改 matchExpressions。
```shellsession
cd $GOPATH/src/github.com/kubeedge/examples/kubeedge-counter-demo/crds
```
```shellsession
# 替换 "demo" 为你的 edge 节点名称
sed -i "s#edge-node#demo#" kubeedge-counter-instance.yaml
```
```shellsession
kubectl create -f kubeedge-counter-instance.yaml
```
4. 部署云端应用
   1. 依次执行以下命令，修改代码。云端应用 web-controller-app 用来控制边缘端的 pi-counter-app 应用，该程序默认监听的端口号为80，此处修改为8989。
```shellsession
cd $GOPATH/src/github.com/kubeedge/examples/kubeedge-counter-demo/web-controller-app
```
```shellsession
sed -i "s#80#8989#" main.go
```
   2. 依次执行以下命令，构建镜像。
<dx-alert infotype="notice" title="">
构建镜像时，如果开启了 go mod，则请关闭。
</dx-alert>
```shellsession
make
```
```shellsession
make docker
```
   3. 依次执行以下命令，部署 web-controller-app。
```shellsession
cd $GOPATH/src/github.com/kubeedge/examples/kubeedge-counter-demo/crds
```
```shellsession
kubectl create -f kubeedge-web-controller-app.yaml
```
5. 部署边缘端应用
边缘端的 pi-counter-app 应用受云端应用控制，主要与 mqtt 服务器通信，进行简单的计数功能。
   1. 依次执行以下命令，构建镜像。
```shellsession
cd $GOPATH/src/github.com/kubeedge/examples/kubeedge-counter-demo/counter-mapper
```
```shellsession
make
```
```shellsession
make docker
```
   2. 依次执行以下命令，部署 pi-counter-app。
```shellsession
cd $GOPATH/src/github.com/kubeedge/examples/kubeedge-counter-demo/crds
```
```shellsession
kubectl create -f kubeedge-pi-counter-app.yaml
```
为防止 Pod 的部署卡在 ContainerCreating，请依次执行以下命令，直接通过 docker save、scp 和 docker load 命令将镜像发布到边缘端。
```shellsession
docker save -o kubeedge-pi-counter.tar kubeedge/kubeedge-pi-counter:v1.0.0
```
```shellsession
scp kubeedge-pi-counter.tar root@<demo 内网 IP>:/root
```
```shellsession
docker load -i kubeedge-pi-counter.tar
```
6. 查看运行效果
KubeEdge Demo 的云端部分和边缘端的部分都已经部署完毕，如下所示：
```shellsession
[root@VM-0-9-centos crds]# kubectl get pods -o wide
NAME                                    READY   STATUS    RESTARTS   AGE   IP           NODE            NOMINATED NODE   READINESS GATES
kubeedge-counter-app-55848d84d9-545kh   1/1     Running   0          27m   <VM-0-9-centos 内网 IP>   vm-0-9-centos   <none>           <none>
kubeedge-pi-counter-54b7997965-t2bxr    1/1     Running   0          31m   <demo 内网 IP>   demo            <none>           <none>
```
    1. 执行 ON 命令
    在 Web 页面上选择 ON，并单击 **Execute**，可以在 edge 节点上通过以下命令查看执行结果：
```shellsession
# 修改 counter-container-id 为kubeedge-pi-counter容器id
docker logs -f counter-container-id
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/42f363a3e7bd645d5d333097c35aa02f.png)
    2. 查看 counter STATUS
    在 Web 页面上选择 **STATUS**，并单击 **Execute**，会在 Web 页面上返回 counter 当前的 status。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/012467a9709340360c59c19fafefa25a.png)
    3. 执行 OFF 命令
    在 Web 页面上选择 **OFF**，并单击 **Execute**，可以在 edge 节点上通过以下命令查看执行结果：
```shellsession
# 修改 counter-container-id 为kubeedge-pi-counter容器id
docker logs -f counter-container-id
```
返回结果如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7a7afddc9cdde529602d0580951f5767.png)
