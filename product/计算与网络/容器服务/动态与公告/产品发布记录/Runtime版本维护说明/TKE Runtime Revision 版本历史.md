## Containerd
### TKE containerd 1.6.9 patch releases
<table>
<thead>
  <tr>
    <th>时间</th>
    <th>版本</th>
    <th>更新内容</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2023-01-09</td>
    <td>containerd-1.6.9-tke.2</td>
    <td>修复社区 bug <a href="https://github.com/containerd/containerd/pull/7848">#7848</a>，重启 containerd 后再重启 kubelet 会导致 Pod 重启。 </td>
  </tr>
  <tr>
    <td>2022-12-01</td>
    <td>containerd-1.6.9-tke.1</td>
    <td>同社区版本，添加了安装、升级脚本。</td>
  </tr>
</tbody>
</table>

### TKE containerd 1.4.3 patch releases

<table>
<thead>
  <tr>
    <th>时间</th>
    <th>版本</th>
    <th>更新内容</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2022-10-27</td>
    <td>containerd-1.4.3-tke.2</td>
    <td>containerd 升级 ttrpc，避免 ttrpc 的 bug 导致 Pod Terminating。</td>
  </tr>
  <tr>
    <td>2021-06-22</td>
    <td>containerd-1.4.3-tke.1</td>
    <td>可以通过修改 containerd 的配置 [plugins.cri.cni] interface_name=eth1，支持自定义 sandbox 网卡名称。</td>
  </tr>
</tbody>
</table>

### （停止维护）TKE containerd 1.3.4 patch releases
<table>
<thead>
  <tr>
    <th>时间</th>
    <th>版本</th>
    <th>更新内容</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2022-01-19</td>
    <td>containerd-1.3.4-tke.6</td>
    <td>修复重启 containerd 后容器状态错误导致 Pod Terminating 的问题。</td>
  </tr>
  <tr>
    <td>2021-11-18</td>
    <td>containerd-1.3.4-tke.5</td>
    <td>containerd 支持开启 writable cgroup，支持不开启特权启动 systemd 容器。</td>
  </tr>
  <tr>
    <td>2021-06-25</td>
    <td>containerd-1.3.4-tke.4</td>
    <td>containerd 支持使用 xfs quota 来限制容器 rwlayer 的容量。</td>
  </tr>
  <tr>
    <td>2020-12-08</td>
    <td>containerd-1.3.4-tke.3</td>
    <td>containerd kill 容器时支持使用 image 中配置的 signal。</td>
  </tr>
  <tr>
    <td>2020-09-10</td>
    <td>containerd-1.3.4-tke.2</td>
    <td>可以通过修改 containerd 的配置 [plugins.cri.cni] interface_name=eth1，支持自定义 sandbox 网卡名称。</td>
  </tr>
  <tr>
    <td>2020-04-27</td>
    <td>containerd-1.3.4-tke.1</td>
    <td>修复 containerd 没处理 runc 返回值（delete container not found）导致容器删除失败以及 Pod Terminating 的问题。</td>
  </tr>
</tbody>
</table>

## Docker
### TKE docker 19.03.9 patch releases
<table>
<thead>
  <tr>
    <th>时间</th>
    <th>版本</th>
    <th>更新内容</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2022-11-01</td>
    <td>docker v19.3.9-tke.1</td>
    <td>修复 docker 丢失 containerd event 后，Pod 状态卡在 Terminating 的问题。保证 docker 和 containerd 数据不一致时，容器可以被正常 kill 掉。</td>
  </tr>
  <tr>
    <td>2021-01-04</td>
    <td>docker 19.03.9</td>
    <td>同社区版本。</td>
  </tr>
</tbody>
</table>

### （停止维护）TKE docker 18.06.3 patch releases
<table>
<thead>
  <tr>
    <th>时间</th>
    <th>版本</th>
    <th>更新内容</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>2022-03-10</td>
    <td>docker v18.6.3-ce-tke.4</td>
    <td><li>升级 runc 到 1.0.0-rc95，避免 <a href="https://nvd.nist.gov/vuln/detail/CVE-2019-16884">CVE-2019-16884</a>。</li><li>docker 支持正确识别 runc 的版本，减少错误日志的输出。可以通过 docker info 来确认 runc 的 commit id，之前的版本使用 runc 1.0.2 看到 commit 为 N/A。</li></td>
  </tr>
  <tr>
    <td>2021-06-22</td>
    <td>docker v18.6.3-ce-tke.3</td>
    <td>当 event 丢失之后保证容器仍然可以被删除。通过命令 <code>id=$(docker run -d busybox top); kill -9 $(pidof docker-containerd) && pkill top; docker stop $id</code> 可以验证，老版本 docker 会得到一个无法删除的容器，新版 docker 可以正确 docker stop 掉容器。</td>
  </tr>
  <tr>
    <td>2021-01-14</td>
    <td>docker 18.06.3-tke.2</td>
    <td>修复 grpc 社区 bug <a href="https://github.com/grpc/grpc-go/pull/2818">#2818</a>，delete container 可能长时间卡住，导致 docker 不再处理之后的 event，在 docker18 中添加 timeout，避免 event 不被处理。</td>
  </tr>
  <tr>
    <td>2020-08-13</td>
    <td>docker 18.06.3-tke.1</td>
    <td><li>修复重启 containerd 可能会导致 grpc 收到 cancel 的问题。</li><li>修复 exec 连接未关闭导致的事件阻塞。</li></td>
  </tr>
</tbody>
</table>
