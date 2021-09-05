## 操作场景

您可以通过 Kubernetes 命令行工具 kubectl 从本地客户端机器连接到 TKE 集群。

## 操作步骤

### 安装 kubectl 工具

如果您已经安装 kubectl 工具，请忽略本步骤。详细安装过程参考 [Installing and Setting up kubectl](https://kubernetes.io/docs/user-guide/prereqs/)。

#### 下载 kubectl 工具
- Mac OS X 系统
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.8.13/bin/darwin/amd64/kubectl
```
- Linux 系统
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.8.13/bin/linux/amd64/kubectl
```
- Windows 系统
```
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.8.13/bin/windows/amd64/kubectl.exe
```
>!  kubenretes版本大于1.10请使用1.10以上的kubectl工具，小于1.10版本请使用1.10以下的kubectl工具，上述命令中v1.8.13可根据需求替换成业务所需的kubectl版本。

#### 添加执行权限

使用以下命令添加执行权限：
```
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

#### 测试安装结果

测试安装结果，输入以下命令，输出版本信息即安装成功。
```
kubectl version
Client Version: version.Info{Major:"1", Minor:"5", GitVersion:"v1.5.2", GitCommit:"08e099554f3c31f6e6f07b448ab3ed78d0520507", GitTreeState:"clean", BuildDate:"2017-01-12T04:57:25Z", GoVersion:"go1.7.4", Compiler:"gc", Platform:"linux/amd64"}
```

### 获取集群账号密码以及证书信息
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/ccs) 并选择左侧导航栏中的**集群**。
2. 单击需要连接的**集群 ID/名称**，查看集群详情。
3. 在集群信息页，单击**显示凭证**，进入集群凭证详情页，查看用户名、密码和证书信息。如下图所示：
![](https://main.qcloudimg.com/raw/ebd970e0be5609a01456296501804053.png)
>?您可以根据实际需求，单击**复制**或**下载**将集群 CA 证书保存到本地。
4. 获取访问入口。
 - 获取外网访问入口：开启外网访问，并配置来源授权，单击**保存**，创建完成之后即可获取。开启后如下图所示：
![](https://main.qcloudimg.com/raw/d2c8e34cb9cce1af798034508bbe25de.png)
开启外网访问地址后可参考 [通过证书信息使用 kubectl 操作集群](#step3) 直接使用。
 - 获取内网访问入口：开启内网访问，并设置集群所在子网。指定了客户端主机的 **hosts**，用于支持域名解析。 即：在`/etc/hosts`文件后追加内网返回的 **IP** 和域名。用户可以参考下图中的代码，也可以手动设置。开启后如下图所示：
    ![](https://main.qcloudimg.com/raw/871fd4909fb3913b27c2e34a8e14074e.png)
配置完成后，可参考 [通过证书信息使用 kubectl 操作集群](#step3) 使用内网访问地址域名来访问。
>! 若集群无可用节点（包括节点异常,已封锁等状态），内网访问将在集群内有可用节点时生效。
 - 集群内直接访问：无须任何配置，可直接在集群内的主机上执行 kubectl 命令。

<a id="step3"></a>
### 通过证书信息使用 kubectl 操作集群

#### 单次 kubectl 操作请求，附带证书信息

该方法适用于单次操作集群，不将容器集群的证书信息保存到机器上。
请求方法，kubectl 命令格式：
<pre>
<span class="hljs-string">-s</span> "域名信息" <span class="hljs-string">--username</span>=用户名 <span class="hljs-string">--password</span>=密码 <span class="hljs-string">--certificate-authority</span>=集群CA证书保存路径
</pre>
示例：
<pre>
kubectl get node <span class="hljs-string">-s</span> "https://cls-66668888.ccs.tencent-cloud.com" <span class="hljs-string">--username</span>=admin <span class="hljs-string">--password</span>=6666o9oIB2gHD88882quIfLMy6666 <span class="hljs-string">--certificate-authority</span>=/etc/kubernetes/cluster-ca.crt
</pre>

#### 修改 kubectl 配置文件，长期有效

该方法适用于长期通过 kubectl 操作集群， 一次配置，只要文件不修改就长期有效。
设置 kubectl 配置，修改以下命令中的密码、server访问地址、证书路径。
<pre>
kubectl config set-credentials default-admin <span class="hljs-string">--username</span>=admin <span class="hljs-string">--password</span>=6666o9oIB2gHD88882quIfLMy6666
kubectl config set-cluster default-cluster <span class="hljs-string">--server</span>=https://cls-66668888.ccs.tencent-cloud.com <span class="hljs-string">--certificate-authority</span>=/etc/kubernetes/cluster-ca.crt
kubectl config set-context default-system <span class="hljs-string">--cluster</span>=default-cluster <span class="hljs-string">--user</span>=default-admin
kubectl config use-context default-system
</pre>
配置完成，直接使用 kubectl 命令：
```
kubectl get nodes
NAME        STATUS    AGE
10.0.0.61   Ready     10h
```


### 设置 kubectl 命令自动补全
您可以通过配置 kubectl 自动补全，提高可使用性。
```shell
source <(kubectl completion bash)
```
