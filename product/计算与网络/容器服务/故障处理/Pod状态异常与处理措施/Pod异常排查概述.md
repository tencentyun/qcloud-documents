为满足一定的业务需求，用户往往需要对容器服务集群进行一系列复杂的自定义配置。而当集群中的 Pod 出现某种异常时，可能一时无法直接通过异常状态准确定位异常原因。  

基于以上现象，您可参考 [Pod 异常问题](https://cloud.tencent.com/document/product/457/42945#.E9.97.AE.E9.A2.98.E5.AE.9A.E4.BD.8D) 系列文档进行问题排查、定位及解决。

## 常用命令

排查过程的常用命名如下：

* 查看 Pod 状态：
```
kubectl get pod <pod-name> -o wide
```
* 查看 Pod 的 yaml 配置：
```
kubectl get pod <pod-name> -o yaml
```
* 查看 Pod 事件：
```
kubectl describe pod <pod-name>
```
* 查看容器日志：
```
kubectl logs <pod-name> [-c <container-name>]
```

## Pod 状态

下表中列举了 Pod 的状态信息：
<table>
	<tr>
	<th>状态</th> <th>描述</th>
	</tr>
	<tr>
	<td>Error</td>	<td>Pod 启动过程中发生错误。</td>
	</tr>
	<tr>
	<td>NodeLost</td>	<td>Pod 所在节点失联。</td>
	</tr>
	<tr>
	<td>Unkown</td>	<td>Pod 所在节点失联或其他未知异常。</td>
	</tr>
	<tr>
	<td>Waiting</td>	<td> Pod 等待启动。</td>
	</tr>
	<tr>
	<td>Pending</td>	<td>Pod 等待被调度。</td>
	</tr>
	<tr>
	<td>ContainerCreating</td>	<td>Pod 容器正在被创建。</td>
	</tr>
	<tr>
	<td>Terminating</td>	<td> Pod 正在被销毁。</td>
	</tr>
	<tr>
	<td>CrashLoopBackOff</td>	<td>容器退出，Kubelet 正在将它重启。</td>
	</tr>
	<tr>
	<td>InvalidImageName</td>	<td>无法解析镜像名称。</td>
	</tr>
	<tr>
	<td>ImageInspectError</td>	<td>无法校验镜像。</td>
	</tr>
	<tr>
	<td>ErrImageNeverPull</td>	<td>策略禁止拉取镜像。</td>
	</tr>
	<tr>
	<td>ImagePullBackOff</td>	<td>正在重试拉取。</td>
	</tr>
	<tr>
	<td>RegistryUnavailable</td>	<td>连接不到镜像中心。</td>
	</tr>
	<tr>
	<td>ErrImagePull</td>	<td>通用的拉取镜像出错。</td>
	</tr>
	<tr>
	<td>CreateContainerConfigError</td>	<td>不能创建 Kubelet 使用的容器配置。</td>
	</tr>
	<tr>
	<td>CreateContainerError</td>	<td>创建容器失败。</td>
	</tr>
	<tr>
	<td>RunContainerError</td>	<td>启动容器失败。</td>
	</tr>
	<tr>
	<td>PreStartHookError</td>	<td>执行 preStart hook 报错。</td>
	</tr>
	<tr>
	<td>PostStartHookError</td>	<td>执行 postStart hook 报错。</td>
	</tr>
	<tr>
	<td>ContainersNotInitialized</td>	<td>容器没有初始化完毕。</td>
	</tr>
	<tr>
	<td>ContainersNotReady</td>	<td>容器没有准备完毕。</td>
	</tr>
	<tr>
	<td>ContainerCreating</td>	<td>容器创建中。</td>
	</tr>
	<tr>
	<td>PodInitializing</td>	<td>Pod 初始化中。</td>
	</tr>
	<tr>
	<td>DockerDaemonNotReady</td>	<td>Docker 还没有完全启动。</td>
	</tr>
	<tr>
	<td>NetworkPluginNotReady</td>	<td>网络插件还没有完全启动。</td>
	</tr>
</table>


## 问题定位
您可根据 Pod 的异常状态，选择对应参考文档进一步定位异常原因：
- [Pod 一直处于 ContainerCreating 或 Waiting 状态](https://cloud.tencent.com/document/product/457/42946)
- [Pod 一直处于 ImagePullBackOff 状态](https://cloud.tencent.com/document/product/457/42947)
- [Pod 一直处于 Pending 状态](https://cloud.tencent.com/document/product/457/42948)
- [Pod 一直处于 Terminating 状态](https://cloud.tencent.com/document/product/457/43238)
- [Pod 健康检查失败](https://cloud.tencent.com/document/product/457/43129)
- [Pod 处于 CrashLoopBackOff 状态](https://cloud.tencent.com/document/product/457/43130)
- [Pod 无限重启且流量异常](https://cloud.tencent.com/document/product/457/78805)
- [容器进程主动退出](https://cloud.tencent.com/document/product/457/43148)
