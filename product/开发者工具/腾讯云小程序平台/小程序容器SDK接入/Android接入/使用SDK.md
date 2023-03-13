## 调试

通过关键字 TMF_APPLET 过滤得到小程序日志。

## SDK 初始化

### 配置文件获取

开发人员从开放平台获取对应 App 的配置文件，该配置文件是一个 json 文件，包含该 App 使用小程序平台的所有信息，将配置文件引入到项目的 assets 根目录。

> **说明：**配置文件中的 packageName 必须与应用的包名保持一直，否则 App 运行失败。
> 


### 配置信息设置

根据配置文件初始化一下 AppletConfig 对象，并使用 AppletConfig 初始化 TMF 小程序引擎。

参考如下：
``` cpp

AppletConfig config = builder
        .configAssetName("TMF_CONFIGURATIONS")//assets中配置文件名称
        .imei("IMEI");////配置设备id，⽤于在管理平台上根据设备标识进⾏⼩程序的灰度发布使⽤
        .build();
TmfAppletService.init(this, config);
```

### 其他初始化动作

设置地区或者账号，方便进行灰度推送时使用。
``` cpp
/**
 * 设置账号信息
 * @param userId
 */public static void setUserId(String userId)
 
/**
 * 设置位置信息
 * @param country
 * @param province
 * @param city
 */public static void setLocation(String country, String province, String city)
```

## 小程序管理 API

### 打开小程序

#### 打开普通小程序

打开小程序时，会先判断本地是否有缓存的小程序，如果没有，则会自动从远程服务器上下载小程序，然后打开。如果有缓存的小程序，则会先打开本地小程序，然后在后台校验服务器端是否有新版本。

如果有新版本，则下载新版小程序，下次打开时，就会使用新版小程序。如果没有新版本，则仍使用原版本。
``` cpp
/**
 * 根据appId打开小程序
 * @param activity
 * @param appId 
 * @param options 打开小程序参数
 */
 public static void startApplet(Activity activity, String appId, AppletOptions options) 
```

#### 打开二维码小程序

TMF 内置扫码模块，通过 scan 接口启动扫码，在 onActivityResult 中调用 scanResult 对扫码结果进行处理。
``` cpp
/**
* 启动扫码
*
* @param activity
*/
public static void scan(Activity activity) 
/** 
* 扫码结果处理,在onActivityResult中调用
* 
* @param activity
* @param requestCode 
* @param resultCode
* @param data 
*/
public static void scanResult(Activity activity, int requestCode, int resultCode, Intent data, ValueCallback<BaseEntity> callback)
```

### 删除小程序

由于小程序的运行，会将小程序包和小程序信息缓存在本地，以后打开时速度会非常快。 所以，如果想要将小程序的所有信息都删除，那么可以调用以下 API 删除某个小程序或者删除所有小程序。
``` cpp
/** 
* 删除小程序 
* @param appId 
*/
public static void deleteApp(String appId) 
/** 
* 删除所有小程序 
*/
public static void deleteAllApp() 
```

### 获取小程序信息

#### 获取本地缓存的所有小程序信息
``` cpp
/**
* 获取本地所有小程序
* @return 
*/
public static List<AppEntity> getAllApp()
```

#### 获取本地缓存的指定小程序信息
``` cpp
/** 
* 获取本地小程序
* 
* @param appId
* @return null:本地没有小程序
*/
public static AppEntity getApp(String appId)
```

### 自定义 API

#### 数据返回

自定义 API 数据返回分为同步和异步。

同步返回方法：
``` cpp
protected String getSuccess(String method, JSONObject result)
public String getError(String err, String method)
```

示例代码：
``` cpp
@Override
public String handle(String method, String args, String callbackId) throws Exception {
    //同步返回数据
    return getSuccess( method, result);
    }
```

异步返回方法：
``` cpp
protected void sendSuccess(String callbackId, JSONObject result, String method)
protected void sendError(String callbackId, String err, String method)
```

示例代码：
``` cpp
@Override
public String handle(String method, String args, String callbackId) throws Exception {
/** 
* 异步和同步只能使用其中一种返回数据 
*/  
//异步返回数据 
sendSuccess(callbackId, method);
return "";
}
```

> **说明**：return 返回空字符串即可。
> 


#### 自定义 JSAPI

创建自定义 API。
- 继承 JsApiExt。

- method 设置 API 名称。
   

   > **说明：**请设置为具有自身标识的名称，避免和内置 API 冲突。
   > 

   ``` cpp
   public class CustomJsApi extends JsApiExt {
   /**
   * 事件名（唯一）
   *
   * @return 
   */ 
   @Override   
   public String method() { 
   return "CustomEventName";  
   }  
   /**    
   * 调用处理   
   *  
   * @param method     事件名  
   * @param args       事件参数 
   * @param callbackId 异步返回id，参见父类sendError、sendSuccess、getError、getSuccess 
   * @return 同步返回  
   * @throws Exception   
   */   
   @Override   
   public String handle(String method, String args, String callbackId) throws Exception {  
   /**    
   * 异步和同步只能使用其中一种返回数据    
   */    
   //异步返回数据   
   sendSuccess(callbackId, method);  
   return "";  
   }
   }
   ```

   将 API 设置到系统中


   `TmfAppletService.addJsApi(new CustomJsApi());`


#### 自定义扫码

SDK提供默认扫码实现，如需使用默认能力需添加如下 SDK。

`implementation "com.tencent.tmf.android:qrcode:xxxxx"`

如需使用自定义扫码组件，可以移除上面的依赖，然后参考如下步骤实现自定扫码。
1. 继承 BaseScanCodeApi。

   ``` cpp
   public class CustomScanCodeJsApi extends BaseScanCodeApi {
   /**  
   * 扫码启动  
   *  
   * @param activity       小程序activity  
   * @param requestCode    请求code  
   * @param onlyFromCamera 是否仅从相机扫码   
   * @param scanType       扫码类型  
   * @param extend         扩展参数，暂未使用 
   */  
   @Override  
   public void onStartScan(Activity activity, int requestCode, boolean onlyFromCamera, String[] scanType, JSONObject extend) { 
   Intent intent = new Intent(activity, CustomScanActivity.class);  
   intent.putExtra("onlyFromCamera", onlyFromCamera); 
   //此处必须使用参数requestCode   
   activity.startActivityForResult(intent, requestCode);  
   }
   }
   ```
2. 添加 API 到系统中。


   `TmfAppletService.addJsApi(new CustomScanCodeJsApi());`

3. 在自定义 Activity 中需按照如下格式返回数据：

   ``` cpp
   Intent intent = new Intent();
   intent.putExtra("result", result);
   intent.putExtra("charSet", "");
   intent.putExtra("scanType", "");
   setResult(RESULT_OK, intent);
   ```

#### 自定义分享

用户点击小程序胶囊按钮中的分享按钮，触发分享业务逻辑，接入方需要接入分享逻辑，接入步骤如下：
- 继承 BaseCustomizeJsApi。

   ``` bash
   
   package com.tencent.tmf.applet.demo.jsapi;
   import static com.tencent.tmf.applet.demo.App.TAG;
   import android.app.Activity;
   import android.text.TextUtils;
   import android.util.Log;
   import android.widget.Toast;
   import com.tencent.tmf.applet.api.jsapi.impl.BaseCustomizeJsApi;
   import com.tencent.tmf.applet.api.jsapi.impl.IBaseJsApiHandle;
   import com.tencent.tmf.applet.api.jsapi.impl.ICallBack;
   import com.tencent.tmf.applet.demo.utils.ShareUtil;
   import com.tencent.tmf.share.api.ITMFShareListener;
   import org.json.JSONException;
   import org.json.JSONObject;
   public class CustomShareJsApi extends BaseCustomizeJsApi implements IBaseJsApiHandle {
   public CustomShareJsApi() { 
   super();  
   }  
   @Override  
   public String method() { 
   return APIMethod.METHOD_SHARE;
   } 
   @Override   
       public IBaseJsApiHandle getCustomHandle() {  
             return this; 
    }   
   @Override
   public void onHandle(Activity activity, JSONObject params, ICallBack callback) {        
       final JSONObject data = new JSONObject();        
         Log.i(TAG, "onShare event reach,do custom login strategy {} params" + params);        
           try {          
           //从参数中提取控制台绑定的微信小程序id（wxAppId）            
               String wxAppId = params.optString("wxAppId");            
               if (TextUtils.isEmpty(wxAppId)) {                
               activity.runOnUiThread(new Runnable() {                    
             @Override                    
              public void run() {                  
                 Toast.makeText(activity, "尚未绑定微信小程序ID，请在控制台绑定", Toast.LENGTH_SHORT).show();        
               }        
           });       
         }            
         ShareUtil.shareWxMiniProgram(activity, new ITMFShareListener() {   
         @Override           
         public void onSuccess(int i, Object o) {      
           Log.i(TAG, "onSuccess " + i + " " + o);     
           try {             
               data.put("success", true);       
               //成功回调          
                callback.onSuccess(data);  
             } catch (JSONException e) {    
                 e.printStackTrace();     
           }        
       }          
         @Override             
           public void onError(int i, int i1, String s) {           
               Log.i(TAG, "onError " + i + " " + i1 + " " + s);   
               try {               
                     data.put("success", false);    
                      //失败回调        
                     callback.onFailed(data);                   
                     } catch (JSONException e) {      
                     e.printStackTrace();           
                   }           
               }      
             }, false, params);     
           } catch (Exception e) {   
             Log.i("TMF_APPLET", "catch Exception 1 " + e);     
           }   
         }
      }
   ```
- 重写 method 方法，将 method 方法的返回值填写为：APIMethod.METHOD_SHARE。

- 实现 IBaseJsApiHandle 接口的 onHandle 方法，在方法内完成分享的业务逻辑。

- 分享的业务逻辑步骤完成后，根据分享情况，将分享的结果调用 ICallBack 实例回调。

- 添加 API 到系统中：


   `TmfAppletService.addJsApi(new CustomShareJsApi());`


#### 自定义登录

SDK 提供登录透传接口，用户可以按照如下的步骤实现自定义登录：
- 继承 BaseCustomizeJsApi。

   ``` cpp
   package com.tencent.tmf.applet.demo.jsapi;
   
   import static com.tencent.tmf.applet.demo.App.TAG;
   
   import android.app.Activity;
   import android.content.Intent;
   import android.util.Log;
   import android.webkit.ValueCallback;
   
   import com.tencent.tmf.applet.api.jsapi.impl.BaseCustomizeJsApi;
   import com.tencent.tmf.applet.api.jsapi.impl.IBaseJsApiHandle;
   import com.tencent.tmf.applet.api.jsapi.impl.ICallBack;
   import com.tencent.tmf.applet.demo.LoginActivity;
   import com.tencent.tmf.applet.demo.utils.WxApiUtil;
   
   import org.json.JSONException;
   import org.json.JSONObject;
   
   public class CustomLoginJsApi extends BaseCustomizeJsApi implements IBaseJsApiHandle {
       public CustomLoginJsApi() {
           super();
       }
   
       @Override
       public String method() {
           return APIMethod.METHOD_LOGIN;
       }
   
       @Override
       public IBaseJsApiHandle getCustomHandle() {
           return this;
       }
   
       @Override
       public void onHandle(Activity activity, JSONObject params, ICallBack callback) {
           Log.i(TAG, "login event reach,do custom login strategy {} params " + params);
           int type = params.optInt("type");
           if (type == 0) {//使用微信登录
               WxApiUtil.getInstance().sendLogin(params, new ValueCallback<JSONObject>() {
                   @Override
                   public void onReceiveValue(JSONObject value) {
                       Log.i("TMF_APPLET", "wechat login " + value);
                     //登录成功回调
                       callback.onSuccess(value);
                   }
               });
           } else if (type == 1) {//使用其他方式登录
               Intent intent = new Intent(activity, LoginActivity.class);
               intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
               activity.startActivity(intent);
               JSONObject jsonObject = new JSONObject();
               try {
                   jsonObject.put("success", true);
               } catch (JSONException e) {
                   e.printStackTrace();
               }
           }
       }
   }
   ```
- 重写 method 方法，将 method 方法的返回值填写为：APIMethod.METHOD_LOGIN。

- 实现 IBaseJsApiHandle 接口的 onHandle 方法，在方法内完成自定义登录的业务逻辑。

- 自定义的登录业务逻辑完成后，根据登录结果，利用 ICallBack 进行回调：登录成功调用 onSuccess 方法，失败调用 onFailed 方法。

- 添加 API 到系统中：


   `TmfAppletService.addJsApi(new CustomLoginJsApi());`






