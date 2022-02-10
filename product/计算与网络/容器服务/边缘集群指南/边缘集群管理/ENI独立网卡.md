## 操作场景
本文介绍如何启用ENI独立网卡，在CVM边缘节点的pod中绑定ENI独立网卡，实现高可用网络方案；

- [启用ENI独立网卡](#openEniNetwork)
- [关闭ENI独立网卡](#closeEniNetwork)
## 操作步骤
[](id:openEniNetwork)
### 启用ENI独立网卡
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**边缘集群**。
2. 单击需要启用ENI独立网卡的集群 ID，进入该集群详情页。
3. 选择页面左侧**基本信息**，进入集群基本信息页面，点击**开启独立网卡**开关,开启ENI独立网卡功能，详细操作如下：
      - 3.1 点击**访问API密钥**超链接，跳转至密钥信息页面。
            ![](https://qcloudimg.tencent-cloud.cn/raw/d04413124b004f1144c4f8b1b7db2084.png)
      - 3.2 复制密钥ID和密钥Key,返回确认密钥弹框页并完成输入。
            ![](https://qcloudimg.tencent-cloud.cn/raw/6793d7c93a7c073447c412e56931c819.png)
            ![](https://qcloudimg.tencent-cloud.cn/raw/1a460dc9b1e9e4056577cd18ec9d6f71.png)
      - 3.3 点击**确认**按钮，完成启用ENI网卡。
      ![](https://qcloudimg.tencent-cloud.cn/raw/5bd65c52558866b83afa333f18c18652.png)
4. 选择页面左侧**工作负载 -> Deployment**，进入deployment列表页，若列表中已有deployment，则跳过该步骤;否则，[新建deployment](https://cloud.tencent.com/document/product/457/31705)
5. 选择页面左侧**节点管理 -> 节点**，进入节点列表页，若列表中已有CVM节点，则跳过该步骤;否则，[新建CVM节点](https://cloud.tencent.com/document/product/457/42890#createCVMNode)

6. 在目标边缘集群的pod中配置ENI。
   - 配置截图:
  ![](https://qcloudimg.tencent-cloud.cn/raw/77d0d2111bafa54c86c608624427b5ac.png)
   - 边缘节点ENI独立网卡能力，只能支持腾讯云 CVM 类型的节点资源，因此部署应用的时候，需要通过 nodeAffinity 的能力将挂载ENId独立网卡的应用 pod调度到实际的边缘 CVM 节点上，如下图所示（支持填写多个 CVM 节点 ID）：
  ![](https://qcloudimg.tencent-cloud.cn/raw/b63509fce7abc1d53f27bfdb80ab6acb.png)
   - 实际代码:
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
                    - cvm-2cxgi4ow #访问目标的cvm节点ID
    ```

[](id:closeEniNetwork)
### 关闭ENI独立网卡
1. 登录 [腾讯云容器服务控制台](https://console.cloud.tencent.com/tke2)，选择左侧导航栏中的**边缘集群**。
2. 单击需要启用ENI独立网卡的集群 ID，进入该集群详情页。
3. 选择页面左侧**基本信息**，进入集群基本信息页面，点击**开启独立网卡**开关,关闭ENI独立网卡功能，如下图所示：
  ![](https://qcloudimg.tencent-cloud.cn/raw/ccff43c3422cfe2e5b1ffb08922ba350.png)
