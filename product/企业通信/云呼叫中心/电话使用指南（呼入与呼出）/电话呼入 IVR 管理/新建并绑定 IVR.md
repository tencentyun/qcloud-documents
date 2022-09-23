## 前提条件
1. 登录 [腾讯云呼叫中心 TCCC 管理工作台](https://cloud.tencent.com/document/product/679/73497#logintccc)。
2. 完成 [电话号码购买](https://cloud.tencent.com/document/product/679/73526) 或 [自携电话号码对接](https://cloud.tencent.com/document/product/679/73527)。

## 新建并绑定 IVR
1. 左侧导航栏单击**电话客服-IVR 管理**进入 IVR 管理页面，单击**呼入 IVR**，在页面左上角单击**新建**。
2. 在 IVR 画布左上角输入 IVR 名称，如：电话呼入流程测试。
![](https://qcloudimg.tencent-cloud.cn/raw/443a674077276d36dc0eafc27a55d1cf.png)
3. 根据您的场景需要拖拽 IVR 模块到画布区域合适的位置释放，连接模块并在各个模块填写相应信息（具体可参见下述 [基础 IVR 模块](https://cloud.tencent.com/document/product/679/73551) 与 [多功能 IVR 模块](https://cloud.tencent.com/document/product/679/73552)）。每个 IVR 流程必须以**开始**模块为第一个模块，以**结束**模块为最后一个模块。
![](https://qcloudimg.tencent-cloud.cn/raw/adb5d81423216389a051de3a48dc6e07.png)
4. 配置完成后在 IVR 画布右上角单击**保存**后回到 IVR 列表。
5. 在**关联电话**列单击**绑定**进入**号码管理**页面。
![](https://qcloudimg.tencent-cloud.cn/raw/c7f9873f1ee52dc0ea918220941ffeef.png)
6. 在目标号码的操作列单击**编辑**。
![](https://qcloudimg.tencent-cloud.cn/raw/0fc63bb9248759a3fdbf6598761d98e3.png)
7. 在呼入设置-呼入IVR 中单击需要绑定的 IVR 名称，如“电话呼入流程测试”，选择后单击**确定**后完成绑定。
![](https://qcloudimg.tencent-cloud.cn/raw/1c77cac15f22a1d087a3d1f8d7efb2e0.png)
