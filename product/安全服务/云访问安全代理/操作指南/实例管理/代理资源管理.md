## 前提条件
需已 [购买开通 CASB 实例](https://cloud.tencent.com/document/product/1303/53298)。

## 操作步骤
### 查看 Proxy 资源信息
1. 登录 [云访问安全代理控制台](https://console.cloud.tencent.com/casb)， 在左侧导航栏中，单击**实例** > **实例列表**。
2. 在实例列表页面，选择已购买实例的地域，查看已购买的 [实例列表](https://console.cloud.tencent.com/casb)。单击需要操作的**实例 ID**，进入实例详情页面。
![](https://qcloudimg.tencent-cloud.cn/raw/bc44cfa26adb0251ad8189940208a9ff.png)
3. 选择 **Proxy 资源**标签，可查看 CASB 实例提供的所有代理资源列表及代理资源已绑定的元数据、功能启停状态信息。
![](https://qcloudimg.tencent-cloud.cn/raw/b654d07abbcc92510d83072aa01ec0a9.png)

### 绑定代理和元数据
1. 在代理资源列表中，选择一个尚未绑定元数据的代理 Proxy 地址，单击操作列中的**绑定**，弹出“绑定元数据”对话框。
![](https://qcloudimg.tencent-cloud.cn/raw/554c21c798bbe7af9d11fb5b2d909857.png)
2. 选择需要绑定的元数据，以及需要开通的加密/脱敏功能。
![](https://qcloudimg.tencent-cloud.cn/raw/d13d0e0dc04d6ea53334db07d0b9a11b.png)
> ?若此项功能已购买的配额已用完，可购买 [功能扩展包](https://cloud.tencent.com/document/product/1303/53298) 增加配额。
> 
3. 单击**确定**，即可完成代理和元数据的绑定。
   > ?代理和元数据绑定后，需 [设置代理账号](https://cloud.tencent.com/document/product/1303/64635) 后，才可以通过代理账号访问代理。

### 解绑代理和元数据
> !解绑元数据后，代理地址下的所有代理账号及绑定到代理账号的脱敏策略、访问控制策略都将被删除、请谨慎操作。
> 
在代理资源列表中，选择需要解绑元数据的代理 Proxy 地址，单击操作栏中的**解绑**，弹出“解绑元数据”确认框，单击**确认**后即可完成解绑。
![](https://qcloudimg.tencent-cloud.cn/raw/497e1f99de873bf90640278d8a73530e.png)
