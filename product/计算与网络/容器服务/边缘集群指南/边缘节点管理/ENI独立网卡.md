## 操作场景
如果用户将腾讯云上的 CVM 作为边缘节点加入边缘集群，平台支持启用 ENI 独立网卡，在 CVM 节点部署的 pod 中绑定 ENI 独立网卡，实现高可用网络方案。

具体架构如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/577140d6573126918c7fba27b9c91b6c.png)

用户也可以在 CVM 所在 VPC 上使用 ENI 对外暴露 Pod，然后将不同的 ENI 网卡绑定到 CLB 上，使能高性能网络转发能力。

- [启用 ENI 独立网卡](#openEniNetwork)
- [关闭 ENI 独立网卡](#closeEniNetwork)


## 操作步骤
[](id:openEniNetwork)
### 启用 ENI 独立网卡
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在集群管理页面，单击需要启用 ENI 独立网卡的集群 ID，进入该集群详情页。
3. 选择页面左侧**基本信息**，进入集群基本信息页面，单击**开启独立网卡**开关，开启 ENI 独立网卡功能，详细操作如下：
      - 3.1 单击**访问 API 密钥**，跳转至密钥信息页面。
![](https://qcloudimg.tencent-cloud.cn/raw/d819119564f60fe78b96557d34ac9800.png)
      - 3.2 在 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 页面中创建并复制 `SecretId` 和 `SecretKey`。
      - 3.3 在“确认密钥信息”弹窗中，单击**确认**，完成启用 ENI 网卡。
 ![](https://qcloudimg.tencent-cloud.cn/raw/157c1d1d3ffedcb11e634c98459e60bb.png)
4. 选择页面左侧**工作负载 > Deployment**，进入 deployment 列表页，若列表中已有 deployment，则跳过该步骤；否则，[新建 deployment](https://cloud.tencent.com/document/product/457/31705)。
5. 选择页面左侧**节点管理 > 节点**，进入节点列表页，若列表中已有 CVM 节点，则跳过该步骤；否则，[新建 CVM 节点](https://cloud.tencent.com/document/product/457/83208)。
6. 在目标边缘集群的 pod 中配置 ENI。
   - 配置截图：
![](https://qcloudimg.tencent-cloud.cn/raw/8f593ac9a04080b44ad57f0b6b5387c9.png)
   - 边缘节点 ENI 独立网卡能力，只能支持腾讯云 CVM 类型的节点资源，因此部署应用的时候，需要通过 nodeAffinity 的能力将挂载 ENI 独立网卡的应用 pod 调度到实际的边缘 CVM 节点上，如下图所示（支持填写多个 CVM 节点 ID）：
![](https://qcloudimg.tencent-cloud.cn/raw/8b10f8a7ebe3f550700346a097739d29.png)
   - 实际代码：
    ```
      template:
        metadata:
          annotations:
            tke.cloud.tencent.com/networks: tke-direct-eni,flannel
    ```
		```
        spec:
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                - matchExpressions:
                  - key: kubernetes.io/hostname
                    operator: In
                    values:
                    - cvm-2cxgi4ow #访问目标的 cvm 节点 ID
    ```

[](id:closeEniNetwork)
### 关闭 ENI 独立网卡
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在集群管理页面，单击需要启用 ENI 独立网卡的集群 ID，进入该集群详情页。
3. 选择页面左侧**基本信息**，进入集群基本信息页面，单击**开启独立网卡**开关，关闭 ENI 独立网卡功能，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/7b40408ccd7df1088d35830747fcf613.png)
