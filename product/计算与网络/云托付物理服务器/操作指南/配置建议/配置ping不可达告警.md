## 操作场景
本文介绍如何配置 ping 不可达告警，可用于监控网络状态，及时发现网络中断等故障。


## 操作步骤

### 创建事件规则
1. 登录事件总线控制台，选择左侧导航栏中的 **[事件规则](https://console.cloud.tencent.com/eb/rule)**。
2. 在“事件规则”页面上方，选择**广州**地域及 **default** 事件集，并单击**新建规则**。
3. 在“新建事件规则”页面的“事件模式”步骤中，参考以下信息进行配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b362afcea0c0de43ee23b7ab60cba1ec.png)
主要配置如下，其余配置请按需选择：
 - **事件模式**：选择“云服务预设事件”。
 - **云服务类型**：选择“云服务器”。
 - **事件类型**：选择 “ping不可达”。
 - **事件模式预览**：若您仅希望某几台服务器接收告警，则请单击**编辑**。参考以下格式编辑告警事件，在 `subject` 字段中填写需要接收告警的服务器实例 ID。
```json
 {
  "source":"cvm.cloud.tencent",
  "type":[
    "cvm:ErrorEvent:PingUnreachable"
  ],
  "subject":["ins-mowubhsz","ins-mfsdajl"]
}
```
4. 单击**下一步**，进入“事件目标”步骤，参考以下信息进行配置。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/973d024432f51a6483f5d1b935325451.png)
 主要配置如下，其余配置请按需选择：
 - **触发方式**：选择“消息推送”。
5. 单击**完成**即可成功配置 ping 不可达告警。
<dx-alert infotype="explain" title="">
配置 ping 不可达告警后，如果在 OS 内手动关机、通过 BMC 手动关机，均会触发该告警。
</dx-alert>
