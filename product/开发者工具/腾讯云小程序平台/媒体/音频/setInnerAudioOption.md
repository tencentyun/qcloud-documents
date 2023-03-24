# wx.setInnerAudioOption

#### wx.setInnerAudioOption(Object object)

设置 [InnerAudioContext](./InnerAudioContext.md) 的播放选项。设置之后对当前小程序全局生效。

#### 参数

##### Object object

属性             | 类型       | 默认值  | 必填 | 说明                                               
-------------- | -------- | ---- | -- | -------------------------------------------------
mixWithOther   | boolean  | true | 否  | 是否与其他音频混播，设置为 true 之后，不会终止其他应用的音乐            
obeyMuteSwitch | boolean  | true | 否  | （仅在 iOS 生效）是否遵循静音开关，设置为 false 之后，即使是在静音模式下，也能播放声音
success        | function |      | 否  | 接口调用成功的回调函数                                      
fail           | function |      | 否  | 接口调用失败的回调函数                                      
complete       | function |      | 否  | 接口调用结束的回调函数（调用成功、失败都会执行）    
