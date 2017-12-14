
## 功能描述
分享类型参数 Tencent.SHARE_TO_QQ_KEY_TYPE，目前只支持图文分享，而 Tencent.shareToQzone() 函数既完善了分享消息到 QZone 的功能，又可直接调用，不用用户授权（使用手机 QQ 当前的登录态）。开发者可以调用此 API 打开手机 QQ 或浏览器 QQ 的空间界面进行分享操作。

## 方法原型

```
 public void shareToQzone(Activity activity, Bundle params, IUiListener listener)
```

## 参数说明

| 参数名 |必选/可选 | 类型 |参数说明 |
|---------|---------|---------|---------|
| QzoneShare.SHARE_TO_QQ_KEY_TYPE | 选填 | Int |SHARE_TO_QZONE_TYPE_IMAGE_TEXT（图文）。 |
| QzoneShare.SHARE_TO_QQ_TITLE | 必选 |Int |分享的标题，最多 200 个字符。|
| QzoneShare.SHARE_TO_QQ_SUMMARY | 选填 | String |分享的摘要，最多 600 字符。 |
| QzoneShare.SHARE_TO_QQ_TARGET_URL | 必选 | String|需要跳转的链接，URL 字符串。 |
| QzoneShare.SHARE_TO_QQ_IMAGE_URL | 选填 | String |分享的图片, 以 ArrayList<String> 的类型传入，以便支持多张图片（注：图片最多支持 9 张图片，多余的图片会被丢弃）。 |

>**注意：**
>QZone 接口暂不支持发送多张图片的能力，若传入多张图片，则会自动选入第一张图片作为预览图。分享多图的能力将会在以后实现。

## 实际示例 

```
private void shareToQzone () {//分享类型
　　params.putString(QzoneShare.SHARE_TO_QQ_KEY_TYPE,SHARE_TO_QZONE_TYPE_IMAGE_TEXT );
    params.putString(QzoneShare.SHARE_TO_QQ_TITLE, "标题");//必填
    params.putString(QzoneShare.SHARE_TO_QQ_SUMMARY, "摘要");//选填
    params.putString(QzoneShare.SHARE_TO_QQ_TARGET_URL, "跳转URL");//必填
    params.putStringArrayList(QzoneShare.SHARE_TO_QQ_IMAGE_URL, "图片链接ArrayList");
    mTencent.shareToQzone(activity, params, new BaseUiListener());
}
```
