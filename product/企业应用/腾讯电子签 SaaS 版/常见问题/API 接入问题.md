## 接入前常见问题
### 应用号是什么？
应用号是您企业账号下每款应用的唯一标识符，用于快速标记您企业下的各款应用。
当您在腾讯电子签创建企业后，可通过申请应用号的方式对您企业下的若干款应用进行标记，以区分企业下不同应用之间的数据及请求。各应用号之间的数据相互隔离。


### 通过小程序注册的企业，如何查看对应企业的 API 密钥信息？
通过小程序注册的企业，单击**查询密钥**，即可查看对应企业的 API 密钥信息。
![](https://qcloudimg.tencent-cloud.cn/raw/fadeda9efb8cce940ceb7bf5829405bc.png)     
>!
- API 密钥是构建腾讯云 API 请求的重要凭证，请妥善保管。
- 查询密钥过程中，可能需要通过短信验证码进行安全校验，如您不是该手机号所有人，请与企业超级管理员联系。
- 此入口当前仅小程序注册的企业可见，电脑端注册企业的 API 密钥查看方式请参见 [访问密钥](https://cloud.tencent.com/document/product/598/40487) 文档。


### 子账号可以调用开放平台的 API 吗？
可以，您可使用主账号登录腾讯云访问管理，为子账号授权绑定电子签策略 QcloudESSBASICFullAccess，授权之后即可使用子账号调用腾讯电子签集成版 API 接口。授权指引请参见 [授权指引文档](https://cloud.tencent.com/document/product/1420/58765#.E5.A6.82.E4.BD.95.E4.BD.BF.E7.94.A8.E5.AD.90.E7.94.A8.E6.88.B7.E8.B4.A6.E5.8F.B7.E7.99.BB.E5.BD.95.E7.94.B5.E5.AD.90.E7.AD.BE.EF.BC.9F.3Ca-id.3D.22q6.22.3E.3C.2Fa.3E)。

## SDK 相关 
### 如何获取 SDK 调用样例？  
电子签集成版目前提供了 [PHP](https://github.com/TencentCloud/tencentcloud-sdk-php/tree/master/examples/ess) 、[Python](https://github.com/TencentCloud/tencentcloud-sdk-python/tree/master/examples/ess) 、[Java](https://github.com/TencentCloud/tencentcloud-sdk-java/tree/master/examples/ess) 、[Go](https://github.com/TencentCloud/tencentcloud-sdk-go/tree/master/examples/ess)  等语言的调用 Demo 供您在接入时参考，已上传至 GitHub 腾讯云官方 SDK 项目。

### 如何导入 SDK ？  
目前官方提供了 PHP、Python、Java、Go、.NET、Node.js、C++、Ruby 等语言的 SDK 支持，请根据您的实际需要进行导入，请参见  [SDK 导入指引](https://cloud.tencent.com/document/sdk) 。


## 小程序相关
### 客户小程序如何跳转到电子签小程序完成签署？  
请参见小程序 [官方文档](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html) 。小程序支持直接跳转到签署页面，完成签署后可返回客户小程序。可参见以下代码：  
```
wx.navigateToMiniProgram({  
  appId:'wxa023b292fd19d41d', // 电子签小程序的appId  
  path:'pages/guide?from=SFY&to=CONTRACT_DETAIL&id=${flowId}&name=%E6%9D%A8%E5%B8%88&phone=MTc2MTI3Nzg1Mjk%3D', //${flowId}为流程 id，name、phone 按需给  
  envVersion:'release’,  
  success(res){
    // 打开成功 
  } 
})
```
path 里的参数（name，phone）均使用 `~${base64url(value)}` 统一编码。

### 客户 App 如何跳转到电子签小程序完成签署？  
1. Android App 请参见 [官方文档](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Launching_a_Mini_Program/Android_Development_example.html) 。 
2. iOS App 请参见 [官方文档](https://developers.weixin.qq.com/doc/oplatform/Mobile_App/Launching_a_Mini_Program/iOS_Development_example.html)  。
3. 所需参数：
电子签小程序 Appid：`wxa023b292fd19d41d`。
电子签小程序原始 ID：`gh_da88f6188665`。
电子签小程序合同详情页：`path：pages/guide?from=app&to=CONTRACT_DETAIL&id=${flowId}&name=&phone=`。

### 为什么客户在小程序中无法找到自己的合同？  
请确认客户有使用和发起时相同的姓名、手机号进行小程序登录。且在**个人中心** > **切换身份**确认已切换为签署时要求的身份。
<img style="width:500px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7b732d9eb1777f687dfdb2d189fc9f3a.png" />



## 接口报错相关
### 接口调用报错如何处理？  
您可以尝试按照接口返回的 message 的提示进行修改，或者记录下 requestId 并提供给对接人员进行处理。

### 接口调用返回签名错误？  
请先检查 SecretId 和 SecretKey 是否正确。如果您未使用 SDK 进行接入，请参见腾讯云官方 [开发指南](https://cloud.tencent.com/document/product/1278/46637) 中的样例代码进行签名计算。


## 静默签相关
### 如何发起静默签？  
1. 使用文件创建合同接入  
需要在 CreateFlowByFiles 接口传入 ApproverInfo 数组时，设置签署者的 ApproverType 为3。注意目前仅支持发起者（企业方）进行静默签署。  
2. 使用模板创建合同接入  
登录 [腾讯电子签控制台](https://ess.tencent.cn/template-mgr)，进入**模板管理**，在编辑或者新增模板**配置模板信息**步骤中设置己方签署方式为“自动签署”，完成后保存模板并以此模板 ID 重新发起合同。  
![](https://qcloudimg.tencent-cloud.cn/raw/2fadd416c6b2bf438dde208769c65f23.png)

### 能够让非发起方企业进行静默签么？  
静默签署需要控制对应企业的印章，且签署具有法律效益，故业务上仅允许发起方企业控制己方进行静默签署。


## 回调相关
### 回调地址如何配置？  
如您需要开通此功能，需提供回调地址 CallbackUrl，由对接人在后台设置好回调地址后即可接收回调通知，并返回 CallbackUrlKey 给您用于解密，请确保 CallbackUrl 可公网访问并正常处理回调通知。电子签会在合同状态产生变化时向该地址发送通知。

### 回调数据如何解密？  
腾讯电子签回调开发者回调接口传入的参数为加密的数据，开发者需要使用腾讯电子签提供的 CallbackUrlKey 来解密数据。
解密步骤如下：  
1. 对收到的数据进行 Base64 解码得到密文。  
2. 对密文进行对称解密，密钥为腾讯电子签提供的 CallbackUrlKey，数据采用 PKCS#7 填充。  
3. 解密得到的数据为输入参数的 Json 格式。

### 回调数据有哪些参数呢？  
- **回调数据对象 FlowInfo 结构**：
<table>
   <tr>
      <th width="0px" >参数名称</td>
      <th width="0px" >类型</td>
      <th width="0px">描述</td>
   </tr>
   <tr>
      <td>FlowId</td>
      <td>string</td>
      <td>流程编号。</td>
   </tr>
   <tr>
      <td>DocumentId</td>
      <td>string</td>
      <td>使用的文档 ID。</td>
   </tr>
   <tr>
      <td>CallbackType</td>
      <td>string</td>
      <td>回调的类型： <br>sign：签署回调 <br>review：审核回调</td>
   </tr>
   <tr>
      <td>FlowName</td>
      <td>string</td>
      <td>流程名称。</td>
   </tr>
   <tr>
      <td>FlowType</td>
      <td>string</td>
      <td>流程的类型。</td>
   </tr>
   <tr>
      <td>FlowDescription</td>
      <td>string</td>
      <td>流程的描述。</td>
   </tr>
   <tr>
      <td>Unordered</td>
      <td>bool</td>
      <td>流程类型顺序：<br> true：为无序<br> false：为有序</td>
   </tr>
   <tr>
      <td>CreateOn</td>
      <td>int</td>
      <td>流程的创建时间戳。</td>
   </tr>
   <tr>
      <td>UpdatedOn</td>
      <td>int</td>
      <td>流程的修改时间戳。</td>
   </tr>
   <tr>
      <td>DeadLine</td>
      <td>int</td>
      <td>流程的过期时间0为永远不过期。</td>
   </tr>
   <tr>
      <td>FlowCallbackStatus</td>
      <td>int</td>
      <td>流程现在的状态：<br>1：待签署 <br>2：部分签署 <br>3：已拒签 <br>4：已签署 <br>5：已过期 <br>6：已撤销</td>
   </tr>
   <tr>
      <td>UserId</td>
      <td>string</td>
      <td>本环节需要操作人 UserId。</td>
   </tr>
   <tr>
      <td>RecipientId</td>
      <td>string</td>
      <td>签署区 ID。</td>
   </tr>
   <tr>
      <td>Operate</td>
      <td>string</td>
      <td>动作：<br>start：发起 <br>sign：签署 <br>reject：拒签 <br>cancel：取消 <br>finish：结束 <br>deadline：过期</td>
   </tr>
   <tr>
      <td>UserData</td>
      <td>string</td>
      <td>创建的时候设置的透传字段。</td>
   </tr>
   <tr>
      <td>Approvers</td>
      <td>Approver 数组</td>
      <td>流程签约方列表。</td>
   </tr>
</table>
  
- **FlowInfo 参数 Approver 结构**：
<table>
   <tr>
      <th width="0px" >参数名称</td>
      <th width="0px" >类型</td>
      <th width="0px">描述</td>
   </tr>
   <tr>
      <td>UserId</td>
      <td>string</td>
      <td>本环节需要操作人的 UserId。</td>
   </tr>
   <tr>
      <td>RecipientId</td>
      <td>string</td>
      <td>签署区 ID。</td>
   </tr>
   <tr>
      <td>ApproverType</td>
      <td>int</td>
      <td>参与者类型： <br>0：企业<br>1：个人<br>3：企业静默签署</td>
   </tr>
   <tr>
      <td>OrganizationName</td>
      <td>string</td>
      <td>企业或者个人的名字。</td>
   </tr>
   <tr>
      <td>Required</td>
      <td>bool</td>
      <td>是否需要签名。</td>
   </tr>
   <tr>
      <td>ApproverName</td>
      <td>string</td>
      <td>本环节需要操作人的名字。</td>
   </tr>
   <tr>
      <td>ApproverMobile</td>
      <td>string</td>
      <td>本环节需要操作人的手机号。</td>
   </tr>
   <tr>
      <td>ApproverIdCardType</td>
      <td>string</td>
      <td>签署人证件类型：<br>ID_CARD：身份证。 <br>HONGKONG_AND_MACAO：港澳居民来往内地通行证。<br> HONGKONG_MACAO_AND_TAIWAN：港澳台居民居住证(格式同居民身份证)。</td>
   </tr>
   <tr>
      <td>ApproverIdCardNumber</td>
      <td>string</td>
      <td>签署人证件类型。</td>
   </tr>
   <tr>
      <td>ApproveCallbackStatus</td>
      <td>int</td>
      <td>签署状态：<br>2：待签署 <br>3：已签署 <br>4：已拒签 <br>5：已过期 <br>6：已撤销</td>
   </tr>
   <tr>
      <td>ApproveMessage</td>
      <td>string</td>
      <td>拒签的原因。</td>
   </tr>
   <tr>
      <td>VerifyChannel</td>
      <td>string</td>
      <td>签署意愿方式，WEIXINAPP：人脸识别。</td>
   </tr>
   <tr>
      <td>ApproveTime</td>
      <td>int</td>
      <td>签约的时间。</td>
</table>

### 回调地址是否支持同时配置多个？  
支持，回调地址可以同时存在多个，您可以提供需要配置的回调地址给对接人员进行配置，根据您的需求不同的地址可以配置相同或者不同的 CallbackUrlKey。

### 回调地址是否支持更改或删除？  
支持，您可以提供需要删除的回调地址给对接人员进行对应操作。

### 回调地址配置后多长时间生效呢？  
配置完成后立即生效，以对接人员通知您配置完成的时间为准。

### 为什么客户收到 FlowCallbackStatus 为4（已签署）的回调通知后，又收到了 FlowCallbackStatus 为1（待签署）的通知？  
以单方签署的合同为例，FlowCallbackStatus 状态变化一般是由1变为4。少量回调可能因状态变化间隔比较短、重发、或者网络传输等原因，小几率出现到达顺序不一致，建议开发者从代码层面进行适当控制，例如状态更新为4后不能再更新为1。


## 短信相关
### 为什么客户收不到短信通知？  
根据签署类型，可以分为个人签署用户和企业签署用户。如果为个人签署用户，建议先引导客户查看手机拦截记录，检查短信是否被拦截；如果为企业签署用户，电子签目前默认对企业签署方不发送短信通知，如果您有此需求可以联系我们的对接人员进行配置。具体原因以对接人员的最终排查结果为准。


## 印章相关
### 如何查看印章审核状态？  
请登录 [腾讯电子签控制台](https://ess.tencent.cn/seal-mgr) ，访问**印章管理**单击**印章详情**对印章审核状态进行查看。

### 为什么印章审核通不过？  
请确认印章为非绘制印章，且在图片中清晰完整。目前电子签提供以下生成印章的方式：  
- 新建印章时，选择**模板印章**的创建方式，即可自动生成企业电子印章。  
- 上传印章前在白纸上清晰盖章后拍照，确保印章在图片中清晰完整，在新建印章时，选择**本地上传**并上传图片。  

请确保印章有按照以上方生成。具体失败原因以审核人提供的拒绝理由为准。

### 创建流程提示“无权限操作该印章”?  
请登录 [腾讯电子签控制台](https://ess.tencent.cn/seal-mgr) ，访问**印章管理**单击**印章详情**确认已添加用户为印章持有人，只有持有人才拥有印章使用权限。


## PDF 相关
### 如何计算 PDF 签名位置？  
以 Adobe 阅读器为例：
1. 单击**准备表单**。
<img style="width:400px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7ea2975a0c3ecc619247a40aea69e562.png" />
2. 单击**添加文本域**。
<img style="width:800px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/15a369537e611233f041055b565fcd27.png" />
>!此处仅做定位使用。
3. 单击**文本域属性** > **位置**，单位选点。
![](https://qcloudimg.tencent-cloud.cn/raw/32aaa5fbba148e5c1ffb3928c338bb34.png)
>!此时下方位置显示坐标值，注意此坐标值以页面左下角为原点。
4. 坐标计算  
ComponentPosX = 左对齐坐标39.4847 
ComponentPosY = 页面高度 - 上对齐坐标37.3135  
页面高度获取：可先将控件移至页面顶部，此时上对齐坐标值即为页面高度。
