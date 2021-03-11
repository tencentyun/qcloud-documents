## 定义

edgectl是边缘节点管理工具，用于远程添加边缘节点，通过节点管理【脚本添加节点】操作获取该工具。

edgectl提供了三个命令, 如下：
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

## edgectl  check 命令
### 含义
> 检查节点是否满足安装边缘节点的条件。

check项目包含：
- check 是否root用户
- check 系统是否在支持范围内
- check 交换区是否关闭
- check 防火墙是否关闭
- check ufw是否关闭
- check 端口是否被占用（check的端口有 1443 {10249..10259} {51000..51020}）
- check 是否开启cgroup memory
- check 节点之前是否安装过kubeadm docker kubelet kubectl

### 举例
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
比如本次执行，提示了用户2个风险项目：
- 该边缘节点的端口1443已经被占用, 请关闭其服务
> ` WARN >> Port: 1443 occupied. Please turn off port service.`

- 节点有 kubelet 残留，建议重装节点系统，或执行 `edgectl  clear` 命令，进行清理操作。
> ` WARN >> The machine is not clean. Please reinstall the system. ` 
  `/usr/bin/kubelet` ## 之前安装过kubelet;

## edgectl  clear  命令
### 含义
> 清理边缘节点

 会清除如下信息：
 - 删除边缘节点上运行的所有容器和Pod;
 - 停止kubelet、lite-apiserver、docker；
 - 删除创建的网络信息和路由信息；
 - 删除如下文件夹或文件夹：
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
### 举例
```
# ./edgectl clear
removed '/etc/kubernetes/cluster-ca.crt'
...
 >> Clear Node Complete! << 
```
>!
- edgectl clear 会删除节点上的所有容器和Pod，请谨慎执行。
- edgectl clear 会删除相关的文件夹或文件，请提前备份重要的资料。
- edgectl install 命令默认会执行edgectl clear，执行edgectl install 前请考虑edgectl clear删除的风险项。


## edgectl  install 命令
### 含义
> 安装边缘节点

```
# ./edgectl install -h
Usage:
  edgectl install [flags]
Flags:
  -n,  --node-name     Node name in edge cluster. Must！## 节点的名字，必填
  -i,  --interface     Default network interface name. ## 节点的默认网卡名，可选项
```
有两个选项：
- --node-name：边缘节点的名字，简写-n
	- 名字是必传选项，必须严格遵守kubernetes的[node节点的命名规范](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/)；
	- 特别提示，一定要保证节点名在所加的集群里面唯一，不然会产生同一节点名所对应节点不断切换的问题；
	- 节点名不支持直接用IP，会在用节点name请求coredsn解析其对应IP时出错，引起kubectl log 和kubectl exec 命令失效；

- --interface： 边缘节点的默认网卡名, 简写-i
	- 可选项，边缘节点的默认网卡名，填写错误会引起flannel和coredns组件异常；
	- 默认值为从腾讯云页面填的`指定网卡`名称，指定--interface将覆盖原默认值；
### 举例
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
- 此边缘节点安装执行完成后, 可执行`kubectl -n kube-system get pod` 查看所有Pod是否Running。
- edgectl install 命令`一小时有效`，失效请重新到腾讯云页面请求新的edgectl;
- 要是安装过程中无提示退出，请参看`NOTE中提示的安装日志位置 logPath: /tmp/tke-edge-install.log` 查看具体的错误。
- 执行完没有`Install Edge Node: node-192.168.67.91 Success!` 都认为安装失败，请查看安装日志排错。
- edgectl install 一小时有效，用户可封装在一小时内进行批量添加边缘节点。
