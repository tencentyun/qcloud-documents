## 前提条件
- 需已 [购买开通 CASB 实例](https://cloud.tencent.com/document/product/1303/53298)。

## 操作步骤
### 查看Proxy资源信息。
1.  点击`实例-实例列表`菜单，选择已购买实例的地域，查看已购买的[实例列表](https://console.cloud.tencent.com/casb)。点击需要操作的实例ID，进入实例详情页面。

    ![](https://qcloudimg.tencent-cloud.cn/raw/851e7e1678e688bde029d18b38cbbd5d.png)

2. 选择“Proxy资源”标签，可查看CASB实例提供的所有代理资源列表及代理资源已绑定的元数据、功能启停状态信息。

   ![](https://qcloudimg.tencent-cloud.cn/raw/239e9bd7224ea643d977e2a302529efa.png)

### 绑定代理和元数据。
1. 在代理资源列表中，选择一个尚未绑定元数据的代理Proxy地址，点击操作栏中的**绑定**，弹出“绑定元数据”对话框。
   ![](https://qcloudimg.tencent-cloud.cn/raw/a646784827ff1dcaffec418dc36c381c.png)
2. 选择需要绑定的元数据，以及需要开通的加密/脱敏功能。
   ![](https://qcloudimg.tencent-cloud.cn/raw/cda43100c6fbb616625185ab734f610d.png)
    > ?若此项功能已购买的配额已用完，可购买[功能扩展包](https://cloud.tencent.com/document/product/1303/53298)增加配额。
3. 点击确定，即可完成代理和元数据的绑定。
   > ?代理和元数据绑定后，需[设置代理账号]((https://cloud.tencent.com/document/product/1303/64635))后，才可以通过代理账号访问代理。

### 解绑代理和元数据。
> !解绑元数据后，代理地址下的所有代理账号及绑定到代理账号的脱敏策略、访问控制策略都将被删除、请谨慎操作。
1. 在代理资源列表中，选择需要解绑元数据的代理Proxy地址，点击操作栏中的**解绑**，弹出“解绑元数据”确认框，点击确认后即可完成解绑。
 
    ![](https://qcloudimg.tencent-cloud.cn/raw/d22fa741c181da61d0cccccce271975b.png)

