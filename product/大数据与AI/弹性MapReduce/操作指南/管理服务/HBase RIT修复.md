## 功能介绍
HBase RIT 修复适用于在 HBase（HBase 版本在2.2.0及以上）集群中遇到 RIT（Region-In-Transition）问题，且 Region 处于较⻓时间的 RIT 状态时，对处于 FAILED_OPEN、FAILED_CLOSED、CLOSING 状态的 Region 进⾏修复。

## 操作步骤
1. 登录 [EMR 控制台](https://console.cloud.tencent.com/emr)，在集群列表中单击对应的**集群 ID/名称**进入集群详情页。
2. 在集群详情页中单击**集群服务**，然后选择 HBase 组件右上角**操作 > RIT 修复**，即可查看 RIT 状态的 Region 并对其进行修复。
![](https://qcloudimg.tencent-cloud.cn/raw/f25780276c81edc394bd568ad37b9e18.png)
3. 单击列表操作中**修复**，或者勾选需要修复的 Region 后单击**批量修复**，在RIT修复弹框页，确认相关信息。
4. 确认信息无误后，单击**确定**进行 RIT 修复。
5. RIT 修复执行进度和结果可在任务中心查看。

