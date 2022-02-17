## Notebook 概述

Notebook 作为一个灵活的交互式可视化开发工具，非常适合需要多次比对优化的算法调试环节。下文将介绍如何在智能钛机器学习平台建立、使用 Notebook 文件。

## Notebook 上手案例教程

智能钛机器学习平台为用户准备了利用 [Notebook 实现手写数字识别](https://cloud.tencent.com/document/product/851/38030) 案例，用户可以单击此案例进行查看及进行上手操作。

## Notebook 使用说明

#### 新建 Notebook 容器
单击【菜单栏】的 Notebook，页面将跳转至 Notebook 的容器列表页面，此页面将展示所有的容器信息。
单击【新增】按钮，输入容器名称以及选择此容器的框架。
目前支持 TensorFlow 和 PySpark，选择需要使用的资源和 COS 存储桶，单击确定完成新建。
![](https://main.qcloudimg.com/raw/de300b2221a0dae63c173643927e835d.png)
可以对容器进行打开、停止、删除操作。单击【打开】进入容器内部，单击【停止】容器将会停止运行，单击【删除】，此容器记录销毁。
 
>!只有在停止状态下，才可以对容器的运行环境和运行资源进行配置和修改。

#### Notebook 操作页面
单击【打开】进入容器内部，右边为容器资源监控，中间为 notebook 内容展示区域。左栏主要为文件管理和各类功能键。
![](https://main.qcloudimg.com/raw/9364b81dffc85d648bd1066394969022.png)
1. 通过在 Terminal 文件中输入**pip list**命令行，查看容器内已有的依赖包。
![](https://main.qcloudimg.com/raw/1394023d944f66f15233b076058b0543.png)
2. 按照自己的需求通过**pip install --user**来安装内置列表外的依赖包。 

#### 注意事项
用户安装依赖包时会遇到两种情况，一种是在镜像中已有，另一种在镜像中不存在此依赖包，需要用户下载依赖包后上传。可新建文件，并输入*“！pip install<包名> --user”* 运行后根据提示判断所属哪种情况。
- 第一种情况,用户所需的依赖包在镜像中已有，用户后续可直接输入 import 命令使用：
![](https://main.qcloudimg.com/raw/e0dffd92ba1f9016dd25ecb03c2aac66.png)   
- 第二种情况，用户所需的依赖包在镜像中并不存在，此时用户需要将所需的第三方依赖包下载后通过 pip install 命令安装成功后，后续再进行import命令使用：
![](https://main.qcloudimg.com/raw/d3b3fe88ed67815a19419f251a3c5cd8.png)  
- 上传依赖包并安装的具体操作如下：
单击【上传文件】，将依赖包上传。
![](https://main.qcloudimg.com/raw/7371e81145b0a47544d6d087cf75efb3.png)
- 新建 terminal 文件，并输入“pip install <包名> --user”命令安装。
- 如果系统出现以下提示代表需要升级 pip，需要先通过在 terminal 文件中输入“pip install --upgrade pip --user”来进行升级，升级后再进行 “pip install”操作。 
![](https://main.qcloudimg.com/raw/8076fe29324e3fb55aa0d812982d401b.png)
- 安装完依赖包后，需要重启 kernel 才能进行 import 操作。
![](https://main.qcloudimg.com/raw/3e72d7e56d4fcf96f44b4ea6163f1c19.png)

#### 工作流应用 Notebook 文件
如果用户需要在工作流中应用 Notebook 文件，可拖入一个**自定义脚本**的组件，单击【执行脚本】输入框。
![](https://main.qcloudimg.com/raw/3591c5e680e2d948a0e4ed877d436975.png)
弹出【选择脚本】，单击右下角的 notebook 图标。
![](https://main.qcloudimg.com/raw/4214c87cf96e4d83817b77ceb74f8231.png)
选择需要导入到任务流的 notebook 文件，并单击【导入】。
![](https://main.qcloudimg.com/raw/965c80c94fb7eb5bf4e14ef24181ec77.png)
导入的 notebook 文件将会显示在资源列表中，选择需要应用到任务流的执行脚本，打钩即可。
![](https://main.qcloudimg.com/raw/c68dc325c08664f0c9583060b892cadd.png)
