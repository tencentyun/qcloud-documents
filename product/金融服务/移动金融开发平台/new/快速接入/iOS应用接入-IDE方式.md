本文将为您介绍如何在 iOS 环境下，新建工程且使用 IDE 工具接入。

## 前置条件
- 已经下载并安装了 TMF IDE 工具。
- 已经在控制台创建应用。

## 操作步骤
### 步骤一：软件安装[](id:install)
1. [下载 IDE 开发工具 Apollo](https://tmf-warehouse-1257849200.cos.ap-beijing.myqcloud.com/tmf/ide/TMFApollo.zip)。
>?文件下载完成后浏览器可能会提示存在危险，请选择保留。
>
2. 将下载的文件解压缩后，移动至**应用程序**目录下。
3. 选择 Xcode Source Editor 设置，并勾选 Apollo。
4. 在应用程序中选择 Apollo 进行启动。

### 步骤二：使用 IDE 工具创建工程[](id:new)
>?如果您想在现有工程中使用 TMF，可以跳过本步骤。
>
1. 单击**创建工程**进行工程创建。
<img src="https://qcloudimg.tencent-cloud.cn/raw/0b017958a9f54a7af4784b400df91de2.png" width=70%> 
2. 输入项目名称，然后单击**下一步**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/53a07fc74b57ff6ecec967c578811f81.png" width=70%> 
3. 选择合适的基线版本，然后单击**下一步**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c3c59e3221c2bbb448b05fa7c2c53ead.png" width=70%> 
4. 勾选想要集成的TMF SDK，然后单击**下一步**。  
<img src="https://qcloudimg.tencent-cloud.cn/raw/c231688e7028d2459dd0562c257a6f5e.png" width=70%> 
5. 选择工程存放路径，单击**下一步**完成创建。


### 步骤三：导入工程[](id:import)
1. 将项目的 xcworkspace 文件拖入方框或单击选择文件。
>?该过程会自动解析出该工程的 SDK 静态库和动态库。
>
<img src="https://qcloudimg.tencent-cloud.cn/raw/ace14abfed3d902cd8c2e55b2fe26f26.png" width=70%>  
2. 在编辑模块中登录控制台，选择应用并下载配置文件。
<img src="https://qcloudimg.tencent-cloud.cn/raw/c906ca9f2e1f7167b1c4c33ea3df6953.png" width=70%> 
   - **编辑组件操作说明**：
     -  删除某组件，需要取消选中已安装的组件，关闭窗口后，单击**更新项目**即可生效。
     -  添加某组件，需要选中未安装的组件，关闭窗口后，单击**更新项目**即可生效。
   - **图标操作说明**：
     - <img src="https://qcloudimg.tencent-cloud.cn/raw/6e3650f205a573646736104032736ad7.png" width=3%> ：选择 Xcode 工程文件
     - <img src="https://qcloudimg.tencent-cloud.cn/raw/b49a012d622c40cff7201c4c3cb2c14d.png" width=3%> ：打开工程所在目录
     - <img src="https://qcloudimg.tencent-cloud.cn/raw/a35dfd9e64b80ba97f28e623e27bdd6d.png" width=3%> ：关闭当前工程
3. 单击**编辑组件**，可以在此处点击下载 TMF Demo 工程和 SDK 文档。
