## 功能简介

本文旨在指导开发者如何快速使用千帆神笔 aPaaS 搭建应用，并以快速创建访客应用作为案例进行介绍。


## 登录控制台
1. 进入 [千帆神笔 aPaaS](https://apaas-pro.cloud.tencent.com/sign/in) 登录页面。
2. 选择**企微登录**或**腾讯云登录**方式，成功登录到千帆神笔 aPaaS 首页。
>?如您还未注册千帆神笔 aPaaS 账号，可参考 [开发者注册流程](https://cloud.tencent.com/document/product/1365/68054) 进行注册。

## 创建应用

1. 创建应用。您可以通过以下三种方式创建应用：
- 在首页顶部导航单击**模板中心**。
- 在首页单击**选择模板创建**。
- 在首页单击**创建空白应用**。
![img](https://qcloudimg.tencent-cloud.cn/raw/68ff08563172a768863cc85db48a5315.png)
2. 创建后，请填写新建**应用名称**（必填项）和**应用简介**（非必填项），同时可以选择应用图标和应用主题。
![img](https://qcloudimg.tencent-cloud.cn/raw/71cf9c80b343a17215e48d74f694cb0a.png)

## 创建对象模型

1. 在首页或顶部导航单击**新建对象**按钮，创建新对象。
![image-20211207104222222](https://qcloudimg.tencent-cloud.cn/raw/0affb1ce0a4bb2b546f7fc53d6eeca25.png)
2. 填写新创建对象基本信息以及设置新对象主字段类型，并单击**确定**按钮。
![image-20211207104759626](https://qcloudimg.tencent-cloud.cn/raw/489692cf86775469a2ab486db8832a2c.png)
3. 在对象列表下方单击**添加字段**按钮或从左侧字段菜单栏拖拽选择添加对象字段。
![img](https://qcloudimg.tencent-cloud.cn/raw/453a713de7b26c873ff7b043ee524523.png)
4. 设置新建字段属性。
![img](https://qcloudimg.tencent-cloud.cn/raw/0b7453570b9b06bf28c8a05b74eae64d.png)
5. 单击字段名称支持在右侧菜单栏修改当前字段属性。
![img](https://qcloudimg.tencent-cloud.cn/raw/dcf3edd0d5ef13df5de7d92465b3eb3e.png)
6. 单击主字段名称支持在右侧菜单栏修改主字段属性及当前对象字段排序。
![img](https://qcloudimg.tencent-cloud.cn/raw/f5c5a787224751bae9b04bff03d4dd43.png)

## 页面设计

1. 在页面顶部导航单击**页面设计**按钮，在左侧菜单栏单击**创建页面**按钮，可支持创建标准页面、审批流程页面、仪表盘页面等。
![img](https://qcloudimg.tencent-cloud.cn/raw/991f4bf0837a578fdce9af368c48bd7f.png)
2. 在左侧组件框选择所需组件拖拽至画布。
![img](https://qcloudimg.tencent-cloud.cn/raw/e1ccc0c016f27c43325f79a779dee832.png)
3. 为所选组件关联数据源并选择填充对象，并在右侧菜单栏设置组件属性和样式。
![img](https://qcloudimg.tencent-cloud.cn/raw/9c9cefeaae0efe34dfe6098228083890.png)
4. 完成页面设计。
![img](https://qcloudimg.tencent-cloud.cn/raw/080c460ffd67c513965f338152dd89b8.png)

## 导航设置

1. 在页面顶部导航单击**导航设置**按钮，在右侧菜单栏根据业务需求设置导航布局。
![img](https://qcloudimg.tencent-cloud.cn/raw/977d4eae02433439527c75a2ec0c91e9.png)
2. 单击**+**按钮，添加导航菜单。
![img](https://qcloudimg.tencent-cloud.cn/raw/5d1ee60812f42f0e93248d18794ad005.png)
3. 添加菜单属性：
- 菜单标题：必填项。
- 菜单图标：非必填项。
- 打开页面：必填项。
![img](https://qcloudimg.tencent-cloud.cn/raw/5ea24cd0707b675f544f5be4b07b341a.png)
4. 单击**确认**即可完成所需导航添加。
![img](https://qcloudimg.tencent-cloud.cn/raw/b3bc1c0fda93b88674684245bb4eaa7c.png)

## 发布应用

1. 单击页面顶部导航**发布**按钮，将当前应用发布至生产环境。
>?在发布应用时，系统将自动检查当前应用是否报错，如无报错将显示**校验成功**，继续发布应用；如**校验失败**系统将作出提示，请根据错误提示进行修正，直至应用显示**校验成功**方可发布应用。
>
![img](https://qcloudimg.tencent-cloud.cn/raw/07f9f6560eee3b42f238f98f75a8d029.png)
2. 单击**下一步**按钮确认发布至生产环境，并建议勾选**生成软件包**。
>?勾选后，本次发布会自动打包生成软件包，同时添加到软件包管理列表中，以便备份。建议勾选。
>
![image-20211207105556895](https://qcloudimg.tencent-cloud.cn/raw/01c02958adfb18eeb9cf1f06fefe2ee0.png)
3. 发布完成，单击**点击体验**，跳转至应用中心查看已发布的应用。
![img](https://qcloudimg.tencent-cloud.cn/raw/5445ddf6f7d6d2445581b97afabb7cfc.png)

## 访问应用

1. 在首页单击**访问线上应用**即可进入应用中心查看已发布的应用。 ![img](https://qcloudimg.tencent-cloud.cn/raw/95b548ac8fcf675f07a23d72bd3f9960.png)
![img](https://qcloudimg.tencent-cloud.cn/raw/f97c266c3c7c0492f6f30c2db1ef0d2d.jpg)
2. 单击应用卡片任意区进入应用运行态。
![img](https://qcloudimg.tencent-cloud.cn/raw/5f9a06ddaddfcf7b6c619c254d948e69.png)
