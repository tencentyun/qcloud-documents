按照自建 K8S 集群安装 LogListener 部署完成后，就可以通过创建 LogConfig 或者通过控制台去设置采集配置，开始日志采集了
如果出现日志采集异常，首先按照下面的流程自查一下
### 1. 确认 logconfig 状态
 - 查看集群所有的采集配置：kubectl get logconfig
 - 查看具体某一个采集配置： kubectl get logconfig xxx -o yaml
 - 查看 logconfig 同步的状态，status 非 Synced 状态都是异常的，异常信息会在 reason 里面，正常都是 success 的状态。
   如上 logconfig 的状态同步是成功的，那么采集异常的原因就是其他方面的。如下图所示:
![](https://qcloudimg.tencent-cloud.cn/raw/ffbc202c6c56603bff704ca6bd74457d.jpeg)
想要进一步了解同步错误的原因，可以看下 cls-provisioner 的日志

### 2. 查看 cls-provisioner 日志
 - 确定 cls-provisioner 的 Pod: kubectl get pods -n kube-system -o wide |grep cls-provisioner
 - 查看日志: kubectl logs cls-provisioner-xxx -n kube-system
如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8780c5adc9c7a5f79bf87417217beadc.png)
查看 cls-provisione 的日志，来看同步错误的具体原因。
>!cls-provisioner 组件的作用是和 CLS 服务端通信，将 logconfig 采集配置经过转换，同步到 CLS 服务端，这样采集器才能从服务端获取到采集配置，进而进行正常日志采集。

### 3. 查看采集端日志
如果采集配置同步正常，但是日志还是采集有异常，可以具体看下采集端的相关日志。
 - 查看软连是否建立成功。
我们以采集标准输出为例：
会在/var/log/tke-log-agent/<采集配置名称(logconfig 名称)>/stdout-docker-json 下创建需要采集的 Pod 的标准输出日志的软连，创建好之后才能正常采集。
![](https://qcloudimg.tencent-cloud.cn/raw/16c564af4065fa7f7728d2a4d21db965.jpeg)
我们是以 Docker 为例的，如果 runtime 是 containerd，那么路径是/var/log/tke-log-agent/<采集配置名称(logconfig 名称)>/stdout-containerd。
采集 contianer file 的软连建立方式如下：
/var/log/tke-log-agent/<采集配置名称(logconfig 名称)>/<pod_uid>
如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/fa4372a1971fb7c625366f4494246934.png)
确认按照上面示例的软连是否建立 OK，如果未建立，则是有异常的。如果建立成功，则要继续看下采集器 loglistener 的日志
 - 查看采集器 loglistener 日志。
kubectl get pods -n kube-system -o wide |grep tke-log-agent
首先找到日志采集异常 Pod 对应宿主机上的 tke-log-agent 的 Pod，然后查看 loglistener 日志
kubectl logs tke-log-agent-xxx -n kube-system -c loglistener
![](https://qcloudimg.tencent-cloud.cn/raw/c15b99a09b5838c4f7706200f4329ed1.jpeg)
确定是否有如上图所示类似 **readFile logs send succ!|topicid** 的字样，如果有，则表示日志成功采集到对应的 topic 了；如果没有如上的字样，那说明采集有问题，可以联系相关研发人员。
如果已经采集到了 topic，但是检索不到，可以先看下是否打开 topic 的全文索引。
