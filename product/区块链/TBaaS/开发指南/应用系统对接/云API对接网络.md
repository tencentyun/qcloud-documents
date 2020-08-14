# 云API对接网络

腾讯云为使用云API提供了各种语言的sdk，应用系统需要根据语言集成SDK。SDK的集成方法参考对应的链接。（目前Go SDK支持的请求类型较丰富）

- [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
- [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
- [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
- [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
- [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
- [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)

SDK的使用流程如下图所示

<img src="https://main.qcloudimg.com/raw/3abf6af1b8f0f1096619fa0945a3d789.png" alt="img" style="zoom: 33%;" />            

下面将先介绍如何获取云API调用合约需要的关键参数，并以Java和Go为例介绍SDK的使用方法。

## 获取账户信息

使用云API调用合约时除了需要网络、合约的相关参数，还需要提供购买TBaaS节点的账户信息，包括**SecretId**和**SecretKey**。在腾讯云登录账号后按照如下图所示的步骤获取SecretId和SecretKey。

<img src="https://main.qcloudimg.com/raw/53e9d7b00ac4c0a8e6ddf1abb5f7b4e8.png" alt="img" style="zoom:50%;" /> 

 <img src="https://main.qcloudimg.com/raw/39e2268db4612847e6f785ec62c6eb0e.png" alt="img" style="zoom:50%;" />     

如果当前账户没有密钥，可新建。

<img src="https://main.qcloudimg.com/raw/abadb98d1a60a72f124b0a9da32c16f8.png" alt="img" style="zoom:100%;" />            

## 调用合约

### Java

Java SDK集成方法：[Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)

下面的代码段主要用于说明不同步骤的代码编写，如需运行，需要将不同步骤的代码按照Java语言要求整合。

1. 导入基础包，并配置参数

```java
import com.tencentcloudapi.common.Credential;
import com.tencentcloudapi.common.exception.TencentCloudSDKException;
import com.tencentcloudapi.common.profile.ClientProfile;
import com.tencentcloudapi.tbaas.v20180416.TbaasClient;
import com.tencentcloudapi.tbaas.v20180416.models.*;

// 通道名称
private static final String CHANNEL_NAME = "";
// 智能合约名称
private static final String CHAINCODE_NAME = "";
// 区块链网络ID
private static final String CLUSTER_ID = "";
// 组织名称
private static final String ORG_NAME = "";
// 调用模块名称
private static final String MODULE_NAME = "";
// 节点名称
private static final String PEER_NAME = "";

private static final String SECRET_ID = "";
private static final String SECRET_KEY = "";

private static final String REGIION = "";
```

2. 创建用户

```java
// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
Credential cred = new Credential(SECRET_ID, SECRET_KEY);

ClientProfile clientProfile = new ClientProfile();
clientProfile.setSignMethod(ClientProfile.SIGN_TC3_256);
TbaasClient client = new TbaasClient(cred, REGIION, clientProfile);
```

3. 构造调用请求

SDK中根据不同请求类型提供了6种Request结构体，定义在包com.tencentcloudapi.tbaas.v20180416.models中，每种XxxRequest都有对应的发送请求接口以及XxxResponse。其中字段Opeartion和Module的取值需要参考对应的类定义。

```java
private static InvokeRequest getInvokeRequest() {
    InvokeRequest invokeRequest = new InvokeRequest();
    invokeRequest.setChannelName(CHANNEL_NAME);
    invokeRequest.setChaincodeName(CHAINCODE_NAME);
    invokeRequest.setClusterId(CLUSTER_ID);
    invokeRequest.setModule(MODULE_NAME);
    invokeRequest.setGroupName(ORG_NAME);
    PeerSet peerSet = new PeerSet();
    peerSet.setPeerName(PEER_NAME);
    peerSet.setOrgName(ORG_NAME);
    invokeRequest.setPeers(new PeerSet[] { peerSet });
    
    invokeRequest.setOperation("invoke");
    
    //被调用合约的方法名
    invokeRequest.setFuncName("write");
    return invokeRequest;
}
```

4. 处理请求结果

参考类定义使用对应的setter/getter方法取出属性即可。

### Go

Go SDK集成方法： [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)

1. 导入基础包，并配置参数

```go
import (
    "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
    "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
    tbaas "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tbaas/v20180416"
)

ChannelName:=   ""
ChaincodeName:= ""
ClusterID:=     ""
OrgName:=       ""
ModuleName:=    ""
PeerName:=      ""
SecretID:=      ""
SecretKey:=     ""
```

2. 创建用户

提供SecretID SecretKey和Region参数。

```go
credential := common.Credential{
    SecretId: SECRET_ID, 
    SecretKey: SECRET_KEY
    }
clientProfile := profile.NewClientProfile()
client, _ := tbaas.NewClient(
    &credential, "ap-guangzhou", clientProfile)
```

3. 构造调用请求

SDK中根据不同请求类型提供了18种Request结构体，定义在github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tbaas/v20180416/models.go文件中，每种XxxRequest都有对应的NewXxxRequest方法，需要使用该方法进行初始化，同时还有对应的发送请求接口以及XxxResponse。按照步骤1中的方法导入包后，可使用tbaas.NewXxxRequest()进行调用。

本节仅以InvokeRequest为例说明构造方法。

```go
//填写基本参数
invokeRequest := tbaas.NewInvokeRequest()
invokeRequest.ChaincodeName = &ChaincodeName
invokeRequest.ChannelName = &ChannelName
invokeRequest.ClusterId = &ClusterID
invokeRequest.GroupName = &OrgName
invokeRequest.Module = &ModuleName

peerSet := tbaas.PeerSet{
    PeerName: &PeerName,
    OrgName:  &OrgName,
}
invokeRequest.Peers = []*tbaas.PeerSet{&peerSet}

//不同类型的Request有对应的Operation参数值，
//具体值需要在SDK的tbaas/models.go中查看对应的结构体字段说明
operationInvoke = "invoke"
invokeRequest.Operation = &operationInvoke

//funcName为被调用的合约方法名
var funcName = "write"
invokeRequest.FuncName = &funcName

orderKey:=""
orderValue:=""
invokeRequest.Args = []*string{&orderKey, &orderValue}
```

4. 发送请求

```go
//不同类型的请求对应着不同的发送接口
//比如：InvokeRequest——Invoke
//GetTransactionDetailForUserRequest
//            ——GetTransactionDetailForUser
invokeResponse, err := client.Invoke(invokeRequest)
```

5. 处理请求结果

Response的基本结构如下，根据结构体定义取出对应的字段即可。

```go
type XxxResponse struct {
    *tchttp.BaseResponse
    Response *struct {
    } `json:"Response"`
}

type InvokeResponse struct {
    *tchttp.BaseResponse
    Response *struct {
        // 交易ID
        Txid *string `json:"Txid,omitempty" name:"Txid"`
        // 交易执行结果
        Events *string `json:"Events,omitempty" name:"Events"`
        // 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        RequestId *string `json:"RequestId,omitempty" name:"RequestId"`
    } `json:"Response"`
}

func (r *InvokeResponse) ToJsonString() string {
    b, _ := json.Marshal(r)
    return string(b)
}

func (r *InvokeResponse) FromJsonString(s string) error {
    return json.Unmarshal([]byte(s), &r)
}
```
