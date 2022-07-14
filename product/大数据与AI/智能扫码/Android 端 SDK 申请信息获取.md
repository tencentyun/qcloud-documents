## 获取 Android PackageName

- 在项目的 App 模块中 src/main 目录下的 AndroidManifest.xml 注册文件里找到 package 的值。

![](https://main.qcloudimg.com/raw/28349f0278547fe5665cea2b982adfa6.png)

- 代码获取：Context.getPackageName();(例子：com.tencent.cloud)

## 获取 App 签名哈希值(Android)

- 第一步：在终端输入下面命令：keytool –list –v –keystore <签名文件路径>

- 第二步：拷贝 SHA1 的值，**去除冒号**填入输入框中。(例子：560E84804895CB00D2ABF8592145C44840D66661)

![](https://main.qcloudimg.com/raw/2d276c53456d6cf3e3cfbbee3de8d451.png)
