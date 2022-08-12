## 接入前常见问题
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

### JDK1.7 使用 sdk 调用上传文件接口报 javax.net.ssl.SSLException-Received fatal alert: protocol_version？
JDK1.7 默认使用 TLSv1.0，需要强制设置成 TLSv1.2，官方使用的 HTTP 客户端是 okhttp，需要自行修改官网 SDK 源码。
在 com.tencentcloudapi.common.http.HttpConnection 类中修改构造函数如下：
```
 public HttpConnection(Integer connTimeout, Integer readTimeout, Integer writeTimeout) {
    this.client = new OkHttpClient();
    SSLContext sslContext = null; //这边指定tls版本
    try {
        sslContext = SSLContext.getInstance("TLSv1.2");
        sslContext.init(null, null,null);
    } catch (Exception e) {
        e.printStackTrace();
        throw new RuntimeException(e.getMessage());
    }
    SSLSocketFactory factory = sslContext.getSocketFactory();
    this.client.setSslSocketFactory(factory);
    this.client.setConnectTimeout(connTimeout, TimeUnit.SECONDS);
    this.client.setReadTimeout(readTimeout, TimeUnit.SECONDS);
    this.client.setWriteTimeout(writeTimeout, TimeUnit.SECONDS);
  }
```

## 小程序相关
### 客户小程序如何跳转到电子签小程序完成签署？  
请参见小程序 [官方文档](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html) 。小程序支持直接跳转到签署页面，完成签署后可返回客户小程序。可参见以下代码：  
正式环境：
```plaintext
wx.navigateToMiniProgram({  
  appId:'wxa023b292fd19d41d', // 电子签小程序的appId  
  path:'pages/guide?from=SFY&to=CONTRACT_DETAIL&id=${flowId}&name=%E6%9D%A8%E5%B8%88&phone=MTc2MTI3Nzg1Mjk%3D', //${flowId}为流程 id，name、phone 按需给  
  envVersion:'release’,  
  success(res){
    // 打开成功 
  } 
})
```
测试环境：
```plaintext
wx.navigateToMiniProgram({  
  appId:'wx371151823f6f3edf', // 电子签小程序的appId  
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
 - 正式环境：
电子签小程序 Appid：wxa023b292fd19d41d。
电子签小程序原始 ID：gh_da88f6188665。
电子签小程序合同详情页：path：pages/guide?from=app&to=CONTRACT_DETAIL&id=${flowId}&name=&phone=。
 - 测试环境：
电子签小程序 Appid：wx371151823f6f3edf。
电子签小程序原始 ID：gh_39a5d3de69fa。
电子签小程序合同详情页：path：pages/guide?from=app&to=CONTRACT_DETAIL&id=${flowId}&name=&phone=。

### 为什么客户在小程序中无法找到自己的合同？  
请确认客户有使用和发起时相同的姓名、手机号进行小程序登录。且在**个人中心** > **切换身份**确认已切换为签署时要求的身份。
<img style="width:500px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/7b732d9eb1777f687dfdb2d189fc9f3a.png" />

### 如何选择通过全屏或半屏方式打开电子签小程序？
可参见微信官方文档：
- [全屏方式](https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html)
- [半屏方式](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html)

### 如何配置跳转至电子签小程序的不同页面？
请参见以下表格及说明：
#### 参数说明
下表描述的是外部小程序拉起电子签小程序首页、列表页、个人中心页、合同封面页、合同详情页的参数配置。

| 参数 | 类型 | 默认值 |必填 |描述 |
|---------|---------|---------|---------|---------|
| path | string | - |是 |目标页面路由。 |
| login | number | 0 |否 |是否需要登录。 |
| verify | number | 0 |否 |是否需要实名。 |
| accountType | string |- | 否 |personal：切换个人身份。 |
| userIds | string | - |否 |如果该链接目标用户只有一个人使用，则直接取该用户的 userId；如果该链接目标用户多人使用，可以将 userId1，userId2 这样赋值：[userId1，userId2]。 |
| organizationId | string | - |否 |企业账号的企业 ID，如果添加此参数则还要同步携带 orgName。 |
| orgName | string | - |否 |企业账号的名称，如果添加 organizationId 则还要同步携带此参数。 |
| id | string | - |否 |合同 ID，如果是到合同封面页或者合同详情页，此参数必填。 |
| channel | string | - |否 |其他小程序渠道的标记，方便统计使用。 |
| quickSponsor   | string | false  | 否   | 到首页是否需要立即拉起快速发起合同弹框。<br>true：出现快速发起弹框。 <br>false：不出现。     |

#### 首页
##### C 端用户进入首页
```josn
- pages/guide/index?path=/pages/home/home-index&accountType=personal&channel=${channel}
```

##### C 端用户进入首页-快速发起合同
```josn
- pages/guide/index?path=/pages/home/home-index&login=1&accountType=personal&channel=${channel}&quickSponsor=true
```

###### B 端用户进入首页
进入 B 端首页必须已登录已实名，可指定用户的 userIds 合集，或者 organizationId（指定了 organizationId，则需要同步携带 orgName
以下两种方式均可：
```josn
- pages/guide/index?path=/pages/home/home-index&login=1&verify=1&userIds=${userIds}&channel=${channel}
- pages/guide/index?path=/pages/home/home-index&login=1&verify=1&organizationId=${organizationId}&orgName=${orgName}&channel=${channel}
```

###### B 端用户进入首页-快速发起合同
```josn
- pages/guide/index?path=/pages/home/home-index&login=1&verify=1&userIds=${userIds}&channel=${channel}&quickSponsor=true
- pages/guide/index?path=/pages/home/home-index&login=1&verify=1&organizationId=${organizationId}&orgName=${orgName}&channel=${channel}&quickSponsor=true
```

#### 列表页
##### C 端进入用户列表页
```josn
- pages/guide/index?path=/pages/home/home-list&login=1&verify=1&accountType=personal&channel=${channel}
```

##### B 端进入用户列表页
进入 B 端首页必须已登录已实名，可指定用户的 userIds 合集，或者 organizationId（指定了 organizationId，则需要同步携带 orgName。）。
以下两种方式均可：
```josn
- pages/guide/index?path=/pages/home/home-list&login=1&verify=1&userIds=${userIds}&channel=${channel}
- pages/guide/index?path=/pages/home/home-list&login=1&verify=1&organizationId=${organizationId}&orgName=${orgName}&channel=${channel}
```

#### 个人中心
##### C 端进入用户个人中心
```josn
- pages/guide/index?path=/pages/home/home-user&accountType=personal&channel=${channel}
```

##### B 端进入用户个人中心
进入 B 端首页必须已登录已实名，可指定用户的 userIds 合集，或者 organizationId（指定了 organizationId，则需要同步携带 orgName。）。
以下两种方式均可：
```josn
- pages/guide/index?path=/pages/home/home-user&login=1&verify=1&userIds=${userIds}&channel=${channel}
- pages/guide/index?path=/pages/home/home-user&login=1&verify=1&organizationId=${organizationId}&orgName=${orgName}&channel=${channel}
```

#### 合同封面页
##### C 端用户进入合同封面页或 B 端用户合同封面页
未登录或者未实名的用户也可进入到合同封面页，切换到个人身份可以使用两种方式，使用 accountType=personal，或者使用 userIds 赋值个人身份的 userId。
```josn
- pages/guide/index?path=/pages/mvp/contract-preview&accountType=personal&id=${id}&channel=${channel}
- pages/guide/index?path=/pages/mvp/contract-preview&userIds=${userIds}&id=${id}&channel=${channel}
```

#### 合同详情页
无论是 C 端还是 B 端，进入合同详情页均必须已登录已实名。
##### C 端进入合同详情页
以下方式进入：
- 可以设置 accountType=personal 进入。
- 也可指定 C 端用户的个人身份的 userId。
```josn
- pages/guide/index?path=/pages/contracts/contract-detail&login=1&verify=1&id=${id}&accountType=personal&channel=${channel}
- pages/guide/index?path=/pages/contracts/contract-detail&login=1&verify=1&id=${id}&userIds=${userIds}&channel=${channel}
```

>!
>- 如果 B2C 合同发起，对方签署方 C 是新用户，则 C 没有 userId，可指定参数 accountType=personal。
>- 如果 B2C 合同发起，对方签署方 C 是老用户，则以上两种方式均可。

##### B 端进入合同详情页
可指定用户的 userIds 合集，或者 organizationId（指定了organizationId，则需要同步携带 orgName。）。
- 以下两种常用方式均可：
```josn
 - pages/guide/index?path=/pages/contracts/contract-detail&login=1&verify=1&id=${id}&userIds=${userIds}&channel=${channel}
 - pages/guide/index?path=/pages/contracts/contract-detail&login=1&verify=1&id=${id}&organizationId=${organizationId}&orgName=${orgName}&channel=${channel}
```
- 特殊情形：
```josn
- pages/guide/index?path=/pages/contracts/contract-detail&login=1&verify=1&id=${id}&accountType=personal&channel=${channel}
```

>!
>- 如果 B2B 合同发起，对方签署方 B 所在的企业没有注册，那么使用特殊情形，切换到个人身份可查看合同，合同详情页会引导用户申请企业注册。
>- 如果 B2B 合同发起，对方签署方 B 没有加入该企业，那么使用特殊情形，切换到个人身份可查看合同，合同详情页会引导用户申请加入企业。
>- 如果 B2B 合同发起，对方签署方 B 是该企业的员工，那么以上两种常用方式均可使用。


## 接口报错相关
### 接口调用报错如何处理？  
您可以尝试按照接口返回的 message 的提示进行修改，或者记录下 requestId 并提供给对接人员进行处理。

### 接口调用返回签名错误？  
请先检查 SecretId 和 SecretKey 是否正确。如果您未使用 SDK 进行接入，请参见腾讯云官方 [开发指南](https://cloud.tencent.com/document/product/1278/46637) 中的样例代码进行签名计算。

### StartFlow（发起流程）接口报错，提示“文档不可用”？
在调用 CreateDocument 接口后，需要等待文档的异步合成，所以不能立即调用 StartFlow 接口；如果调用 StartFlow 报错，可以尝试等待后重试。

### CreateDocument（创建电子文档）接口报错，提示“流程已关联文档”？
每个流程有且仅有一次能用于绑定文档，请重新使用 CreateFlow 接口创建新的流程。

## 静默签相关
### 如何发起静默签？  
1. 使用文件创建合同接入  
需要在 CreateFlowByFiles 接口传入 ApproverInfo 数组时，设置签署者的 ApproverType 为3。注意目前仅支持发起者（企业方）进行静默签署。  
2. 使用模板创建合同接入  
登录 [腾讯电子签控制台](https://ess.tencent.cn/template-mgr)，进入**模板管理**，在编辑或者新增模板**配置模板信息**步骤中设置己方签署方式为“自动签署”，完成后保存模板并以此模板 ID 重新发起合同。  
![](https://qcloudimg.tencent-cloud.cn/raw/2fadd416c6b2bf438dde208769c65f23.png)

### 能够让非发起方企业进行静默签么？  
静默签署需要控制对应企业的印章，且签署具有法律效益，故业务上仅允许发起方企业控制己方进行静默签署。

### 使用静默签时为什么不能给签署方添加填写控件?
企业静默签在发起时，需要保证合同内容的完整，所以发起后，签署方不能进行随意填写。

## 回调相关
### 回调地址如何配置？  
如您需要开通此功能，需提供回调地址 CallbackUrl，由对接人在后台设置好回调地址后即可接收回调通知，并返回 CallbackUrlKey 给您用于解密，请确保 CallbackUrl 可公网访问并正常处理回调通知。电子签会在合同状态产生变化时向该地址发送通知。

### 回调数据如何解密？  
腾讯电子签回调开发者回调接口传入的参数为加密的数据，开发者需要使用腾讯电子签提供的 CallbackUrlKey 来解密数据。
解密步骤如下：  
1. 对收到的数据进行 Base64 解码得到密文。  
2. 对密文进行对称解密，算法为 AES-256-CBC，密钥为腾讯电子签提供的 CallbackUrlKey，IV 取 CallbackUrlKey 值的前16位，数据采用 PKCS#7 填充。  
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

### 回调样例
回调请求包：
```plaintext
POST /callback HTTP/1.1
Host: www.esstest.com
User-Agent: Go-http-client/1.1
Content-Length: 1088
Content-Type: text/plain
Accept-Encoding: gzip

YyYyLZonMceFMFFi5jRnnOWrOasvzmKtGAvRPq1IzuYma88UvTqyZy8QpNVMKxvJY3Sp+NJW6mgTfU35u7SbUon+QCjul1P9P6mcVRuVvYrM2DoFBDgjLURfX+CWnZ9m967nNqiubw9vj9ToysJDZyr0zo4NN1CCfvsyxnVNKhSNbRAy74x4SlLscZ/wcFwdy55S2rBxbjLCqViIj6llQFo74mLHJ8oumngBD1WJZ5ginDNEScPB7+cIHeKF5w3UvUpDqDIUjAj7KFUmIQM8/zY8EafhgCNhWRaGxuFxGF+iMqwC+HJYosbBmrKZ44+8xwL5WlXLx/Cf8bK7J4mJIWbKyul8PBE9Xh8lL/d0Ufnf4sUB0ypbdy/KIr+XQJgFjR2AQGENXvxxlCfdVY5svGfXYaaSSyDND1u9C8kMxQRfNHJye7ulTprROYTtq4GJ8UJQbJbuHvTcppGyMbGO2AvgXcoSogM0JuZzLK/gcPFIWIf9oFTg47M62sLf9YY7UASVITfA5LnE+/1clN4vn748wjS4tdxCL8wjWanPOONTPCMrwH0wsZ86xEf7aLl0/qBWGF13VYh4C4XgiDLtaOs6DdlzMz5EszWISpRRzfJLxcBnhHL9sQu7YWLZzRL6vmP1qtdWZbUYt4Z/eKff5gfmmDGHOxVjd3XhxhfHSdW3a8LzlMT3n69CPBEiOjXA4abshkiT6+hOlJ8uCws+ja2BSmwruqpUn4tq7Je91cT0AhGHuvq9s1VCB7vw8KsVimRHrC6eOa1rgm6qgQNP0fMgGRe+qu4BtfND1a/j9BBuIHQSjLSn2JB2P/EAvbb5J2iPVZj3SppgzhwVCgYUu+osA3LNC4NsYxm/yMs8mq7nOCIZd6D/BM9py5WKS6//e4mM6sY3/S2wOr8snkUsEuu5M35zyRcrCjIaRzV9OKZjP+aqkk2GcF/Figd3N/zCZ+WjC+L9r/ELHn64qEJxZDvXKXVE3dUOchbUPelCb3YO+Mub+76bnvt8IQ2MRf9NaFO7cWlh9mDWkZMXxmOTlxOxQtOeTrW+QywTkZaDGkP83HRjqXd7bn3YBcdFiOy/
```
此处使用 CallbackUrlKey:"TencentEssEncryptTestKey12345678" 解密后可获取以下明文：
>!该 CallbackUrlKey 仅用于此处测试样例。

```plaintext
{
  "FlowId": "yDRtrAAAAAAAAAAAAAAAAAAAAAAAAAAA",
  "DocumentId": "yDRtrBBBBBBBBBBBBBBBBBBBBBBBBBB",
  "CallbackType": "sign",
  "FlowName": "测试流程",
  "FlowDescription": "",
  "FlowType": "",
  "FlowCallbackStatus": 4,
  "Unordered": true,
  "CreateOn": 1658892449,
  "UpdatedOn": 1659604019,
  "DeadLine": 1661615999,
  "UserId": "",
  "RecipientId": "yDRtrCCCCCCCCCCCCCCCCCCCCCCCCCCC",
  "Operate": "sign",
  "UserData": "",
  "Approvers": [
    {
      "UserId": "yDRtrDDDDDDDDDDDDDDDDDDDDDDDDDDD",
      "RecipientId": "yDRtrCCCCCCCCCCCCCCCCCCCCCCCCCCC",
      "ApproverType": 1,
      "OrganizationName": "",
      "Required": true,
      "ApproverName": "张三",
      "ApproverMobile": "15912345678",
      "ApproverIdCardType": "ID_CARD",
      "ApproverIdCardNumber": "440300200101010001",
      "ApproveCallbackStatus": 3,
      "ApproveMessage": "",
      "ApproveTime": 1659604019,
      "VerifyChannel": "WEIXINAPP"
    }
  ],
  "CallbackUrl": "https://www.esstest.com"
}
```

### 回调解密 demo
<dx-tabs>
::: Java
```plaintext
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.Base64;


public class CallbackAes {

    public static byte[] pkcs7Padding(byte[] ciphertext, int blockSize) {
        int padding = blockSize - ciphertext.length % blockSize;
        byte[] padtext = repeat((byte) padding, padding);
        ciphertext = append(ciphertext, padtext);
        return ciphertext;
    }

    public static byte[] repeat(byte val, int count) {
        byte[] result = new byte[count];
        for (int i = 0; i < count; i++) {
            result[i] = val;
        }
        return result;
    }

    public static byte[] append(byte[] a, byte[] b) {
        byte[] result = new byte[a.length + b.length];
        System.arraycopy(a, 0, result, 0, a.length);
        System.arraycopy(b, 0, result, a.length, b.length);
        return result;
    }

    public static byte[] pkcs7UnPadding(byte[] origData) {
        int length = origData.length;
        int unpadding = origData[length - 1];
        byte[] result = new byte[length - unpadding];
        System.arraycopy(origData, 0, result, 0, result.length);
        return result;
    }

    public static byte[] aesEncrypt(byte[] origData, byte[] key) throws Exception {
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
        int blockSize = cipher.getBlockSize();
        origData = pkcs7Padding(origData, blockSize);
        SecretKeySpec keyspec = new SecretKeySpec(key, "AES");
        byte[] iv = new byte[blockSize];
        System.arraycopy(key, 0, iv, 0, iv.length);
        IvParameterSpec ivspec = new IvParameterSpec(iv);
        cipher.init(Cipher.ENCRYPT_MODE, keyspec, ivspec);
        byte[] encrypted = cipher.doFinal(origData);
        return Base64.getEncoder().encode(encrypted);
    }

    public static byte[] aesDecrypt(byte[] crypted, byte[] key) throws Exception {
        byte[] decoded = Base64.getDecoder().decode(crypted);
        Cipher cipher = Cipher.getInstance("AES/CBC/NoPadding");
        int blockSize = cipher.getBlockSize();
        SecretKeySpec keyspec = new SecretKeySpec(key, "AES");
        byte[] iv = new byte[blockSize];
        System.arraycopy(key, 0, iv, 0, iv.length);
        IvParameterSpec ivspec = new IvParameterSpec(iv);
        cipher.init(Cipher.DECRYPT_MODE, keyspec, ivspec);
        byte[] origData = cipher.doFinal(decoded);
        return pkcs7UnPadding(origData);
    }

    public static void main(String[] args) throws Exception {
        // 传入CallbackUrlKey
        byte[] key = "***************".getBytes();
        // 传入密文
        byte[] origData = aesDecrypt("****************".getBytes(StandardCharsets.UTF_8), key);
        // 打印解密后的内容，格式为json
        System.out.println(new String(origData, StandardCharsets.UTF_8));
    }
}
```
:::
::: PHP
```plaintext
<?php
require_once __DIR__.'/../../../vendor/autoload.php';

class Aes
{
    public $key = '';
    public $iv = '';

    public function __construct($config)
    {
        foreach($config as $k => $v){
            $this->$k = $v;
        }
    }

    //解密
    public function aesDe($data){
        return openssl_decrypt(base64_decode($data),  $this->method, $this->key, OPENSSL_RAW_DATA, $this->key);
    }
}

$config = [
    'key' =>  '********************', // 此处填入CallbackUrlKey
    'method'  => 'AES-256-CBC' //加密方式
];

$obj = new Aes($config);

// 此处填入收到的密文
$data = '*****************************';

echo $obj->aesDe($data);//解密

```
:::
::: Golang
```plaintext
package v20201111

import (
	"crypto/aes"
	"crypto/cipher"
	"encoding/base64"
	"fmt"
	"testing"
)

func AesDecrypt(crypted, key []byte) ([]byte, error) {
	block, err := aes.NewCipher(key)
	if err != nil {
		return nil, err
	}
	blockSize := block.BlockSize()
	blockMode := cipher.NewCBCDecrypter(block, key[:blockSize])
	origData := make([]byte, len(crypted))
	blockMode.CryptBlocks(origData, crypted)
	origData = PKCS7UnPadding(origData)
	return origData, nil
}

// PKCS7UnPadding 去除填充
func PKCS7UnPadding(origData []byte) []byte {
	length := len(origData)
	unPadding := int(origData[length-1])
	return origData[:(length - unPadding)]
}

func TestDecrypt(t *testing.T) {
	// 传入CallbackUrlKey
	key := "***********"
	// 传入密文
	content := "***********"

	// base64解密
	crypted, err := base64.StdEncoding.DecodeString(content)
	if err != nil {
		fmt.Printf("base64 DecodeString returned: %s", err)
		return
	}

	origData, err := AesDecrypt(crypted, []byte(key))
	if err != nil {
		fmt.Printf("AesDecrypt returned: %s", err)
		return
	}
	fmt.Printf("%s", string(origData))
}
```
:::
::: Python
```plaintext
# -*- coding: utf-8 -*-
import base64

from Cryptodome.Cipher import AES


def decode_aes256(data, encryption_key):
    iv = encryption_key[0:16]
    aes = AES.new(encryption_key, AES.MODE_CBC, iv)
    d = aes.decrypt(data)
    unpad = lambda s: s[0:-ord(d[-1:])]
    return unpad(d)

# 此处传入密文
data = '**************************************************'
data = base64.b64decode(data)
# 此处传入CallbackUrlKey
e = decode_aes256(data, bytes('**************************************************', encoding="utf8"))
print(type(e))
print(str(e, encoding="utf8"))
```
:::
::: C#
```plaintext
using System;
using System.Security.Cryptography;
using System.Text;
namespace TencentCloudExamples
{

    class EssCallback
    {

        static void Main1(string[] args)
        {
            try
            {
                // 传入CallbackUrlKey
                String key = "*************";
                // 传入密文
                String content = ""*************";";

                String plaintext = AESDecrypt(content, Encoding.ASCII.GetBytes(key));

                Console.WriteLine(plaintext);
            }
            catch (Exception e)
            {
                Console.WriteLine(e.ToString());
            }
            Console.Read();

        }

        public static string AESDecrypt(string encryptStr, byte[] key)
        {
            byte[] toEncryptArray = Convert.FromBase64String(encryptStr);
            RijndaelManaged rDel = new RijndaelManaged();
            rDel.Key = key;
            byte[] iv = new byte[16];
            Array.Copy(key, iv, iv.Length);
            rDel.IV = iv;
            rDel.Mode = CipherMode.CBC;
            rDel.Padding = PaddingMode.PKCS7;
            ICryptoTransform cTransform = rDel.CreateDecryptor();
            byte[] resultArray = cTransform.TransformFinalBlock(toEncryptArray, 0, toEncryptArray.Length);
            return UTF8Encoding.UTF8.GetString(resultArray);
        }

    }

}
```
:::
</dx-tabs>


## 短信相关
### 为什么客户收不到短信通知？  
根据签署类型，可以分为个人签署用户和企业签署用户。如果为个人签署用户，建议先引导客户查看手机拦截记录，检查短信是否被拦截；如果为企业签署用户，电子签目前默认对企业签署方不发送短信通知，如果您有此需求可以联系我们的对接人员进行配置。具体原因以对接人员的最终排查结果为准。

### 如何在发起流程时不对签署方发送短信?
在调用 CreateFlowByFiles 或者 CreateFlow 接口时，签署人信息设置 NotifyType 参数为“none”。

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

## 合规相关
### 合同签署后是否能作废？
如果所有用户均已签署则合同不能作废（撤回）。

### 电子签支持哪些类型的证件呢？
目前电子签支持的证件类型有：身份证、港澳居民来往内地通行证、港澳台居民居住证(格式同居民身份证)。

### 电子签支持哪些意愿认证渠道呢？
目前主要使用人脸识别进行意愿认证，暂不支持其他方式。

### 使用 WPS 打开签署后的文件，签名属性显示“签名无效或文档自签名以来已被修改”？
使用 WPS 打开 PDF 文件时会直接进入编辑状态，因此会显示文件已被修改。

## 控件相关
### 在调用 CreateFlowByFiles（用PDF文件创建签署流程）时，经办人内容控件中 ComponentName 是否为必传值？
ComponentId 和 ComponentName 选择传入一项即可，此处建议传入 ComponentName。


### 在调用CreateFlowByFiles（用 PDF 文件创建签署流程）时，如何获取经办人内容控件中 ComponentName 值？
在 [腾讯电子签控制台](https://ess.tencent.cn/template-mgr)  进行模板新建或者编辑时，于**指定签约区域**步骤，可以查看控件属性，属性值“控件名称”即为 ComponentName 值。
![](https://qcloudimg.tencent-cloud.cn/raw/159d8b245586f902cffd293a4a281cee.png)


### 在调用 CreateFlowByFiles（用PDF文件创建签署流程）接口时，签署者信息入参 SignComponents，能否支持传入填写控件和签署控件两种？
此处只能传入签署控件，如果需要为签署者添加填写控件，请使用模板发起流程。


### 控件如何进行关键字定位？
Component 入参时，GenerateMode 参数选择填入 KEYWORD，并使用 ComponentId 指定关键字。


### 关键字定位如何调整控件位置？
使用关键字定位时，控件区域的左上角和关键字区域的左上角为重叠关系，可以通过 Component 的入参 OffsetX以及OffsetY 来完成控件在横纵坐标上的偏移。


### 控件如何进行表单域定位？
Component 入参时，GenerateMode 参数选择填入 FIELD，并使用 ComponentName 指定关键字。


