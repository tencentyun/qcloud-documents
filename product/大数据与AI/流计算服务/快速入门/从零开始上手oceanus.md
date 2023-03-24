流计算 Oceanus 是位于云端的流式数据汇聚、计算服务，提供全托管的云上服务，您无须关注基础设施的运维，便能便捷对接云上数据源，获得完善的配套支持。

通过阅读本文，您将可以零基础上手流计算 Oceanus。

## 步骤1 登录控制台
登录  [流计算 Oceanus 控制台](https://console.cloud.tencent.com/oceanus/job)。

## 步骤2 新建集群
选择控制台左侧菜单栏 [计算资源](https://console.cloud.tencent.com/oceanus/cluster)，在页面左上角选择地域，然后单击**新建集群**。创建独享集群，详情可参见 [创建独享集群](https://cloud.tencent.com/document/product/849/48298)。
![](https://qcloudimg.tencent-cloud.cn/raw/cd2607397d9db748c92d7bce932a58bf.png)

创建成功独享集群后，单击**操作**中的**关联空间**，可以将集群关联到某一工作空间，关联后该工作空间可以使用这一集群的计算资源来运行作业。

## 步骤3 新建作业
选择控制台左侧菜单栏[工作空间](https://console.cloud.tencent.com/oceanus/workspace)。单击进入空间。
![](https://qcloudimg.tencent-cloud.cn/raw/893c0135a7c946d48a68969c3565ec76.png)
进入空间后，单击控制台左侧菜单栏 [作业管理](https://console.cloud.tencent.com/oceanus/job)，选择新建作业所在集群的地域，然后单击**新建**，单击**新建作业**。
![](https://qcloudimg.tencent-cloud.cn/raw/0995172f3316654f9b927ed0db2374b7.png)
选择所需创建的作业，填写作业名称，选择运行集群，以上内容填写完成后，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/035138a51db138d1bd7c4523ecf6fee6.png)

## 后续操作
- 流计算 Oceanus 可创建四种类型的作业，详情可参见 [创建 SQL 作业](https://cloud.tencent.com/document/product/849/48301)、[创建 JAR 作业](https://cloud.tencent.com/document/product/849/48300)、[创建 Python 作业](https://cloud.tencent.com/document/product/849/81987)、[创建 ETL 作业](https://cloud.tencent.com/document/product/849/57853)。
- 作业创建成功后，可查看 [作业类型](https://cloud.tencent.com/document/product/849/59421) 和 [作业信息](https://cloud.tencent.com/document/product/849/48286)，以及支持的 [作业操作](https://cloud.tencent.com/document/product/849/48289)。
- 作业创建完成后，即可进行作业开发，更多内容可参见 [作业开发](https://cloud.tencent.com/document/product/849/59419)。
- 如果遇到权限问题或需要对子账户进行权限控制，可以查看文档 [权限管理](https://cloud.tencent.com/document/product/849/70605) 一章。
