## 上传 IDFA 注意事项

由于 iOS SDK 默认采集 IDFA，而使用 IDFA 原则上需要集成任意一家的广告 SDK，如果您期望采集 IDFA 但是并未使用任何广告，可以采用以下方法通过 Appstore 审核。
![img](https://main.qcloudimg.com/raw/fd68d9444cc4f8858b09c71433c65153/0.png)             

1. Serve advertisements within the app
应用内广告服务，适用于应用内集成了广告的场景，如果您的情况符合，需要勾选此选项。
2. Attribute this app installation to a previously served advertisement
用于跟踪和统计广告带来的安装量，需要勾选。
3. Attribute an action taken within this app to a previously served advertisement
用于跟踪和统计广告安装后带来的用户行为，需要勾选。
4. Limit Ad Tracking setting in iOS
此项属于确认项，需要勾选。
