## 操作场景
Consul 引擎支持使用 Gossip Encryption 进行通信加密。您可以配置 Gossip Encryption Key，对集群 Agent 之间的 Gossip 进行加密传输，增强集群访问的安全性。

## Gossip 加密参数配置
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏单击注册中心，单击目标实例的“ID/名称”，在系统参数 页，选择 Gossip 加密功能项，可查看当前 Gossip 加密参数。
参数说明如下：
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>encrypt</td>
<td>Gossip 通信密钥， 您可通过 consul keygen 命令生成该密钥。</td>
</tr>
<tr>
<td>encrypt_verify_incoming</td>
<td>是否对流入流量加密校验，默认为 false。</td>
</tr>
<tr>
<td>encrypt_verify_outgoing</td>
<td>是否对流出流量进行加密，默认为 false。</td>
</tr>
</tbody></table>
>?对于新建的 TSE Consul 实例，Gossip 加密功能默认打开，但不会对通信进行校验。因此，您无需配置 Gossip 密钥即可访问集群。

## 场景一：直接启用 Gossip 通信加密
如果您的 Consul Agent Client 还未加入 Consul 集群，推荐使用该方式快速使用 Gossip 通信加密功能。

### 操作步骤
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏单击**注册配置中心** > **consul**，单击目标实例的“ID/名称”，在系统参数页，选择 Gossip 加密功能项，单击**修改参数**，编辑 JSON 内容，将 encrypt_verify_incoming 和 encrypt_verify_outgoing 修改为 true，单击**保存**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ecb7b408f23a45b4eeae90134d998620.jpg">
3. 等待 Consul Server 集群滚动重启，此过程大概需要3-8分钟。
4. 当实例处于运行中状态，表明重启完毕，您需要在 Consul Agent Client 的启动配置中添加相同的密钥配置（encrypt），并重启 Agent Client。
<dx-codeblock>
:::  json
{
  "encrypt": "VVIh+c4YAG04hHvBg16aoUrHGjUf8rCWNTTX/uUIJAg="
}
:::
</dx-codeblock>
5. 观察 Consul 启动日志，确保 Consul Agent Client 正常加入 Consul 集群。

## 场景二：平滑启用 Gossip 通信加密
如果您的 Consul Agent Client 已加入 Consul 集群且未配置过 Gossip 通信，为了避免开启 Gossip 通信加密后，Client 无法与 Server 进行通信，推荐使用该方式进行平滑开启 Gossip 通信加密功能。

### 操作步骤
1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在左侧导航栏单击**注册配置中心** > **consul**，单击目标实例的“ID/名称”，在系统参数页，选择 Gossip 加密功能项，单击**修改参数**，编辑 JSON 内容，将 encrypt_verify_incoming 和 encrypt_verify_outgoing 设置为 false，单击**保存**。
3. 等待 Consul Server 滚动重启完毕，修改已经启动的 Consul Agent Client 配置，使之保持与 Consul Server 配置一致，并进行滚动重启。
>!由于 encrypt_verify_incoming 设置为 false，此时流入流量不会进行加密校验。
>
<dx-codeblock>
:::  json
{
    "encrypt": "VVIh+c4YAG0*********rHGjUf8rCWNTTX/uUIJAg=",
    "encrypt_verify_incoming": false,
    "encrypt_verify_outgoing": false
}
:::
</dx-codeblock>
4. 开启入流量加密校验：将 Consul Server 与 Consul Client 的 encrypt_verify_outgoing 配置项设置为 true，单击**保存**，并进行滚动重启。
>!此时入流量已加密，但 Consul Server 不会进行校验。
>
<dx-codeblock>
:::  json
{
    "encrypt": "VVIh+c4YAG0*********rHGjUf8rCWNTTX/uUIJAg=",
    "encrypt_verify_incoming": false,
    "encrypt_verify_outgoing": true
}
:::
</dx-codeblock>
5. 等待所有 Consul Agent 启动，验证通信正常。
6. 开启出流量加密校验：将 Consul Server 与 Consul Client 的 encrypt_verify_incoming 配置项设置为 true，单击**保存**，并进行滚动重启。
>!此时出入流量均已加密，所有 Agent 均开启了完整的 Gossip 通信加密校验。
>
<dx-codeblock>
:::  json
{
    "encrypt": "VVIh+c4YAG0*********rHGjUf8rCWNTTX/uUIJAg=",
    "encrypt_verify_incoming": true,
    "encrypt_verify_outgoing": true
}
:::
</dx-codeblock>
7. 观察 Consul 启动日志，Consul Client 能够加入 Consul 集群，并正常通信。
