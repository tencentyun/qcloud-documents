## 操作场景
Consul 引擎支持使用Gossip Encryption进行通信加密。您可以配置Gossip Encryption Key，对集群Agent之间的Gossip进行加密传输，增强集群访问的安全性。

## Gossip加密参数配置
1. 登录 TSE 控制台 。
2. 在左侧导航栏单击注册中心，单击目标实例的“ID/名称”，在系统参数 页，选择Gossip加密功能项，可查看当前Gossip加密参数。
参数说明如下：
|参数	|说明|
|-----|-----|
|encrypt	|Gossip通信密钥， 您可通过consul keygen命令生成该密钥。|
|encrypt_verify_incoming	|是否对流入流量加密校验，默认为false。|
|encrypt_verify_outgoing	|是否对流出流量进行加密，默认为false。|
说明：对于新建的 TSE Consul |实例，Gossip加密功能默认打开，但不会对通信进行校验。因此，您无需配置Gossip密钥即可访问集群。|

## 场景一：直接启用Gossip通信加密
如果您的Consul Agent Client 还未加入Consul集群，推荐使用该方式快速使用Gossip通信加密功能。
### 操作步骤
1. 登录 TSE 控制台 。
2. 在左侧导航栏单击注册中心，单击目标实例的“ID/名称”，在系统参数 页，选择Gossip加密功能项，点击修改参数，编辑JSON内容，将encrypt_verify_incoming和encrypt_verify_outgoing修改为true，点击保存。

3. 等待Consul Server集群滚动重启，此过程大概需要3-8分钟。
4. 当实例处于运行中状态，表明重启完毕，您需要在Consul Agent Client的启动配置中添加相同的密钥配置（encrypt），并重启Agent Client。
```
{
  "encrypt": "VVIh+c4YAG04hHvBg16aoUrHGjUf8rCWNTTX/uUIJAg="
}
```

5. 观察Consul启动日志，确保Consul Agent Client正常加入Consul集群。

## 场景二：平滑启用Gossip通信加密
如果您的Consul Agent Client 已加入Consul集群且未配置过Gossip通信，为了避免开启Gossip通信加密后，Client无法与Server进行通信，推荐使用该方式进行平滑开启Gossip通信加密功能。

### 操作步骤
1. 登录 TSE 控制台 。
2. 在左侧导航栏单击注册中心，单击目标实例的“ID/名称”，在系统参数 页，选择Gossip加密功能项，点击修改参数，编辑JSON内容，将encrypt_verify_incoming和encrypt_verify_outgoing设置为false，点击保存。
3. 等待Consul Server滚动重启完毕，修改已经启动的Consul Agent Client配置，使之保持与Consul Server配置一致，并进行滚动重启。
注意：由于encrypt_verify_incoming设置为false，此时流入流量不会进行加密校验。
```
{
    "encrypt": "VVIh+c4YAG0*********rHGjUf8rCWNTTX/uUIJAg=",
    "encrypt_verify_incoming": false,
    "encrypt_verify_outgoing": false
}
```

4. 开启入流量加密校验：将 Consul Server 与 Consul Client 的encrypt_verify_outgoing配置项设置为true，点击保存，并进行滚动重启。
注意：此时入流量已加密，但Consul Server不会进行校验。
```
{
    "encrypt": "VVIh+c4YAG0*********rHGjUf8rCWNTTX/uUIJAg=",
    "encrypt_verify_incoming": false,
    "encrypt_verify_outgoing": true
}
```

5. 等待所有Consul Agent启动，验证通信正常。
6. 开启出流量加密校验：将 Consul Server 与 Consul Client 的encrypt_verify_incoming配置项设置为true，点击保存，并进行滚动重启。
注意：此时出入流量均已加密，所有Agent均开启了完整的Gossip通信加密校验。
```
{
    "encrypt": "VVIh+c4YAG0*********rHGjUf8rCWNTTX/uUIJAg=",
    "encrypt_verify_incoming": true,
    "encrypt_verify_outgoing": true
}
```
7. 观察Consul启动日志，Consul Client能够加入Consul集群，并正常通信。
