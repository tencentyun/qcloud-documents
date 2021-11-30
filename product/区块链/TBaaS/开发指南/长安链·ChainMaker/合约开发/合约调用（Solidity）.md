

# 合约调用（Solidity）

## ABI编码示例

以Token合约为例，对transfer函数的函数名及调用参数进行ABI编码

```go
import (
    "encoding/hex"
    "fmt"
    "io/ioutil"
    "math/big"
    "strings"

    "chainmaker.org/chainmaker-go/common/evmutils"
    "github.com/ethereum/go-ethereum/accounts/abi"
)

const (
    // 编译合约后获取的abi文件的路径
    tokenABIPath = "./testdata/token-evm-demo/token.abi"
    // 入参1：转账地址
    clientAddr = "0xa55f1e0cb68b0cc589906078237094bdb9715bfd"
    // 入参2：转账金额
    amount = 200
)

func testUserContractTokenEVMTransfer() {
    abiJson, err := ioutil.ReadFile(tokenABIPath)
    if err != nil {
        fmt.Printf("fail to read the abi file:%v", err)
    }

    myAbi, err := abi.JSON(strings.NewReader(string(abiJson)))
    if err != nil {
        fmt.Printf("fail to get abi object:%v", err)
    }

    addr := evmutils.BigToAddress(evmutils.FromHexString(clientAddr[2:]))

    dataByte, err := myAbi.Pack("transfer", addr, big.NewInt(amount))
    if err != nil {
        fmt.Printf("fail to pack contract input:%v", err)
    }

    data := hex.EncodeToString(dataByte)
    method := data[0:8]

    pairs := map[string]string{
        "data": data,
    }

    // 编码后的函数名
    fmt.Printf("FuncName: %s\n", method)
    // 编码后的参数
    fmt.Printf("FuncParam %v\n", pairs)
}
```

输出结果如下

```shell
FuncName: a9059cbb
FuncParam map[data:a9059cbb000000000000000000000000a55f1e0cb68b0cc589906078237094bdb9715bfd00000000000000000000000000000000000000000000000000000000000000c8]
```

## 长安链SDK调用示例

将ABI编码后的函数名及调用参数分别作为method与params

```go
    method := "a9059cbb"
    params := map[string]string{
        "data": "a9059cbb000000000000000000000000a55f1e0cb68b0cc589906078237094bdb9715bfd00000000000000000000000000000000000000000000000000000000000000c8",
    }
    resp, err := client.InvokeContract("fact", method, "", params, -1, true)
    if err != nil {
        fmt.Printf("fail to invoke contract:%v", err)
    }
```

## 云API调用示例

将ABI编码后的函数名及调用参数分别填入FuncName与FuncParam字段

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
    params = json.dumps(action_params)
    req = models.InvokeChainMakerContractRequest()
    # 调用InvokeChainMakerContractRequest的from_json_string方法，使用params初始化req对象
    req.from_json_string(params)

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.InvokeChainMakerContract(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())
```