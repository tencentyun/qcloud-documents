## 操作场景
K3s 是开源、极轻量的 Kubernetes 发行版，目前为 CNCF 云原生计算基金会沙箱项目。K3s 对服务器计算资源要求较低，可单机运行。K3s 应用镜像已预置 Kubernetes-dashboard 可视化工具，方便您通过浏览器进行 Kubernetes 集群管理。本文介绍如何使用 K3s 应用镜像搭建 Kubernetes 集群管理环境。

<dx-alert infotype="explain" title="">
本文示例 K3s 镜像底层基于  CentOS 8.2 64位操作系统。应用镜像会进行不定期更新，请以购买页面实际镜像信息为准。
</dx-alert>


 


## 操作步骤
### 使用 K3s 镜像创建实例
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。配置如下图所示参数：
 - **地域、可用区**：建议选择靠近目标客户的地域及可用区，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
 - **镜像**：选择 “K3s” 应用镜像。
 - **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
 - **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
 - **购买时长**：默认1个月。
 - **购买数量**：默认1台。
2. 单击**立即购买**，并根据页面提示提交订单完成支付。

### 配置轻量应用服务器网络防火墙[](id:configFirewall)
1. 在“服务器”页面中，选择并进入实例详情页。
2. 选择**防火墙**页签，单击**添加规则**后根据界面提示放通9090端口。如下图所示：
<dx-alert infotype="explain" title="">
Kubernetes Dashboard 默认端口为9090。
</dx-alert>
<img src="https://main.qcloudimg.com/raw/6286b5633ff774117c266a78bd951fea.png"/>


### 登录 Kubernetes Dashboard
1.  在“服务器”页面中，选择并进入实例详情页。
2. 选择**应用管理**页签，进入应用管理详情页。您可以在此页面查看应用的各项配置信息。
3. [](id:Step3)在“应用内软件信息”栏中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" style="margin:-3px 0px">，复制 Kubernetes Dashboard 的管理员 TOKEN。如下图所示：
 ![](https://main.qcloudimg.com/raw/4c6d21f54dab5b3f027d09a6536951d9.png)
4. 在“应用内软件信息”栏中，单击**登录**。
5. 在弹出的登录窗口中，粘贴并执行 [步骤3](#Step3) 获取的命令，按 **Enter**。
6. [](id:Step6)记录返回结果 TOKEN 值。如下图所示：
![](https://main.qcloudimg.com/raw/3af2c618709b64d9d4dc616f01908512.png)
7. 在“应用内软件信息”栏中获取“访问地址”，并使用浏览器访问，进入 Kubernetes Dashboard。
8. 在登录页面中，输入 [步骤6](#Step6) 获取的 TOKEN 后，单击 **Sign in**。如下图所示：
![](https://main.qcloudimg.com/raw/a8e923c3012570704e8745cd013ca726.png)
登录成功后，即可使用 Kubernetes Dashboard 进行集群管理操作。

## 相关操作

### 增加集群节点
使用 K3s 应用镜像创建的实例即为集群 Master 节点。您可参考本步骤，向集群中增加其他 Node 节点。

1. 进入实例详情页，选择**防火墙**页签，参考 [配置轻量应用服务器网络防火墙](#configFirewall) 步骤放通 `TCP:6443` 端口。
2. 在“应用内软件信息”栏中，单击**登录**。
3. 在弹出的登录窗口中，执行以下命令，加入集群节点 IP。
```
k3s-add-node {node-ip}
```
<dx-alert infotype="explain" title="">
- Master 节点操作系统为 CentOS 8.2，建议您添加同地域同可用区下的其他轻量应用服务器实例作为集群 Node 节点。您可先使用 CentOS 8.2 系统镜像参考 [快速创建 Linux 实例](https://cloud.tencent.com/document/product/1207/44548) 创建实例，再通过以上命令将实例加入集群作为 Node 节点。
- Node 节点需与 Master 节点内网互通。
同账号下同一地域内的不同轻量应用服务器默认内网互通。更多轻量应用服务器内网连通能力介绍，请参见 [内网连通性说明](https://cloud.tencent.com/document/product/1207/50103#IntranetUnicom)。
</dx-alert>
示例命令如下：
```
[lighthouse@VM-5-100-centos ~]$ k3s-add-node 10.0.5.158
```
返回信息如下所示：
```
Please ensure firewall rule(TCP:6443) of master node has been allowed!
root@10.0.5.158's password:
```
4. 输入待加入节点的 `root` 账户密码，并按 **Enter**。待节点初始化结束后，将会加入集群。
<dx-alert infotype="explain" title="">
若您未设置或忘记 `root` 账户密码，可参考 [重置密码](https://cloud.tencent.com/document/product/1207/44575) 进行设置。
</dx-alert>


### 修改 NodePort
默认 NodePort 范围为30000 - 32767。某些情况下，因为网络策略限制，您可能需要修改 NodePort 的端口范围，可参考以下步骤完成修改：

1. 进入实例详情页，选择**防火墙**页签，参考 [配置轻量应用服务器网络防火墙](#configFirewall) 步骤放通修改的 NodePort。例如 `30000-42767` 端口。
2. 在实例详情页的“远程登录”中，单击**登录**。
3. 执行以下命令，编辑 `k3s.service` 配置文件。
```
sudo vi /etc/systemd/system/k3s.service
```
4. 按 **i** 进入编辑模式，找到 `ExecStart` 并增加 `--service-node-port-range` 参数指定 NodePort。例如：
```
ExecStart=/usr/local/bin/k3s server --write-kubeconfig-mode=644 --service-node-port-range=30000-42767
```
修改完成后，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f2942d70f5499b99eb1b93f26a2a2f3f.png)
5. 按 **Esc** 输入 **:wq** 保存修改并退出编辑模式。
6. 执行以下命令，并输入 `root` 账户密码重启 K3s 服务，使配置生效。
```shell
systemctl daemon-reload && systemctl restart k3s
```


### 域名与 DNS 解析设置
您可以给自己的网站设定一个单独的域名。用户可以使用易记的域名访问您的网站，而不需要使用复杂的 IP 地址。有些用户搭建网站仅用于学习，那么可使用 IP 直接访问网站，但不推荐这样操作。

如果您已有域名或者想要通过域名来访问您的网站，请参考以下步骤：
1. 通过腾讯云 [购买域名](https://dnspod.cloud.tencent.com/?from=qcloud)，具体操作请参考 [域名注册](https://cloud.tencent.com/document/product/242/9595)。
2. 进行 [网站备案](https://cloud.tencent.com/product/ba?from=qcloudHpHeaderBa&fromSource=qcloudHpHeaderBa)。 
域名指向中国境内服务器的网站，必须进行网站备案。在域名获得备案号之前，网站是无法开通使用的。您可以通过腾讯云免费进行备案，审核时长请参考 [备案审核](https://cloud.tencent.com/document/product/243/19650)。
3. 通过腾讯云 [DNS解析 DNSPod](https://cloud.tencent.com/product/cns?from=qcloudHpHeaderCns&fromSource=qcloudHpHeaderCns) 配置域名解析。具体操作请参考 [A 记录](https://cloud.tencent.com/document/product/302/3449)，将域名指向一个 IP 地址（外网地址）。

### 开启 HTTPS 访问
可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的网站安装 SSL 证书并开启 HTTPS 访问。
