您可为网关类型为 NAT 型的专线网关配置 IP 转换和配置 IP 端口转换，具体操作如下：

## 配置 IP 转换
### 配置本端 IP 转换
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中，单击【专线网关】，进入管理页面。
3. 单击网关类型为 NAT 型专线网关 ID，进入详情页。
![](https://main.qcloudimg.com/raw/61ed3ea77cf82597f5bd525fee500dad.png)
4. 在专线网关详情页中，选择【本端 IP 转换】选项卡，进行本端 IP 转换配置，操作如下：
  1. **配置本端 IP 转换地址**
    - **新增**
       1. 在 IP 映射页左上角，单击【新增】。
 ![](https://main.qcloudimg.com/raw/272179c4b42889d1135b425b1d258262.png)
       2. 在弹框中，输入原 IP、映射 IP 及备注（可选），单击【确定】即可。
![](https://main.qcloudimg.com/raw/42172589f8ebd012cc9f2a6a3eec556a.png)
 >?新增本端 IP 转换规则，默认添加了 ALL PASS 的 ACL 规则，即本端 IP 转换对所有专用通道生效，您可以编辑本端 IP 转换的 ACL 规则，以改变本端 IP 转换的适用范围。
>
    - **修改**
在 IP 映射页中，单击 IP 转换规则所在行右侧的【修改 IP 映射】，即可编辑本端 IP 转换规则的原 IP、映射 IP 和备注（可选），单击【确认】 后，IP 转换生效。
![](https://main.qcloudimg.com/raw/3c494598938fed7c420eca5fb8bed248.png)
    - **删除**
  在 IP 映射页中，单击 IP 转换规则所在行右侧的【删除】， 并确认操作即可，IP 转换规则删除后将联动删除该 IP 转换规则下的 ACL 规则。
 2. **配置本端 IP 转换的网络 ACL 规则**
 >!当专线网关同时配置对端 IP 转换时，本端 IP 转换 ACL 规则的**目的 IP** 需要填写**对端 IP 转换的映射 IP** ，而不是原 IP。
 >
ACL 规则支持 TCP 和 UDP 协议，本端 IP 映射 ACL 规则支持源端口、目的 IP、目的端口。
其中，端口、IP 不填代表 ALL；当协议选择 ALL 时，端口和 IP 默认均选择 ALL。
    - **新增**
       1. 在 IP 映射页中，单击 IP 映射规则所在行右侧的【编辑 ACL 规则】，进入 ACL 规则编辑状态。
       2. 在已有 ACL 规则底部，单击【新增一行】，完成 ACL 规则的新增后，单击【保存】即可。
![](https://main.qcloudimg.com/raw/16abb569b8c167cfdab3c27fb34f3e44.png)
    - **修改**
       1. 单击 IP 映射规则所在行右侧的【编辑 ACL 规则】，进入 ACL 规则编辑状态，修改完 ACL 规则后，单击【保存】即可。
![](https://main.qcloudimg.com/raw/71a7d06ead7676dd14f06a2a4f968c5b.png) 
       2. 您也可直接单击<img src="https://main.qcloudimg.com/raw/b2347f733a56962b935f57d086824290.png" style="margin:-3px 0px;width:15px">展开 IP 映射规则，单击 ACL 规则所在行右侧的【修改】，完成修改后保存操作即可。
![](https://main.qcloudimg.com/raw/615d98ecc7d818cca9a616f0c3a37131.png) 
    - **删除**
       1. 在 IP 映射页中，单击 IP 映射规则所在行右侧的【编辑 ACL 规则】，进入 ACL 规则编辑状态，单击 ACL 规则右侧的【删除】，并保存操作，即可删除该 ACL 规则。
![](https://main.qcloudimg.com/raw/685ca8069048ecf2fa1a388654aad808.png)
       2. 您也可直接单击<img src="https://main.qcloudimg.com/raw/b2347f733a56962b935f57d086824290.png" style="margin:-3px 0px;width:15px">展开 IP 映射规则，单击 ACL 规则所在行右侧的【删除】，并确认操作即可。
![](https://main.qcloudimg.com/raw/a79cb5e695771c806e91b55c9155bffc.png)

**规则限制**
 - 原 IP 必须在私有网络 CIDR 范围内。
 - 映射 IP 不可以在专线网关所在私有网络 CIDR 范围内。
 - 原 IP 唯一不可以重复，即私有网络内 1 个 IP 只能唯一映射为1个 IP。
 - 映射 IP 唯一不可以重复，即不支持多个私有网络 IP 映射为同1个 IP。
 - 原目的 IP 不支持广播地址（255.255.255.255）、D 类地址（224.0.0.0 - 239.255.255.255）、E 类地址（240.0.0.0 - 255.255.255.254）。
 - 专线网关的本端IP转换规则数上限为100条，每个本端 IP 转换最大支持20条 ACL 规则（如需提升配额，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)）。

### 配置对端 IP 转换
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中，单击【专线网关】，进入管理页面。
3. 单击网关类型为 NAT 型专线网关 ID，进入详情页。
![](https://main.qcloudimg.com/raw/61ed3ea77cf82597f5bd525fee500dad.png)
4. 在专线网关详情页中，选择【对端 IP 转换】选项卡，进行对端 IP 转换配置，操作如下：
 - **新增**
    1. 在 IP 映射页左上角，单击【新增】。
![](https://main.qcloudimg.com/raw/b19fdd3168a490a73ad2ed5e1fa1b494.png)
    2. 在弹框中，输入原 IP、映射 IP 及备注（可选），单击【确定】即可。
![](https://main.qcloudimg.com/raw/362404885ef7e18b2ae2d3af7883f779.png)
 - **修改**：单击 IP 转换规则所在行右侧的【修改 IP 映射】，即可修改对端 IP 转换规则的原 IP、映射 IP 和备注（可选），单击【确定】后 IP 转换生效。
 ![](https://main.qcloudimg.com/raw/7d9190677c7b27476bc5219fc3fe2089.png)
 - **删除**
 在 IP 映射页中，单击 IP 转换规则所在行右侧的【删除】，并确认操作即可。
 
**规则限制**
 - 映射 IP 不可以在专线网关所在私有网络 CIDR 范围内。
 - 原 IP 唯一不可以重复，即专线对端1个 IP 只能唯一映射为1个 IP。
 - 映射 IP 唯一不可以重复，即不支持多个专线对端 IP 映射为同1个 IP。
 - 原目的 IP 不支持广播地址（255.255.255.255）、D 类地址（224.0.0.0 - 239.255.255.255）、E 类地址（240.0.0.0 - 255.255.255.254）。
 - 专线网关的对端 IP 转换规则数上限为100条（如需提升配额，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)）。

## 配置 IP 端口转换
### 配置本端源 IP 端口转换
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中，单击【专线网关】，进入管理页面。
3. 单击网关类型为 NAT 型专线网关 ID，进入详情页。
![](https://main.qcloudimg.com/raw/61ed3ea77cf82597f5bd525fee500dad.png)
4. 在专线网关详情页中，选择【本端源 IP 端口转换】选项卡，进行本端源 IP 端口转换配置，操作如下：
 1. **配置本端源 IP 端口转换地址池**
    - **新增**
       1. 在映射 IP 池页左上角，单击【新增】。
![](https://main.qcloudimg.com/raw/51e5c340f4cbbc6d8027763eb2fef678.png)
        2. 在弹框中，输入映射 IP 池（支持 IP 或 IP 段，IP 段格式为 “A - B”）和备注（可选），新增 IP 池的 ACL 规则为 ALL DROP，需要额外编辑 ACL 规则才可以实现网络转换。
![](https://main.qcloudimg.com/raw/d6eb837b6e564195a2baab5eb77696ff.png) 
    - **修改**
在映射 IP 池页中，单击 IP 地址池所在行右侧的【修改映射 IP 池】，即可对此映射 IP 池的 IP 和备注进行修改。
![](https://main.qcloudimg.com/raw/a315499745732682f666a353a1ad7d65.png)
    - **删除**
在映射 IP 池页中，单击 IP 地址池所在行右侧的【删除】并确认操作，即可删除该地址池，地址池删除后，将自动删除地址池关联的 ACL 规则。
 2. **配置本端源 IP 地址池的网络 ACL 规则**
 >!当专线网关同时配置对端 IP 转换时，本端源 IP 端口转换 ACL 规则的**目的 IP** 需要填写**对端 IP 转换的映射 IP**，而不是原 IP。
>
ACL 规则支持配置协议（支持 TCP 或 UDP）、源 IP、源端口、目的 IP、目的端口。
    - **新增**
       1. 在映射 IP 池页中，单击 IP 地址池所在行右侧的【编辑 ACL 规则】，即可进入 ACL 规则编辑状态。
        2. 在已有 ACL 规则底部，单击【新增一行】，完成 ACL 规则的新增后，单击【保存】即可。
![](https://main.qcloudimg.com/raw/8190fbfe5346034a60d754c28a3162e5.png)
    - **修改**
        1. 在映射 IP 池页中，单击 IP 地址池所在行右侧的【编辑 ACL 规则】，进入 ACL 规则编辑状态，修改完 ACL 规则后，单击【保存】即可。
![](https://main.qcloudimg.com/raw/b4c4ef797b1dd2b41a422ad58af78e95.png)
        2. 您也可直接单击<img src="https://main.qcloudimg.com/raw/b2347f733a56962b935f57d086824290.png" style="margin:-3px 0px;width:15px">展开 IP 地址池规则，单击 ACL 规则所在行右侧的【修改】，完成修改后保存操作即可。
![](https://main.qcloudimg.com/raw/fb81b50ccf1ab4d420ce029568f149d6.png)
    - **删除**
       1. 在映射 IP 池页中，单击 IP 地址池所在行右侧的【编辑 ACL 规则】，进入 ACL 规则编辑状态，单击规则右侧的【删除】并保存操作，即可删除该 ACL 规则。
![](https://main.qcloudimg.com/raw/81f37dca60b5349bc6fd15c967b0742d.png) 
        2. 您也可直接单击<img src="https://main.qcloudimg.com/raw/b2347f733a56962b935f57d086824290.png" style="margin:-3px 0px;width:15px">展开 IP 地址池规则，单击 ACL 规则所在行右侧的【删除】，并确认操作即可。
 ![](https://main.qcloudimg.com/raw/d3b358179719023ccad6f1e13371b212.png)

**规则限制**
 - IP 地址池不可以在专线网关所在私有网络的 CIDR 范围内。
 - 多个 IP 地址池的 ACL 规则不可以重叠，否则会导致网络地址转换冲突。
 - 多个 IP 地址池之间 IP 不可以重叠。
 - IP 地址池仅支持单 IP 或连续 IP，且连续 IP 的 /24 网段需保持一致，即支持“192.168.0.1 - 192.168.0.6”，不支持“192.168.0.1 - 192.168.1.2”。
 - 地址池不支持广播地址（255.255.255.255）、D 类地址（224.0.0.0 - 239.255.255.255）、E 类地址（240.0.0.0 - 255.255.255.254）。
 - 本端源 IP 端口转换最大支持100个 IP 地址池，每个地址池支持最大20条 ACL 规则（如需提升配额，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)）。

>?当本端 IP 转换和本端源 IP 端口转换冲突时，优先匹配本端 IP 转换。
>
### 配置本端目的 IP 端口转换
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧导航栏中，单击【专线网关】，进入管理页面。
3. 单击网关类型为 NAT 型专线网关 ID，进入详情页。
![](https://main.qcloudimg.com/raw/61ed3ea77cf82597f5bd525fee500dad.png)
4. 在专线网关详情页，选择【本端目的 IP 端口转换】选项卡，进行本端目的 IP 端口转换配置，操作如下：
 - **新增**
    1. 在 IP 端口映射页左上角，单击【新增】。
![](https://main.qcloudimg.com/raw/080dd2d1feb276f1dfe871aa34194cd8.png)
    2. 在弹框中，选择协议，输入原 IP 端口、映射后 IP 端口及备注，单击【确定】即可。
![](https://main.qcloudimg.com/raw/13d2a59a47f960d4fa0afeed4bcab9a4.png)
 - **修改**
在 IP 端口映射页中，单击 IP 端口映射所在行右侧的【修改 IP 端口映射】，即可修改此 IP 端口映射的映射关系及备注。
![](https://main.qcloudimg.com/raw/05fee1b43be789d66960df88d5109481.png)
 - **删除**
在 IP 端口映射页中，单击 IP 端口映射所在行【删除】，即可删除该映射。
 
**规则限制**
 - 原 IP 必须在专线网关所在私有网络 CIDR 范围之内。
 - 原 IP 端口唯一，即私有网络内同一 IP 端口只能唯一映射为一个 IP 端口。
 - 映射 IP 端口不可以在私有网络 CIDR 范围之内。
 - 映射 IP 端口不可以重复，即不存在一个 IP 端口映射多个私有网络 IP 端口。
 - 原 IP 和映射 IP 不支持广播地址（255.255.255.255）、D 类地址（224.0.0.0 - 239.255.255.255）、E 类地址（240.0.0.0 - 255.255.255.254）。
 - 本端目的 IP 端口转换最大支持100个 IP 端口映射（如需提升配额，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category)）。

