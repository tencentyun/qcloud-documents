# Notebook使用说明

Notebook作为一个灵活的交互式可视化开发工具，非常适合算法调试这种需要多次比对优化的开发场景。现在我们来看一下在智能钛机器学习平台如何建立、使用Notebook文件。

#### 新建Notebook容器

点击**菜单栏**的Notebook，页面将跳转至Notebook的容器列表页面，此页面将展示所有的容器信息。

点击**新增**按钮，输入容器名称以及选择此容器的框架。

目前支持**TensorFlow和PySpark**，选择需要使用的资源和COS存储桶，点击确定完成新建。

![https://main.qcloudimg.com/raw/1cec5070959d021ccd13342d70d78867.png](https://main.qcloudimg.com/raw/1cec5070959d021ccd13342d70d78867.png)

可以对容器进行打开、停止、删除操作。点击“打开”进入容器内部，点击“停止”容器将会停止运行，点击“删除”，此容器记录销毁。

注意：只有在停止状态下，才可以对容器的运行环境和运行资源进行配置和修改。

#### Notebook操作页面

点击**打开**进入容器内部，右边为容器资源监控，中间为notebook内容展示区域。左栏主要为文件管理和各类功能键。

![https://main.qcloudimg.com/raw/9364b81dffc85d648bd1066394969022.png](https://main.qcloudimg.com/raw/9364b81dffc85d648bd1066394969022.png)

用户可以：

1. 通过在Terminal文件中输入**pip list**命令行，查看容器内已有的依赖包；
2. 按照自己的需求通过**pip install**来安装内置列表外的依赖包。 



![https://main.qcloudimg.com/raw/26ceb2082443f7214146efe04395dc2e.png](https://main.qcloudimg.com/raw/26ceb2082443f7214146efe04395dc2e.png)

工作流应用Notebook文件
----------------------

如果用户需要在工作流中应用Notebook文件，可拖入一个**自定义脚本**的组件，点击“执行脚本”输入框。

![https://main.qcloudimg.com/raw/f61731a049acf84c9fac96088fde7b05.png](https://main.qcloudimg.com/raw/f61731a049acf84c9fac96088fde7b05.png)

弹出**选择脚本**弹窗，点击右下角的**notebook**图标。

![https://main.qcloudimg.com/raw/3e4fbf56552804ad26ec7d4e0d15841c.png](https://main.qcloudimg.com/raw/3e4fbf56552804ad26ec7d4e0d15841c.png)

选择需要导入到任务流的notebook文件，并点击**导入**按钮。

![https://main.qcloudimg.com/raw/42c0dd19a1119fc8a26518d6bd8f0eaf.png](https://main.qcloudimg.com/raw/42c0dd19a1119fc8a26518d6bd8f0eaf.png)

导入的notebook文件将会显示在资源列表中，选择需要应用到任务流的执行脚本，打钩即可。

![https://main.qcloudimg.com/raw/0c24f957fffc12fcb15f96513c580096.png](https://main.qcloudimg.com/raw/0c24f957fffc12fcb15f96513c580096.png)
