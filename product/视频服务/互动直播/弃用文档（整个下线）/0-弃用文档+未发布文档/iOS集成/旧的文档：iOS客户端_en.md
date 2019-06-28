## 1 Unzip the SDK

After the SDK is unzipped, you can see the following directories, and the role of each directory is as follows:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-1.png)

## 2 Import SDK

You need to introduce the header file at first:

Add the two folders in the "include" folder of the SDK to Header Search Paths in Build Settings:
Add the folders "base" and "sdk" in the folder "include" of the SDK, as shown below.

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-2.png)

On the IOS platform, the SDK's library files are currently provided in the form of static link library (.a). In Build Phases, please add various libraries under libs to the Link list, and you also need to add the static libraries that we rely on, details as follows:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-3.png)

## 3 Set the C++ compilation method for project

To unify the STL libraries connected in the code, you need to specify the non-C++11 compilation method,  as shown below:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-4.png)

## 4 Real machine compilation problems with project

You need to set bundle identifier and certificate when the real machine is compiled,  as shown below:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-5.png)

The certificate configuration is as follows:

![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/yinshipinioskehuduanjicheng-6.png)

## 5. Developer Document

For more information, please see [Audio/Video Communication Development Guide](http://cloud.tencent.com/wiki/%E9%9F%B3%E8%A7%86%E9%A2%91%E9%80%9A%E4%BF%A1%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)
