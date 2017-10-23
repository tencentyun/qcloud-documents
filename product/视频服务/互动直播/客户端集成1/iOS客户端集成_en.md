## 1. Decompress the SDK

When the SDK zip file is decompressed, you can see the following directories. The following describes what each directory is for.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-1.png)

## 2. Import SDK

You need to introduce the header file first:

Add the two folders in the "include" folder of the SDK to Header Search Paths in Build Settings:
Add the folders "base" and "sdk" in the folder "include" of the SDK, as shown below.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-2.png)

On the iOS platform, the SDK's library files are provided in the form of static link libraries (.a). At Build Phases, add the libraries under libs, together with the static libraries they are dependent on to the Link list, as shown below:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-3.png)

## 3. Set C++ Compilation Method for Project

To unify the STL libraries connected in the code, you need to specify non-C++11 compilation method, as shown below:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-4.png)

## 4. Real-machine Compilation for Project

You need to set bundle identifier and certificate for real-machine compilation, as shown below:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-5.png)

The certificate configuration is as follows:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-6.png)

## 5. Developer Document

For more information, please see [Audio/Video Messaging Development Guide](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)
