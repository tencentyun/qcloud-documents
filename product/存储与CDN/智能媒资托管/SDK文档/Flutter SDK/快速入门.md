本文介绍smh_flutter_sdk如何快速入门以及api介绍。

## 相关资源
* sdk github 地址：https://github.com/tencentyun/smh_flutter_sdk
* demo github 地址：https://github.com/tencentyun/smh_flutter_example

## 准备工作

1. 您需要一个纯Flutter项目或flutter原生混合项目，这个应用可以是您现有的工程，也可以是您新建的一个空的工程。
2. Flutter 版本要求：
```
  sdk: ">=2.17.6 <3.0.0"
  flutter: ">=3.0.0 <4.0.0"
```

## 第一步：SDK 介绍
smh_flutter_sdk 目前兼容支持iOS、Android。
分为两个版本：
|名称| 功能描述 |
|:-----| :-----|
|完整版本|包含smh全部功能以及灯塔事件上报模块。|
|含灯塔版本|仅含smh全部功能。|

具体可以按照项目需求集成对应版本sdk.

## 第二步：集成 SDK

#### 集成完整版本
```
smh_flutter_sdk:
    git:
      url: https://github.com/tencentyun/smh-flutter-sdk.git
```

#### 集成不含灯塔版本
```
smh_flutter_sdk:
    git:
      url: https://github.com/tencentyun/smh-flutter-sdk.git
      ref: 'slim'
```
## 第三步：开始使用

#### 1. 自定义Accesstoken刷新类
>? sdk内部已经做了accesstoken缓存。业务测需要提供accessToken的刷新机制。

自定义 AccessToken刷新工具类并实现 SMHRefreshAccessTokenHander 接口。
实例代码参考：
```
class CustomRefreshAccessTokenHander extends SMHRefreshAccessTokenHander {
  @override
  Future<SMHAccessTokenEntity>? refreshAccessToken(
      String? spaceId, String? spaceOrgId) async {
    // spaceId 为空时调用 SMHUserSpaceApis.getUserInfoAndAccessToken 接口
    if (spaceId == null) {
      SMHResponse? response;
      try {
        response = await SMHUserSpaceApis.getUserInfoAndAccessToken(
            organizationId: organizationId, // 用户组织id
            userToken: userToken); // 用户UserToken
      } catch (e) {}
      return response?.data;
    } else {
    // spaceId 不为空时调用 SMHUserSpaceApis.getSpaceAccessToken 接口
      SMHResponse? response;
      try {
        response = await SMHUserSpaceApis.getSpaceAccessToken(
            organizationId:organizationId, // 用户组织id
            userToken: userToken, // 用户UserToken
            spaceId: spaceId, // 用户空间id
            spaceOrgId: spaceOrgId); // 当前空间 所属组织id。可选
      } catch (e) {}
      return response?.data;
    }
  }
}

```

#### 2. 初始化SDK

```
  // 注意 请在 WidgetsFlutterBinding.ensureInitialized(); 后进行初始化

  // 注册SMHUserService
  SMHServicesManager().registerService(SMHUserService());
  // 实例化SMHAPIService并设置accesstoken 刷新Handler 
  // CustomRefreshAccessTokenHander 为
  SMHAPIService apiService = SMHAPIService()
    ..setAccessTokenRefreshHandle(CustomRefreshAccessTokenHander());
  // 注册SMHAPIService
  SMHServicesManager().registerService(apiService);
  // 配置开发域名
  SMHServicesManager()
      .configHostWithEnv("https://devhost/", SMHHostType.dev);
  // 配置测试域名
  SMHServicesManager()
      .configHostWithEnv("https://testhost/", SMHHostType.test);
  // 配置预发布域名 
  SMHServicesManager()
      .configHostWithEnv("https://previewhost/", SMHHostType.preview);
  // 配置发布域名
  SMHServicesManager()
      .configHostWithEnv("https://releasehost/", SMHHostType.release);
  // 设置当前模式 开发、测试、预发布、发布
  SMHServicesManager().setupCurrentEnv(SMHHostType.dev);
```
>? 设置host 根据项目实际使用场景设置，除了release模式外，其他都为可选。

#### 3. 初始化灯塔（若集成不含灯塔版本，跳过次步骤）
```
// 需要 用户id以及组织id，请在登录完成以后 进行初始化灯塔sdk。
SMHServicesManager().initBeaconSDK(
        userId: userId,
        organizationId: organizationId,
        isDebug: true);
```

## 第四步：访问 SMH 服务

例如：列出文件列表
```
 SMHResponse<SMHFileListEntity>? smhResponse;
    try {
      smhResponse = await SMHAPIDirectoryApis.listDirectory(
          libraryId: 'libraryId',
          spaceId: 'spaceId',
          dirPath: '/');
    } on SMHError catch (e) {
    }
```

## 文件传输任务队列并发数设置
该项为选择性设置，支持自定义并发数量，也可以使用sdk默认策略。
任务并发数根据当前网速自动调节，当前并发数最大不能超过最大并发数，最小为2.

* 设置最大任务并发数（默认5）：
```
SMHTaskManager.instance.setMaxConcurrentCount(8);
```
* 设置当前任务并发数（默认3）：
```
SMHTaskManager.instance.setCustomConcurrentCount(5);
```

## 通用参数介绍

* LibraryId: 媒体库 ID，必选参数；
* SpaceId: 空间 ID，如果媒体库为单租户模式，则该参数固定为连字符(-)；如果媒体库为多租户模式，则必须指定该参数；
* AccessToken: 访问令牌，必选参数；
* UserId: 用户身份识别，当访问令牌对应的权限为管理员权限且申请访问令牌时的用户身份识别为空时用来临时指定用户身份，详情请参阅生成访问令牌接口，可选参数；
* OrganizationId: 组织 ID，必选参数
* UserToken: 用户令牌，必选参数

>? 更多概念 请[点击查看](https://cloud.tencent.com/document/product/1339/49939)
