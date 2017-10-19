## Android 应用
### 1 接入要求
    Android系统2.3以上；
### 2 开发步骤
1)	将VerifySDK.jar拷贝到libs目录下关联到工程

[Android-SDK下载](https://mc.qcloudimg.com/static/archive/48720dad0a66293a8837a60b88ceef4e/archive.zip)

2)	如AndroidManifest.xml未声明以下权限，则添加声明
```
<uses-permission android:name="android.permission.INTERNET" />
```
3)	AndroidManifest.xml中添加声明
```
<activity android:name="com.token.verifysdk.VerifyActivity"></activity>
```
4)	需要下发验证码前从后台获取jsurl（参考服务端开发获取验证码JSURL的接口）

5)	获取到jsurl后调用接口VerifyCoder.getVerifyCoder().startVerifyActivityForResult(Context context,String jsurl,int requestCode)并实现onActivityResult来接收是否验证成功的通知
```
/*
 *  参数说明：
 *  context         调用验证码时当前界面的上下文，
 *                  用于(Activity) context).startActivityForResult，
 *                  请勿使用application的上下文
 *  jsurl           验证码的js链接，从我们后台获取
 *  requestCode     对应onActivityResult的requestCode，可自定义
 */
VerifyCoder.getVerifyCoder().startVerifyActivityForResult(Context context,String jsurl,int requestCode)

//onActivityResult实现实例：
@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		if (requestCode == 1) {//此处对应startVerifyActivityForResult的参数值
			if(resultCode==Activity.RESULT_OK){
				Log.e("onActivityResult", "verifysucc");
				Toast.makeText(MainActivity.this, "验证成功",2000).show();
			}
			else{
				Toast.makeText(MainActivity.this, "未验证成功",2000).show();
			}
		}
	}
```

6)	如有混淆，需要添加脚本
```
<arg value="-libraryjars ${lib}/VerifySDK.jar"/>
<arg value="-keep public class com.token.verifysdk{*; }" />
```
### 3 其它接口说明
```		  
public static VerifyCoder getVerifyCoder()      //获取单例
public void release()                           //重置参数，释放资源
public void setShowtitle(boolean showtitle)	    //是否显示验证码页面标题栏
Public void setJson(String json)	            //用于扩展参数，如实现自定义样式等
public WebView getWebView(Context context,String jsurl,VerifyListener listener) //获取验证码WebView 
```

