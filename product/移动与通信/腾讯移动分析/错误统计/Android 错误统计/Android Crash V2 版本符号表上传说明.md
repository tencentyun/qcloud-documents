用于 MTA Android Crash V 2版本符号表上传说明，主要分为 Java 符号表和 Native（C/C++）符号表两部分，用于系统还原混淆后的堆栈信息。

### Java 符号表
1. Eclipse
通常符号表名为“mapping.txt”，位于 proguard 目录下，如果是使用 ant 脚本编译，则在脚本指定的目录下。
2. Android Studio
在 build.gradle 文件中开启混淆代码，minifyEnabled 设置为 true 时生成 mapping 文件，路径一般为工程目录下的`build/outputs/mapping/release/mapping.txt`
![](http://developer.qq.com/wiki/mta/imgs/20170524182818_63386.png)
![](http://developer.qq.com/wiki/mta/imgs/20170524182930_41284.png)
3. Java 符号表上传
在前台打开符号表上传页面，填写 App 版本号，选择【Java】文件类型，单击【选择文件】，选取 mapping.txt 文件后单击上传即可。
![](http://developer.qq.com/wiki/mta/imgs/20170524183030_67938.png)

### Native 符号表

Native 符号表是为了找回 so 文件 Crash 堆栈还原使用的，由于编译器的问题，发布的 so 文件是已去符号化的，而编译过程中产生的中间文件才是带符号表信息的，因此建议大家每次构建版本时备份好 debug so 文件。
1. Eclipse
使用 eclipse 构建的 so 文件，debug so 位于项目的`/obj/local/xxxeabi/`目录下，其中 xxxeabi 为具体的架构信息，见下图：
![](http://developer.qq.com/wiki/mta/imgs/20170524183109_57363.png)
我们需要把 local 目录打包，建议打包前把架构下的 Objs 目录清除掉。
2. Android Studio
使用 Android Studio 编译的 so 文件，分为 Debug 和 Release 两个不同的版本，对应的目录通常为：`/<Module>/build/intermediates/cmake/debug/obj/xxxeabi/`和`/<Module>/build/intermediates/cmake/release/obj/xxxeabi/`，我们需要将 obj 目录整体打包成 zip 格式。
![](http://developer.qq.com/wiki/mta/imgs/20170524183147_55166.png)
不同的 Android studio 版本可能存在路径差异，可以使用以下方法来判断，以 Linux/Mac OS 系统为例：
i. 打开终端命令行，cd 到当前工程目录，输入`find ./ -name your-lib-name.so`，找到 so 编译生成目录
![](http://developer.qq.com/wiki/mta/imgs/20170524183225_69933.png)
ii. 输入`file your-full-so-path`，如果输出【not stripped】表示是带符号信息的 so 文件，输出【stripped】表示是删除符号表信息的 so 文件。
![](http://developer.qq.com/wiki/mta/imgs/20170524183233_30230.png)
3. Native 符号表上传
在前台打开符号表上传页面，填写 App 版本号，选择【native】文件类型，单击【选择文件】，选取刚刚打包的 zip 文件后单击上传即可。