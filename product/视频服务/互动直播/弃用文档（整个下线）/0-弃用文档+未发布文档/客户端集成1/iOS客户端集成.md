## 1 解压SDK

SDK的zip包解压后，可以看到如下目录，各目录的作用如下：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-1.png)

## 2 导入SDK

首先需要引入头文件：

在Build Settings 里的Header Search Paths 加入sdk的include里的两个文件夹：
如下图，添加SDK的include文件夹的base和sdk文件夹。

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-2.png)

在IOS平台上，SDK的库文件目前以静态链接库(.a)的形式提供。请在Build Phases里添加libs下的各个库到到Link列表里，另外还需要把我们依赖的静态库也添加下去，详情如下：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-3.png)

## 3 设置项目C++编译方式。

为了统一代码里连接的STL库，需要指定非C++11编译方式。如下图：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-4.png)

## 4 项目的真机编译问题

真机编译时需要设置bundle identifier 和证书。如下图：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-5.png)

证书配置如下图：

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-6.png)

## 5 开发者文档

详情参考[音视频通信开发指南](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)