## 操作背景
Prometheus 监控服务的集成了云监控服务，当您在新建集成时选择对象存储 COS，由于 COS 不支持内网访问，需要用户对集成云监控 Exporter 所在 EKS 开通外网访问。


## 操作步骤
1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 单击对应的实例，进入实例管理页，单击 **集成中心** > **集成列表**。
3. 在**集成列表**的**操作**列中选择类型为云监控的一列，单击 **日志** 进入 EKS 集群。
![](https://qcloudimg.tencent-cloud.cn/raw/b530661b793a667fa09d8988e4b8f8e4.png)
4. 在顶部的菜单栏，切换到 Pod 管理界面，单击实例名称名字，进入集群界面。
5. 在**基本信息**页面，单击 **容器网络**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/3cfd0c417180bc30c7636c68e683da00.png" width="60%">
6. 在容器网络顶部菜单，切换为**路由策略**栏。单击路由表链接（列表上的 rtb-xxx）进入路由表界面。
![](https://qcloudimg.tencent-cloud.cn/raw/a2001cac8be8145bd920a2d75e9d47f5.png)
7. 在路由表界面单击 **新增路由策略**。
 - **目的端**：填写 0.0.0.0/0。
 - **下一跳类型**：选择 NAT 网关。
 - **下一跳**：选择对应的网关，若无网关，可参见 [NAT 网关](https://cloud.tencent.com/document/product/552/18186#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E5.88.9B.E5.BB.BA-nat-.E7.BD.91.E5.85.B3.3Ca-id.3D.22step1.22.3E.3C.2Fa.3E) 指引进行创建 。
![](https://qcloudimg.tencent-cloud.cn/raw/40926c047d170805805b5be381d52570.png)
8. 填写完后，单击 **创建**。创建成功后表示 EKS 开通外网访问。
