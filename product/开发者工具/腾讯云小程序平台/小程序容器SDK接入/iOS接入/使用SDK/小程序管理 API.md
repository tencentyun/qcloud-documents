## 打开小程序

### 打开普通小程序

打开小程序时，会先判断本地是否有缓存的小程序，如果没有，则会自动从远程服务器上下载小程序，然后打开。如果有缓存的小程序，则会先打开本地小程序，然后在后台校验服务器端是否有新版本。

如果有新版本，则下载新版小程序，下次打开时，就会使用新版小程序；如果没有新版本，则什么也不做。
``` html
/// 通过小程序id打开小程序
/// @param appID 小程序ID
/// @param scene 场景值
/// @param firstPage 打开页面
/// @param paramsStr 带入参数
/// @param parentVC 从哪个vc呼起
/// /// @param completion 错误回调
- (void)startUpMiniAppWithAppID:(NSString *)appID
                          scene:(TMAEntryScene)scene
                      firstPage:(NSString * _Nullable)firstPage
                         paramsStr:(NSString * _Nullable)paramsStr
                       parentVC:(UIViewController *)parentVC
                     completion:(void (^)(NSError * _Nullable))completion;
```

options 支持的参数列表：
<table>
<tr>
<td rowspan="1" colSpan="1" >名称</td>

<td rowspan="1" colSpan="1" >必须</td>

<td rowspan="1" colSpan="1" >类型</td>

<td rowspan="1" colSpan="1" >作用</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >appID</td>

<td rowspan="1" colSpan="1" >YES</td>

<td rowspan="1" colSpan="1" >NSString</td>

<td rowspan="1" colSpan="1" >打开指定小程序的小程序 id</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >scene</td>

<td rowspan="1" colSpan="1" >YES</td>

<td rowspan="1" colSpan="1" >TMAEntryScene</td>

<td rowspan="1" colSpan="1" >打开小程序使用的场景值，参见TMAEntryScene</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >firstPage</td>

<td rowspan="1" colSpan="1" >NO</td>

<td rowspan="1" colSpan="1" >NSString</td>

<td rowspan="1" colSpan="1" >打开页面</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >paramsStr</td>

<td rowspan="1" colSpan="1" >NO</td>

<td rowspan="1" colSpan="1" >NSString</td>

<td rowspan="1" colSpan="1" >打开传递参数</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >parentVC</td>

<td rowspan="1" colSpan="1" >YES</td>

<td rowspan="1" colSpan="1" >UIViewController</td>

<td rowspan="1" colSpan="1" >从哪个VC呼起</td>
</tr>

<tr>
<td rowspan="1" colSpan="1" >completion</td>

<td rowspan="1" colSpan="1" >YES</td>

<td rowspan="1" colSpan="1" >block</td>

<td rowspan="1" colSpan="1" >错误回调</td>
</tr>
</table>


### 打开二维码小程序

TMF 支持识别二维码的内容给小程序引擎打开小程序。
``` html
/// 通过二维码呼起小程序
/// @param qrData 二维码内容
/// @param parentVC 从哪个vc呼起
/// @param completion 错误回调
- (void)startUpMiniAppWithQrData:(NSString *)qrData
                       parentVC:(UIViewController *)parentVC
                      completion:(void (^)(NSError * _Nullable error))completion;
```

## 关闭小程序
``` html
///关闭所有内存中正在运行的小程序

- (void)closeAllApplications;
```

## 清理缓存

由于小程序的运行，会将小程序包和小程序信息缓存在本地，以后打开时速度会非常快。 所以，如果想要将小程序的所有信息都删除，那么可以调用以下 API 删除所有小程序缓存数据。
``` html
/// 移除小程序所有相关缓存 包含资源包、基础库、小程序/小游戏沙箱数据
- (void)clearMiniAppCache;
```

## 获取小程序信息

### 获取当前正在运行的小程序信息
``` html
/// 获取当前正在运行的小程序对象
/// @return TMFAppletInfo 小程序信息
- (TMFMiniAppInfo *)currentApplet;
```

### 获取最近打开过的所有小程序信息
``` html
//获取最近打开的所有小程序信息
///@return 小程序数组<TMFMiniAppInfo>
- (NSArray *)loadAppletsFromCache;
```

## 搜索小程序

可以根据关键词搜索目前小程序平台上已经发布的小程序列表。
``` html
/// 搜索小程序
/// @param name 搜索名称关键词
/// @param completion 搜索结果
- (void)searchAppletsWithName:(NSString *)name
                      completion:(void (^)(NSArray<TMFAppletSearchInfo *> * _Nullable, NSError * _Nullable))completion;
```































