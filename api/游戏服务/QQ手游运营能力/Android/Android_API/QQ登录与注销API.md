
## 登录/授权
### 功能描述
通过调用 Tencent 类的 login 函数发起登录/校验登录态。

该API具有两个作用：
- 如果开发者没有调用 mTencent 实例的 setOpenId 、setAccessToken API，则该 API 执行正常的登录操作。
- 如果开发者先调用 mTencent 实例的 setOpenId 、setAccessToken API，则该 API 执行校验登录态的操作。
 - 如果登录态有效，则返回成功给应用。
 - 如果登录态失效，则会自动进入登录流程，将最新的登录态数据返回给应用。

>**注意：**
>- 建议开发者在每次应用启动时调用一次该 API (先调用 setOpenId 、setAccessToken)，以确保每次打开应用时用户都是有登录态的。
- 在某些低端机上调用登录后，由于内存紧张导致 APP 被系统回收，登录成功后无法成功回传数据。解决办法如下：
在调用 login 的 Activity 或者 Fragment 重写 onActivityResult 方法，示例代码如下：

```
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
    if(requestCode == Constants.REQUEST_API) {
	if(resultCode == Constants.RESULT_LOGIN) {
	         mTencent.handleLoginData(data, loginListener);
    }
    super.onActivityResult(requestCode, resultCode, data);
}
```

### 方法原型

```
public void login(Activity activity, String scope, IUiListener listener)
```
### 参数说明

| 参数名 | 参数说明 | 
|---------|---------|---------|
| activity | 调用者 activity。应用使用 SDK 时，会从应用自己的 Activity 跳转到 SDK 的 Activity，应用调用 SDK 的 Activity 即为这里的调用者 activity。 | 
| scope | 应用需要获得的 API 的权限，由“，”分隔。例如：SCOPE = “get_user_info,add_t”；所有权限用 “all”。 | 
| listener | 回调 API，IUiListener 实例。| 

### 返回码

| 返回码 | 返回码描述 | 
|---------|---------|
| 10 | 解码失败。 |
| 110201 | 票据无效。 |
| 110405 | 登录请求被限制，请稍后在登录。 |
| 110404 | 请求参数缺少 APPID。  |
| 110401 | 请求的应用不存在。 |
| 110407 | 应用已经下架。 |
| 110406 | 应用没有通过审核。|
| 100044 | 错误的 sign。 |
| 110500 | 获取用户授权信息失败。 |
| 110501 | 获取应用的授权信息失败。 |
| 110502 | 设置用户授权失败。 |
| 110503 | 获取 token 失败。 |
| 110504 | 系统内部错误。 |
| 110505 |参数错误。 |
| 110506 | 获取 APP info 信息失败。 |
| 110507 | 校验 APP info 签名信息失败。|
| 110508 | 获取 code 失败。 |
| 110509 | SKEY 校验失败。 |
| 110510 | 应用被禁止登录。 |

### 实例演示

```
private void doLogin() {
 	IUiListener listener = new BaseUiListener() {
 		@Override
 		protected void doComplete(JSONObject values) {
 			updateLoginButton();
 		}
 	};
 	mTencent.login(this, SCOPE, listener);
}
```

## 注销
### 功能描述
通过调用 Tencent 类的 logout 函数注销。
### 方法原型

```
 public void logout(Context context)
```
### 参数说明

| 参数名 | 参数说明 |
|---------|---------|
| context | 调用者的 context 。Context 是上下文的意思，每一个 Activity 都有对应的 Context 。示例中的 this 为调用者 Activity 对应的 Context。 | 
### 实例演示

```
mTencent.logout(this);
```
