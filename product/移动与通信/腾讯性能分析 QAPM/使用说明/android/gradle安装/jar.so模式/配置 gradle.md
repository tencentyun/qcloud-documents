1. 使用 gradle 安装的，首先打开工程根目录下的 build.gradle
 ![](https://main.qcloudimg.com/raw/18f37f7a8bd2271cac31f2e9a4fb1850.png)

2. 在 android 模块中添加
```
sourceSets {
    main {
        jniLibs.srcDir(['libs'])
    }
}
```
![](https://main.qcloudimg.com/raw/7fa7055484fbc715d717fd7bfebce966.png)

3. 在 dependencies 模块中添加代码
```
compile files('libs/QAPM.jar')
```
![](https://main.qcloudimg.com/raw/fff3b98c8ee7e4d1b4d34f9305c7a443.png)