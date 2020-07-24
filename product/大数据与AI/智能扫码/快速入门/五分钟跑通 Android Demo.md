## 准备工作
请先按照 [接入准备](https://cloud.tencent.com/document/product/1214/45793) 所述流程下载好 Demo 工程文件。

## 步骤1：设置密钥

使用 Android Studio 打开下载好的 Demo 工程文件，在 MainActivity 的 SECRET_ID和SECRET_KEY 中填入您的专属密钥。

<img src="https://main.qcloudimg.com/raw/e34f31c9afad4eae7a02eeca8c030913.png" style="zoom:70%;" />

## 步骤2：设置 App 签名文件

在 App 模块下的 build.gradle 文件中，设置 signingConfigs。storeFile file 里填入您的 App 签名文件的路径（**注意：该签名文件要与您在控制台申请密钥时用来获取哈希值的签名文件相一致**），并填入对应的 storePassword、keyAlias 和 keyPassword 的值。

![](https://main.qcloudimg.com/raw/ea8f32dbb5d59d735fd425b439333cef.png)

## 步骤3：替换 App 包名

需要更改 Demo 工程文件的包名为您申请密钥时使用的包名，然后重新 build 工程。步骤如下：

1. 在 AndroidManifest.xml 更改 package 值为您申请密钥时填写的 App 包名。

2. 在工程的 java 目录下新建对应包名目录结构的目录，例如您的包名为 aaa.bbb.ccc 则在 java 下新建目录结构为：
   - java
      - aaa
         - bbb
            - ccc

3. 将 Demo 工程文件原始 java 目录下最底层的一个子目录的文件复制到上述新建目录的最底层目录里，即 ccc 下。

4. 确认复制过去的文件头部的包名是您的 App 包名，如果不是，可以在项目或者 module 右键，单击 replace in path，替换文件中的包名。

5. 删除掉原本 Demo 工程文件里 java 目录下的子目录及相关文件，重新 build 整个项目。

   <img src="https://main.qcloudimg.com/raw/be756316dcf4b0eef20715bd4a72d8d2.png" alt="image-20200616104735085" style="zoom:67%;" />

## 步骤4：运行真机调试


