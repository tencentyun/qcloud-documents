
## 长安链证书转换 EVM 地址

ChainMake Solidity 语言版本智能合约完全兼容 EVM，更多长安链证书与 EVM 地址的转换详情可参见 [EVM 地址说明](https://docs.chainmaker.org.cn/v2.2.0_alpha/html/operation/%E6%99%BA%E8%83%BD%E5%90%88%E7%BA%A6.html#evm)。

在“证书管理”界面申请证书后，可根据获得的用户证书文件 user_sign.crt 获取该用户的 EVM 地址，代码示例如下：

```go
import (
    "encoding/hex"
    "encoding/pem"
    "fmt"
    "io/ioutil"

    "chainmaker.org/chainmaker/common/v2/crypto/x509"
    "chainmaker.org/chainmaker/common/v2/evmutils"
    "github.com/ethereum/go-ethereum/accounts/abi"
)

func MakeAddrAndSkiFromCrtFilePath() {
    crtFilePath := "./user_sign.crt"

    crtBytes, err := ioutil.ReadFile(crtFilePath)
    if err != nil {
        fmt.Printf("fail to read the crt file:%v", err)
    }

    blockCrt, _ := pem.Decode(crtBytes)
    crt, err := x509.ParseCertificate(blockCrt.Bytes)
    if err != nil {
        fmt.Printf("fail to parse certificate:%v", err)
    }

    ski := hex.EncodeToString(crt.SubjectKeyId)
    addrInt, err := evmutils.MakeAddressFromHex(ski)
    if err != nil {
    fmt.Printf("fail to make address from hex:%v", err)
    }

    // 证书 SKI
    fmt.Printf("clientAddrSki: %s\n", ski)
    // EVM 地址（十进制）
    fmt.Printf("clientAddrInt: %s\n", addrInt.String())
    // EVM 地址
    fmt.Printf("clientEthAddr: 0x%x\n", addrInt.AsStringKey())
}
```

成功运行可以查看到如下图输出：
<img src="https://qcloudimg.tencent-cloud.cn/raw/651338befdcad21d798dcdad278c3abd.png" />

## ABI 编码示例

ChainMake Solidity 语言版本智能合约完全兼容 EVM，更多 ABI 编码的详情可参见 [Solidity 官方文档](https://docs.soliditylang.org/en/v0.5.6/abi-spec.html)。

### 合约初始化

以 Token 合约为例，对合约初始化参数进行 ABI 编码。代码示例如下：

```go
import (
    "encoding/hex"
    "fmt"
    "io/ioutil"
    "math/big"
    "strings"

    "chainmaker.org/chainmaker/common/v2/evmutils"
    "github.com/ethereum/go-ethereum/accounts/abi"
)

const (
    // 编译合约后获取的 abi 文件的路径
    tokenABIPath = "./testdata/token-evm-demo/token.abi"
    // 合约安装时调用 constructor ，调用方法设为空字符串
    function = ""
    // 入参 1：发行 EVM 地址，可根据用户证书转换取得
    clientAddr = "0x89f4090e315621696d6936453661ec4b9795ad27"
)

func testUserContractTokenEVMConstructor () {
    abiJson, err := ioutil.ReadFile (tokenABIPath)
    if err != nil {
        fmt.Printf ("fail to read the abi file:%v", err)
    }

    myAbi, err := abi.JSON (strings.NewReader (string (abiJson)))
    if err != nil {
        fmt.Printf ("fail to get abi object:%v", err)
    }

    addr := evmutils.BigToAddress (evmutils.FromHexString (clientAddr [2:]))

    dataByte, err := myAbi.Pack (function, addr)
    if err != nil {
        fmt.Printf ("fail to pack contract input:%v", err)
    }

    data := hex.EncodeToString (dataByte)

    pairs := map [string] string {
        "data": data,
    }

    // 编码后的参数
    fmt.Printf ("FuncParam %v\n", pairs)
}
```

输出结果如下：

```shell
FuncParam map [data:00000000000000000000000089f4090e315621696d6936453661ec4b9795ad27]
```

通过 TBaaS 控制台安装合约并填写对应初始化参数：
- key 取值：data
- value 取值：00000000000000000000000089f4090e315621696d6936453661ec4b9795ad27
<img src="https://main.qcloudimg.com/raw/8a141576b1193db70183413d1d792ab3.png"/>

### 合约调用

以 Token 合约为例，对 transfer 函数的函数名及调用参数进行 ABI 编码。代码示例如下：

```go
import (
    "encoding/hex"
    "fmt"
    "io/ioutil"
    "math/big"
    "strings"

    "chainmaker.org/chainmaker/common/v2/evmutils"
    "github.com/ethereum/go-ethereum/accounts/abi"
)

const (
    // 编译合约后获取的 abi 文件的路径
    tokenABIPath = "./testdata/token-evm-demo/token.abi"
    // 调用方法
    function = "transfer"
    // 入参 1：转账 EVM 地址，可根据用户证书转换取得
    clientAddr = "0xa55f1e0cb68b0cc589906078237094bdb9715bfd"
    // 入参 2：转账金额
    amount = 200
)

func testUserContractTokenEVMTransfer () {
    abiJson, err := ioutil.ReadFile (tokenABIPath)
    if err != nil {
        fmt.Printf ("fail to read the abi file:%v", err)
    }

    myAbi, err := abi.JSON (strings.NewReader (string (abiJson)))
    if err != nil {
        fmt.Printf ("fail to get abi object:%v", err)
    }

    addr := evmutils.BigToAddress (evmutils.FromHexString (clientAddr [2:]))

    dataByte, err := myAbi.Pack (function, addr, big.NewInt (amount))
    if err != nil {
        fmt.Printf ("fail to pack contract input:%v", err)
    }

    data := hex.EncodeToString (dataByte)
    method := data [0:8]

    pairs := map [string] string {
        "data": data,
    }

    // 编码后的函数名
    fmt.Printf ("FuncName: %s\n", method)
    // 编码后的参数
    fmt.Printf ("FuncParam %v\n", pairs)
}
```

输出结果如下：

```shell
FuncName: a9059cbb
FuncParam map [data:a9059cbb000000000000000000000000a55f1e0cb68b0cc589906078237094bdb9715bfd00000000000000000000000000000000000000000000000000000000000000c8]
```

## 长安链 SDK 调用示例

将 ABI 编码后的函数名及调用参数分别作为 method 与 params，代码示例如下：

```go
    method := "a9059cbb"
    dataString := "a9059cbb000000000000000000000000a55f1e0cb68b0cc589906078237094bdb9715bfd00000000000000000000000000000000000000000000000000000000000000c8"
    params := []*common.KeyValuePair{
        {
            Key:   "data",
            Value: []byte(dataString),
        },
    resp, err := client.InvokeContract ("fact", method, "", params, -1, true)
    if err != nil {
        fmt.Printf ("fail to invoke contract:%v", err)
    }
```

## 云 API 调用示例

将 ABI 编码后的函数名及调用参数分别填入 FuncName 与 FuncParam 字段，代码示例如下：

```python
    action_params = {
        "ClusterId": "chainmaker-txtxtxtxtx",
        "ChainId": "chain_txtxt",
        "ContractName": "fact",
        "FuncName": "a9059cbb",
        "FuncParam": "{\"data\":\"a9059cbb000000000000000000000000a55f1e0cb68b0cc589906078237094bdb9715bfd00000000000000000000000000000000000000000000000000000000000000c8\"}",
        "AsyncFlag": 0,
        "Action": "InvokeChainMakerContract",
        "Version": "2018-04-16",
        "Region": "ap-beijing"
    }
    # 实例化一个请求对象，根据调用的接口和实际情况，可以进一步设置请求参数
    params = json.dumps (action_params)
    req = models.InvokeChainMakerContractRequest ()
    # 调用 InvokeChainMakerContractRequest 的 from_json_string 方法，使用 params 初始化 req 对象
    req.from_json_string (params)

    # 通过 client 对象调用想要访问的接口，需要传入请求对象
    resp = client.InvokeChainMakerContract (req)
    # 输出 json 格式的字符串回包
    print (resp.to_json_string ())
```
