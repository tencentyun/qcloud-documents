
## 功能描述
通过调用 Tencent 类的 gameBindGroup 调用绑定群接口。
>**注意：**
>CGI 调用需要登录态！若是没有登录态则不会跳到手 Q。

## 方法原型

```
public boolean gameBindGroup(Activity activity, Bundle params)
```

## 参数说明

| 参数名 | 必选/可选 | 类型 |参数说明 |
|---------|---------|---------|---------|
| MGameAppOperation.GAME_UNION_ID | 必选 | String |公会 ID。 |
| MGameAppOperation.GAME_ZONE_ID | 必选 | String |游戏区域 ID。 |
| MGameAppOperation.GAME_UNION_NAME | 必选 | String |公会名称。|
| MGameAppOperation.GAME_ROLE_ID | 必选 | String |游戏角色 ID。|
| MGameAppOperation.GAME_APP_KEY | 必选 | String |与 APPID 对应，第三方申请。 |
## 实际示例

```
mTencent = Tencent.createInstance(APPID, this);
Bundle params = new Bundle();
params.putString(MGameAppOperation.GAME_UNION_ID,  unionid.getText().toString());
params.putString(MGameAppOperation.GAME_ZONE_ID , zoneid.getText());
params.putString(MGameAppOperation.GAME_UNION_NAME, union_name.getText());
params.putString(MGameAppOperation.GAME_ROLE_ID, role_id.getText());
params.putString(MGameAppOperation.GAME_APP_KEY, appkey.getText());
mTencent.gameBindGroup(this, params);
```
