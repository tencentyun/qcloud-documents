腾讯云呼叫中心电话功能需要通信号码进行呼入/呼出，企业若已有号码可以与腾讯云呼叫中心对接。自有号码对接分为：自有固话 SIP_Trunk 对接与 [自有400号码对接](https://cloud.tencent.com/document/product/679/76428)。

腾讯云呼叫中心支持通过 SIP Trunk 的方式与企业自带的固话号码与进行对接，实现使用企业自有号码进行呼入和呼出。对接完成后企业自行与号码所属运营商结算该号码产生的通信费用，腾讯云呼叫中心不收取对接与号码产生的通信费用。

请联系您的号码运营商确认是否支持 SIP 中继，如不支持 SIP 中继，请咨询运营商能否协助变更为 SIP中继方式与腾讯云呼叫中心对接，如无法变更，您可购买网关设备和 SIP 服务搭建一套 SIP 中继服务与腾讯云呼叫中心对接。

### 步骤1：提交申请
进入 [腾讯云呼叫中心号码管理](https://console.cloud.tencent.com/ccc)，选择自有号码接入，单击**提交自有号码**。
![](https://qcloudimg.tencent-cloud.cn/raw/16fb131a87e90a616c6b91add8fe67df.png)

### 步骤2：填写您或运营商的 SIP 网关 IP 和 SIP UDP 端口
将您或运营商的 SIP 网关 IP 和 SIP UDP 端口填写至第一步窗口中。
![](https://qcloudimg.tencent-cloud.cn/raw/b5d883d07230588495282a22115ff857.png)
您可在您的网关后台查找 SIP 网关 IP 和 SIP UDP 端口，例如：
![](https://qcloudimg.tencent-cloud.cn/raw/81d5de98f3100f3ff0c87ff8aeed9aad.png)
![](https://qcloudimg.tencent-cloud.cn/raw/69887f6e7027474e78eb024908a9664e.png)

### 步骤3：腾讯云网关 IP 加入白名单
1. 复制腾讯云网关 IP 和端口：
![](https://qcloudimg.tencent-cloud.cn/raw/a6bc1d9217da1bad7914b6a18c4906cd.png)
2. 将其添加至自有/运营商的网关白名单中：
![](https://qcloudimg.tencent-cloud.cn/raw/7914831a1341b9ec9d2a2be21b8c94d0.png)
3. 完成后单击**测试**，测试连通性。
![](https://qcloudimg.tencent-cloud.cn/raw/bde0aed0cbe1a77f937720eb526263b2.png)

### 步骤4：提交自有号码
请选择自有号码需要绑定的应用，填写需要配置的业务号码、送号前缀、以及联系方式等。

测试联调完成后腾讯云呼叫中心将号码分配到企业开通的云呼叫中心实例下即可正式使用。
![](https://qcloudimg.tencent-cloud.cn/raw/45e725ede9b7a3b4448a3fc4e161c69f.png)
腾讯云呼叫中心 SIP 对接相关信息如下：

<table ><thead ><tr>
<table><thead><tr>
 <th>呼入给腾讯云</th><th>呼出给对方或回信令</th></tr>

 </thead>
<tbody>
<tr>
 <td><ul>
 <li>sip.pstn.avc.qcloud.com:5089</li>
 <li>域名对应 IP:（139.199.233.98:5089、114.221.144.81:5089）</li>
 </ul>

 </td>
 <td><ul>
 <li>139.199.4.25:5089</li>
 <li>203.195.240.224:5089</li>
 <li>129.211.167.158:5089</li>
 <li>129.211.167.34:5089</li>
 <li>129.211.166.16:5089</li>
 <li>129.204.27.73:5089</li>
 <li>43.134.208.145:5089</li>
 <li>43.155.104.84:5089</li>
 <li>43.134.214.81:5089</li>
 <li>43.154.18.59:5089</li>
 <li>175.27.32.131:5089</li>
 <li>175.27.32.121:5089</li>
 <li>175.27.32.95:5089</li>
 <li>175.27.32.18:5089</li>
 <li>43.137.160.222:5089</li>
 <li>175.27.206.106:5089</li>
 <li>43.137.160.37:5089</li>
 <li>175.27.206.71:5089</li>
 <li>101.42.153.119:5089</li>
 <li>101.42.171.187:5089</li>
 <li>101.42.165.146:5089</li>
 <li>43.138.101.135:5089</li>
 </ul>

 </td>
 </tr>

 </tbody>
 </table>

 
