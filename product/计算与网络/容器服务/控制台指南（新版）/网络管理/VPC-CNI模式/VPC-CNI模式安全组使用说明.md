

您可以通过下述方式为 VPC-CNI 模式创建的弹性网卡绑定指定的安全组。

## 前提条件

- IPAMD 组件版本在 v3.2.0+（可通过镜像 tag 查看）。
- IPAMD 组件启动了安全组能力，启动参数：`--enable-security-groups`（默认未启用）。
- 目前仅支持多 Pod 共享网卡模式。

## IPAMD 开启安全特性

- 修改现存的 tke-eni-ipamd deployment：`kubectl edit deploy tke-eni-ipamd -n kube-system`。
- 执行以下命令，在 `spec.template.spec.containers[0].args` 中加入启动参数。
  修改后，ipamd 会自动重启并生效。
	生效后，存量网卡没有关联安全组的会按以下策略绑定安全组，增量网卡则都会绑定以下安全组。
```yaml
- --enable-security-groups
# 如果希望默认继承自主网卡/实例的安全组，则不添加 security-groups 参数
- --security-groups=sg-xxxxxxxx,sg-xxxxxxxx
```



## 功能逻辑

- 若未设置启动参数 `--security-groups`，或者其值为空，则各节点安全组继承自节点实例绑定的安全组。
- 特性开启以后，如果设置了 `--security-groups`，则各节点安全组设置为该安全组集合。
- 执行以下命令可查看节点安全组。其中 `spec.securityGroups` 域包含了节点安全组信息。
  ```
	kubectl get nec <nodeName> -oyaml
	```
	执行以下命令可修改节点安全组，修改后即刻生效。
	```
	kubectl edit nec <nodeName> 
	```
- 特性开启以后，节点同步时，存量网卡如果没绑定安全组，则会绑定节点安全组。如果绑定了则不做操作，保留原绑定。增量网卡都会绑定节点安全组。
