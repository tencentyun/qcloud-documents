## 操作场景

本文档指导您设置节点 Label。

## 使用限制

<li> \*kubernetes\* 和 \*qcloud\* 相关标签禁用编辑和删除。</li>
<li> \*kubernetes\* 和 \*qcloud\* 标签为保留键，不支持添加。</li>
<li> 当前仅支持单个节点设置 Label，不支持批量设置。</li>


## 操作步骤

<dx-tabs>
::: 控制台设置节点Label
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击 **[集群](https://console.cloud.tencent.com/tke2/cluster?rid=1)**，进入集群管理页面。
3. 选择需要设置节点 Label 的集群 ID/名称，进入集群详情。
4. 在左侧导航栏中，选择**节点管理** > **节点**，进入“节点列表” 页面。
5. 选择需要设置 Label 的节点行，单击**更多** > **编辑标签**。
6. 在弹出的 “编辑 Label” 窗口中，编辑 Label，单击**确定**。如下图所示：
![](https://main.qcloudimg.com/raw/c7ae35397224f60986027556d315c00b.png)
:::
::: Kubectl设置节点Label
1. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
2. 执行以下命令，设置节点 Label。
```shell
kubectl label nodes <node-name> <label-key>=<label-value>
```
3. 执行以下命令，查看节点 Label。
```shell
kubectl get nodes --show-labels
```
返回类似如下信息：
<dx-codeblock>
::: shell
NAME           STATUS    ROLES     AGE       VERSION         LABELS
172.17.124.5   Ready     <none>    12d       v1.10.5-tke.3   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=QCLOUD,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/region=sh,failure-domain.beta.kubernetes.io/zone=200001,kubernetes.io/hostname=172.17.124.5
172.17.124.8   Ready     <none>    12d       v1.10.5-tke.3   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=QCLOUD,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/region=sh,failure-domain.beta.kubernetes.io/zone=200001,kubernetes.io/hostname=172.17.124.8
:::
</dx-codeblock>

:::
</dx-tabs>

