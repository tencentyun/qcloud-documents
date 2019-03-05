
## 功能描述
分享消息到 QQ 的接口。可将新闻、图片、文字、应用等消息分享给 QQ 好友、讨论组和群。Tencent 类的 shareToQQ 函数可直接调用，不用用户授权（使用手机 QQ 当前的登录态）。调用将打开分享的界面，用户选择好友、讨论组或群之后，单击【确定】即可完成分享，并进入相应的对话窗口。

本接口支持多种模式，每种模式的参数设置不同，下面分别进行介绍：
## 方法原型

```
 public void shareToQQ(Activity activity, Bundle params, IUiListener listener)
```

## 参数说明
分享图文消息：

| 参数名 | 必选/可选 | 类型 |参数说明|
|---------|---------|---------|---------|
| QQShare.SHARE_TO_QQ_KEY_TYPE | 必选| Int |分享的类型。图文分享(普通分享)填 Tencent.SHARE_TO_QQ_TYPE_DEFAULT。 |
| QQShare.PARAM_TARGET_URL | 必选 | String |分享给好友的 URL。 |
| QQShare.PARAM_TITLE | 必选 | String |分享的标题, 最长 30 个字符。 |
| QQShare.PARAM_SUMMARY | 可选| String |分享的消息摘要，最长 40 个字。 |
| QQShare.SHARE_TO_QQ_IMAGE_URL | 可选 | String |分享图片的 URL 或者本地路径。  |
| QQShare.SHARE_TO_QQ_APP_NAME | 可选 | String |手Q客户端顶部，替换【返回】按钮文字，如果为空，用“返回”代替。 |
| QQShare.SHARE_TO_QQ_EXT_INT | 可选 | Int |分享额外选项，两种类型可选（默认是不隐藏分享到 QZone 按钮且不自动打开分享到 QZone 的对话框）：QQShare.SHARE_TO_QQ_FLAG_QZONE_AUTO_OPEN：分享时自动打开分享到 QZone 的对话框。QQShare.SHARE_TO_QQ_FLAG_QZONE_ITEM_HIDE：分享时隐藏分享到  QZone按钮。 |

分享纯图片：

| 参数名 |必选/可选 | 类型 |参数说明|
|---------|---------|---------|---------|
| QQShare.SHARE_TO_QQ_KEY_TYPE | 必选 | Int |分享的类型。分享纯图片时填写 QQShare.SHARE_TO_QQ_TYPE_IMAGE。 |
| QQShare.SHARE_TO_QQ_IMAGE_LOCAL_URL | 必选 | String |需要分享的本地图片路径。 |
| QQShare.SHARE_TO_QQ_APP_NAME| 可选 | String |手Q客户端顶部，替换【返回】按钮文字，如果为空，用“返回”代替。 |
| QQShare.SHARE_TO_QQ_EXT_INT | 可选 | Int |分享额外选项，两种类型可选（默认是不隐藏分享到 QZone 按钮且不自动打开分享到 QZone 的对话框）：QQShare.SHARE_TO_QQ_FLAG_QZONE_AUTO_OPEN：分享时自动打开分享到 QZone 的对话框。QQShare.SHARE_TO_QQ_FLAG_QZONE_ITEM_HIDE：分享时隐藏分享到  QZone按钮。 |

##  实际示例
分享图文消息：

```
private void onClickShare() { 
    final Bundle params = new Bundle();
    params.putInt(QQShare.SHARE_TO_QQ_KEY_TYPE, QQShare.SHARE_TO_QQ_TYPE_DEFAULT);
    params.putString(QQShare.SHARE_TO_QQ_TITLE, "要分享的标题");
    params.putString(QQShare.SHARE_TO_QQ_SUMMARY,  "要分享的摘要");
    params.putString(QQShare.SHARE_TO_QQ_TARGET_URL,  "http://www.qq.com/news/1.html");
    params.putString(QQShare.SHARE_TO_QQ_IMAGE_URL,"http://imgcache.qq.com/qzone/space_item/pre/0/66768.gif");
    params.putString(QQShare.SHARE_TO_QQ_APP_NAME,  "测试应用222222");
    params.putInt(QQShare.SHARE_TO_QQ_EXT_INT,  "其他附加功能");		
    mTencent.shareToQQ(MainActivity.this, params, new BaseUiListener());
}
```
分享纯图片：

```
private void onClickShare() {
    Bundle params = new Bundle();
    params.putString(QQShare.SHARE_TO_QQ_IMAGE_LOCAL_URL,imageUrl.getText().toString());
    params.putString(QQShare.SHARE_TO_QQ_APP_NAME, appName.getText().toString());
    params.putInt(QQShare.SHARE_TO_QQ_KEY_TYPE, QQShare.SHARE_TO_QQ_TYPE_IMAGE);
    params.putInt(QQShare.SHARE_TO_QQ_EXT_INT, QQShare.SHARE_TO_QQ_FLAG_QZONE_AUTO_OPEN);
    mTencent.shareToQQ(MainActivity.this, params, new BaseUiListener());
}
```
