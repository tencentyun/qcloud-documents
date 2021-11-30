本文介绍如何在腾讯云控制台上配置云点播 CDN 指标的监控和告警。

## 配置云点播 CDN 指标监控

### 步骤1：开通云点播
确认您的腾讯云账号已经开通云点播服务。如果尚未开通，请参见 [快速入门 - 步骤1](https://cloud.tencent.com/document/product/266/8757#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E4.BA.91.E7.82.B9.E6.92.AD) 进行操作。

### 步骤2：创建云监控 Dashboard
访问云监控控制台  [Dashboard 列表](https://console.cloud.tencent.com/monitor/dashboard2/dashboards) 页面，单击 【新建 Dashboard】页面，如下所示：
![](https://main.qcloudimg.com/raw/a22840b028b39c15ec6b5499c1e9f1b6.png)

### 步骤3：新建并配置图表[](id:step3)
1. 在新 Dashboard 的空白页面中，单击【新建图表】，如下所示：
![](https://main.qcloudimg.com/raw/8ac620012b8cfb37a4c030a228957664.png)
2. 在【指标】左侧下拉菜单中选择【云点播-CDN-域名】，右侧下拉框使用默认值【核心指标-带宽(Mbps)】，单击【筛选】该项右侧下拉框：
![](https://main.qcloudimg.com/raw/95a89b875efd804d16b2269db212c3ad.png)
3. 下拉菜单中，选择将被监控的域名，勾选想要进行监控的计费分区。示例：假设选中了一个域名在中国大陆地区的数据作为监控对象，右侧可以看到已勾选的监控对象列表，确认无误后单击【确认】按钮：
![](https://main.qcloudimg.com/raw/5a089d4e26c6b72825ef1b684a20ea7d.png)
4. 编辑界面展示被选中的监控对象的指标数据，其表的右侧【图表名】输入框是该图表的名称，可按自己的需要填写，这里我们使用默认值。单击左上角的【回退箭头】返回到 Dashboard 页面，如下所示：
![](https://main.qcloudimg.com/raw/d70c0e84ba1acb13de20c877893371f7.png)

### 步骤4：添加其它图表
1. 在 Dashboard 页面单击【新建】按钮，根据自身的需求重复 [步骤3](#step3) 的操作添加需要监控的其它指标。这里的例子中我们为相同监控对象添加了流量、HTTP 状态码4xx等监控。最后单击【保存】按钮保存 Dashboard：
![](https://main.qcloudimg.com/raw/a0647ad94eab40c5d1eb64a25ee001d3.png)
2. 在弹出的对话框中按需要填写 Dashboard 的名字。示例：假设我们的 Dashboard 专用于存放云点播相关的监控，所以取名为 VOD，单击【确认】保存，如下所示：
![](https://main.qcloudimg.com/raw/c5c5983776f115775f17f6f353a1491f.png)

### 步骤5：完成操作
之后可以在云监控控制台  [Dashboard 列表](https://console.cloud.tencent.com/monitor/dashboard2/dashboards) 页面看到 VOD 这个 Dashboard 的入口，可以将其设为默认 Dashboard，方便后续通过左侧菜单的 [默认 Dashboard](https://console.cloud.tencent.com/monitor/dashboard2/default) 页面入口来查看监控，如下所示：
![](https://main.qcloudimg.com/raw/5b84ea5689327629a1a38c4c602ac415.png)
## 配置云点播 CDN 指标告警
1. 访问 [告警策略](https://console.cloud.tencent.com/monitor/alarm2/policy) 页面，单击【新建】按钮创建新的告警策略。在配置页面中，【策略类型】一项选择云点播-CDN-域名，【告警对象】一项在右侧下拉框中选择想要进行告警的对象（同上文配置指标监控 [步骤3](#step3) 中的描述），如下所示：
![](https://main.qcloudimg.com/raw/be8c2bdfebf952d9d41eeb3c20d32fb7.png)
2. 除了【策略类型】和【告警对象】之外，其它方面的配置与云监控通用的告警策略配置方式完全相同，具体请参见云监控 [新建告警策略](/document/product/248/50398) 。
