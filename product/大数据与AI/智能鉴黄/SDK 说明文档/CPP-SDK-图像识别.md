

## 开发准备
>! 以下为 Linux 等类 UINX 系统使用手册，暂不支持 Windows 系统。

### SDK 获取
智能图像 C++ SDK 下载地址：[cpp-SDK-V2.0](https://github.com/tencentyun/image-cpp-sdk-v2.0) 。
### 开发准备
依赖静态库：curl jsoncpp (在 lib 文件夹下)；
依赖动态库： ssl crypto rtz (需要安装)；
(1)安装 openssl 的库和头文件 [http://www.openssl.org/source/](http://www.openssl.org/source/) ；
(2)安装 curl 的库和头文件 [http://curl.haxx.se/download/curl-7.43.0.tar.gz](http://curl.haxx.se/download/curl-7.43.0.tar.gz) ；
(3)安装 jsoncpp 的库和头文件 [https://github.com/open-source-parsers/jsoncpp](https://github.com/open-source-parsers/jsoncpp) ；
(4)安装 cmake 工具 [http://www.cmake.org/download/](http://www.cmake.org/download/) 。

### SDK 配置
直接下载 github 上提供的源代码，集成到您的开发环境。

执行下面的命令：
```
cd ${image-cpp-sdk-v2.0}
mkdir -p build
cd build
cmake ..
make
```
image_demo.cpp 里面有常见 API 的例子。生成的 image_demo 可直接运行，生成的静态库名称为：libimagesdk.a 。生成的 libimagesdk.a  放到用户自己的工程里 lib 路径下，include 目录拷贝到用户的工程的 include 路径下。
## 快速入门
### 在腾讯云申请业务的授权
授权包括： APPID 、SecretId 、 SecretKey ，目前只支持主账号及密钥进行调用。

### 创建对应操作类的对象
如果要使用图片，需要创建图片操作类对象：

```
//设置全局参数（非必须）
ImageSysConfig::setAuthExpiredTime(300); //设置签名超时时长300s
//生成ImageAPI对象
ImageConfig config(APP_ID, SECRET_ID, SECRET_KEY);
ImageAPI image(config);
```
### 调用对应的方法
在创建完对象后，根据实际需求，调用对应的操作方法就可以了。
### 图片识别
图片识别包括：图片鉴黄、图像分析、OCR - 身份证识别及 OCR - 名片识别。
#### 图片鉴黄
```
//单个或多个图片 Url
vector<string> pornUrls;   pornUrls.push_back("http://hearthstone.nos.netease.com/1/artworkGvG/GoblinBlastmagel.jpg");
pornUrls.push_back("http://hearthstone.nos.netease.com/1/artworknaxx/Faerlinal.jpg");
pornUrls.push_back("http://hearthstone.nos.netease.com/1/artworknaxx/KelThuzadl.jpg");
PornDetectReq pornReq(BUCKET, pornUrls);
ret = image.PornDetect(pornReq);
cout<<ret<<endl;
//单个或多个图片 File
map<string, string> pornImages;
pornImages["1.jpg"] = FileUtil::getFileContent("pic/1.jpg");
pornImages["2.jpg"] = FileUtil::getFileContent("pic/2.jpg");
pornImages["3.jpg"] = FileUtil::getFileContent("pic/3.jpg");
PornDetectReq pornReq2(BUCKET, pornImages);
ret = image.PornDetect(pornReq);
cout<<ret<<endl;      
```
#### 图像分析
```
//单个图片 Url
TagDetectReq tagReq(BUCKET);
tagReq.SetUrl("http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png");
ret = image.TagDetect(tagReq);
cout<<ret<<endl;
//单个图片 File
TagDetectReq tagReq(BUCKET);
tagReq.SetImage("hot1.jpg");
ret = image.TagDetect(tagReq);
cout<<ret<<endl;
```

#### OCR - 身份证识别
```
//单个或多个图片 Url,识别身份证正面
vector<string> idZUrls;
idZUrls.push_back("http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg");
idZUrls.push_back("http://img5.iqilu.com/c/u/2013/0530/1369896921237.jpg");
IdCardOcrReq idReq(BUCKET, idZUrls,0);
ret = image.IdCardOcr(idReq);
cout<<ret<<endl;
//单个或多个图片 File,识别身份证正面
map<string, string> idZImages;
idZImages["id6zheng.jpg"] = FileUtil::getFileContent("id6zheng.jpg");
idZImages["id2zheng.jpg"] = FileUtil::getFileContent("id2zheng.jpg");
IdCardOcrReq idReq2(BUCKET, idZImages, 0);
ret = image.IdCardOcr(idReq2);
cout<<ret<<endl;
//单个或多个图片 Url,识别身份证反面
vector<string> idFUrls;    idFUrls.push_back("http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg");    idFUrls.push_back("http://www.4009951551.com/upload/image/20151026/1445831136187479.png");
IdCardOcrReq idReq3(BUCKET, idFUrls,1);
ret = image.IdCardOcr(idReq3);
cout<<ret<<endl;
//单个或多个图片 File,识别身份证反面
map<string, string> idFImages;
idFImages["id5fan.jpg"] = FileUtil::getFileContent("id5fan.jpg");
idFImages["id7fan.jpg"] = FileUtil::getFileContent("id7fan.jpg");
IdCardOcrReq idReq4(BUCKET, idFImages, 1);
ret = image.IdCardOcr(idReq4);
cout<<ret<<endl;
```
#### OCR - 名片识别
```
//单个或多个图片 Url
vector<string> nameUrls;
nameUrls.push_back("http://pic1.nipic.com/2008-12-03/2008123181119306_2.jpg");
nameUrls.push_back("http://pic.58pic.com/58pic/12/49/04/80k58PICzYP.jpg");
NameCardOcrReq nameReq(BUCKET, nameUrls, 0);
ret = image.NameCardOcr(nameReq);
cout<<ret<<endl;
//单个或多个图片 File
map<string, string> nameImages;
nameImages["r.jpg"] = FileUtil::getFileContent("r.jpg");
nameImages["name2.jpg"] = FileUtil::getFileContent("name2.jpg");
NameCardOcrReq nameReq2(BUCKET, nameImages, 0);
ret = image.NameCardOcr(nameReq2);
cout<<ret<<endl;
```
