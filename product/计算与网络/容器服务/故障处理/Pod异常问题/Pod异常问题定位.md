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
	<td><code>Error</code></td>	<td>Pod 启动过程中发生错误。</td>
	</tr>
	<tr>
	<td><code>NodeLost</code></td>	<td>Pod 所在节点失联。</td>
	</tr>
	<tr>
	<td><code>Unkown</code></td>	<td>Pod 所在节点失联或其他未知异常。</td>
	</tr>
	<tr>
	<td><code>Waiting</code></td>	<td> Pod 等待启动。</td>
	</tr>
	<tr>
	<td><code>Pending</code></td>	<td>Pod 等待被调度。</td>
	</tr>
	<tr>
	<td><code>ContainerCreating</code></td>	<td>Pod 容器正在被创建。</td>
	</tr>
	<tr>
	<td><code>Terminating</code></td>	<td> Pod 正在被销毁。</td>
	</tr>
	<tr>
	<td><code>CrashLoopBackOff</code></td>	<td>容器退出，Kubelet 正在将它重启。</td>
	</tr>
	<tr>
	<td><code>InvalidImageName</code></td>	<td>无法解析镜像名称。</td>
	</tr>
	<tr>
	<td><code>ImageInspectError</code></td>	<td>无法校验镜像。</td>
	</tr>
	<tr>
	<td><code>ErrImageNeverPull</code></td>	<td>策略禁止拉取镜像。</td>
	</tr>
	<tr>
	<td><code>ImagePullBackOff</code></td>	<td>正在重试拉取。</td>
	</tr>
	<tr>
	<td><code>RegistryUnavailable</code></td>	<td>连接不到镜像中心。</td>
	</tr>
	<tr>
	<td><code>ErrImagePull</code></td>	<td>通用的拉取镜像出错。</td>
	</tr>
	<tr>
	<td><code>CreateContainerConfigError</code></td>	<td>不能创建 Kubelet 使用的容器配置。</td>
	</tr>
	<tr>
	<td><code>CreateContainerError</code></td>	<td>创建容器失败。</td>
	</tr>
	<tr>
	<td><code>RunContainerError</code></td>	<td>启动容器失败。</td>
	</tr>
	<tr>
	<td><code>PreStartHookError</code></td>	<td>执行 preStart hook 报错。</td>
	</tr>
	<tr>
	<td><code>PostStartHookError</code></td>	<td>执行 postStart hook 报错。</td>
	</tr>
	<tr>
	<td><code>ContainersNotInitialized</code></td>	<td>容器没有初始化完毕。</td>
	</tr>
	<tr>
	<td><code>ContainersNotReady</code></td>	<td>容器没有准备完毕。</td>
	</tr>
	<tr>
	<td><code>ContainerCreating</code></td>	<td>容器创建中。</td>
	</tr>
	<tr>
	<td><code>PodInitializing</code></td>	<td>Pod 初始化中。</td>
	</tr>
	<tr>
	<td><code>DockerDaemonNotReady</code></td>	<td>Docker 还没有完全启动。</td>
	</tr>
	<tr>
	<td><code>NetworkPluginNotReady</code></td>	<td>网络插件还没有完全启动。</td>
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
- [容器进程主动退出](https://cloud.tencent.com/document/product/457/43148)
