iOS SDK 支持发起 QQ 临时会话，获取指定 QQ 帐号在线状态。使用 WPA 功能需要设置 QQ 业务回调，请参考 [处理 QQ 业务的回调](https://cloud.tencent.com/document/product/630/11887)。


## 发起 QQ 临时会话
下面是向指定 QQ 号码发起临时会话的示例代码：
```
(void)onOpenWPA:(QElement *)sender {
　　[self.view endEditing:YES];
　　[self.root fetchValueUsingBindingsIntoObject:self];
　　QQApiWPAObject *wpaObj = [QQApiWPAObject objectWithUin:self.binding_uin];
　　SendMessageToQQReq *req = [SendMessageToQQReq reqWithContent:wpaObj];
　　QQApiSendResultCode sent = [QQApiInterface sendReq:req];
　　[self handleSendResult:sent];
}
```

## 获取指定 QQ 号码的在线状态
```
(void)getQQUinOnlineStatues:(QElement *)sender {
　　[self.view endEditing:YES];
　　[self.root fetchValueUsingBindingsIntoObject:self];
　　NSArray *ARR = [NSArray arrayWithObjects:self.binding_uin, nil];
　　[QQApiInterface getQQUinOnlineStatues:ARR delegate:self];
}
```
