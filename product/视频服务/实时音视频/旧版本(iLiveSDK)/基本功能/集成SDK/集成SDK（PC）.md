本文将指导您完成在 PC 端下实时音视频客户端功能的 SDK 集成。
## 源码下载
在此我们提供以下所讲到的完整 Demo 代码，如有需要请您自行下载。
[Demo 代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/Demo/PC/demo_import.zip)
## 操作步骤
### 创建 Win32 Console 工程
1. 打开 Visual Studio ，单击【 文件 】菜单，选择【 新建 】-【 项目 】-【新建一个项目】：
![](https://main.qcloudimg.com/raw/d372db4d91a96b59e51b5d4e8666c92d.png)

2. 创建一个空工程：
![](https://main.qcloudimg.com/raw/45f4a6a7e495cc4519e11504eb5f5103.png)

3. 往工程中添加一个 cpp 文件，编写一个空的主函数：
![](https://main.qcloudimg.com/raw/b8d0335b0411d85630b14729235fc4fc.png)

### 集成 iLiveSDK

1. 下载iLiveSDK
从github上[下载iLiveSDK](https://github.com/zhaoyang21cn/iLiveSDK_PC_Suixinbo)

2. 拷贝文件
将iLiveSDK目录下的include和libs拷贝到解决方案文件( .sln文件 )所在的目录：
![](https://main.qcloudimg.com/raw/bf2314afd8169bdd18d6f8930ce18b8d.png)

3. 添加 include 目录
在项目的附加包含目录中添加 include 目录，`$(SolutionDir)include`：
![](https://main.qcloudimg.com/raw/ac105f6a7e9c5aa62cded86f6bf646ff.png)

4. 添加库目录
在项目的附加库目录中添加 lib 文件所在目录，`$(SolutionDir)libs`：
![](https://main.qcloudimg.com/raw/078a7447425662586f2e4af0e04a00d8.png)
>**注意:**
>上面添加 include 目录和库目录时，Debug 和 Release 版本都需要配置。

5. 包含头文件
在项目中包含头文件,并使用 ilive 命名空间，加载动态库的 lib 文件：
```c++
#include "iLive.h"
using namespace ilive;
#pragma comment(lib, "iLiveSDK.lib")
```

6. 拷贝 dll 文件到程序(.exe)所在目录：
将 libs 目录下的所有 dll 文件复制到解决方案的 Debug 和 Relase 目录下( 至少编译一次 Debug 和 Relase 才会生成这两个目录 )，此时可删除 libs 目录下的 dll 文件。
>**注意:**
>]这里不要将 iLiveSDK.lib 也删除了。

7. 验证是否配置成功
调用 GetILive() -> getVersion() ,输出返回值，查看当前 iLiveSDK 的版本号：
```c++
cout << GetILive()->getVersion() << endl;
```

### 源码说明

* Demo 源码编译报错：
![](https://main.qcloudimg.com/raw/0d24bb5f04331191ce82587dd083aced.png)

 - 可能是因为项目配置选择了64位。
![](https://main.qcloudimg.com/raw/6406babab972b935b36bdbef8741f6c5.png)
iLiveSDK暂时没有64位版本，需要切换成32位编译即可。


### 运行结果
按【 CTRL+F5 】运行程序，输出版本号：
![](https://main.qcloudimg.com/raw/9148232b9dee4bb1a7f7c6e90d8087cb.png)

恭喜，至此说明 iLiveSDK 已经成功集成。
