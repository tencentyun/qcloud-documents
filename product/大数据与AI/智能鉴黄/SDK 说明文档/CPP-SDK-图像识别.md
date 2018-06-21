## 开发准备
><font color="#0000cc">**注意：** </font>
以下为 Linux 等类 UINX 系统使用手册，暂不支持 windows 系统。

### SDK 获取
万象优图 C++ SDK 下载地址：[cpp-SDK-V2.0](https://github.com/tencentyun/image-cpp-sdk-v2.0) 。
### 开发准备
依赖静态库: curl jsoncpp (在 lib 文件夹下)；
依赖动态库: ssl crypto rtz (需要安装)；
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
授权包括： APPID 、SecretId 、 SecretKey 及存储桶名（可参考 [域名管理](https://cloud.tencent.com/document/product/460/6937) ）。

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
在创建完对象后，根据实际需求，调用对应的操作方法就可以了。SDK 提供的方法包括：图片识别、人脸识别及人脸核身等。
### 图片识别
图片识别包括：图片鉴黄、图片标签、OCR - 身份证识别及 OCR - 名片识别。
#### 图片鉴黄
```
//单个或多个图片Url
vector<string> pornUrls;   pornUrls.push_back("http://hearthstone.nos.netease.com/1/artworkGvG/GoblinBlastmagel.jpg");
pornUrls.push_back("http://hearthstone.nos.netease.com/1/artworknaxx/Faerlinal.jpg");
pornUrls.push_back("http://hearthstone.nos.netease.com/1/artworknaxx/KelThuzadl.jpg");
PornDetectReq pornReq(BUCKET, pornUrls);
ret = image.PornDetect(pornReq);
cout<<ret<<endl;
//单个或多个图片File
map<string, string> pornImages;
pornImages["1.jpg"] = FileUtil::getFileContent("pic/1.jpg");
pornImages["2.jpg"] = FileUtil::getFileContent("pic/2.jpg");
pornImages["3.jpg"] = FileUtil::getFileContent("pic/3.jpg");
PornDetectReq pornReq2(BUCKET, pornImages);
ret = image.PornDetect(pornReq);
cout<<ret<<endl;      
```
#### 图片标签
```
//单个图片url
TagDetectReq tagReq(BUCKET);
tagReq.SetUrl("http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png");
ret = image.TagDetect(tagReq);
cout<<ret<<endl;
//单个图片file
TagDetectReq tagReq(BUCKET);
tagReq.SetImage("hot1.jpg");
ret = image.TagDetect(tagReq);
cout<<ret<<endl;
```

#### OCR - 身份证识别
```
//单个或多个图片Url,识别身份证正面
vector<string> idZUrls;
idZUrls.push_back("http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg");
idZUrls.push_back("http://img5.iqilu.com/c/u/2013/0530/1369896921237.jpg");
IdCardOcrReq idReq(BUCKET, idZUrls,0);
ret = image.IdCardOcr(idReq);
cout<<ret<<endl;
//单个或多个图片file,识别身份证正面
map<string, string> idZImages;
idZImages["id6zheng.jpg"] = FileUtil::getFileContent("id6zheng.jpg");
idZImages["id2zheng.jpg"] = FileUtil::getFileContent("id2zheng.jpg");
IdCardOcrReq idReq2(BUCKET, idZImages, 0);
ret = image.IdCardOcr(idReq2);
cout<<ret<<endl;
//单个或多个图片Url,识别身份证反面
vector<string> idFUrls;    idFUrls.push_back("http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg");    idFUrls.push_back("http://www.4009951551.com/upload/image/20151026/1445831136187479.png");
IdCardOcrReq idReq3(BUCKET, idFUrls,1);
ret = image.IdCardOcr(idReq3);
cout<<ret<<endl;
//单个或多个图片file,识别身份证反面
map<string, string> idFImages;
idFImages["id5fan.jpg"] = FileUtil::getFileContent("id5fan.jpg");
idFImages["id7fan.jpg"] = FileUtil::getFileContent("id7fan.jpg");
IdCardOcrReq idReq4(BUCKET, idFImages, 1);
ret = image.IdCardOcr(idReq4);
cout<<ret<<endl;
```
#### OCR - 名片识别
```
//单个或多个图片Url
vector<string> nameUrls;
nameUrls.push_back("http://pic1.nipic.com/2008-12-03/2008123181119306_2.jpg");
nameUrls.push_back("http://pic.58pic.com/58pic/12/49/04/80k58PICzYP.jpg");
NameCardOcrReq nameReq(BUCKET, nameUrls, 0);
ret = image.NameCardOcr(nameReq);
cout<<ret<<endl;
//单个或多个图片file
map<string, string> nameImages;
nameImages["r.jpg"] = FileUtil::getFileContent("r.jpg");
nameImages["name2.jpg"] = FileUtil::getFileContent("name2.jpg");
NameCardOcrReq nameReq2(BUCKET, nameImages, 0);
ret = image.NameCardOcr(nameReq2);
cout<<ret<<endl;
```
### 人脸识别
人脸识别包括：人脸检测、五官定位、个体信息管理、人脸验证、人脸对比及人脸检索。
#### 人脸检测
```
//单个图片Url, mode:1为检测最大的人脸 , 0为检测所有人脸
FaceDetectReq faceDetectReq(BUCKET);
faceDetectReq.SetMode(0);
faceDetectReq.SetUrl("http://burningtest-10006599.cosgz.myqcloud.com/laobao.jpg");
ret = image.FaceDetect(faceDetectReq);
cout<<ret<<endl; 
//单个图片file
faceDetectReq.SetImage("zhao2.jpg");
ret = image.FaceDetect(faceDetectReq);
cout<<ret<<endl; 
```
#### 五官定位
```
//单个图片Url,检测最大的人脸
FaceShapeReq faceShapeReq(BUCKET);
faceShapeReq.SetMode(0);
faceShapeReq.SetUrl("http://burningtest-10006599.cosgz.myqcloud.com/laobao.jpg");
ret = image.FaceShape(faceShapeReq);
cout<<ret<<endl; 
//单个图片file
faceShapeReq.SetImage("zhao2.jpg");
ret = image.FaceShape(faceShapeReq);
cout<<ret<<endl; 
```
#### 个体信息管理
```
//创建一个Person，并将Person放置到group_ids指定的组当中, 使用图片url
FaceNewPersonReq newPersonReq(BUCKET);
newPersonReq.SetUrl("http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png");
newPersonReq.SetPersonId("person2222");
newPersonReq.AddGroupId("group2222");
ret = image.FaceNewPerson(newPersonReq);
cout<<ret<<endl; 
//单个图片file
newPersonReq.SetPersonId("person3333");
newPersonReq.SetImage("zhao2.jpg");
ret = image.FaceNewPerson(newPersonReq);
cout<<ret<<endl; 
//增加人脸,将单个或者多个Face的url加入到一个Person中.
FaceAddFaceReq addFaceReq(BUCKET);
addFaceReq.AddUrl("http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg");
addFaceReq.AddUrl("http://n.sinaimg.cn/fashion/transform/20160704/flgG-fxtspsa6612705.jpg");
addFaceReq.SetPersonId("person2222");
ret = image.FaceAddFace(addFaceReq);
cout<<ret<<endl; 
//增加人脸,将单个或者多个Face的file加入到一个Person中
addFaceReq.AddImage("zhao1.jpg");
addFaceReq.AddImage("zhao2.jpg");
addFaceReq1.SetPersonId("person2222");
ret = image.FaceAddFace(addFaceReq);
cout<<ret<<endl; 
//删除人脸
FaceDelFaceReq delFaceReq(BUCKET);
delFaceReq.SetPersonId("person2222");
delFaceReq.AddFaceId("1831408218312574949");
delFaceReq.AddFaceId("1831408248150847230");
ret = image.FaceDelFace(delFaceReq);
cout<<ret<<endl; 
//设置信息
FaceSetInfoReq setInfoReq(BUCKET);
setInfoReq.SetPersonId("person2222");
setInfoReq.SetPersonName("ying");
ret = image.FaceSetInfo(setInfoReq);
cout<<ret<<endl;
//获取信息
FaceGetInfoReq getInfoReq(BUCKET);
getInfoReq.SetPersonId("person2222");
ret = image.FaceGetInfo(getInfoReq);
cout<<ret<<endl;
//获取组列表
FaceGetGroupIdsReq getGroupIdReq(BUCKET);
ret = image.FaceGetGroupIds(getGroupIdReq);
cout<<ret<<endl;
//获取人列表
FaceGetPersonIdsReq getPersonIdReq(BUCKET);
getPersonIdReq.SetGroupId("group2222");
ret = image.FaceGetPersonIds(getPersonIdReq);
cout<<ret<<endl;
//获取人脸列表
FaceGetFaceIdsReq getFaceIdReq(BUCKET);
getFaceIdReq.SetPersonId("person2222");
ret = image.FaceGetFaceIds(getFaceIdReq);
cout<<ret<<endl;
//获取人脸信息
FaceGetFaceInfoReq getFaceInfoReq(BUCKET);
getFaceInfoReq.SetFaceId("1704147773393235686");
ret = image.FaceGetFaceInfo(getFaceInfoReq);
cout<<ret<<endl;
//删除个人
FaceDelPersonReq delPersonReq(BUCKET);
delPersonReq.SetPersonId("person2222");
ret = image.FaceDelPerson(delPersonReq);
cout<<ret<<endl;
```
#### 人脸验证
给定一个 Face 和一个 Person ，返回是否是同一个人的判断以及置信度：
```
//单个图片Url
FaceVerifyReq faceVerifyReq(BUCKET);
faceVerifyReq.SetUrl("http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png");
faceVerifyReq.SetPersonId("person1");
ret = image.FaceVerify(faceVerifyReq);
cout<<ret<<endl; 
//单个图片file
faceVerifyReq.SetImage("yang3.jpg");
ret = image.FaceVerify(faceVerifyReq);
cout<<ret<<endl;  
```
#### 人脸对比
```
//两个对比图片的文件url
FaceCompareReq fcReq(BUCKET);
fcReq.AddUrl("http://burningtest-10006599.cosgz.myqcloud.com/laobao.jpg");
fcReq.AddUrl("http://burningtest-10006599.cosgz.myqcloud.com/laobao.jpg");
ret = image.FaceCompare(fcReq);
cout<<ret<<endl; 
//两个对比图片的文件file
fcReq.AddImage("zhao1.jpg");
fcReq.AddImage("zhao2.jpg");
ret = image.FaceCompare(fcReq);
cout<<ret<<endl;  
```
#### 人脸检索
对一张待识别的人脸图片，在一个或多个 group 中识别出最相似的 Top5 person 作为其身份返回，返回的 Top5 中按照相似度从大到小排列。
```
//单个图片Url
FaceIdentifyReq identifyReq(BUCKET);
identifyReq.SetUrl("http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png");
identifyReq.SetGroupId("group2222");
ret = image.FaceIdentify(identifyReq);
cout<<ret<<endl; 
//单个图片file
identifyReq.SetImage("yang3.jpg");
ret = image.FaceIdentify(identifyReq);
cout<<ret<<endl;  
```
### 人脸核身

#### 身份证识别对比

```
FaceIdCardCompareReq idCompareReq(BUCKET);
idCompareReq.SetUrl("http://docs.ebdoor.com/Image/CompanyCertificate/1/16844.jpg");
idCompareReq.SetIdCardNumber("330782198802084329");
idCompareReq.SetIdCardName("季锦锦");
ret = image.FaceIdCardCompare(idCompareReq);
idCompareReq.SetImage("idcard.jpg");
ret = image.FaceIdCardCompare(idCompareReq);
cout<<ret<<endl; 
```

#### 活体检测 - 获取唇语验证码
```
FaceLiveGetFourReq getFourReq(BUCKET);
ret = image.FaceLiveGetFour(getFourReq);
cout<<ret<<endl; 
string validate = "";
Json::Value obj = StringUtil::StringToJson(ret);
```
#### 活体检测 - 视频与用户照片的比对

```
FaceLiveDetectFourReq detectFourReq(BUCKET);
detectFourReq.SetValidateData(validate);
detectFourReq.SetVideo("ZOE_0171.mp4");
ret = image.FaceLiveDetectFour(detectFourReq);
cout<<ret<<endl; 
```
#### 活体检测 - 视频身份信息核验
```
FaceIdCardLiveDetectFourReq iddetectFourReq(BUCKET);
iddetectFourReq.SetValidateData(validate);
iddetectFourReq.SetVideo("ZOE_0171.mp4");
iddetectFourReq.SetIdCardName("季锦锦");
iddetectFourReq.SetIdCardNumber("330782198802084329");
ret = image.FaceIdCardLiveDetectFour(iddetectFourReq);
cout<<ret<<endl; 
return 0;
```
