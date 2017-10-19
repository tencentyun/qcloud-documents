## IOS 应用
### 1 概述
SDK工具包目录结构说明:
> * TCWebCodesSDK.framework:包含TCWebCodesSDK.framework
> * TCWebCodesSDKDemo:示例工程,演示了如何使用TCWebCodesSDK.framework

本SDK运行环境与项目要求:
> 适用于iOS6.0及以上的系统版本
> 
[IOS-SDK下载](https://mc.qcloudimg.com/static/archive/e712602cb7317ed4642b2d785caf2f60/iOS_SDK_Demo_20170816.zip)

### 2 接口说明
```
/**
 设置回调
 @note 成功/失败可以通过 resultJSON[@"ret"] 判断，0为成功，非0为失败
 @warning 为了避免引用，内部再回调完成后会重置回调为空，请记得每次都需要设置回调
 */
@property (nonatomic, copy) void (^callback)(NSDictionary *resultJSON, UIView *webView);
```
<mark>主要函数，设置验证结果的callback回调；<mark>

```
/**
 开始加载H5
 @param url，业务服务器通过腾讯云拉取的验证码URL
 @param frame, webView控件大小
 @return 返回H5的webView控件
 @note 该函数用于开始加载，并且返回H5的webView控件，用于显示
 @warning 请不要设置返回webView控件的回调
 */
- (UIView*)startLoad:(NSString*)url webFrame:(CGRect)frame;
```
<mark>主要函数，通过腾讯云返回的验证码URL创建一个用于显示的webView控件；<mark>

```
/**
返回单例
*/
+ (instancetype)sharedBridge;  
```
返回 TCWebCodesBridge 全局对象；
  
```
/**
设置是否显示H5的内部导航头部
*/
@property (nonatomic) BOOL showHeader;
```
配置函数，设置是否显示H5页面的头部，默认不显示；
  
```
/**
设置其余属性
@note 该接口是为了后续扩展
@warning 请设置value为基本类型: string, number
*/
- (void)setCapValue:(id)aValue forKey:(id<NSCopying>)aKey;  
```
可扩展函数，用于设置后续显示H5界面的一些样式；

