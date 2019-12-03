>? 目前共享带宽包处于内测阶段，如需使用，请提交 [内测申请](https://cloud.tencent.com/act/apply/bwp_apply)。

## 创建带宽包
### 限制说明
设备带宽包用户可以提 [工单申请](https://console.cloud.tencent.com/workorder/category) 修改账户类型为上移版本，以使用 IP 带宽包。

### 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航的【共享带宽包】。
3. 选择地域，单击左上角的【+新建】。
4. 在弹窗中，输入名称、选择计费类型，单击【确定】完成创建。
![](https://main.qcloudimg.com/raw/23c1b760951981842d57c53aa504bdfa.png)
5. 创建完成后，为了防止产生高额费用，建议您为带宽包内的资源设置带宽上限。可参考如下操作：
 - EIP 设置带宽上限：
    1. 登录 [EIP 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
    2. 在操作栏下，选择【调整网络】进行带宽上限的设置。
    ![](https://main.qcloudimg.com/raw/d010dfeba3c9aae10a0a8f6fdb7a6aeb.png)
 - 负载均衡设置带宽上限：
    1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb/index?rid=1&type=2%2C3)。
    2. 在操作栏下，选择【更多】>【调整带宽】进行带宽上限的设置。
    ![](https://main.qcloudimg.com/raw/13139eeab16879feedc40e5ad14daaa7.png)
		
		
## 删除带宽包
>! 设备带宽包删除后，该地域所有云服务器、负载均衡网络计费模式都将变更为按流量计费，请您知悉。
>
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航的【共享带宽包】。
3. 选择地域，在指定带宽包的操作栏，单击【删除】，并确定操作即可。
![](https://main.qcloudimg.com/raw/d066d0473afd8f3d2a158081abc07bb7.png)

## 添加 EIP
创建共享带宽实例后，您需要将使用该共享带宽的 EIP 添加到共享带宽实例中。

### 限制说明
1. 仅支持按流量计费和按小时带宽计费的EIP加入带宽包，包年包月的 EIP 不支持加入带宽包。
2. 添加 EIP 到共享带宽包后，EIP 原本的计费模式将变更为共享带宽包模式，不额外收取流量费和带宽费用，但正常收取实例占有费。
3. EIP 的实例占有费与是否加入共享带宽包无关，当 EIP 绑定有实例时，IP 的占有费用减免。
4. 单个共享带宽包最多可添加100个 EIP。

### 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航的【共享带宽包】。
3. 选择地域，在列表中找到目标共享带宽包实例，单击实例 ID 进入详情页。
4. 在详情页的“带宽包资源”模块，单击【+添加资源】。
5. 在弹窗中，选择资源类型和资源实例，单击【确认】即可。
![](https://main.qcloudimg.com/raw/80ab4f9301b49cdb34d3f04ba3e1be39.png)

## 移除 EIP
您可以移出共享带宽实例中的 EIP。EIP 移出共享带宽实例后，EIP 将恢复为加入共享带宽实例前的带宽峰值和计费方式。

### 限制说明
带宽包内的 EIP 移除后，计费模式将统一变更为按流量计费。

### 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧导航的【共享带宽包】。
3. 选择地域，在列表中找到目标共享带宽包实例，单击实例 ID 进入详情页。
4. 在详情页的“带宽包资源”模块，选择您要移出带宽包的 EIP，单击【移除资源】，并确认操作即可。
![](https://main.qcloudimg.com/raw/cc95861a9884f409e58b592165ba8760.png)
