PAG 插件用于生成高级模版，本文介绍 PAG 插件的安装说明。

## 简介
- PAG（Portable Animated Graphics）是一套完整的动效工作流解决方案。目标是降低或消除动效相关的研发成本，能够一键将设计师在 AE（Adobe After Effects）中制作的动效内容导出成素材文件。PAG 文件的后缀为 `.pag`。
- PAGViewer 是一个桌面工具，提供从**导出插件**到**桌面预览**等一系列完善的桌面效率工具，让设计师可以所见即所得地生产素材，研发无需介入还原效果，极大降低了设计与研发的对接成本。

## 操作步骤
### 步骤1：安装 PAGViewer
目前 PAG 预览程序支持 macOS 和 Windows 操作系统。
<dx-tabs>
::: macOS
- **命令行安装**
复制以下文本内容，粘贴到“终端”程序按下回车即可开始在线安装，安装过程可能会要求输入本机密码以获取文件写入权限。
```
curl -s dldir1.qq.com/qqmi/libpag/install|bash
```
目前 PAGViewer 预览程序和 PAG 导出插件仅支持 macOS 10.14及以上。安装成功后，PAGViewer会出现在“应用程序”文件夹中，并自动关联本地 pag 文件，双击 pag 文件即可呼起 PAGViewer 直接预览播放。
- **图形化安装**
进入 [PAGViewer.dmg](https://dldir1.qq.com/qqmi/libpag/PAGViewer.dmg) 单击下载离线安装包，双击打开 `PAGViewer.dmg` 文件，拖拽 PAGViewer 到应用程序文件夹即可。
:::
::: Windows
PAGViewer Beta 版现在支持在 Windows 下预览 PAG 文件。安装成功后，PAGViewer 会出现在开始菜单中，并自动关联本地 pag 文件，双击 pag 文件即可呼起 PAGViewer 直接预览播放。
**安装方法如下：**
进入 [PAGViewer_Installer.exe](https://dldir1.qq.com/qqmi/libpag/PAGViewer_Installer.exe) 单击**下载**安装程序，双击即可安装，安装过程中可能会要求取得管理员权限。
:::
</dx-tabs>

### 步骤2：测试
下载 [pag_files.zip ](https://pag.art/file/pag_files.zip) 并解压，按照如下操作测试PAGViewer是否安装成功。
1. 直接双击文件夹里的 pag 文件，即可看到动效的预览效果。
![](https://qcloudimg.tencent-cloud.cn/raw/2fd91a4dc8618b1889c304aa59a65884.png)
2. 文件夹中的 **Replacement.pag** 文件是个占位图动效示例，您可以双击打开它后拖拽任意一张其他图片到窗口里，即可看到窗口里的动效效果被套用到了拖进去的图片上。您也可以直接使用压缩包里的 AE 源文件自行导出 pag 文件进行预览。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/ce66aeee00a2e3ad67d2e3a347a4a8e7.png" width=400/>

如果以上操作均能实现则表明 PAGViewer 安装成功。


### 步骤3：安装 PAG 插件
1. 如果 AE 正在运行，则关闭。
2. 打开 PAGViewer。PAGViewer 将自动检测是否需要安装/更新 AE 导出插件，按提示安装即可。
<img src="https://qcloudimg.tencent-cloud.cn/raw/9b59c1ecb9dee9a829079f1951f9a6ed.png" width=600/><br>
3. 如果 PAGViewer 没有自动提示安装，则可以单击触发安装：
	- MAC：单击菜单栏 **PAGViewer > 安装 AE 插件**。
	- Windows：单击菜单栏 **文件 > 安装 AE 插件**。
![](https://qcloudimg.tencent-cloud.cn/raw/e8b5150eddd7448f0aceb15a40fdeb53.png)

### 步骤4：验证
打开 AE 软件，在菜单项中将会看到：**文件 > 导出 > PAG File...**，则说明已经成功安装。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1bad72d88c73494ad10c764cd18a43b2.png" width=600/>

## 总结
学习完本教程后，我们已初步了解如何安装 PAGViewer 及 PAG 导出插件。
