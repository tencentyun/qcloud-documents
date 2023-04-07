## 操作场景
OrcaTerm 为腾讯云推荐的登录方式，您可以直接使用腾讯云 OrcaTerm 工具一键登录 Linux 实例。其优点如下：
- 支持复制、粘贴。
- 支持鼠标滚屏。
- 支持中文输入法。


<dx-alert infotype="explain" title="">
- OrcaTerm 原名 WebShell。
- 创建 Linux 操作系统的轻量应用服务器时，该服务器默认绑定1个密钥。此密钥对应的用户名为 `lighthouse`，具备 root 权限。
- 当您使用 OrcaTerm 工具登录 Linux 实例时，系统默认使用此密钥（对应的用户名为 `lighthouse`）进行登录。
</dx-alert>



## 适用本地操作系统
Windows，Linux 或者 Mac OS

## 前提条件

在登录前，请确认实例的防火墙已放行22端口（创建实例时默认已开通22端口）。

## 操作步骤

1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse/instance/index)。
2. 在服务器列表中找到对应的实例，并根据实际的操作习惯选择不同的方式进行登录。
 - 在服务器列表中的实例卡片上，单击**登录**。
![](https://main.qcloudimg.com/raw/ad83b4066ea56c22ca1593a6ab808ff0.png)
 - 单击实例卡片进入服务器详情页，单击“远程登录”中的**登录**，或页面右上角的**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/239f46c5fe0fc02e0c1d87655acdec5b.png)
 - 使用 [应用镜像](https://cloud.tencent.com/document/product/1207/44361#appOS) 创建的实例，可在实例详情页选择**应用管理**，单击页面右上角的**登录**。
![](https://qcloudimg.tencent-cloud.cn/raw/5ce9b1c13518ec9d17b6fa5a79a9f6cd.png)
登录成功界面如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ada571d01b40eea998b914cac03d5b7b.png)
    - 成功登录后，您可参考 [最佳实践](https://cloud.tencent.com/document/product/1207/45116) 及 [第三方教程](https://cloud.tencent.com/document/product/1207/58793)，进行搭建中小型网站、Web 应用、博客、论坛、小程序/小游戏、电商、云盘/图床、云端开发测试和学习环境等轻量级、低负载且访问量适中的应用。
    - WebSehll 界面功能丰富，您可参考 [更多 OrcaTerm 功能](#wedShellWork) 使用移动端的虚拟键盘，在控制台上更改 OrcaTerm 外观、上传/下载文件、发起实例自助检测、开启多会话、分屏、获取提示，开启轻量应用服务器的便捷使用。

### 更多 OrcaTerm 功能[](id:wedShellWork)

OrcaTerm 目前具备丰富的功能，希望您在使用过程中拥有满意的体验。欢迎您参与 [OrcaTerm 使用满意度调研](https://wj.qq.com/s2/10389082/ca3a/) 来提出更多建议或反馈，我们会不断改进 OrcaTerm，使您拥有更好的产品体验！

OrcaTerm 功能介绍如下：
<dx-accordion>
::: 支持多种快捷键[](id:hotKey)

OrcaTerm 已支持多种快捷键，您可在 OrcaTerm 界面中查看已支持的快捷键。步骤如下：
1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 在 OrcaTerm 界面中，打开“键盘快捷方式”窗口查看已支持的快捷键。
  - 本地操作系统为 Mac OS：按 `⌘ + /`。
  - 本地操作系统为 Windows：按 `Ctrl + /`。
  本文以 Windows 为例，查看已支持“键盘快捷方式”如下图所示，您可按需使用。
	![](https://qcloudimg.tencent-cloud.cn/raw/04d1b5c3bca238681fc54bd0873ee366.png)


:::
::: 查看实例监控数据[](id:monitoringData)

您可在 OrcaTerm 界面中查看实例实时监控数据，目前监控数据的刷新粒度为10s。查看步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 在 OrcaTerm 界面下方，即可查看实例监控数据。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c9cbc3ab7f54edaf9431621a8cb65e49.png)



:::
::: 修改用户名[](id:modifyUsername)

您可在使用 OrcaTerm 登录时，指定需登录的用户。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 在弹出的“登录”窗口中，用户名默认为 `lighthouse`，您可按需修改。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e11b7d3f8a2c9c8b20f744bcfcbce64d.png)
3. 修改完成后，单击**登录**即可。



:::
::: 一键安装自动化助手[](id:installTAT)


使用 OrcaTerm 一键免密登录方式需自动化助手支持。若您的实例未安装自动化助手，可在登录时选择安装。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 在弹出的“登录”窗口中，若提示您的实例未安装自动化助手，您可按需选择安装方式。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e509b7c48e88489a5f53f089a770b1e0.png)
   - 选择**一键安装(需要重启)**：请阅读注意事项，勾选“安装过程需要您同意强制关机”后，单击**一键安装自动化助手**即可。
   - 选择**手动安装(不需要重启)**：请参考 [安装自动化助手客户端](https://cloud.tencent.com/document/product/1340/51945) 完成安装。
3. 安装完成后，即可使用 OrcaTerm 方式一键登录实例。

:::
::: 使用命令块模式[](id:block)

您可通过该步骤，在 OrcaTerm 界面中使用命令块模式。开启后，执行的每条命令会以模块进行展示，帮助您便捷使用 OrcaTerm。您也可按需关闭命令块模式。具体操作步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 在 OrcaTerm 界面中，您可开启或关闭命令行模式。
  - **开启命令行模式**：选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/2a7a6b5795be349496600bda16a038c6.png" style="margin:-3px 0px"> 即可开启命令块模式。开启后执行命令效果如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/2b3752cb5644e4e06af15d037a7992cb.png)
  - **关闭命令行模式**：选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/bb5426e4e2012fc77ff78561de913e15.png" style="margin:-3px 0px"> 即可关闭命令块模式。关闭后执行命令效果如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/5862c7588022194f1a855f26e87b6f86.png)
<dx-alert infotype="explain" title="">
若关闭后重新开启命令块模式，需重新连接 OrcaTerm。
</dx-alert>



:::
::: 查看发布说明[](id:changelogs)
您可通过该步骤，查看 OrcaTerm 最近一次的发布说明，包含新特性、Bug 修复、即将上线的功能。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择 OrcaTerm 界面右下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/4796538ba87024b0a264e8d512c4544b.png" style="margin:-3px 0px">。
3. 您即可在弹出窗口中查看最近一次的发布说明。如需查看所有发布记录，可参见 [OrcaTerm 更新记录](https://cloud.tencent.com/document/product/1207/76448)。

:::
::: 选择实例登录[](id:choose)
您可通过该步骤，在一个 OrcaTerm 窗口中选择任意一台实例登录。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/5bb1db36d10fd49f34ecc27eda0e306a.png" style="margin:-3px 0px">。
3. 首次选择会弹出的“选择要展示的实例”窗口，请选择您期望登录的实例，并单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ebc15cae5b84fc92dca6c8380dade5ab.png)
4. 选择 <img src="https://qcloudimg.tencent-cloud.cn/raw/5bb1db36d10fd49f34ecc27eda0e306a.png" style="margin:-3px 0px"> > **添加实例**，并按需添加多个实例。
<dx-alert infotype="explain" title="">
目前最多支持添加10个实例。
</dx-alert>
5. 添加成功后，您选择任意实例即可登录。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/41089996dd2363a7516c2683794e3cbf.png)



:::
::: 上传/下载文件[](id:updownload)



您可通过该步骤，向实例上传本地文件，或将实例文件下载至本地。具体步骤如下：<br>

**上传文件：**
1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择以下任意一种方式上传文件：
	A. 拖拽上传。直接将本地文件拖进 OrcaTerm 页面，即可上传文件。
	B. 选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/81fbdd2c2b7cb70f17c508073496f58e.png" style="margin:-3px 0px"> > **上传**，按需选择“本地上传”或 “URL上传”。
	![](https://qcloudimg.tencent-cloud.cn/raw/be8bed15b836bc34773d87cd0e48105f.png)
		&nbsp;&nbsp;a. 选择“本地上传”，则请单击**点击上传**后选择本地文件。选择 “URL上传”，则请在 “URL地址”中输入需上传文件的 URL。
		&nbsp;&nbsp;b. 选择需上传位置后，单击**确定**即可。
<dx-alert infotype="explain" title="">
目前仅支持上传文件至  `home > lighthouse` 目录。
  </dx-alert>
3. 您可单击页面右下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/a78e204de7cde3473482732c8b9fef98.png" style="margin:-3px 0px">，在弹出窗口中查看操作结果。上传成功则如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/742c648fbb6191849f0f1b4ad31df288.png)




**下载文件：**
1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择以下任意一种方式上传文件：
 A：选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/81fbdd2c2b7cb70f17c508073496f58e.png" style="margin:-3px 0px"> > **下载**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/949a7c8ce622be22f5f74d029c42b3be.png)
 B：选择所需文件右键 > 下载。
<img style="width:900px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/47281d12404156294c8543d421afee8f.png" />

3. 在弹出窗口的“下载文件”窗口中，依次再开目录，选择需下载的文件。
4. 单击**确定**，并在弹出窗口中，选择需存储的本地位置。
5. 您可单击页面右下角的 <img src="https://qcloudimg.tencent-cloud.cn/raw/a78e204de7cde3473482732c8b9fef98.png" style="margin:-3px 0px">，在弹出窗口中查看操作结果。下载成功则如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/5e54b868de203f3dd24e4213eb9ad194.png)


:::
::: 使用实例自助检测[](id:selfCheck)

若您在登录或使用实例过程中遇到问题，可随时使用实例自助检测。步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/2d3d7e693d09bb8a58d58557e4f25ff4.png" style="margin:-3px 0px">。
3. 在弹出的“实例自助检测”窗口中，单击**确定**即可使用实例自助检测。您可参考 [使用实例自助检测](https://cloud.tencent.com/document/product/1207/74704) 了解实例自助检测及检测项。


:::
::: 开启多标签窗口会话[](id:multilabel)

您可通过该步骤，在 OrcaTerm 界面以标签的形式打开多个实例连接界面，以便捷使用实例。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择 OrcaTerm 界面上方的 <img src="https://qcloudimg.tencent-cloud.cn/raw/fc93655617db690aecdc7b1cea0baf39.png" style="margin:-3px 0px">。
3. 您即可看到已新建了标签 `(1)实例 ID`，如下图所示：
<dx-alert infotype="explain" title="">
- 最多支持同时打开5个标签。
- 标签将以 `（递增数字）实例 ID` 命名，帮助您区分标签。
</dx-alert> <img src="https://qcloudimg.tencent-cloud.cn/raw/0728ea1b064247a70ee8cb0d8d2b9738.png"/>


:::
::: 开启分屏[](id:splitScreen)

您可通过该步骤，在 OrcaTerm 界面开启分屏，开启后您可同屏查看并执行多个操作任务，以便捷使用实例。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择 OrcaTerm 界面上方的 <img src="https://qcloudimg.tencent-cloud.cn/raw/bf17a1103ce6fa76150df87768987f79.png" style="margin:-3px 0px">。
3. 您即可看到已执行分屏，命名为 `(1)实例 ID`。如下图所示为3个分屏效果：
<dx-alert infotype="explain" title="">
- 最多支持同时4个分屏。
- 分屏将以 `（递增数字）实例 ID` 命名，帮助您进行区分。
</dx-alert> <img src="https://qcloudimg.tencent-cloud.cn/raw/a728109914be625fef86de80a5a0eb65.png"/>


:::
::: 更改皮肤[](id:changeAppearance)

您可通过该步骤，修改 WedShell 界面的文字大小、字体及配色。具体步骤如下：

1. 参考 [使用 OrcaTerm 方式登录 Linux 实例](https://cloud.tencent.com/document/product/1207/44642)，登录实例。
2. 选择 OrcaTerm 界面工具栏中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/183be38a53180ccd705dddbb859820e3.png" style="margin:-3px 0px">。
3. 在弹出的菜单中修改字体大小、字体或配色，按照喜好更改 OrcaTerm 外观。
![](https://qcloudimg.tencent-cloud.cn/raw/cca68be8bd34a8aa7be49387322701e5.png)



:::
::: 使用移动端虚拟键盘[](id:virtualKeyboard)


1. 微信搜索“腾讯云助手”小程序，并登录腾讯云账号。
2. 选择页面下方的**控制台**，并单击页面中“收藏的云产品”中的**更多云产品**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/194d2b7f4625d0442f1546eda1bb7816.jpg)
3. 在“云产品中心”页面，选择**轻量应用服务器**。
4. 在“轻量应用服务器”控制台页面，选择实例所在地域，并单击实例卡片中的 <img src="https://qcloudimg.tencent-cloud.cn/raw/278e10214177bff2c64ae55480c99493.png" style="margin:-3px 0px">。
5. 在弹出窗口中，单击**登录**。
6. 登录成功后，可选择键盘右上方的**虚拟**。开启后如下图所示，您可再次单击**系统**切换回手机系统键盘。
![](https://qcloudimg.tencent-cloud.cn/raw/4b7d0c48fb3da02ccf3ab06e9ad50be4.png)



:::
</dx-accordion>
