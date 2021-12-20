本文为您介绍容器服务 TKE 监控告警最佳实践。


## 新版 TKE 监控特性

● 支持自动更新监控对象。
● 新增 Workload/Component/Node 监控场景。
● 更多的监控指标监控，新版 TKE 指标总数可达140个。
● 可针对某个监控维度屏蔽特殊对象（例如频繁告警的 Pod）。


## 操作步骤

下列以“容器监控-pod”维度为例，介绍如何实现 [自动更新 Dashboard 监控对象](#step1)、[自动更新告警监控对象](#step2) 和 [屏蔽频繁告警监控对象](#step3)。



### 自动更新 Dashboard 监控对象[](id:step1)

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。
2. 选择 **Dashboard** > **Dashboard 列表** > **新建 Dashboard** > **新建图表**。
3. 参考下列步骤配置监控图表。
 -  **监控类型**：选择云产品监控。
 -  **指标**：选择云产品为“容器服务（新）-pod”，选择指标为“CPU利用率（%)”。
 -  **筛选**：可以通过维度筛选绑定图表对象（地域、集群、命名空间、工作负载等）。
    -  **地域**：选择监控对象所在的地域
    -  **集群**：选择监控对象所在的集群。
 -  **筛选条件**：需要创建两个筛选条件，一个为命名空间；另一个为工作负载均衡类型，监控指定 Workload 下的所有 Pod，并在 Pods 发生频繁新增/更新时进行自动更新 Dashboard 监控对象。如下图所示：
    ![](https://main.qcloudimg.com/raw/3c45f321a4260e5191cf433d84311012.png)
4. 配置完后在页面右上方单击**保存**，即可保存图表。


###  自动更新告警监控对象[](id:step2)

1. 登录 [云监控控制台](https://console.cloud.tencent.com/monitor)。
2. 选择**告警配置** > **告警策略** > **新建**，进入新建告警策略页。
3. 选择策略类型为 “容器服务（新）-pod”，并参考下列步骤配置告警对象。
   - **地域**：选择监控对象所在的地域
   - **集群**：选择监控对象所在的集群。
   - **筛选条件**：需要创建两个筛选条件，一个为命名空间；另一个为工作负载均衡类型，监控指定 Workload 下的所有 Pod，并在 Pods 发生频繁新增/更新时进行自动更新告警监控对象。如下图：
 ![](https://main.qcloudimg.com/raw/6bdcfc8733137084fbf70493bdbfe62a.png)
>?如需了解更多告警配置请参见 [新建告警策略](https://cloud.tencent.com/document/product/248/50398)。

### 屏蔽频繁告警监控对象[](id:step3)

当 Pod 频繁触发告警，您可以参考以下说明屏蔽 Node下部分或所有 Pods 监控告警对象。

如下图，可通过配置 Pod 名称 “!=”操作符进行部分 Pod 告警屏蔽。
![](https://main.qcloudimg.com/raw/8b716e592e679c6b1bd1cf7952b1d4d9.png)



> ?若在使用 TKE 监控过程中有任何问题可联系云监控小助手（微信 ID：hitherecm）我们将竭诚为您服务！
> <img src="https://main.qcloudimg.com/raw/c59dcbad163bcc27bba3fc98c7c017c7.png" ></img>






