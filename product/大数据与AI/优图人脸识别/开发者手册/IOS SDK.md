## 前期准备
>	下载 腾讯云•优图人脸识别 [iOS SDK](http://imgcache.qq.com/qcloud/tianyan/sdk/QCloudFR_iOS_SDK1.0.zip)。
SDK支持iOS 5.0及以上版本的手机系统；
手机必须要有网络（GPRS、3G或Wifi网络等）；
在[腾讯云密钥管理页面](https://console.cloud.tencent.com/capi/project)，为您的项目申请安全密钥

## 导入SDK
1.iOS SDK下载地址为：[iOS SDK](http://imgcache.qq.com/qcloud/tianyan/sdk/QCloudFR_iOS_SDK1.0.zip)。

2.将下载下来的TXqCloudFrSdk.framework添加到工程中
3.在工程General->Embedded Binaries 中添加导入的TXqCloudFrSdk.framework
4.如果需要适配iOS 9，请在工程的Info.plist中添加以下key，添加方法可以用Source Code的方式打开Info.plist，添加以下配置：
```
<key>NSAppTransportSecurity</key>
    <dict>
        <key>NSAllowsArbitraryLoads</key>
        <true/>
    </dict>
```

## API详细说明
### 概念解释
|标识符|解释|
|---------|---------|---------|
|id|接入人脸识别服务时,生成的唯一id, 用于唯一标识接入业务|
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
### 初始化
>申请项目密钥，并请求您的业务服务器生成签名，详见[鉴权签名文档](http://imgcache.qq.com/qcloud/tianyan/wiki/Authorization.pdf)

>导入优图人脸识别的SDK相关framework包后，通过以下方法对优图sdk进行初始化：
TXQcloudFrSDK *sdk = [[TXQcloudFrSDK alloc] initWithName:APP_IDDauthorization: AUTHORIZATION];

### SDK方法的调用
>SDK方法的调用通用格式如下，调用每个方法时传入一个成功后执行的block，处理后台返回的Json数据；传入一个失败后的block来处理请求失败的情况。以delPerson方法为例：
```
[sdk delPerson:@"personId" successBlock:^(id responseObject) { 
		//SDK方法调用成功，得到返回的json NSDictionary
		NSDictionary *jsonResult = responseObject;
		//处理后台返回的Json数据
	} failureBlock:^(NSError *error) {
		//SDK方法调用失败;
	}];
```
### 人脸检测与分析
检测给定图片中的所有人脸(Face)的位置和相应的面部属性。位置包括人脸在图片的坐标宽高信息(x, y, w, h)，面部属性包括性别(gender), 年龄(age), 表情(expression), 眼镜(glass)和姿态(pitch，roll，yaw).单次请求的图片大小限制在2M以下。
```
/*!
 * 
 *
 * @param image 人脸图片 
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block 
 */
- (void)detectFace:(UIImage *)image 
successBlock:(HttpRequestSuccessBlock)successBlock 		failureBlock:(HttpRequestFailBlock)failureBlock;
```
### 人脸对比
给定两张人脸照片，计算两个人脸Face的相似性以及五官相似度。
```
/*!
 *  
 *
 * @param imageA  第一张人脸图片
 * @param imageB  第二张人脸图片
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block 
 */
- (void)faceCompare:(UIImage *)imageA imageB:(UIImage *)imageB
	successBlock:(HttpRequestSuccessBlock)successBlock 		failureBlock:(HttpRequestFailBlock)failureBlock;
```

### 人脸验证
给定一张人脸照片和一个已有的Person个体ID，判断照片是否和给定的Person相同并给出该次判断的可置信度。
```
/*!
 *  
 *
 * @param image 需要验证的人脸图片
 * @param personId 验证的目标person
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block 
 */
- (void)faceVerify:(UIImage *)image personId:(NSString *)personId 
successBlock:(HttpRequestSuccessBlock)successBlock 		failureBlock:(HttpRequestFailBlock)failureBlock;
```

### 人脸识别
给定一张待识别的人脸图片和一个已有的Group，在该Group中的所有Person个体中，识别出最相似的Top5 Person作为其身份返回，返回的Top5中按照相似度从大到小排列。
```
/*!
 *  
 *
 * @param image 需要识别的人脸图片
 * @param groupId 人脸face组
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)faceIdentify:(UIImage *)image groupId:(NSString *)groupId successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```

### 个体(Person)管理
### #个体Person创建
用给定的人脸照片和person id来创建一个Person，并将该Person加入到group_ids指定的组当中，一个person可以被加到多个Group组中
```
/*!
 *  
 *
 * @param image 需要新建的人脸图片
 * @param personId 指定创建的人脸ID
 * @param groupIds 加入的group列表(NSString* 数组)
 * @param personName 名字,可选
 * @param personTag  备注,可选
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)newPerson:(UIImage *)image personId:(NSString *)personId groupIds:(NSArray *)groupIds personName:(NSString*) personName personTag:(NSString *) personTag successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```

### #个体Person删除
根据指定的person id删除已有的Person
```
/*!
 *   
 * @param personId 要删除的person ID
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)delPerson:(NSString *)personId successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```

### #增加人脸
给指定Person中增加人脸图片Face。注意，一个人脸Face只能被加入到一个Person中，一个Person最多允许包含100个人脸Face。
```
/*!
 *  
 *  
 *
 * @param personId 人脸Face的person id
 * @param imageArray 人脸图片UIImage列表
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)addFace:(NSString *)personId imageArray:(NSArray *)imageArray successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```

### #人脸删除
删除给定person id下的face列表，包括删除其特征、属性和face_id信息。
```
/*!
 *  
 *
 * @param personId 待删除人脸的person ID
 * @param faceIdArray 删除人脸id的列表
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)delFace:(NSString *)personId faceIdArray:(NSArray *)faceIdArray successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```

### #设置个体(Person)信息
设置Person的name
```
/*!
 *  
 *
 * @param personName 新的name
 * @param personId 要设置的person id
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)setInfo:(NSString *)personName personId:(NSString *)personId successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```
### #获取个体(Person)信息
获取一个Person的信息, 包括其name, id, tag, 相关的face, 以及groups等信息
```
/*!
 *  
 *
 * @param personId 待查询个体的ID
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)getInfo:(NSString *)personId successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```

### 信息查询
### #获取组列表
获取已有的全部group列表信息
```
/*!
 *  
 *
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)getGroupIdsWithsuccessBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;

```
### #获取个体(Person)列表
获取指定的Group中所有person信息列表
```
/*!
 *  
 *
 * @param groupId 待查询的组id
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)getPersonIds:(NSString *)groupId successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```
### #获取人脸列表
获取给定的person id中所有face id列表信息
```
/*!
 *  
 *
 * @param personId 待查询的个体id
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)getFaceIds:(NSString *)personId successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```
### #获取人脸信息
获取给定的face id的相关特征信息
```
/*!
 *  
 *
 * @param faceId 带查询的人脸ID
 * @param successBlock 方法调用成功后处理的block
 * @param failureBlock 方法调用失败后处理的block
 */
- (void)getFaceInfo:(NSString *)face_id successBlock:(HttpRequestSuccessBlock)successBlock failureBlock:(HttpRequestFailBlock)failureBlock;
```