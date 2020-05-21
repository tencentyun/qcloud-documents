### iOS 获取 DEVELOPMENT_TEAM 的方法
- 方法1：cd 到 项目 aaa.xcodeproj 文件同目录下，执行 grep-h-r--include *.pbxproj DEVELOPMENT_TEAM . | uniq 
- 方法2：在 Xcode 直接去查看 DEVELOPMENT_TEAM

### Android 获取签名文件的哈希值的方法
第一步：在终端输入下面命令：keytool –list –v –keystore <签名文件路径>
第二步：拷贝 SHA1 的值，**去除冒号**填入输入框中。
![](https://main.qcloudimg.com/raw/d39d975493a67f55554417f5145965da/202004291035.png)
