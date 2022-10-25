Kubernetes 页面基于 CIS Kubernetes Benchmark 标准展示 K8S 资产的基线合规情况，包括基线概览、检测信息、Kubernetes 检测项结果列表。
## 查看 Kubernetes 概览
1. 登录 [容器安全服务控制台](https://console.cloud.tencent.com/tcss)，在左侧导航中，单击**基线管理** > **Kubernetes**。
2. 在 Kubernetes 页面，基线概览窗口展示合规 K8S 检测项通过率占比以及严重、高危、中危、低危四个威胁等级的检测项数量。
>?检测项通过率计算逻辑为：通过的检测项数量/检测项总数。
>
![](https://main.qcloudimg.com/raw/30564c4cf4c142494542134cfbef5a0e.png)
3. 在 Kubernetes 页面，单击百分比中的**查看**，可在弹出的抽屉中查看 Kubernetes 资产的检测结果列表。
![](https://main.qcloudimg.com/raw/9dad3f454b2b290201e8ee9dc1a87456.png)
4. 在 Kubernetes 页面，单击搜索框，可通过“ID 和基线检查项”关键词对 Kubernetes 基线检测项的检测结果进行查询。
![](https://main.qcloudimg.com/raw/b2a3c9d120df76f8a65f4a68088b6dbf.png)
5. 在 Kubernetes 页面，单击![](https://main.qcloudimg.com/raw/21ff3bd68750cb41c5ce662a24629cb3.png)图标勾选所需的 Kubernetes 基线检测项后，单击**重新检测** > **确定**，将会对选中的 Kubernetes 基线检测项进行重新检测。
>?选定多个 Kubernetes 基线检测项，单击②处的**重新检测**，可进行批量重新检测。
>
![](https://qcloudimg.tencent-cloud.cn/raw/bf6ce95850123825400fc2b3aa64123e.png)

## 查看检测信息
1. 登录 [容器安全服务控制台](https://console.cloud.tencent.com/tcss)，在左侧导航中，单击**基线管理** > **Kubernetes**。
2. 在 Kubernetes 页面，检测信息窗口展示 Kubernetes 基线检测项最近一次的基线检测时间、检测耗时和自动检测周期配置。
![](https://qcloudimg.tencent-cloud.cn/raw/24547837e58e4bb2b85c5b34c53cf7d7.png)
3. 在 Kubernetes 页面，单击**重新检测**，可立即对 Kubernetes 基线检测项进行一次基线检测。
![](https://qcloudimg.tencent-cloud.cn/raw/3641b487f46035d401073e8bc615dd39.png)
4. 在 Kubernetes 页面，单击**基线设置**，可设置基线策略和基线忽略列表。
![](https://qcloudimg.tencent-cloud.cn/raw/4667c0ce9e42d2c0914c1da2b29450f4.png)

### 设置基线策略
基线策略设置展示当前资产检测的基线标准，基线检查项数量。
1. 在基线策略设置页面，可通过单击![](https://qcloudimg.tencent-cloud.cn/raw/1d06b60e53ef5b971de76fb26f686b85.png)图标开关开启或关闭当前基线标准的周期性检测。
2. 在基线策略设置页面，单击检测周期的**编辑**，弹出检测周期设置弹窗，可在检测周期设置弹窗中设定检测周期。
![](https://qcloudimg.tencent-cloud.cn/raw/87f5d039732921ae57da80f2ae7013e2.png)
3. 在检测周期设置弹窗，可设置检测周期为：1天、3天、7天，以及设定具体时间点。
![](https://main.qcloudimg.com/raw/866e9423fe9874bf3e61cb5800f1a5e1.png)
4. 单击**确定**，即可完成检测周期设置。

### 基线忽略列表
基线忽略列表展示了忽略的容器基线检测项。
1. 在基线忽略列表页面，单击搜索框，可通过“基线检测项、主机名称、主机 IP”关键词对 Kubernetes 基线检测项进行查询。
![](https://qcloudimg.tencent-cloud.cn/raw/a293399537a8f73d9d6f55374757cae9.png)
2. 在基线忽略列表页面，单击![](https://main.qcloudimg.com/raw/21ff3bd68750cb41c5ce662a24629cb3.png)图标勾选所需的 Kubernetes 资产后，单击**取消忽略**，将会对选中的 Kubernetes 基线检测项取消忽略。
>?检测项取消忽略后，检测内容将恢复正常检测。

## 查看检测结果列表
### 筛选刷新基线检测项
1. 登录 [容器安全服务控制台](https://console.cloud.tencent.com/tcss)，在左侧导航中，单击**基线管理** > **Kubernetes**。
2. 在 Kubernetes 页面，单击搜索框，可通过“基线检测项”关键词对 Kubernetes 基线检测项进行查询。
![](https://main.qcloudimg.com/raw/ef00b3ca988e983a3c7431bc5bfad558.png)
3. 在 Kubernetes 页面，单击左上角的类型下拉框，按类型对 Kubernetes 基线检测项进行筛选。
![](https://main.qcloudimg.com/raw/e4bebd2c178960f5aed6f8861fc71702.png)
4. 在 Kubernetes 页面，单击左上角的威胁等级下拉框，按威胁等级对 Kubernetes 基线检测项进行筛选。
![](https://main.qcloudimg.com/raw/fa546b8f0d32caf590f283c813b9aaac.png)
5. 在 Kubernetes 页面，单击操作栏右侧![](https://main.qcloudimg.com/raw/84b6cc4d2eabf9ed7fc0bea43503bb1d.png)图标，即可刷新Kubernetes 基线检测项。

### 重新检测基线检测项
1. 登录 [容器安全服务控制台](https://console.cloud.tencent.com/tcss)，在左侧导航中，单击**基线管理** > **Kubernetes**。
2. 在 Kubernetes 页面，单击![](https://main.qcloudimg.com/raw/21ff3bd68750cb41c5ce662a24629cb3.png)图标勾选所需 Kubernetes 基线检测项后，单击**重新检测** > **确认**，可对 Kubernetes 基线检测项进行重新检测。
>?选定多个 Kubernetes 基线检测项，单击②处的**重新检测**，可进行批量检测。
>
![](https://qcloudimg.tencent-cloud.cn/raw/9a2f20fabed43384b94a226cd10ccb17.png)

### 忽略基线检测项
1. 登录 [容器安全服务控制台](https://console.cloud.tencent.com/tcss)，在左侧导航中，单击**基线管理** > **Kubernetes**。
2. 在 Kubernetes 页面，击![](https://main.qcloudimg.com/raw/21ff3bd68750cb41c5ce662a24629cb3.png)图标勾选所需 Kubernetes 基线检测项后，单击**忽略** > **确定**，可对 Kubernetes 基线检测项进行忽略。
>?选定多个 Kubernetes 基线检测项，单击②处的**忽略**，可进行批量忽略。
>
![](https://qcloudimg.tencent-cloud.cn/raw/401e66e40e9572cdf1b98f0d39ed90ff.png)

### 自定义列表管理
1. 登录 [容器安全服务控制台](https://console.cloud.tencent.com/tcss)，在左侧导航中，单击**基线管理** > **Kubernetes**。
2. 在 Kubernetes 页面，单击![](https://main.qcloudimg.com/raw/d42b27540eef9bf90a9e30f96b500bf3.png)图标，弹出自定义列表管理弹窗，在弹窗中可以自定义设定列表管理。
3. 在自定义列表管理弹窗，选择所需的类型后，单击**确定**，即可完成设置自定义列表管理。
![](https://main.qcloudimg.com/raw/b53867c43a2bd9d5c14589987ecd8bc1.png)

#### 列表重点字段说明
1. ID：检测项ID，该ID全局唯一。
2. 基线检测项：检测内容，单击“ 基线检测项”，可查看检测项详情。
3. 类型：检测项的类型。
4. 基线标准：检测项所属基线标准。
5. 威胁等级：检测项的威胁等级定义，含严重、高危、中危、底危、提示。
6. 检测结果：展示当前检测项下通过的资产数量和未通过的资产数量。
7. 操作：重新检测和忽略。
