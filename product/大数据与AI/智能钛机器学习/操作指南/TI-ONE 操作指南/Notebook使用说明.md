
Notebook 作为一个灵活的交互式可视化开发工具，非常适合需要多次比对优化的算法调试环节。下文将介绍如何在智能钛机器学习平台建立、使用Notebook文件。

**新建 Notebook 容器**
单击【菜单栏】的 Notebook，页面将跳转至 Notebook 的容器列表页面，此页面将展示所有的容器信息。
单击【新增】按钮，输入容器名称以及选择此容器的框架。
目前支持 TensorFlow 和 PySpark，选择需要使用的资源和 COS 存储桶，单击确定完成新建。
![](https://main.qcloudimg.com/raw/1cec5070959d021ccd13342d70d78867.png)

可以对容器进行打开、停止、删除操作。单击【打开】进入容器内部，单击【停止】容器将会停止运行，单击【删除】，此容器记录销毁。

>!只有在停止状态下，才可以对容器的运行环境和运行资源进行配置和修改。

**Notebook 操作页面**
单击【打开】进入容器内部，右边为容器资源监控，中间为 notebook 内容展示区域。左栏主要为文件管理和各类功能键。
![](https://main.qcloudimg.com/raw/9364b81dffc85d648bd1066394969022.png)
用户可以：
1. 通过在 Terminal 文件中输入 pip list 命令行，查看容器内已有的依赖包；
2. 按照自己的需求通过 pip install 来安装内置列表外的依赖包。 
![](https://main.qcloudimg.com/raw/26ceb2082443f7214146efe04395dc2e.png)

**工作流应用 Notebook 文件**
如果用户需要在工作流中应用 Notebook 文件，可拖入一个**自定义脚本**的组件，单击【执行脚本】输入框。
![](https://main.qcloudimg.com/raw/3591c5e680e2d948a0e4ed877d436975.png)
弹出【选择脚本】弹窗，单击右下角的 notebook 图标。
![](https://main.qcloudimg.com/raw/3e4fbf56552804ad26ec7d4e0d15841c.png)
选择需要导入到任务流的 notebook 文件，并单击【导入】按钮。
![](https://main.qcloudimg.com/raw/42c0dd19a1119fc8a26518d6bd8f0eaf.png)
导入的 notebook 文件将会显示在资源列表中，选择需要应用到任务流的执行脚本，打钩即可。
![](https://main.qcloudimg.com/raw/0c24f957fffc12fcb15f96513c580096.png)
