## 操作步骤
### 步骤1: 新建 NAT 网关
1. 打开 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?rid=1)，单击 **新建**。（确保所选区域与云桌面所在区域相同）
![](https://qcloudimg.tencent-cloud.cn/raw/5ef1bfb7c0034c3f6e9d3d35ceaf663b.png)
2. 输入网关名称，所属网络选择云桌面所在 VPC，网关类型及出带宽上限根据企业实际需求进行选择（创建完成后可更改），弹性 IP 选择 **新建弹性 IP** ，确认无误后单击下方 **立即开通**。
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/2aae202d4671740d15140db0f98d7057.png" />
3. 确认信息无误后，单击 **确认订单**。
<img style="width:600px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/405ff9204a834e868ec96d6ddf3be410.png" />
4. 完成 NAT 网关创建。
![](https://qcloudimg.tencent-cloud.cn/raw/6cea97c518e881c09c57574a7b1eb96c.png)

### 步骤2: 配置路由表
1. 打开 [路由表控制台](https://console.cloud.tencent.com/vpc/route?rid=1)，单击对应的路由表，编辑路由表。
![](https://qcloudimg.tencent-cloud.cn/raw/7b728d1743adb0392997b998ff5b124b.png)
2. 单击 **新增路由策略**。
![](https://qcloudimg.tencent-cloud.cn/raw/46e41b38235995cd1585f9bdad7dea0f.png)
3. 新增路由目的端填写“0.0.0.0/0”、下一跳类型选择 **NAT 网关**，下一跳选择刚才创建的 NAT 网关。
![](https://qcloudimg.tencent-cloud.cn/raw/6861503fb9af71966c6040e781baf0a9.png)
>!目的端填写“0.0.0.0/0”代表将所有出网流量都指向 NAT 网关。
4. 检查确认新建的路由策略处于**启用状态**，此时可在云桌面内实现访问互联网。
![](https://qcloudimg.tencent-cloud.cn/raw/eac1bd3744c1790e14dc32da5230d546.png)
