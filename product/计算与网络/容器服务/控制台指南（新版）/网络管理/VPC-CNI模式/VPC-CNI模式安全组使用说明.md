

您可以通过下述方式为 VPC-CNI 模式创建的弹性网卡绑定指定的安全组。

## 前提条件

- IPAMD 组件版本在 v3.2.0+（可通过镜像 tag 查看）。
- IPAMD 组件启动了安全组能力，启动参数：`--enable-security-groups`（默认未启用）。
- 目前仅支持多 Pod 共享网卡模式。

## IPAMD 组件开启安全组特性

### tke-eni-ipamd 组件版本 >= v3.5.0

1. 登录 [容器服务控制台](https://console.qcloud.com/tke2)，单击左侧导航栏中**集群**。
2. 在“集群管理”页面，选择需开启安全组的集群 ID，进入集群详情页。
3. 在集群详情页面，选择左侧**组件管理**。
4. 在组件管理页面中，找到**eniipamd**组件，选择**更新配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/8ba9443b2e1da9800b429060adf89416.png)
5. 在更新配置页面，勾选**安全组**。
6. 如果希望继承主网卡安全组，则不指定安全组，否则需指定安全组，最后点击完成。
![](https://qcloudimg.tencent-cloud.cn/raw/998ed9fc25b90cd5d413faae7d7919d7.png)

### tke-eni-ipamd 组件版本 < v3.5.0 或组件管理中无 eniipamd 组件

- 修改现存的 tke-eni-ipamd deployment：
```
kubectl edit deploy tke-eni-ipamd -n kube-system
```
- 执行以下命令，在 `spec.template.spec.containers[0].args` 中加入启动参数。
修改后，ipamd 会自动重启并生效。
生效后，存量节点上的辅助弹性网卡没有关联安全组的会按以下策略绑定安全组，如果绑定了也会与设置的安全组强同步，除非之前已开启特性，节点安全组已设置。增量节点的弹性网卡则都会绑定以下安全组。
```yaml
- --enable-security-groups
# 如果希望默认继承自主网卡/实例的安全组，则不添加 security-groups 参数
- --security-groups=sg-xxxxxxxx,sg-xxxxxxxx
```

### 存量节点同步网卡安全组设置的方法

 如果想让已设置安全组的存量节点也生效，需要手动禁用安全组，再开启来达到同步。以下为存量节点的同步方法：
 1. 给节点加上注解清空并禁用节点的弹性网卡绑定安全组,添加后，节点的存量弹性网卡会解绑所有安全组：
```shell
kubectl annotate node <nodeName> --overwrite tke.cloud.tencent.com/disable-node-eni-security-groups="yes"
```
 2. 重新设置为 no 后，则可以重新绑定以上策略配置的安全组：
```shell
kubectl annotate node <nodeName> --overwrite tke.cloud.tencent.com/disable-node-eni-security-groups="no"
```










## 功能逻辑

- 若未设置启动参数 `--security-groups`，或者其值为空，则各节点安全组继承自节点实例绑定的安全组。
- 特性开启以后，如果设置了 `--security-groups`，则各节点安全组设置为该安全组集合。
- 特性开启以后，如果变更 `--security-groups` 参数，增量节点安全组设置会与全局参数同步，存量节点安全组设置不会改变，若需同步存量节点安全组设置，则需禁用节点安全组再开启，来达到同步。操作方法见 [IPAMD 组件开启安全组特性](https://cloud.tencent.com/document/product/457/50360#ipamd-.E7.BB.84.E4.BB.B6.E5.BC.80.E5.90.AF.E5.AE.89.E5.85.A8.E7.BB.84.E7.89.B9.E6.80.A7)。
- 安全组设置的优先级与节点安全组设置的顺序一致，若继承自主网卡，则与主网卡保持一致。
- 执行以下命令可查看节点安全组。其中 `spec.securityGroups` 域包含了节点安全组信息。
```
kubectl get nec <nodeName> -oyaml
```
执行以下命令可修改节点安全组，修改后即刻生效。
```
kubectl edit nec <nodeName> 
```
- 特性开启以后，节点同步时，存量网卡如果没绑定安全组，则会绑定节点安全组。存量网卡的安全组会与节点安全组强同步，保证与设置的节点安全组保持一致。增量网卡都会绑定节点安全组。
