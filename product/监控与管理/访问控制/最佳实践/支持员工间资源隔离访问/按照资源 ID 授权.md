## 操作场景
该任务指导您按照资源 ID 授权，实现子用户 cvmtest01 只能管理 ins-duglsqg0 的 [资源级接口](https://cloud.tencent.com/document/product/598/69910) 权限。
[查看详细操作场景 >>](https://cloud.tencent.com/document/product/598/74104)

## 策略内容
按照资源 ID 授权，最终实现上述预期结果时，对应的策略内容如下：
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "cvm:*"
            ],
            "resource": [
                "qcs::cvm::uin/12345678:instance/ins-duglsqg0",//12345678为主账号UIN
                "qcs::cvm::uin/12345678:image/img-eb30mz89"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "vpc:DescribeVpcEx",
                "vpc:DescribeNetworkInterfaces",
                "cvm:DescribeCbsStorages"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```


## 操作步骤

### 步骤1：使用管理员账号创建策略并授权
1. 使用管理员账号登录访问管理控制台，在 [策略](https://console.cloud.tencent.com/cam/policy/createV3) 页面，按照策略生成器创建自定义策略（参考 [创建自定义策略 - 按策略生成器创建](https://cloud.tencent.com/document/product/598/37739#.E6.8C.89.E7.AD.96.E7.95.A5.E7.94.9F.E6.88.90.E5.99.A8.E5.88.9B.E5.BB.BA)）。
![](https://qcloudimg.tencent-cloud.cn/raw/c97abb4b536c87191a2471411309681b.png)
	- 效果：允许
	- 服务：云服务器cvm
	- 操作：全部操作
	- 资源：特定资源 - 添加自定义资源六段式
	- 分别填写：资源前缀：instance 和资源 ID：ins-duglsqg0，以及资源前缀：image 和资源 ID：img-eb30mz89
>?
>- 如何确定资源的前缀：在云服务器支持 CAM 的接口中有云服务器对应的资源六段式，具体可参考 [云服务器支持 CAM 的接口](https://cloud.tencent.com/document/product/598/69910)。
>- 云服务器产品页面除了调用 CVM 相关接口外，还会使用 VPC 等接口，这时我们可以先跳过，继续生成策略，在实际操作的时候按照 CAM 的提示添加相关接口。
>
2. 单击**下一步**，指定策略的名称为 cvm-test01，并将策略授予子账号 cvmtest01。
3. 单击**完成**，完成授权。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1f24d6103425c4b9fcf72db40fe48333.png"> 



### 步骤2：使用子账号登录验证权限[](id:step2)
1. 使用子用户登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)，进入实例列表页面。此时 CVM 页面会提示缺少 VPC 产品 DescribeVpcEx 以及对应资源的权限。
2. 根据页面提示内容，联系管理员账号在策略中添加对应授权。
<img src="https://qcloudimg.tencent-cloud.cn/raw/31c8b1c1c21e8795e5ffe37e6ac165da.png">    


### 步骤3：使用管理员账号调整策略内容

1. 使用主账号在 [VPC 支持 CAM 的接口](https://cloud.tencent.com/document/product/598/70069) 清单中，找到 DescribeVpcEx 确定接口为操作级的接口。
![](https://qcloudimg.tencent-cloud.cn/raw/3046262623e98f99335be9432b5974cf.png)
2. 在访问管理控制台的 [策略](https://console.cloud.tencent.com/cam/policy) 页面，找到策略 cvm-test01，单击策略名进入策略详情。[](id:3)
3. 在策略语法中单击**编辑**，按照操作级接口的授权书写形式在策略详情中添加接口授权。
<img src="https://qcloudimg.tencent-cloud.cn/raw/06b3da3075c13938a5ec9f589e4b73c1.png" >  
添加之前：
<img src="https://qcloudimg.tencent-cloud.cn/raw/cc9aea271b5f8f8379dcea7565fa78d8.png" >       
添加之后：
<img src="https://qcloudimg.tencent-cloud.cn/raw/7252943a333af7604cf5ef5191bc9915.png" >    [](id:4)    
4. 添加之后重复 [步骤2](#step2)，使用子账号 cvmtest01 再次验证，发现仍有异常，缺少 VPC 下 DescribeNetworkInterfaces 以及对应资源的访问权限，查看 [私有网络支持 CAM 的接口](https://cloud.tencent.com/document/product/598/70069) 确定 DescribeNetworkInterfaces 为操作级的接口。
<img src="https://qcloudimg.tencent-cloud.cn/raw/410ef6729908e922a2152f268e7b5fff.png" > 
5. 按照 [步骤3](#3) 继续调整策略内容，直至系统没有报错。
最终策略的内容如下：
<img src="https://qcloudimg.tencent-cloud.cn/raw/a78f76d9363c4ae99f3b2a6845e6710c.png" >  
>?在书写 CAM 策略时，在需要操作具体资源时，资源级的接口授权需要和操作级分开书写，多个操作级接口可以书写在一起。
>


### 步骤4：验证结果
使用子用户 cvmtest01 再次验证，达到预期效果。
至此，子用户 cvmtest01 可以对实例进行开关机、重启、更名、重置密码等操作。
<img src="https://qcloudimg.tencent-cloud.cn/raw/f52e729bf9fb570f08d240b8a157b761.png" >    
