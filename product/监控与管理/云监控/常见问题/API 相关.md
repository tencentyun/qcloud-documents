### 如何调整 GetMonitorData 接口每秒频率上限？
GetMonitorData 接口默认调用频率上限为 20次/秒，超过该频率会导致接口调用失败。若调用接口出现如下报错： “您当前每秒请求 `20+n` 次，超过了每秒频率上限 `20`次，请稍后重试" 。可进入 [云监控接口调频申请页](https://cloud.tencent.com/apply/p/ndlajjkklws)  申请提高 GetMonitorData 接口频率上限。


###  如何解决 GetMonitorData 接口报错 ？
GetMonitorData 接口常见报错 ：<font color="red">**Unauthorized operation or the instance has been destroyed** </font>（未经授权的操作或实例已被销毁）

出现该错误提示主要有以下几个原因：
**1. 未找到该实例。**请检查实例是否已销毁、实例 ID 是否输入正确或实例是否属于当前账号。
**2. 您当前账户无该实例权限**。请参见 [云监控-访问管理](https://cloud.tencent.com/document/product/248/45428#.E4.BA.91.E7.9B.91.E6.8E.A7.E7.9B.B8.E5.85.B3.E7.9A.84.E4.BA.91.E4.BA.A7.E5.93.81.E7.AD.96.E7.95.A5) 并使用主账户授予当前子账户权限。
**3. Instance.N 参数错误。**请参见 [拉取指标监控数据](https://cloud.tencent.com/document/api/248/31014) 的入参说明及示例检查 Intances.N, Dimensions.N 数组、字段名和实例维度等参数是否填写正确。


