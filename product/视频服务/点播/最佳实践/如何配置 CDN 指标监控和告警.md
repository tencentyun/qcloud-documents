本文介绍如何在腾讯云控制台上配置云点播 CDN 指标的监控和告警。

## 配置云点播 CDN 指标监控

### 步骤1：开通云点播

确认您的腾讯云账号已经开通云点播服务。如果尚未开通，请参考 [快速入门 - 步骤1](https://cloud.tencent.com/document/product/266/8757#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.BC.80.E9.80.9A.E4.BA.91.E7.82.B9.E6.92.AD) 进行操作。

### 步骤2：创建云监控 Dashboard

访问云监控控制台  [Dashboard 列表](https://console.cloud.tencent.com/monitor/dashboard2/dashboards) 页面，点击 【新建 Dashboard】页面，如下：

![](https://main.qcloudimg.com/raw/31da7c7c60ac13e0f93021c8b1f19e3d.png)

### 步骤3：新建并配置图表

- 在新 Dashboard 的空白页面中，点击【新建图表】，如下：

![](https://main.qcloudimg.com/raw/4ad1c84a3556377cd652c8ac585da956.png)

- 在图表配置页面中，在【指标】这一项的左侧下拉菜单中选择 云点播-CDN-域名，右侧下拉框使用默认值 核心指标-带宽(Mbps)；然后点击【筛选】这一项的右侧下拉框，如下：

![](https://main.qcloudimg.com/raw/95a89b875efd804d16b2269db212c3ad.png)

- 在弹出的界面中，展开下拉菜单，找到想要进行监控的域名；再次展开菜单，勾选想要进行监控的计费分区。这里的例子中我们选中了一个域名在中国大陆地区的数据作为监控对象。右侧可以看到已勾选的监控对象列表，确认无误后点击【确认】按钮，如下：

![](https://main.qcloudimg.com/raw/d74a80a6b91159b3ea6decb43e1bcd46.png)

- 此时图表编辑界面将展示被选中的监控对象的指标数据；右侧的【图表名】输入框是该图表的名称，可以按自己的需要填写，这里我们使用默认值；点击左上角的回退箭头返回到 Dashboard 页面，如下：

![](https://main.qcloudimg.com/raw/d70c0e84ba1acb13de20c877893371f7.png)

### 步骤4：添加其它图表

- 在 Dashboard 页面点击【新建】按钮，根据自身的需求重复步骤3的操作添加需要监控的其它指标。这里的例子中我们为相同监控对象添加了流量、HTTP 状态码4xx等监控。最后点击【保存】按钮保存 Dashboard，如下：

![](https://main.qcloudimg.com/raw/a0647ad94eab40c5d1eb64a25ee001d3.png)

- 在弹出的对话框中按需要填写 Dashboard 的名字。这里的例子中我们的 Dashboard 专用于存放云点播相关的监控，所以取名为 VOD，点击【确认】保存，如下：

![](https://main.qcloudimg.com/raw/ef548edf31f70ffd2776f2df5fd99926.png)

### 步骤5：完成

之后可以在云监控控制台  [Dashboard 列表](https://console.cloud.tencent.com/monitor/dashboard2/dashboards) 页面看到 VOD 这个 Dashboard 的入口，可以将其设为默认 Dashboard，方便后续通过左侧菜单的 [默认 Dashboard](https://console.cloud.tencent.com/monitor/dashboard2/default) 页面入口来查看监控，如下：

![](https://main.qcloudimg.com/raw/5b84ea5689327629a1a38c4c602ac415.png)

## 配置云点播 CDN 指标告警

访问 [告警策略](https://console.cloud.tencent.com/monitor/alarm2/policy) 页面，点击【新建】按钮创建新的告警策略。在配置页面中，【策略类型】一项选择云点播-CDN-域名，【告警对象】一项在右侧下拉框中选择想要进行告警的对象（同上文配置指标监控步骤3中的描述），如下：

![](https://main.qcloudimg.com/raw/be8c2bdfebf952d9d41eeb3c20d32fb7.png)

除了【策略类型】和【告警对象】之外，其它方面的配置与云监控通用的告警策略配置方式完全相同，具体请参考云监控 [新建告警策略](/document/product/248/50398) 一文，此处不再赘述。
