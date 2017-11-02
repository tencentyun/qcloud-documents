
## 功能描述
游戏 SDK 通过调用 Tencent 类的 gameMakeFriend API 添加游戏好友。

## 方法原型

```
public void gameMakeFriend(Activity activity, Bundle params)
```

## 参数说明

| 参数名 | 必选/可选 | 类型 |参数说明 |
|---------|---------|---------|---------|
|MGameAppOperation.GAME_FRIEND_OPENID | 必选 | String |要添加好友的 openid |
|MGameAppOperation.GAME_FRIEND_LABEL | 必选 | String |要添加好友的备注 |
|MGameAppOperation.GAME_FRIEND_ADD_MESSAGE| 必选 | String |验证信息 |
|MGameAppOperation.GAME_SDK_VERSION	| 必选 | String |是否来自游戏 SDK |

>**注意：**
>和原来的加好友接口不同：需要传递参数 MGameAppOperation.GAME_SDK_VERSION。

## 实际示例

```
Bundle params = new Bundle();
params.putString(MGameAppOperation.GAME_FRIEND_OPENID, fopenid.getText() + "");
params.putString(MGameAppOperation.GAME_FRIEND_LABEL, label.getText() + "");
params.putString(MGameAppOperation.GAME_FRIEND_ADD_MESSAGE, message.getText() + "");
params.putString(MGameAppOperation.GAME_SDK_VERSION, "true");
mTencent.makeFriend(GameLogicActivity.this, params);
```
