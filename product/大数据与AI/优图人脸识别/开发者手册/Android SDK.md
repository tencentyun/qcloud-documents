## 前期准备
>下载 腾讯云•优图人脸识别 [Android SDK](http://imgcache.qq.com/qcloud/tianyan/QCloudFR_ANDROID_SDK1.0.zip)。
>	SDK支持Android 2.2及以上版本的手机系统；
	手机必须要有网络（GPRS、3G或Wifi网络等）；
	在[腾讯云密钥管理页面](https://console.cloud.tencent.com/capi/project)，为您的项目申请安全密钥

## 导入SDK
>将下载的SDK libs下的youtu_sdk_android.jar拷贝到项目的libs下，并导入该包到项目中:
 

## 配置android-manifest.xml
SDK需要网络访问和读取SD卡存储空间的权限，配置如下：
```
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
```

## API详细说明

### 概念解释
|标识符|解释|
|---------|---------|---------|
|id |接入人脸识别服务时,生成的唯一id, 用于唯一标识接入业务|
|user_id	|接入业务自行定义的用户id，用于唯一标识一个用户|
|secret_id	|标识api鉴权调用者的密钥身份|
|secret_key	|用于加密签名字符串和服务器端验证签名字符串的密钥，secret_key 必须严格保管避免泄露|
|group_id	|个体(person)以组（group）的形式存储，一个组可以包含多个个体，一个个体也可以存在于多个组。group_id即用来标识group|
|person_id	|人脸以个体（person）的形式存储，一个个体下可以存储多张人脸。person_id即用来标识person|
|face_id	|标识每张人脸的id|

```
• 注意： 
(1)一个app_id下建立的group_id数量限制为5000个。
(2)一个group_id下建立的person_id数量限制为1000个。
(3)一个person_id下建立的人脸数量限制为20个。
(4)每个请求的包体大小限制为2MB。
(5)SDK的发起请求方式为post。
```

## 初始化
>申请安全密钥，并请求您的业务服务器生成签名，详见[鉴权签名文档](http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf)
导入优图人脸识别的SDK相关jar包后，通过以下方法对优图sdk进行初始化：
```
QcloudFrSDK sdk = new QcloudFrSDK (APP_ID, AUTHORIZATION);
```

## 人脸检测与分析
检测给定图片中的所有人脸(Face)的位置和相应的面部属性。位置包括人脸在图片的坐标宽高信息(x, y, w, h)，面部属性包括性别(gender), 年龄(age), 表情(expression), 眼镜(glass)和姿态(pitch，roll，yaw).单次请求的图片大小限制在2M以下。
```
/**
  * 
  * @param image_path 人脸图片的路径(图片大小限制为2M以下)
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject DetectFace(String image_path) throws IOException,
			JSONException;
```
返回JSON结果：
```
{
  "session_id":"xxxx",
  "image_id":"xxxx",
  "image_height":584,
  "image_width":527,
  "face":[
  {
  "face_id":"1001344647426015231",
  "x":145,
  "y":147,
  "height":305.0,
  "width":305.0,
  "pitch":3,
  "roll":0,
  "yaw":0,
  "age":34,
  "gender":99,
  "glass":true,
  "expression":27
}
],
"errorcode":0,
"errormsg":"ok"
}
```



## 人脸对比
给定两张人脸照片，计算两个人脸Face的相似性以及五官相似度。
```
/**
  * @param image_path_a 第一张人脸图片路径
  * @param image_path_b 第二张人脸图片路径(两张图片加起来总大小限制在2M以下)
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException
  */
public JSONObject FaceCompare(String image_path_a, String image_path_b)
			throws IOException, JSONException;
```
返回JSON结果：
```
{
  "session_id":"sessionid",
  "eye_sim":50.5024,
  "mouth_sim":50.5024,
  "nose_sim":50.5024,
  "eyebrow_sim":50.5024,
  "similarity":50.5024,
  "errorcode":0,
  "errormsg":"ok"
}
```
## 人脸验证
给定一张人脸照片和一个已有的Person个体ID，判断照片是否和给定的Person相同并给出该次判断的可置信度。 
```
/**
  * @param image_path 需要验证的人脸图片路径
  * @param person_id 验证的目标person
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject FaceVerify(String image_path, String person_id)
			throws IOException, JSONException;
```
返回JSON结果：
```
{
  "confidence":50.502410888671878,
  "ismatch":false,
  "session_id":"xxxx",
  "errorcode":0,
  "errormsg":"ok"
}
```
##  人脸识别
给定一张待识别的人脸图片和一个已有的Group，在该Group中的所有Person个体中，识别出最相似的Top5 Person作为其身份返回，返回的Top5中按照相似度从大到小排列。
```
/**
  * @param image_path  需要识别的人脸图片路径
  * @param group_id  人脸face组
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject FaceIdentify(String image_path, String group_id)
			throws IOException, JSONException;
```
返回JSON结果：
```
{
  "session_id":"xxx",
  "candidates":[
  {
     "person_id":"person id",
     "face_id":"1105824303454158847",
     "confidence":94.52433,
     "tag":"xxx"
	},...],
  "errorcode":0,
  "errormsg":"OK"
}
```
## 个体(Person)管理
### 个体Person创建
用给定的人脸照片和person id来创建一个Person，并将该Person加入到group_ids指定的组当中，一个person可以被加到多个Group组中
```
/**  
  * @param image_path  需要新建的人脸图片路径
  * @param person_id   指定创建的人脸
  * @param group_ids   加入的group列表
  * @param personName  名字(可选，如果名字为中文要求编码为UTF-8)
  * @param personTag    备注(可选)
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject NewPerson(String image_path, String person_id,
			List<String> group_ids, String personName, String personTag)
			throws IOException, JSONException;
```

返回JSON结果：
```
{
  "person_id":"hello",
  "suc_group":2,
  "suc_face":1,
  "session_id":"",
  "face_id":"1129309554348195839",
  "group_ids":["group1","group2"],
  "errorcode":0,
  "errormsg":"OK"
}
```

###  个体Person删除
根据指定的person id删除已有的Person
```
/** 
  * @param person_id 要删除的person ID
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject DelPerson(String person_id) throws IOException,
			JSONException;
```
返回JSON结果：
```
{
  "deleted":1,
  "session_id":"",
  "person_id":"hello",
  "errorcode":0,
  "errormsg":"OK"
}
```
### 增加人脸
给指定Person中增加人脸图片Face。注意，一个人脸Face只能被加入到一个Person中，一个Person最多允许包含100个人脸Face。
```
/** 
  * @param person_id  待增加人脸Face的person id
  * @param image_path_arr  人脸图片路径列表(图片总大小限制在2M以下)
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject AddFace(String person_id,
List<String> image_path_arr)throws IOException, JSONException；
```
返回JSON结果：
```
{
  "added":1,
  "face_ids":["1129312909786152959"],
  "session_id":"",
  "errorcode":0,
  "errormsg":"OK"
}
```
###  人脸删除
删除给定person id下的face列表，包括删除其特征、属性和face_id信息
```
/** 
  * @param person_id  待删除人脸的person ID
  * @param face_id_arr  删除人脸id的列表
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject DelFace(String person_id, 
			List<String> face_id_arr)throws IOException, JSONException;
```
返回JSON结果： 
```
{
  "deleted":1,
  "session_id":"",
  "face_ids":["1129312909786152959"],
  "errorcode":0,
  "errormsg":"OK"
}
```

### 设置个体(Person)信息
设置Person的name
```
/** 
  * @param person_name  新的name
  * @param person_id  要设置的person id
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
	public JSONObject SetInfo(String person_name, String person_id)
			throws IOException, JSONException;
```
返回JSON结果：
```
{
  "person_id":"person1",
  "session_id":"",
  "errorcode":0,
  "errormsg":"OK"
}
```
### 获取个体(Person)信息
获取一个Person的信息, 包括其name, id, tag, 相关的face, 以及groups等信息
```
/** 
  * @param person_id  待查询个体的ID
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject GetInfo(String person_id) throws IOException,
			JSONException
```
返回JSON结果：
```
{
  "person_id":"person1",
  "person_name":"newName",
  "tag":"",
  "face_ids":["1129752317850091519"],
  "group_ids":["group3"],
  "session_id":"",
  "errorcode":0,
  "errormsg":"OK"
}
```

## 信息查询
### 获取组列表
获取已有的全部group列表信息
```
/** 
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject GetGroupIds() throws IOException, JSONException;
```
返回JSON结果：
```
{
  "group_ids":["group1" ,"group2"],
  "errorcode":0,
  "errormsg":"OK"
}
```
### 获取个体(Person)列表
获取指定的Group中所有person信息列表
```
/** 
  * @param group_id  待查询的组id
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject GetPersonIds(String group_id) throws IOException,
			JSONException;
```
返回JSON结果：
```
{
  "person_ids":[],
  "errorcode":0,
  "errormsg":"OK"
}
```
###  获取人脸列表
获取给定的person id中所有face id列表信息
```
/** 
  * @param person_id  待查询的个体id
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject GetFaceIds(String person_id) throws IOException,
			JSONException
```
返回JSON结果：
```
{
  "face_ids":["1128396234991665151","1128396245327478783"],
  "errorcode":0,
  "errormsg":"OK"
}
```
###  获取人脸信息
获取给定的face id的相关特征信息
```
/** 
  * @param face_id  带查询的人脸ID
  * @return 调用API请求返回的json结果
  * @throws IOException
  * @throws JSONException 
  */
public JSONObject GetFaceInfo(String face_id) throws IOException,
			JSONException;
```
返回JSON结果：
```
{
  "face_info":
  {
    "face_id":"1128396234991665151",
	"x":106,
	"y":83,
	"height":79,
	"width":79,
	"pitch":7,
	"roll":13,
	"yaw":-9,
	"age":27,
	"gender":99,
	"glass":true,
	"expression":0
  },
  "errorcode":0,
  "errormsg":"OK"
}
```