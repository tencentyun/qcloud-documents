

edgectl 是边缘节点管理工具，用于远程添加边缘节点。您可通过**节点管理** > **[脚本添加节点](https://cloud.tencent.com/document/product/457/42890#.E8.84.9A.E6.9C.AC.E6.B7.BB.E5.8A.A0.E8.8A.82.E7.82.B9)**操作获取该工具。



edgectl 提供了以下三个命令：
<table>
<thead>
<tr>
<th>命令</th>
<th>描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="#check">edgectl check</a></td>
<td>检查节点是否满足安装边缘节点的条件。</td>
</tr>
<tr>
<td><a href="#clear">edgectl clear</a></td>
<td>清理边缘节点。</td>
</tr>
<tr>
<td><a href="#install">edgectl install</a></td>
<td>安装边缘节点。</td>
</tr>
</tbody></table>




示例代码如下所示：
```
# ./edgectl -h
Usage:
   edgectl command [flags]
Available Commands:
   check        Check the edge node if to be add to clusters
   install      Install components to edge node
   clear        Clear edge node and recovery as usual

Flags:
   -h, --help   Help for edgectl
```

## edgectl  check 命令[](id:check)
### 含义
检查节点是否满足安装边缘节点的条件。check 项目包含内容：
- check 是否 root 用户。
- check 系统是否在支持范围内。
- check 交换区是否关闭。
- check 防火墙是否关闭。
- check ufw 是否关闭。
- check 端口是否被占用（check 的端口有 1443 {10249..10259} {51000..51020}）。
- check 是否开启 cgroup memory。
- check 节点之前是否安装过 kubeadm docker kubelet kubectl。

### 使用示例
```
# ./edgectl check 
Unit firewalld.service could not be found.
 WARN >> Port: 1443 occupied. Please turn off port service. 
...
 WARN >> The machine is not clean. Please reinstall the system. 
/usr/bin/kubelet
...
 >> Check Environment Finish! << 
```

例如本次执行示例代码后，提示了用户包含以下2个风险项目：
- 该边缘节点的端口1443已经被占用，请关闭其服务。
```
WARN >> Port: 1443 occupied. Please turn off port service.
```
- 节点有 kubelet 残留，建议重装节点系统，或执行 `edgectl  clear` 命令，进行清理操作。
```
WARN >> The machine is not clean. Please reinstall the system.
/usr/bin/kubelet ## 之前安装过kubelet
```

## edgectl  clear  命令[](id:clear)
### 含义
清理边缘节点。clear 命令会清除如下信息：
- 删除边缘节点上运行的所有容器和 Pod。
- 停止 kubelet、lite-apiserver、docker。
- 删除创建的网络信息和路由信息。
- 删除如下文件夹或文件：
 - /etc/kubernetes
 - /etc/docker
 - /root/.kube/config
 - /var/lib/kubelet >/dev/null 2>&1
 - /var/lib/cni
 - /etc/cni
 - /etc/sysconfig/kubelet/
 - /etc/sysconfig/lite-apiserver
 - /data/lite-apiserver >/dev/null 2>&1
 - /usr/lib/systemd/system/{kubelet,docker,lite-apiserver}.service
 
>!
- `edgectl clear` 会删除节点上的所有容器和 Pod，请谨慎执行。
- `edgectl clear` 会删除相关的文件夹或文件，请提前备份重要的资料。
- `edgectl install` 命令默认会执行 `edgectl clear`，执行 `edgectl install` 前请考虑 `edgectl clear` 删除的风险项。
 
### 使用示例
```
# ./edgectl clear
removed '/etc/kubernetes/cluster-ca.crt'
...
  >> Clear Node Complete! << 
```



## edgectl  install 命令[](id:install)
### 含义
安装边缘节点。
执行如下命令，安装边缘节点。
```
# ./edgectl install -h
Usage:
   edgectl install [flags]
Flags:
   -n,  --node-name     Node name in edge cluster. Must！## 节点的名字，必填
   -i,  --interface     Default network interface name. ## 节点的默认网卡名，可选项
```
- **--node-name**：边缘节点的名字，简写 `-n`。
	- 名字是必传选项，必须严格遵守 kubernetes 的 [node 节点的命名规范](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/)。
	- 请保证节点名在所加的集群里面唯一，否则会产生同一节点名所对应节点不断切换的问题。
	- 节点名不支持直接用 IP，否则会引起 `kubectl log` 和 `kubectl exec` 命令失效。
- **--interface**：边缘节点的默认网卡名，简写 `-i`。
	- 可选项，边缘节点的默认网卡名，填写错误会引起 flannel 和 coredns 组件异常。
	- 默认值为从腾讯云页面填的指定网卡名称，指定 `--interface` 将覆盖原默认值。


### 使用示例
```
# ./edgectl install  --node-name node-192.168.67.91 --interface eth0
NOTE:
      input: [ edgectl install --node-name node-192.168.67.91 --interface eth0 ] ## 输入参数
      logPath: /tmp/tke-edge-install.log ## 本次安装的输出的日志位置
      success-message: Install Edge Node: node-192.168.67.91 Success! ## 安装成功后的提示消息

 Start Install Edge Node node-192.168.67.91, Please Waiting...
 Waiting Running of the base service 
 Dockerd kubelet lite-apiserver has Running! ## Dockerd kubelet lite-apiserver 安装成功
   Install Edge Node: node-192.168.67.91 Success! ## 表示此边缘节点安装成功
```
- 此边缘节点安装执行完成后, 可执行命令 `kubectl -n kube-system get pod` 查看所有 Pod 是否 Running。
- `edgectl install` 命令**一小时有效**，可在有效期内多次添加不同的节点，如过期失效请重新进行 [脚本添加节点](https://cloud.tencent.com/document/product/457/42890#.E8.84.9A.E6.9C.AC.E6.B7.BB.E5.8A.A0.E8.8A.82.E7.82.B9) 操作请求新的 edgectl。
- 要是安装过程中无提示退出，请参见 NOTE 中提示的安装日志位置 `logPath: /tmp/tke-edge-install.log` 查看具体的错误。
- 执行完没有 `Install Edge Node: node-192.168.67.91 Success!` 则认为安装失败，请查看安装日志排错。

