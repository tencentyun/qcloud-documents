# AuthSetting

用户授权设置信息

#### 属性

<!-- ##### boolean scope.userInfo

是否授权用户信息，对应接口 [wx.getUserInfo](https://developers.weixin.qq.com/miniprogram/dev/api/open-api/user-info/wx.getUserInfo.html) -->

##### boolean scope.userLocation

是否授权地理位置，对应接口 [wx.getLocation](../../location/getLocation.md)。

是否授权地理位置，对应接口 [wx.chooseLocation](../../location/chooseLocation.md)。

<!-- ##### boolean scope.address

是否授权通讯地址，对应接口 [wx.chooseAddress](/develop/miniprogram/API/open-port/port_address.html#qq-chooseaddress) -->

<!-- ##### boolean scope.invoiceTitle

是否授权发票抬头，对应接口 [wx.chooseInvoiceTitle](/develop/miniprogram/API/open-port/port_fapiao.html#qq-chooseinvoicetitle) -->

<!-- ##### boolean scope.invoice

是否授权获取发票，对应接口 [wx.chooseInvoice](/develop/miniprogram/API/open-port/port_fapiao.html#qq-chooseinvoicetitle) -->

<!-- ##### boolean scope.qqrun

是否授权宿主App运动步数，对应接口 [qq.getQQRunData](/develop/miniprogram/API/open-port/port_sport.html#qq-getqqrundata-object-object) -->

<!-- ##### boolean scope.record

是否授权录音功能，对应接口 [qq.startRecord](/develop/miniprogram/API/media/record.html#qq-startrecord) -->

##### boolean scope.writePhotosAlbum

是否授权保存到相册 [wx.saveImageToPhotosAlbum](../../media/image/saveImageToPhotosAlbum.md)。
<!-- [wx.saveVideoToPhotosAlbum](/develop/miniprogram/API/media/video.html) -->

##### boolean scope.camera

是否授权摄像头，对应[`<camera />`](/develop/component/media/camera.md) 组件

<!-- ##### boolean scope.appMsgSubscribed

订阅消息（833以下版本使用scope.appMsgSubscribed，833及以上版本使用setting.appMsgSubscribed）, [qq.subscribeAppMsg](/develop/miniprogram/API/open-port/port_subscription.html)  -->


##### boolean scope.addFriend

允许被添加好友，主动调用[wx.authorize](../authorize/authorize.md)接口进行授权
