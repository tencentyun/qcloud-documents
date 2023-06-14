## 获取方式
关于微信 openid 的说明请参见 [小程序 openid 说明](https://developers.weixin.qq.com/community/develop/article/doc/00082a04b94c00a9f3eb879ba5ac13)。
下面通过两个简单的 demo，分别说明在表达式和代码编辑器中如何获取小程序用户的 openid。

### 场景一：从表达式中获取
场景说明：单击按钮时，弹窗展示用户的 openid，具体的操作步骤如下。
1. 绑定按钮的点击事件为打开弹窗。
![](https://qcloudimg.tencent-cloud.cn/raw/5bf89d0778754b560d9fd9bca896ea8a.png)
2. 在打开弹窗的配置面板中，内容字段单击绑定表达式。
![](https://qcloudimg.tencent-cloud.cn/raw/b980fa3eec802b2d060c3307d0fff980.png)
3. 选择表达式中的**变量** > **全局** > **登录用户信息** > **微信/企微 openid** 后，小程序用户的 openid 获取路径就会自动填写到表达式中，单击**保存**。
![](https://qcloudimg.tencent-cloud.cn/raw/03affc3496ebbe437b5c0be7f8ae71ea.png)
4. 将应用发布为小程序，微信扫码打开小程序之后，单击按钮，即可看到用户的 openid。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/7657587fafb6d0deb804b0670fa5dd15.jpeg" style="zoom: 20%;" />

### 场景二：在代码编辑器中获取
场景说明：小程序页面加载时，在控制台打印用户的 openid，具体操作步骤如下。
1. 在大纲树中选择页面，配置**页面显示**事件对应的动作为自定义方法。
![](https://qcloudimg.tencent-cloud.cn/raw/f94bcc131baf658016e968e56bd23322.png)  
2. 在自定义方法配置面板中，选择**新建方法**，填写方法名称和代码后单击**保存**。代码内容如下：
<dx-codeblock>
:::  js
  console.log(app.auth.currentUser.openId)
:::
</dx-codeblock>

 ![](https://qcloudimg.tencent-cloud.cn/raw/5bacb6c6845e79d45532405dacdd48d8.png)
3. 将应用发布为小程序，打开调试模式并刷新页面，可以看到当页面加载时 openid 已经成功输出。
<img src="https://qcloudimg.tencent-cloud.cn/raw/000784181a9407081c2b586feaa44618.png" style="zoom: 50%;" />  
