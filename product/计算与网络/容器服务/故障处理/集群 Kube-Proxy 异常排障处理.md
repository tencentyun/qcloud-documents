
在使用 TKE 集群服务的过程中，某些场景下，可能会出现服务访问不通的问题，如果确认后端 Pod 访问正常，则可能是由于 kube-proxy 组件版本较低，导致节点上的 iptables 或 ipvs 服务转发规则下发失败。本文档整理了低版本 kube-proxy 存在的若干问题，并给出相应的修复指引。若本文档无法解决您所遇到的问题，请 [联系我们](https://cloud.tencent.com/document/product/457/59560) 来寻求帮助。

## kube-proxy 未能正确适配节点 iptables 后端

#### 错误信息示例
```shell
Failed to execute iptables-restore: exit status 2 (iptables-restore v1.8.4 (legacy): Couldn't load target 'KUBE-MARK-DROP':No such file or directory
```

#### 问题原因
1.  kube-proxy 在执行 iptables-restore 时，所依赖的 `KUBE-MARK-DROP` Chain 不存在，导致同步规则失败后退出。 `KUBE-MARK-DROP` Chain 由 kubelet 负责维护。
2.  一些高版本的 OS 使用的 iptables 后端为 nft，而低版本 kube-proxy 使用的 iptables 后端为 legacy。当低版本 kube-proxy 运行在高版本 OS 上时，会因为 iptables 后端不匹配而读不到 `KUBE-MARK-DROP`  Chain。高版本 OS 包括：
    -   tlinux2.6 (tk4)
    -   tlinux3.1
    -   tlinux3.2
    -   CentOS8
    -   Ubuntu20

#### 修复指引
升级 kube-proxy，需要按如下逻辑处理：
<table>
<thead>
  <tr>
    <th>TKE 集群版本</th>
    <th>修复策略</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>&gt;1.18</td>
    <td>不存在此问题，无需修复</td>
  </tr>
  <tr>
    <td>1.18</td>
    <td>升级 kube-proxy 到 v1.18.4-tke.26 及以上</td>
  </tr>
  <tr>
    <td>1.16</td>
    <td>升级 kube-proxy 到 v1.16.3-tke.28 及以上</td>
  </tr>
  <tr>
    <td>1.14</td>
    <td>升级 kube-proxy 到 v1.14.3-tke.27 及以上</td>
  </tr>
  <tr>
    <td>1.12</td>
    <td>升级 kube-proxy 到 v1.12.4-tke.31 及以上</td>
  </tr>
  <tr>
    <td>1.10</td>
    <td>升级 kube-proxy 到 v1.10.5-tke.20 及以上</td>
  </tr>
</tbody>
</table>

>? TKE 最新版本信息，请参见 [TKE Kubernetes Revision 版本历史](https://cloud.tencent.com/document/product/457/9315)。

---
## kube-proxy 操作 iptables 锁相关的问题

### 其它组件未挂载 iptables 锁导致并发写入失败

#### 错误信息示例
```shell
Failed to execute iptables-restore: exit status 1 (iptables-restore: line xxx failed)
```

#### 问题原因
1.  iptables 相关命令（如 iptables-restore）在向内核写入 iptables 规则时，为了避免多个实例并发写入，会利用 file lock 来做同步，linux 下该文件一般为：`/run/xtables.lock`
2.  对于要调用 iptables 相关命令的 Pod，如 kube-proxy, kube-router 以及客户侧的 HostNetwork Pod，如果没有挂载该文件，可能发生如上并发写入的错误。

#### 修复指引
对于要调用 iptables 相关命令的 Pod 需要将主机侧 `/run/xtables.lock` 文件挂载到 Pod 中，配置方式如下：
```yaml
        volumeMounts:
        -   mountPath: /run/xtables.lock
          name: xtables-lock
          readOnly: false
      volumes:
      -   hOStPath:
          path: /run/xtables.lock
          type: FileOrCreate
        name: xtables-lock
```

### iptables-restore 版本低导致不支持阻塞写入

#### 错误信息示例
```shell
Failed to execute iptables-restore: exit status 4 (Another app is currently holding the xtables lock. Perhaps you want to use the -w option?)
```

#### 问题原因
1.  iptables 相关命令（如 iptables-restore）在向内核写入 iptables 规则时，为了避免多个实例并发写入，会利用 file lock 来做同步，iptables-restore 在执行时首先尝试获取 file lock，如果当前有其它进程持有锁，则退出。
2.  该报错是一个软错误，kube-proxy 会在下个同步周期（或下个 Service 相关的事件触发时）再次尝试执行，如果重试多次都获取不到锁，则表现为规则同步时延较大。
3.  高版本 iptables-restore 提供了一个 `-w(--wait)` 选项，如设置 -w=5 时，iptables-restore 会在拿锁操作阻塞 5s，这使得 5s 内一旦其它进程释放锁，iptables-restore 可以继续操作。

#### 修复指引
1.  如果 kube-proxy 为节点侧二进制部署，可以通过升级节点 OS 版本来提升 iptables-restore 版本，需要按如下逻辑处理：
<table>
<thead>
  <tr>
    <th>节点 OS</th>
    <th>升级目标版本</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>CentOS</td>
    <td>7.2 及以上</td>
  </tr>
  <tr>
    <td>Ubuntu</td>
    <td>20.04 及以上</td>
  </tr>
  <tr>
    <td>Tencent Linux</td>
    <td>2.4 及以上</td>
  </tr>
</tbody>
</table>
2.  如果 kube-proxy 为集群内 Daemonset 部署，则可以通过升级 kube-proxy 来提升 iptables-restore 版本，需要按如下逻辑处理：
<table>
<thead>
  <tr>
    <th>TKE 集群版本</th>
    <th>修复策略</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>&gt; 1.12</td>
    <td>不存在此问题，无需修复</td>
  </tr>
  <tr>
    <td>1.12</td>
    <td>升级 kube-proxy 到 v1.12.4-tke.31 及以上</td>
  </tr>
  <tr>
    <td>&lt; 1.12</td>
    <td>升级 TKE 集群到高版本</td>
  </tr>
</tbody>
</table>
>? TKE 最新版本信息，请参见 [TKE Kubernetes Revision 版本历史](https://cloud.tencent.com/document/product/457/9315)。

### 其它组件持有 iptables 锁时间过长

#### 错误信息示例
```shell
Failed to ensure that filter chain KUBE-SERVICES exists: error creating chain "KUBE-EXTERNAL-SERVICES": exit status 4: Another app is currently holding the xtables lock. Stopped waiting after 5s.
```

#### 问题原因
1.  iptables 相关命令（如 iptables-restore）在向内核写入 iptables 规则时，为了避免多个实例并发写入，会利用 file lock 来做同步，iptables-restore 在执行时首先尝试获取 file lock，如果当前有其它进程持有锁，则阻塞特定时间（取决于-w 参数的值，默认5s），该时间内拿到锁，则继续操作，拿不到则退出。
2.  该报错说明其它组件持有 iptables file lock 时间超过 5s。

#### 修复指引
尽量减小其它组件持有 iptables file lock 的时间，如 TKE 控制台组件管理提供的 NetworkPolicy（kube-router）组件，其低版本持有 iptables 锁的时间较长，可以通过升级来解决，当前最新版为：`v1.3.2`

---
## kube-proxy 到 kube-apiserver 连接异常

#### 错误信息示例
```shell
Failed to list *core.Endpoints: Stream error http2.StreamError{StreamID:0xea1, Code:0x2, Cause:error(nil)} when reading response body, may be caused by closed connection. Please retry.
```

#### 问题原因
低版本 Kubernetes 调用 go http2 的包存在一个 bug，该 bug 导致客户端会使用到一个 apiserver 的已经关闭的连接，kube-proxy 踩中这个 bug 后，会导致同步规则失败。更多详情可参考 [Issue87615](https://github.com/kubernetes/kubernetes/issues/87615)、[PR95981](https://github.com/kubernetes/kubernetes/pull/95981)。

#### 修复指引
升级 kube-proxy，需要按如下逻辑处理：
<table>
<thead>
  <tr>
    <th>TKE 集群版本</th>
    <th>修复策略</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>&gt; 1.18</td>
    <td>不存在此问题，无需修复</td>
  </tr>
  <tr>
    <td>1.18</td>
    <td>升级 kube-proxy 到 v1.18.4-tke.26 及以上</td>
  </tr>
  <tr>
    <td>&lt; 1.18</td>
    <td>升级 TKE 集群到高版本</td>
  </tr>
</tbody>
</table>

>? TKE 最新版本信息，请参见 [TKE Kubernetes Revision 版本历史](https://cloud.tencent.com/document/product/457/9315)。

## kube-proxy 首次启动发生 panic，重启后正常
#### 错误信息示例
```
panic: runtime error: invalid memory address or nil pointer dereference
[signal SIGSEGV: segmentation violation code=0x1 addr=0x50 pc=0x1514fb8]
```

#### 问题原因
1.  该版本 kube-proxy 社区的代码存在 bug，初始化时统计加载的内核模块有缺失，导致有变量未初始化即使用。
2.  日志不够详尽，未输出是否能使用 ipvs 模式的判断结果。更多详情可参考 [Issue89729](https://github.com/kubernetes/kubernetes/issues/89729)、[PR89823](https://github.com/kubernetes/kubernetes/pull/89823)、[PR89785](https://github.com/kubernetes/kubernetes/pull/89785)。

#### 修复指引
升级 kube-proxy，需要按如下逻辑处理：
<table>
<thead>
  <tr>
    <th>TKE 集群版本</th>
    <th>修复策略</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>&gt; 1.18</td>
    <td>不存在此问题，无需修复</td>
  </tr>
  <tr>
    <td>1.18</td>
    <td>升级 kube-proxy 到 v1.18.4-tke.26 及以上</td>
  </tr>
  <tr>
    <td>&lt; 1.18</td>
    <td>不存在此问题，无需修复</td>
  </tr>
</tbody>
</table>

>? TKE 最新版本信息，请参见 [TKE Kubernetes Revision 版本历史](https://cloud.tencent.com/document/product/457/9315)。

---
## kube-proxy 不间断 panic
#### 错误信息示例
```shell
Observed a panic: "slice bounds out of range" (runtime error: slice bounds out of range)
```

#### 问题原因
kube-proxy 社区的代码存在 bug，在执行 iptables-save 时将标准输出和标准错误定向到同一个 buffer 中，而这两者的输出先后顺序是不确定的，这导致 buffer 中的数据格式不符合预期，在处理时发生 panic。更多详情可参考 [Issue78443](https://github.com/kubernetes/kubernetes/issues/78443)、[PR78428](https://github.com/kubernetes/kubernetes/pull/78428)。

#### 修复指引
 升级 kube-proxy，需要按如下逻辑处理：
<table>
<thead>
  <tr>
    <th>TKE 集群版本</th>
    <th>修复策略</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>&gt; 1.14</td>
    <td>不存在此问题，无需修复</td>
  </tr>
  <tr>
    <td>1.14</td>
    <td>升级 kube-proxy 到 v1.14.3-tke.27 及以上</td>
  </tr>
  <tr>
    <td>1.12</td>
    <td>升级 kube-proxy 到 v1.12.4-tke.31 及以上</td>
  </tr>
  <tr>
    <td>&lt; 1.12</td>
    <td>不存在此问题，无需修复</td>
  </tr>
</tbody>
</table>

>? TKE 最新版本信息，请参见 [TKE Kubernetes Revision 版本历史](https://cloud.tencent.com/document/product/457/9315)。
---

## kube-proxy ipvs 模式下周期性占用较高 CPU

#### 问题原因
kube-proxy 频繁刷新节点 Service 转发规则导致，触发原因：
-   kube-proxy 周期性同步规则较为频繁。
-   业务 Service 或 Pod 变更频繁。

#### 修复指引
如果是 kube-proxy 周期性同步规则较为频繁导致，需要调整其相关参数，旧版本 kube-proxy 的参数默认为：
```yaml
--ipvs-min-sync-period=1s（最小刷新间隔1s）
--ipvs-sync-period=5s（5s周期性刷新）
```
这导致 kube-proxy 每5s刷新一次节点 iptables 规则，消耗较多 CPU，推荐改为：
```yaml
--ipvs-min-sync-period=0s（发生事件实时刷新）
--ipvs-sync-period=30s（30s周期性刷新） 
```
以上配置值为参数默认值，您可以自行选择是否配置这些参数。
