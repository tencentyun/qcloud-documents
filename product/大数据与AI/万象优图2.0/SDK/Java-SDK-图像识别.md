## 开发准备
### SDK获取
万象优图的 java SDK 下载地址：[image-java-sdk-v2.0](https://github.com/tencentyun/image-java-sdk-v2.0)。

## 快速入门
### 在腾讯云申请业务的授权
开发者使用前，需要先进行 [腾讯云账号注册](https://cloud.tencent.com/register)（详细指引请参考 [注册腾讯云](https://cloud.tencent.com/document/product/378/9603)），并 [创建存储桶](https://cloud.tencent.com/document/product/460/10637)，从而获得 APPID 、SecretId 和 SecretKey 等（获取 APPID 可参考 [域名管理](https://cloud.tencent.com/document/product/460/6937)）。
### 创建对应操作类的对象
如果要使用图片，需要创建图片操作类对象
```
ImageClient imageClient = new ImageClient(APP_ID, SECRET_ID, SECRET_KEY);
String bucketName = BUCKET;
```

### 调用对应的方法
在创建完对象后，根据实际需求，调用对应的操作方法就可以了。sdk 提供的方法包括：图片识别、人脸识别及人脸核身等。
### 图片识别
图片识别包括：图片鉴黄、图片标签、OCR - 身份证识别及 OCR - 名片识别。
####  图片鉴黄
```
// 1. url方式
String[] pornUrlList = new String[3];
pornUrlList[0] = "http://hearthstone.nos.netease.com/1/artworkGvG/GoblinBlastmagel.jpg";
pornUrlList[1] = "http://hearthstone.nos.netease.com/1/artworknaxx/Faerlinal.jpg";
pornUrlList[2] = "http://hearthstone.nos.netease.com/1/artworknaxx/KelThuzadl.jpg";
PornDetectRequest pornReq = new PornDetectRequest(bucketName, pornUrlList);
ret = imageClient.pornDetect(pornReq);
System.out.println("porn detect ret:" + ret);
//2. 图片内容方式
String[] pornNameList = new String[3];
String[] pornImageList = new String[3];
    try {
        pornNameList[0] = "test.jpg";
        pornImageList[0] = CommonFileUtils.getFileContent("F:\pic\test.jpg");
        pornNameList[1] = "hot1.jpg";
        pornImageList[1] = CommonFileUtils.getFileContent("F:\pic\hot1.jpg");
        pornNameList[2] = "hot2.jpg";
        pornImageList[2] = CommonFileUtils.getFileContent("F:\pic\hot2.jpg");
         } 
      catch (Exception ex) {
        Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
         }
pornReq = new PornDetectRequest(bucketName, pornNameList, pornImageList);
ret = imageClient.pornDetect(pornReq);
System.out.println("porn detect ret:" + ret);
```
#### 图片标签

```
// 1. url方式
String tagUrl = "http://hearthstone.nos.netease.com/1/artworkGvG/GoblinBlastmagel.jpg";
TagDetectRequest tagReq = new TagDetectRequest(bucketName, tagUrl);
ret = imageClient.tagDetect(tagReq);
System.out.println("tag detect ret:" + ret);
// 2. 图片内容方式
byte[] tagImage = {0};
try {
     tagImage = CommonFileUtils.getFileContentByte("F:\pic\test.jpg");
    } catch (Exception ex) {
    Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
tagReq = new TagDetectRequest(bucketName, tagImage);
ret = imageClient.tagDetect(tagReq);
System.out.println("tag detect ret:" + ret);
```
#### OCR - 身份证识别
```
// 1. url方式,识别身份证正面
String[] idcardUrlList = new String[2];
idcardUrlList[0] = "http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg";
idcardUrlList[1] = "http://img5.iqilu.com/c/u/2013/0530/1369896921237.jpg";
IdcardDetectRequest idReq = new IdcardDetectRequest(bucketName, idcardUrlList, 0); 
ret = imageClient.idcardDetect(idReq);
System.out.println("idcard detect ret:" + ret);
//识别身份证反面
idcardUrlList[0] = "http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg";
idcardUrlList[1] = "http://www.4009951551.com/upload/image/20151026/1445831136187479.png";
idReq = new IdcardDetectRequest(bucketName, idcardUrlList, 1);   
ret = imageClient.idcardDetect(idReq);
System.out.println("idcard detect ret:" + ret);
//2. 图片内容方式,识别身份证正面
String[] idcardNameList = new String[2];
String[] idcardImageList = new String[2];
try {
    idcardNameList[0] = "id6_zheng.jpg";
    idcardImageList[0] = CommonFileUtils.getFileContent("F:\pic\id6_zheng.jpg");
    idcardNameList[1] = "id2_zheng.jpg";
    idcardImageList[1] = CommonFileUtils.getFileContent("F:\pic\id2_zheng.jpg");
    } catch (Exception ex) {
   Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
idReq = new IdcardDetectRequest(bucketName, idcardNameList, idcardImageList, 0);
ret = imageClient.idcardDetect(idReq);
System.out.println("idcard detect ret:" + ret);
//识别身份证反面
try {
    idcardNameList[0] = "id5_fan.png";
    idcardImageList[0] = CommonFileUtils.getFileContent("F:\pic\id5_fan.jpg");
    idcardNameList[1] = "id7_fan.jpg";
    idcardImageList[1] = CommonFileUtils.getFileContent("F:\pic\id7_fan.png");
    } catch (Exception ex) {
   Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
idReq = new IdcardDetectRequest(bucketName, idcardNameList, idcardImageList, 1);
ret = imageClient.idcardDetect(idReq);
System.out.println("idcard detect ret:" + ret);
Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
idReq = new IdcardDetectRequest(bucketName, idcardNameList, idcardImageList, 1);
ret = imageClient.idcardDetect(idReq);
System.out.println("idcard detect ret:" + ret);
```
#### OCR - 名片识别
```
// 1. url方式
String[] namecardUrlList = new String[2];
namecardUrlList[0] = "http://pic1.nipic.com/2008-12-03/2008123181119306_2.jpg";
namecardUrlList[1] = "http://pic.58pic.com/58pic/12/49/04/80k58PICzYP.jpg";
NamecardDetectRequest nameReq = new NamecardDetectRequest(bucketName, namecardUrlList, 0);
ret = imageClient.namecardDetect(nameReq);
System.out.println("namecard detect ret:" + ret);
//2. 图片内容方式
String[] namecardNameList = new String[2];
String[] namecardImageList = new String[2];
try {
    namecardNameList[0] = "name2.jpg";
    namecardImageList[0] = CommonFileUtils.getFileContent("F:\pic\name2.jpg");
    namecardNameList[1] = "名片.jpg";
    namecardImageList[1] = CommonFileUtils.getFileContent("F:\pic\名片.jpg");
    } catch (Exception ex) {
     Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
nameReq = new NamecardDetectRequest(bucketName, namecardNameList, namecardImageList, 0);
ret = imageClient.namecardDetect(nameReq);
System.out.println("namecard detect ret:" + ret);;
```
### 人脸识别
人脸识别包括：人脸检测、五官定位、个体信息管理、人脸验证、人脸检索及人脸对比。
#### 人脸检测
```
// 1. url方式
String faceDetectUrl = "http://ent.cctv.com/20071217/images/1197849230623_8325711678927688064.jpg";
FaceDetectRequest faceDetectReq = new FaceDetectRequest(bucketName, faceDetectUrl, 1);
ret = imageClient.faceDetect(faceDetectReq);
System.out.println("face detect ret:" + ret);
//2. 图片内容方式
String faceDetectName  = "";
String faceDetectImage = "";
try {
     faceDetectName = "face1.jpg";
     faceDetectImage = CommonFileUtils.getFileContent("F:\pic\face1.jpg");
   } catch (Exception ex) {
     Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
faceDetectReq = new FaceDetectRequest(bucketName, faceDetectName, faceDetectImage, 1);
ret = imageClient.faceDetect(faceDetectReq);
System.out.println("face detect ret:" + ret);
```
#### 五官定位
```
// 1. url方式
String faceShapeUrl = "http://ent.cctv.com/20071217/images/1197849230623_8325711678927688064.jpg";
FaceShapeRequest faceShapeReq = new FaceShapeRequest(bucketName, faceShapeUrl, 1);
ret = imageClient.faceShape(faceShapeReq);
System.out.println("face shape ret:" + ret);
//2. 图片内容方式
String faceShapeName  = "";
String faceShapeImage = "";
try {
    faceShapeName = "face1.jpg";
    faceShapeImage = CommonFileUtils.getFileContent("F:\pic\face1.jpg");
    } catch (Exception ex) {
    Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
faceShapeReq = new FaceShapeRequest(bucketName, faceShapeName, faceShapeImage, 1);
ret = imageClient.faceShape(faceShapeReq);
System.out.println("face shape ret:" + ret);   
```
#### 个体信息管理
```
 //个体创建,创建一个Person，并将Person放置到group_ids指定的组当中，不存在的group_id会自动创建。
 // 1. url方式
String personNewUrl = "http://imgsrc.baidu.com/baike/pic/item/5fdf8db1cb134954a4d833a0534e9258d0094a34.jpg";
String[] groupIds = new String[2];
groupIds[0] = "group3";
groupIds[1] = "group22";
String personName = "yangmi";
String personId = "personY";
String personTag = "star";
FaceNewPersonRequest personNewReq = new FaceNewPersonRequest(bucketName, personId, groupIds, personNewUrl, personName, personTag);
ret = imageClient.faceNewPerson(personNewReq);
System.out.println("person new  ret:" + ret);
//2. 图片内容方式
String personNewName  = "";
String personNewImage = "";
groupIds[0] = "group11";
groupIds[1] = "group33";
personName = "yangmi";
personId = "persony";
personTag = "star";
    try {
        personNewName = "yang.jpg";
        personNewImage = CommonFileUtils.getFileContent("F:\pic\yang.jpg");
    } catch (Exception ex) {
Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
personNewReq = new FaceNewPersonRequest(bucketName, personId, groupIds, personNewName, personNewImage, personName, personTag);
ret = imageClient.faceNewPerson(personNewReq);
System.out.println("person new ret:" + ret); 
//增加人脸,将一组Face加入到一个Person中。注意，一个Face只能被加入到一个Person中。 
// 1. url方式;
String[] addFaceUrlList = new String[2];
addFaceUrlList[0] = "http://img.huainanren.wang/2016/1030/20161030044908523.jpg";
addFaceUrlList[1] = "http://p.ishowx.com/uploads/allimg/161024/648-161024110505.jpg";
String addfacePersonId = "personY";
String addfacePersonTag = "star1";
FaceAddFaceRequest addFaceReq = new FaceAddFaceRequest(bucketName, addFaceUrlList, addfacePersonId, addfacePersonTag); 
ret = imageClient.faceAddFace(addFaceReq);
System.out.println("add face ret:" + ret);
//2. 图片内容方式;
String[] addFaceNameList = new String[2];
String[] addFaceImageList = new String[2];
addfacePersonId = "personY";
addfacePersonTag = "actor";
    try {
        addFaceNameList[0] = "yang2.jpg";
        addFaceImageList[0] = CommonFileUtils.getFileContent("F:\pic\yang2.jpg");
  addFaceNameList[1] = "yang3.jpg";
        addFaceImageList[1] = CommonFileUtils.getFileContent("F:\pic\yang3.jpg");
    } catch (Exception ex) {
        Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
addFaceReq = new FaceAddFaceRequest(bucketName, addFaceNameList, addFaceImageList, addfacePersonId, addfacePersonTag);
ret = imageClient.faceAddFace(addFaceReq);
System.out.println("add face ret:" + ret);
// 删除人脸,删除一个person下的face
String delFacePersonId = "personY";
String[] delFaceIds = new String[2];
delFaceIds[0] = "1831408218312574949";
delFaceIds[1] = "1831408248150847230";
FaceDelFaceRequest delFaceReq = new FaceDelFaceRequest(bucketName, delFacePersonId, delFaceIds);
ret = imageClient.faceDelFace(delFaceReq);
System.out.println("face del  ret:" + ret);
//设置信息
String setInfoPersonId = "personY";
String setInfoPersonName = "mimi";
String setInfoTag = "actress";
FaceSetInfoRequest setInfoReq = new FaceSetInfoRequest(bucketName, setInfoPersonId, setInfoPersonName, setInfoTag);
ret = imageClient.faceSetInfo(setInfoReq);
System.out.println("face set info  ret:" + ret);
//获取信息
String getInfoPersonId = "personY";
FaceGetInfoRequest getInfoReq = new FaceGetInfoRequest(bucketName, getInfoPersonId);
ret = imageClient.faceGetInfo(getInfoReq);
System.out.println("face get info  ret:" + ret);
//获取组列表
FaceGetGroupIdsRequest getGroupReq = new FaceGetGroupIdsRequest(bucketName);
ret = imageClient.faceGetGroupIds(getGroupReq);
System.out.println("face get group ids  ret:" + ret);
//获取人列表
String getPersonGroupId = "group1";
FaceGetPersonIdsRequest getPersonIdsReq = new FaceGetPersonIdsRequest(bucketName, getPersonGroupId);
ret = imageClient.faceGetPersonIds(getPersonIdsReq);
System.out.println("face get person ids  ret:" + ret);
//获取人脸列表
String getFacePersonId = "personY";
FaceGetFaceIdsRequest getFaceIdsReq = new FaceGetFaceIdsRequest(bucketName, getFacePersonId);
ret = imageClient.faceGetFaceIds(getFaceIdsReq);
System.out.println("face get face ids  ret:" + ret);
//获取人脸信息
String getFaceId = "1830582165978517027";
FaceGetFaceInfoRequest getFaceInfoReq = new FaceGetFaceInfoRequest(bucketName, getFaceId);  
ret = imageClient.faceGetFaceInfo(getFaceInfoReq);
System.out.println("face get face info  ret:" + ret);
//删除个人
String delPersonId = "personY";
FaceDelPersonRequest delPersonReq = new FaceDelPersonRequest(bucketName, personId);
ret = imageClient.faceDelPerson(delPersonReq);
System.out.println("face del  person ret:" + ret);
```
#### 人脸验证
给定一个 Face 和一个 Person ，返回是否是同一个人的判断以及置信度
```
// 1. url方式
String  faceVerifyPersonId = "person1";
String faceVerifyUrl = "http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png";
FaceVerifyRequest faceVerifyReq = new FaceVerifyRequest(bucketName, faceVerifyPersonId, faceVerifyUrl);
ret = imageClient.faceVerify(faceVerifyReq);
System.out.println("face verify ret:" + ret);
//2. 图片内容方式
String faceVerifyName  = "";
String faceVerifyImage = "";
faceVerifyPersonId = "person3111";
try {
    faceVerifyName = "yang3.jpg";
    faceVerifyImage = CommonFileUtils.getFileContent("F:\pic\yang3.jpg");
    } catch (Exception ex) {
    Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
faceVerifyReq = new FaceVerifyRequest(bucketName, faceVerifyPersonId, faceVerifyName, faceVerifyImage);
ret = imageClient.faceVerify(faceVerifyReq);
System.out.println("face verify ret:" + ret);
```
#### 人脸检索
对于一个待识别的人脸图片，在一个 Group 中识别出最相似的 Top5 Person 作为其身份返回，返回的 Top5 中按照相似度从大到小排列。
```
String  faceIdentifyGroupId = "group1";
String faceIdentifyUrl = "http://www.5djiaren.com/uploads/2016-07/22-141354_227.jpg";
FaceIdentifyRequest faceIdentifyReq = new FaceIdentifyRequest(bucketName, faceIdentifyGroupId, faceIdentifyUrl);
ret = imageClient.faceIdentify(faceIdentifyReq);
System.out.println("face identify ret:" + ret);
//2. 图片内容方式
String faceIdentifyName  = "";
String faceIdentifyImage = "";
try {
     faceIdentifyName = "yang4.jpg";
     faceIdentifyImage = CommonFileUtils.getFileContent("F:\pic\yang4.jpg");
    } catch (Exception ex) {
        Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
faceIdentifyReq = new FaceIdentifyRequest(bucketName, faceIdentifyGroupId, faceIdentifyName, faceIdentifyImage);
ret = imageClient.faceIdentify(faceIdentifyReq);
System.out.println("face identify ret:" + ret);
```
#### 人脸对比
```
// 1. url方式
String urlA = "http://imgsrc.baidu.com/baike/pic/item/5fdf8db1cb134954a4d833a0534e9258d0094a34.jpg";
String urlB = "http://a-ssl.duitang.com/uploads/item/201610/29/20161029215753_5cMTX.jpeg";
FaceCompareRequest faceCompareReq = new FaceCompareRequest(bucketName, urlA, urlB);
ret = imageClient.faceCompare(faceCompareReq);
System.out.println("face compare ret:" + ret);
//2. 图片内容方式
String[] compareNameList = new String[2]; 
String[] compareImageList = new String[2];
try {
     compareNameList[0] = "zhao1.jpg";
     compareNameList[1] = "zhao2.jpg";
     compareImageList[0] = CommonFileUtils.getFileContent("F:\pic\zhao1.jpg");
     compareImageList[1] = CommonFileUtils.getFileContent("F:\pic\zhao2.jpg");
    } catch (Exception ex) {
   Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
    }
faceCompareReq = new FaceCompareRequest(bucketName, compareNameList, compareImageList);
ret = imageClient.faceCompare(faceCompareReq);
System.out.println("face compare ret:" + ret);
```
### 人脸核身
人脸核身包括用户上传照片与真实身份信息比对以及活体检测中的获取唇语验证码、视频身份信息核验以及视频与用户照片的比对。
#### 用户上传照片与真实身份信息比对

```java
	// 1. url方式
	String  idcardNumber = "330782198802084329";
	String  idcardName = "季锦锦";       
	String idcardCompareUrl = "http://docs.ebdoor.com/Image/CompanyCertificate/1/16844.jpg";
	FaceIdCardCompareRequest idCardCompareReq = new FaceIdCardCompareRequest(bucketName, idcardNumber, idcardName, idcardCompareUrl);

	ret = imageClient.faceIdCardCompare(idCardCompareReq);
	System.out.println("face idCard Compare ret:" + ret);
	
	 //2. 图片内容方式
	String idcardCompareName  = "";
	String idcardCompareImage = "";
	try {
		idcardCompareName = "idcard.jpg";
		idcardCompareImage = CommonFileUtils.getFileContent("F:\\pic\\idcard.jpg");
	} catch (Exception ex) {
		Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
	}
	
	idCardCompareReq = new FaceIdCardCompareRequest(bucketName, idcardNumber, idcardName, idcardCompareName, idcardCompareImage);
	ret = imageClient.faceIdCardCompare(idCardCompareReq);
	System.out.println("face idCard Compare ret:" + ret);
```

#### 活体检测 - 获取唇语验证码	

```java
	String seq = "";
	FaceLiveGetFourRequest getFaceFourReq = new FaceLiveGetFourRequest(bucketName, seq);        
	ret = imageClient.faceLiveGetFour(getFaceFourReq);
	System.out.println("face live get four  ret:" + ret);
	
	String validate = "";
	JSONObject jsonObject = new JSONObject(ret);
	JSONObject data = jsonObject.getJSONObject("data");
	if (null != data) {
		validate = data.getString("validate_data");
	}
```
	
#### 活体检测 - 视频身份信息核验

```java  
	//
	String  liveDetectIdcardNumber = "330782198802084329";
	String  liveDetectIdcardName = "季锦锦";  
	String  video = "";
	try {
		video = CommonFileUtils.getFileContent("F:\\pic\\ZOE_0171.mp4");
	} catch (Exception ex) {
		Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
	}
	
	FaceIdCardLiveDetectFourRequest liveDetectReq = new FaceIdCardLiveDetectFourRequest(bucketName, validate, video, liveDetectIdcardNumber, liveDetectIdcardName, seq);
	ret = imageClient.faceIdCardLiveDetectFour(liveDetectReq);
	System.out.println("face idCard live detect four ret:" + ret);
```

#### 活体检测 - 视频与用户照片的比对

```java  
	String  liveDetectVideo = "";
	String  liveDetectImage = "";
	String liveDetectVvalidate = "123456";        
	boolean compareFlag  = true;
	try {
		liveDetectVideo = CommonFileUtils.getFileContent("F:\\pic\\ZOE_0171.mp4");
		liveDetectImage = CommonFileUtils.getFileContent("F:\\pic\\zhao2.jpg");
	} catch (Exception ex) {
		Logger.getLogger(Demo.class.getName()).log(Level.SEVERE, null, ex);
	}
	
	FaceLiveDetectFourRequest faceLiveDetectReq = new FaceLiveDetectFourRequest(bucketName, validate, compareFlag, video, liveDetectImage, seq);
	ret = imageClient.faceLiveDetectFour(faceLiveDetectReq);
	System.out.println("face  live detect four ret:" + ret);
	
	// 关闭释放资源
	imageClient.shutdown();
	System.out.println("shutdown!");
```
