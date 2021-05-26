### 如何调整 GetMonitorData 接口每秒频率上限？
GetMonitorData 接口默认调用频率上限为 20次/秒，超过该频率会导致接口调用失败。若调用接口出现如下报错： “您当前每秒请求 `20+n` 次，超过了每秒频率上限 `20`次，请稍后重试”。可进入 [云监控接口调频申请页](https://cloud.tencent.com/apply/p/ndlajjkklws)  申请提高 GetMonitorData 接口频率上限。


###  如何解决 GetMonitorData 接口报错 ？
GetMonitorData 接口常见报错 ：<font>**Unauthorized operation or the instance has been destroyed** </font>（未经授权的操作或实例已被销毁）

出现该错误提示主要有以下几个原因：
**1. 未找到该实例。**请检查实例是否已销毁、实例 ID 是否输入正确或实例是否属于当前账号。
**2. 您当前账户无该实例权限**。请参见 [云监控-访问管理](https://cloud.tencent.com/document/product/248/45428#.E4.BA.91.E7.9B.91.E6.8E.A7.E7.9B.B8.E5.85.B3.E7.9A.84.E4.BA.91.E4.BA.A7.E5.93.81.E7.AD.96.E7.95.A5) 并使用主账户授予当前子账户权限。
**3. Instance.N 参数错误。**请参见 [拉取指标监控数据](https://cloud.tencent.com/document/api/248/31014) 的入参说明及示例检查 Intances.N, Dimensions.N 数组、字段名和实例维度等参数是否填写正确。

### GetMonitorData 接口如何查询项目下所有实例的监控数据？
GetMonitorData 接口限制说明：
- GetMonitorData 接口单次调用仅支持单种产品、单个指标，如果要跨产品类型查询，或跨指标查询，需要多次调用。
- GetMonitorData 接口单次调用支持查询多个实例，但不支持根据项目 ID 查询，需要填写明确的实例 ID 列表。

如果业务需要拉取某个项目下所有实例监控数据，可以参考以下两种方法：
#### 方法一：
   进入[云监控 - Dashboard](https://console.cloud.tencent.com/monitor/dashboard2/dashboards) 配置图表，选择实例对象时勾选某项目下全部实例。保存图表后，在图表右上角找到“数据导出”，即可下载监控数据的 csv 文件。
#### 方法二：
1. 调用云产品的开放 API 根据项目 ID 查询出实例列表（例如 cvm 的 [查看实例列表](https://cloud.tencent.com/document/product/213/15728)）。
2. 填写 GetMonitorData 接口的 Instances 参数，实现一次调用拉取项目下所有实例的监控数据。
		
### 如何处理 GetMonitorData 接口请求数据结果为空？
请检查：
1. Instances.N.Dimensions.N.Name 参数所填是否与 [监控指标](https://cloud.tencent.com/document/product/248/6140) 文档所对应。（需要注意大小写一致，例如某些指标需要填小写的“instanceid”，而非“InstanceId”）
2. EndTime 是否与当前时间间隔太短。由于监控数据计算可能存在短暂延时，建议 EndTime 在当前时间基础上向前偏移1～2分钟。
