为完善公网 IP 的访问管理功能，腾讯云将对**[ 解绑并释放普通公网 IP 接口（ReturnNormalAddresses） ](https://cloud.tencent.com/document/api/215/83866)**的鉴权功能进行升级优化，升级后子用户调用此接口需向主账号 申请 CAM 策略授权，否则可能调用失败。您也可以按照以下流程提前为子用户配置策略授权。

## 为子用户配置策略授权
1. 在访问管理控制台的 [策略](https://console.cloud.tencent.com/cam/policy) 页面，单击左上角的**新建自定义策略**。
2. 在弹出的选择创建方式窗口中，单击**按策略语法创建**，进入选择策略模板页面。
3. 选择策略模板页面，选择空白模板，单击**下一步**，进入编辑策略页面。
4. 在编辑策略页面，确认策略名称、复制以下策略内容后单击**完成**，完成按策略语法创建 ReturnNormalAddresses 接口授权策略操作。其中默认的策略名称由控制台自动生成，策略名称默认为 "policygen"，后缀数字根据创建日期生成。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "vpc:ReturnNormalAddresses"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```
<img src="https://qcloudimg.tencent-cloud.cn/raw/b05f6b0668b3d569d707cebea9c46707.png" width="50%"> 
5. 在策略列表中，找到需授权的策略，单击右侧**操作**列的**关联用户/组**。
6. 在弹出的“关联用户/用户组”对话框中，单击左侧列表的目标用户项，将其添加至右侧的“已选择”列表中，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/6e1afcf09f07df99264e41f48e3cbaab.png" width="70%"> 
