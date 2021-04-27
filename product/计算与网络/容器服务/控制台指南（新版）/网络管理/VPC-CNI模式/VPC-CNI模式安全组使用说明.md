

您可以通过下述方式为 VPC-CNI 模式创建的弹性网卡绑定指定的安全组。

## 前提条件

- IPAMD 组件版本在 v3.2.0+（可通过镜像 tag 查看）。
- IPAMD 组件启动了安全组能力，启动参数：`--enable-security-groups`（默认未启用）。
- 目前仅支持多 Pod 共享网卡模式。

## IPAMD 组件角色添加安全组接口访问权限

1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/policy)，选择左侧的【策略】。
2. 在“策略”详情页中，单击【新建自定义策略】。
3. 在弹出的选择创建方式窗口中，单击【按策语法创建】，进入选择策略模板页面。
4. 选择“空白模板”，并单击【下一步】，进入编辑策略页面。
5. 在编辑策略页面，确认策略名称、输入以下策略语法后，单击【完成】即可创建自定义策略。
>? 策略可命名为 `SecurityGroupsAccessForIPAMD`。
```
{
        "version": "2.0",
        "statement": [
            {
                "action": [
                    "cvm:AssociateNetworkInterfaceSecurityGroups",
                    "cvm:DisassociateNetworkInterfaceSecurityGroups"
                ],
                "resource": "*",
                "effect": "allow"
            }
        ]
}
```
6. 在【访问管理控制台】>【[角色](https://console.cloud.tencent.com/cam/role)】中搜索 IPAMD 组件的相关角色 `IPAMDofTKE_QCSRole`，单击角色名称进入角色详情页面。
7. 在权限设置中，单击【关联策略】。
8. 在弹出的关联策略窗口中，勾选已创建的自定义策略 `SecurityGroupsAccessForIPAMD`。单击【确定】，完成为 IPAMD 组件角色添加安全组接口访问权限操作。

## IPAMD 组件开启安全特性

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
