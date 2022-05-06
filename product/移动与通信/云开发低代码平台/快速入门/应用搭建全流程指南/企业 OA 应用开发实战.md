

本文就介绍一下利用微搭低代码工具来搭建一款企业 OA 系统。搭建步骤有：

<dx-steps>
-[创建数据源](#step1)
-[设计工作流](#step2)
-[创建应用](#step3)
-[配置角色、用户权限](#step4)
</dx-steps>


## 业务场景

我们的场景是员工如果需要居家办公的需要发起一个请假流程，填写必要的信息，将流程提交给总监审批，审批通过即视为请假成功。

## 操作步骤
[](id:step1)
### 步骤1：创建数据源

1. 日常员工填写的请假申请，需要将申请单填写的信息保存到数据库中，审批流程的各个办理人审核的过程中从数据库中读取申请信息。为此需要设计数据源进行存储数据，数据源字段设计如下：
<table>
<thead>
<tr>
<th>字段名称</th>
<th>字段类型</th>
<th>字段说明</th>
</tr>
</thead>
<tbody><tr>
<td>请假类型</td>
<td>枚举</td>
<td>事假、病假</td>
</tr>
<tr>
<td>申请人</td>
<td>文本</td>
<td>由发起人填写</td>
</tr>
<tr>
<td>申请人部门</td>
<td>文本</td>
<td>由发起人填写</td>
</tr>
<tr>
<td>请假开始时间</td>
<td>日期</td>
<td>可以弹出选择日期</td>
</tr>
<tr>
<td>请假结束时间</td>
<td>日期</td>
<td>可以弹出选择日期</td>
</tr>
<tr>
<td>请假天数</td>
<td>数字</td>
<td>由发起人填写</td>
</tr>
<tr>
<td>请假事由</td>
<td>文本</td>
<td>由发起人填写</td>
</tr>
<tr>
<td>附件</td>
<td>附件上传</td>
<td>由发起人上传附件</td>
</tr>
</tbody></table>
2. 数据源设计好之后我们就可以创建数据源了，进入**微搭控制台** > [**数据模型**](https://console.cloud.tencent.com/lowcode/datasource/model) 页面，单击**新建数据模型**。
![](https://qcloudimg.tencent-cloud.cn/raw/0fb57242c9792e6c83940e576225560f.png)
3. 输入数据源的名称和标识。
![](https://qcloudimg.tencent-cloud.cn/raw/6a0e5163c4ca200210f0f6d98b2db681.png)
4. 我们数据源的第一个字段是设置的枚举，所谓的枚举就是在申请填写的时候可以有固定的选项，微搭提供了通用选项集来维护枚举项。进入 [通用选项集](https://console.cloud.tencent.com/lowcode/option-set) 页面，单击**新建选项集**。
![](https://qcloudimg.tencent-cloud.cn/raw/3b634828cb4d414c102a8cf58e78193e.png)
5. 在**新建选项集**页面输入选项集的名称，并且配置选项。
![](https://qcloudimg.tencent-cloud.cn/raw/8f07201a24996c33261ed7aa522b88ab.png)
6. 选项集设置好之后，就可以添加字段了，按照我们的数据源设计进行字段的添加。
![](https://qcloudimg.tencent-cloud.cn/raw/6199fb66a2dca37ec80cd94004299940.png)

[](id:step2)
### 步骤2：设计工作流

1. 需要按照考勤制度设计工作流，进入**微搭控制台** > [**工作流**](https://console.cloud.tencent.com/lowcode/flow) 页面，单击**新建流程**。
![](https://qcloudimg.tencent-cloud.cn/raw/51642535636b53c6bb78077a9cbb6acc.png)
2. 输入工作流的名称和标识后单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/55b6a3bb92de0da3968eb2d083986d51.png)
3. 先需要和数据源关联，我们选择刚创建的数据源，**触发方法**选择**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/1964acd8d43c6f4c2c6652f1b1b73e09.png)
4. 然后单击流程图的 **+** 号来添加审核节点，**人工节点**选择**审批**。
![](https://qcloudimg.tencent-cloud.cn/raw/6caa9f4e6d58a9175a82ca967e8bd9a8.png)
5. 选中该审批节点，修改节点信息，设置节点名称，添加**固定审批人**。
![](https://qcloudimg.tencent-cloud.cn/raw/77839160e50d148ef767b1607910b2b3.png)
6. 在审批节点后可以增加一个**发送通知**模板。
![](https://qcloudimg.tencent-cloud.cn/raw/4bed7bdc848c2ac81a8c560100d2bd06.png)
并配置相应信息。
![](https://qcloudimg.tencent-cloud.cn/raw/d664d92879573571356c2a09db5f84e6.png)
7. 目前还没有模板，我们可以新建一个。
![](https://qcloudimg.tencent-cloud.cn/raw/92f11ac6c59a4fb16960768b541db153.png)
8. 然后在流程上选择该通知即可。

[](id:step3)
### 步骤3：创建应用

1. 工作流搭建好之后，进入**微搭控制台** > [**应用**](https://console.cloud.tencent.com/lowcode/app) 页面，单击**新建模型应用**。
![](https://qcloudimg.tencent-cloud.cn/raw/33e335d67abf95fce0e918f438a1996e.png)
2. 输入应用的名称，单击**新建**。
![](https://qcloudimg.tencent-cloud.cn/raw/b42be0e3d87c26d074c0a83b20a21da2.png)
3. 勾选数据源，单击**创建页面**。
![](https://qcloudimg.tencent-cloud.cn/raw/46b817618006daf57d0424bd3f74390f.png)
4. 选中表格组件，进入右侧**属性**面板，单击**选择字段**。
![](https://qcloudimg.tencent-cloud.cn/raw/f368425fcedf586d2fd77dae5cdec3df.png)
只勾选其中业务字段即可。
![](https://qcloudimg.tencent-cloud.cn/raw/0c8ab286483e130089739d9b7ed89fbe.png)
5. 按照同样的方法对详情页的字段进行调整。
![](https://qcloudimg.tencent-cloud.cn/raw/94ec82e75169da79e472d0791a8945f2.png)
6. 配置完成后单击**发布**，发布版本。
![](https://qcloudimg.tencent-cloud.cn/raw/d8047d119bd577b69fdfed0958989cbd.png)
正式发布前可先勾选**体验版**，可通过预览查看页面情况。
![](https://qcloudimg.tencent-cloud.cn/raw/e8b1b7d940149c879d9464e33fd035e1.png)
7. 超级管理员可以单击左侧菜单栏的**系统设置**，对企业工作台的品牌名称和 LOGO 进行配置。
![](https://qcloudimg.tencent-cloud.cn/raw/f0abd1bdbd860a9ae2d8b096e6b263f6.png)
8. 可以在框架配置菜单里进行品牌名称、LOGO 的替换。除了配置品牌名称和 LOGO 外还可以自己定义企业工作台需要显示的菜单名称，单击菜单配置进行修改即可。
![](https://qcloudimg.tencent-cloud.cn/raw/fce7c2b2916e2a1289798c152395c861.png)

[](id:step4)
### 步骤4：配置角色、用户权限

1. 如果要正常使用 OA，发起流程，还需创建用户并且分配角色，进入**微搭控制台** > [**用户**](https://console.cloud.tencent.com/lowcode/permission/user) 页面，按需添加用户。
![](https://qcloudimg.tencent-cloud.cn/raw/9946c30873509937fdd9cc85aaa9060b.png)
2. 用户添加好后，进入 [**角色与权限**](https://console.cloud.tencent.com/lowcode/permission/role) 页面，单击**添加角色**。
![](https://qcloudimg.tencent-cloud.cn/raw/34d98587f5698bdbfc6a99fb1d21649d.png)
设置该角色的**角色名称**和**角色标识**单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/c6707bfe25dc9455748eb01133276721.png)
3. 单击**新建好的角色名称**，进入**角色权限**配置页面，为该角色分配对应的角色权限。
![](https://qcloudimg.tencent-cloud.cn/raw/3160f15c6e57d128c1bc000fd1d2b7cd.png)

## 日常使用

1. 权限和用户配置好后，就可以访问企业工作台，首先是在应用编辑器里，找到企业工作台的发布地址。
![](https://qcloudimg.tencent-cloud.cn/raw/80da0c2f5ed7c743a35a00c8a21307c3.png)
2. 地址记录好之后就需要下发员工的用户名和密码，在用户模块找到用户名。
![](https://qcloudimg.tencent-cloud.cn/raw/75df40175c2ab0886f3f9903929b2382.png)
3. 如果忘记了密码可以修改用户进行重置。
![](https://qcloudimg.tencent-cloud.cn/raw/e5cfc99941389fd07f9e26461cff1ba6.png)
4. 在浏览器里输入企业工作台的访问地址，输入已分配权限的用户名和密码进行登录。
![](https://qcloudimg.tencent-cloud.cn/raw/de5915c6ed1341b38c935795ef2c44f5.png)
5. 登录成功后，单击**新建**发起请假申请。
![](https://qcloudimg.tencent-cloud.cn/raw/00134f42fbe6f6ea43751c4a1eab34f0.png)
填写相关请假信息后单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/83da3417e0c3816051c111435eb3d469.png)
6. 审批人登录企业工作台进行处理即可。
![](https://qcloudimg.tencent-cloud.cn/raw/1faf5740b0677b9ed12b0343476cc06e.png)
