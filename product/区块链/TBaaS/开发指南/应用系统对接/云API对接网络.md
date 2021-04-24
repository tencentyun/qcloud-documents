云 API 为腾讯云向外提供服务的接口，应用系统需要根据语言集成对应的 SDK 调用云 API，SDK 的集成方法请参考以下对应链接：
- [Tencent Cloud SDK 3.0 for Python](https://github.com/TencentCloud/tencentcloud-sdk-python)
- [Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
- [Tencent Cloud SDK 3.0 for PHP](https://github.com/TencentCloud/tencentcloud-sdk-php)
- [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
- [Tencent Cloud SDK 3.0 for NodeJS](https://github.com/TencentCloud/tencentcloud-sdk-nodejs)
- [Tencent Cloud SDK 3.0 for .NET](https://github.com/TencentCloud/tencentcloud-sdk-dotnet)


SDK 的使用流程如下图所示：
<img src="https://main.qcloudimg.com/raw/3abf6af1b8f0f1096619fa0945a3d789.png" alt="img" style="zoom: 33%;" />            

云 API 支持 Fabric、BCOS 和 TrustSQL 调用，本文将以 Fabric 为例进行介绍。
## 获取账户信息
使用云 API 调用合约时除了需要网络、合约的相关参数，还需要提供购买 TBaaS 节点的账户信息，包括 SecretId 和 SecretKey。
>?
>- 如果没有腾讯云账号，请先 [注册新账号](https://cloud.tencent.com/register)。
>- 如果已有腾讯云账号，可以在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中获取 `SecretId` 和 `SecretKey`。

## 调试合约
在应用系统调用合约之前，若需要对合约进行调试，推荐使用 [API 3.0 Explorer](https://console.cloud.tencent.com/api/explorer?Product=tbaas&Version=2018-04-16&Action=GetInvokeTx)。该工具提供在线调用、签名验证、SDK 代码生成和快速检索接口等能力，能显著降低使用 [TBaaS API](https://cloud.tencent.com/document/product/663/19457) 的难度。仅需要在页面上输入 API 密钥以及 [请求结构](https://cloud.tencent.com/document/product/663/19457) 的必要参数。


## 调用合约
本文以 Java 和 Go 为例向您介绍 SDK 的使用方法。
### Java
Java SDK 集成方法：[Tencent Cloud SDK 3.0 for Java](https://github.com/TencentCloud/tencentcloud-sdk-java)
如需运行，需要将不同步骤的代码按照 Java 语言要求整合。以下代码示例为不同步骤的代码编写：
1. 导入基础包，并配置参数。

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

2. 创建用户。

```java
// 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
Credential cred = new Credential(SECRET_ID, SECRET_KEY);

ClientProfile clientProfile = new ClientProfile();
clientProfile.setSignMethod(ClientProfile.SIGN_TC3_256);
TbaasClient client = new TbaasClient(cred, REGIION, clientProfile);
```

3. 构造调用请求。
SDK 中根据不同请求类型提供了6种 Request 结构体，定义在包 `com.tencentcloudapi.tbaas.v20180416.models` 中，每种 `XxxRequest` 都有对应的发送请求接口以及 `XxxResponse`。其中字段 `Opeartion` 和 `Module` 的取值需要参考对应的类定义。

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

4. 处理请求结果。
参考类定义使用对应的 setter/getter 方法取出属性即可。

### Go

Go SDK 集成方法： [Tencent Cloud SDK 3.0 for Go](https://github.com/TencentCloud/tencentcloud-sdk-go)
以下代码示例为不同步骤的代码编写：
1. 导入基础包，并配置参数。[](id:step1)

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

2. 创建用户。
提供 SecretID、SecretKey 和 Region 参数。

```go
credential := common.Credential{
    SecretId: SECRET_ID, 
    SecretKey: SECRET_KEY
    }
clientProfile := profile.NewClientProfile()
client, _ := tbaas.NewClient(
    &credential, "ap-guangzhou", clientProfile)
```

3. 构造调用请求。
SDK 中根据不同请求类型提供了18种 Request 结构体，定义在 github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tbaas/v20180416/models.go 文件中，每种 `XxxRequest` 都有对应的 `NewXxxRequest` 方法，需要使用该方法进行初始化，同时还有对应的发送请求接口以及 `XxxResponse`。按照 [步骤1](#step1) 中的方法导入包后，可使用 `tbaas.NewXxxRequest()` 进行调用。本节以 `InvokeRequest` 为例，说明构造方法：

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

4. 发送请求。

```go
//不同类型的请求对应着不同的发送接口
//例如：InvokeRequest——Invoke
//GetTransactionDetailForUserRequest
//            ——GetTransactionDetailForUser
invokeResponse, err := client.Invoke(invokeRequest)
```

5. 处理请求结果。
`Response` 的基本结构如下，根据结构体定义取出对应的字段即可。

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
