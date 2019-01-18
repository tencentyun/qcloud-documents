
## 功能描述
通过调用 Tencent 类的 checkBindGroup 调用查询公会是否绑定群接口。
>**注意：**
>CGI 调用需要登录态！若是没有登录态则不会跳到手 Q。

## 方法原型

```
 public void checkBindGroup(Context context, Bundle params, IUiListener listener)
```
## 参数说明

| 参数名 | 必选/可选 | 类型 |参数说明 |
|---------|---------|---------|---------|
| context | 必选 | Context |上下文。|
| params| 必选 | Bundle |外部传递参数，参数请查询下表。 |
| listener | 必选 | IUiListener |回调实例。成功：返回码为 0 并且群号不为空。 |

| 参数名 | 必选/可选 | 类型 |参数说明 |
|---------|---------|---------|---------|
| MGameAppOperation.GAME_GUILD_ID  | 必选 | String|公会 ID|
|MGameAppOperation.GAME_GUILD_ZONE_ID| 必选 | String |游戏区域 ID |
|MGameAppOperation.GAME_ROLE_ID | 必选 | String |游戏角色 ID |


## 实际示例

```
mTencent = Tencent.createInstance(APPID, this);
Bundle params = new Bundle();
params.putString(MGameAppOperation.GAME_GUILD_ID,  guild_id.getText());
params.putString(MGameAppOperation.GAME_GUILD_ZONE_ID , zone_id.getText());
params.putString(MGameAppOperation.GAME_ROLE_ID, role_id.getText());
IUiListener listener = new IUiListener() {
    @Override
public void onComplete(Object response) {
    Util.toastMessage(this, “onComplete:”  + response.toString());
    JSONObject jsonObject = (JSONObject )response;
    try{
        String retMsg = jsonObject.getString(“retMsg”);
        int retCode = jsonObject.getInt(“retCode”);
        //todo  根据返回码处理
     }catch (JSONException e) {
        e.printStackTrace();
     }
    }
    @Override
public void onCancel() {
   Util.toastMessage(this, “onCancel ” );
    }
    @Override
public void onError(UiError e) {
    Util.toastMessage(this, “onError:” + e.errorMessage, “e”);
    }
}
mTencent.unBindGroup(this, params，listener);
```
