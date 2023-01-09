## Output 管理
1. 在控制台 [媒体传输](https://console.cloud.tencent.com/mdc/flow) 页面，在列表中单击某一条流，即可查看该流的详细信息。
![](https://qcloudimg.tencent-cloud.cn/raw/3f4ff3de56ce1989e6bdf8b4d5155fe8.png)
2. 进入流信息页，在页面上方单击 **输出**进入输出管理页面。支持对输出节点进行添加、删除、编辑的操作。
![](https://qcloudimg.tencent-cloud.cn/raw/bd9a04e34c3f1071dd85adedccc66e40.png)

## 创建 Output

您可以单击 **创建输出** 按钮添加输出节点，在创建弹窗中填写相关信息，单击 **确认** 完成输出节点的添加。
<img src="https://qcloudimg.tencent-cloud.cn/raw/4fe8d17d551b0a49d357f0daec0d0f4e.png" width=700>
- **输出名称**：您可以填写一个简单的名称，方便您管理多个 Output 信息。
- **输出区域**：输出节点所在区域，在这里选择您将流传输到的区域。
- **输出协议**：需要选择输出节点的传输协议，不同的协议需要的设置不同。
<table>
<thead>
<tr>
<th>输入协议</th>
<th>输出可选协议</th>
</tr>
</thead>
<tbody><tr>
<td>RTMP、RTMP_PULL</td>
<td>RTMP 、RTMP_PUSH、RTMP_PULL</td>
</tr>
<tr>
<td>SRT</td>
<td>SRT、RTMP_PUSH</td>
</tr>
<tr>
<td>RTP</td>
<td>RTP</td>
</tr>
<tr>
<td>RTSP</td>
<td>RTSP</td>
</tr>
</tbody></table>

### RTMP_PUSH
若选择此协议，会将流转推到您指定的地址。
- **目的地 URL**：RTMP URL，示例：`rtmp://example.com/live`。
- **流密钥**：RTMP 流密钥，示例：`e18c3c4dd05aef020946e6afbf9e04ef`。

<img src="https://qcloudimg.tencent-cloud.cn/raw/2d17dc6aaa9c15ac91f9d97cdef0bc08.png" width=600>

### RTMP_PULL

若您需要从输出节点拉流，则可以在输出节点中选择此协议。创建输出后，您可以在输出节点列表中获取拉流地址。
**CIDR IP 白名单**：
- IP 白名单，用于限制推流使用的 IP，以此增强安全性。示例：`203.3.3.3/28`。
- 如需输入多个，请使用分号隔开，示例：`203.3.3.3/28;202.3.3.3/28`。

<img src="https://qcloudimg.tencent-cloud.cn/raw/ed544b8e51b3c487ea045246c73c7923.png" width=600>


### SRT Listener
若选择此协议，则：
- **模式**：选择 Listener 模式，您需要在接收侧使用 SRT Call 模式请求输出节点。拉流地址展示在输出节点列表页。
- **延迟设置**：设置服务侧延迟参数，若推流侧和媒体传输服务的区域在同一个国家，建议设置为120ms；若推流侧和 媒体传输服务的区域在不同的国家，建议设置为200ms；若推流侧和媒体传输服务的区域在不同的洲建议设置1000ms；具体可以根据分配的 IP 进行实际调整。
- **开启加密**：如果开启了加密，您在接收侧也需要开启加密，并填写加密密钥以及密钥长度两个字段，否则将拉流失败。
  - **加密密钥**：您需要在此字段填写相关的密钥，用于加密。
  - **密钥长度**：您需要在此字段选择密钥的长度。
- **CIDR IP 白名单**：IP 白名单，用于限制推流使用的 IP ，以此增强安全性。示例：`203.3.3.3/28`。如需输入多个，请使用分号隔开，示例：`203.3.3.3/28;202.3.3.3/28`。

<img src="https://qcloudimg.tencent-cloud.cn/raw/cc044c8786e5590316ce3fa0c98d6132.png" width=600>


### SRT Caller
若选择此协议，则：
- **模式**：选择 Caller 模式，此模式下，媒体传输将使用 SRT 协议 Call 您提供的接收地址，以此将流传送到您指定的地址。
- **IP目的地**：接收 SRT 推流的 IP 地址，此处也可以填写域名。
- **端口**：接收 SRT 推流的端口。
- **延迟配置**：设置服务侧延迟参数，源流地址和媒体传输服务的区域在同一个国家，建议设置为120ms；源流地址和媒体传输服务的区域在不同的国家建议设置 200ms；源流地址和媒体传输服务的区域在不同的洲建议设置1000ms；具体可以根据分配的 IP 进行实际调整。
- **开启加密**：如果接收侧开启了加密，则需要打开此开关，并填写加密密钥以及密钥长度两个字段，否则 Output 将推送失败。
  - **加密密钥**：您需要在此字段填写相关的密钥，用于加密。
  - **密钥长度**：您需要在此字段选择密钥长度，长度需要和接收侧设置的长度保持一致。

<img src="https://qcloudimg.tencent-cloud.cn/raw/9eb36be4f30ab4bb1e807c54d2e90536.png" width=600>


### RTP
若选择此协议，输出节点会将流推送到您指定的地址。
- **IP 目的地**：会将流推送到您指定的地址。
- **输出协议**：目前输出协议的选择，强依赖于输入的协议。

<img src="https://qcloudimg.tencent-cloud.cn/raw/762ca4a359f7ca7dd449d47ea91e5f9d.png" width=600>
