## 第一课 集成SDK

### 导语
欢迎来到第一课!

在学习iLiveSDK之前，我们将先学习如何集成iLiveSDK。

### 预备知识
本课程要求用户对Visual Studio的使用有基本了解。

### 创建一个Win32 Console工程
打开Visual Studio,点击“文件”菜单，选择“新建”-->“项目”新建一个项目:

![](https://main.qcloudimg.com/raw/d372db4d91a96b59e51b5d4e8666c92d.png)

创建一个空工程

![](https://main.qcloudimg.com/raw/45f4a6a7e495cc4519e11504eb5f5103.png)

往工程中添加一个cpp文件，编写一个空的主函数

![](https://main.qcloudimg.com/raw/b8d0335b0411d85630b14729235fc4fc.png)

### 集成iLiveSDK

1. 下载iLiveSDK

[iLiveSDK下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/iLiveSDK.zip)

2. 将iLiveSDK的include和libs拷贝到解决方案文件(.sln文件)所在的目录，如下图;

![](https://main.qcloudimg.com/raw/bf2314afd8169bdd18d6f8930ce18b8d.png)

3. 添加include目录

在项目的附加包含目录中添加include目录, $(SolutionDir)include,如下图,

![](https://main.qcloudimg.com/raw/ac105f6a7e9c5aa62cded86f6bf646ff.png)

4. 添加库目录

在项目的附加库目录中添加lib文件所在目录,$(SolutionDir)libs,如下图,

![](https://main.qcloudimg.com/raw/078a7447425662586f2e4af0e04a00d8.png)

注: 上面添加include目录和库目录时，Debug和Release版本都需要配置;

5. 包含头文件

在项目中包含头文件,并使用ilive命名空间，加载动态库的lib文件,代码如下，

```c++
#include "iLive.h"
using namespace ilive;
#pragma comment(lib, "iLiveSDK.lib")
```

6. 拷贝dll文件到程序(.exe)所在目录

将libs目录下的所有dll文件复制到解决方案的Debug和Relase目录下(至少编译一次Debug和Relase才会生成这两个目录)，此时可删除libs目录下的dll文件,注意，这里不要将iLiveSDK.lib也删除了;

7. 验证是否配置成功

调用GetILive()->getVersion(),输出返回值，查看当前iLiveSDK的版本号;

```c++
cout << GetILive()->getVersion() << endl;
```

### 源码说明

* demo源码编译报错如下时，

![](https://main.qcloudimg.com/raw/0d24bb5f04331191ce82587dd083aced.png)

可能是因为项目配置选择了64位，如下图，

![](https://main.qcloudimg.com/raw/6406babab972b935b36bdbef8741f6c5.png)

iLiveSDK暂时没有64位版本，需要切换成32位编译即可，后面课程对此问题不再说明;


### 运行结果
按"CTRL+F5"运行程序，输出版本号，如下图

![](https://main.qcloudimg.com/raw/9148232b9dee4bb1a7f7c6e90d8087cb.png)

恭喜，至此说明iLiveSDK已经成功集成！

### [源码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_import.zip)


[下一课 登录](登录.md)