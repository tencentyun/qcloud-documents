## 操作场景
用户可以利用 TBaaS 提供的国密算法的能力，便捷的在智能合约中使用国密算法。在智能合约中使用国密算法一般分为以下两个步骤：
1. 利用 TBaaS 提供的 gmtool 生成国密算法公私钥，同时使用生成的私钥对用户数据签名。
2. 利用 TBaaS 提供的 Go 语言智能合约包 gmssl，在智能合约中直接 import gmssl，编写国密算法相关的业务操作，例如验证签名等。



## 操作步骤
### Gmtool国密算法公私钥生成以及数据签名
1. 执行以下命令，使用 gmtool 生成国密算法公私钥对。
```
./gmtool genkey -pkout=pk.sm2 -skout=sk.sm2
```
其中，pk.sm2 是国密算法公钥文件，sk.sm2 是国密算法私钥文件。
2. 执行以下命令，使用 gmtool 生成的私钥对信息进行签名。
```
./gmtool sign -skin=sk.sm2 -message=message -signature=sig.sm2
```
其中，message 是信息文件包含要签名的信息，sig.sm2 是生成的文件包含签名信息，该签名信息是 base64 编码的。

### 智能合约国密算法示例
该示例中的 Init 函数直接返回成功，无其余操作。Invoke 函数会根据不同业务逻辑进行细分调用，最终调用 verify 业务逻辑接口，用于验证用户的签名是否正确。您可访问 [智能合约代码](https://main.qcloudimg.com/raw/21e2670a6591b6a7b78ef3c7568c4c2c/gm_base64_demo.go) 获得完整代码，以下将对代码中的重要函数进行分析。


#### Init 函数示例
Init 函数主要用于在智能合约实例化和升级的时候默认调用。在实现 Init 函数的过程中，可以使用 [Go 语言版本的合约 API](https://cloud.tencent.com/document/product/663/36243) 来对参数和账本进行操作。
以返回成功为例，示例代码如下：
```
// Init函数不包含具体业务，直接返回成功。
func (t *SimpleAsset) Init(stub shim.ChaincodeStubInterface) peer.Response {
	// Get the args from the transaction proposal
	return shim.Success(nil)
}
```

#### Invoke 函数示例
Invoke 函数可以对用户的不同的智能合约业务逻辑进行拆分。本示例以只实现了一种业务类型国密算法验签 verify 为例，介绍如何通过调用 API GetFunctionAndParameters 获取到用户的具体业务类型和参数，再分别调用不同的函数。
```
// Invoke把用户调用的function细分到几个子function, 这里只实现了verify
// Invoke is called per transaction on the chaincode. 
func (t *SimpleAsset) Invoke(stub shim.ChaincodeStubInterface) peer.Response {
	// Extract the function and args from the transaction proposal
	fn, args := stub.GetFunctionAndParameters()

	var result string
	var err error

	switch fn {
	case "verify": {
		result, err = verify(stub, args)
	}
	default: {
		shim.Error("invalid function")
	}
	}
	if err != nil {
		return shim.Error(err.Error())
	}

	// Return the result as success payload
	return shim.Success([]byte(result))
}
```

#### 业务逻辑 verify 函数示例
本示例以实现国密算法签名验证的业务逻辑 verify 函数为例。调用国密算法的接口 NewPublicKeyFromPEM 用于获取国密算法公钥，调用 ComputeSM2IDDiges，NewDigestContext，Reset，Update，Final 用于生成信息摘要，调用 Verify 用于验证签名是否正确。
```
// verify输入的参数是信息,签名base64以及公钥base64
// verify验证用户的签名是否正确
func verify(stub shim.ChaincodeStubInterface, args []string) (string, error) {
	if len(args) != 3 {
		return "", fmt.Errorf("Incorrect arguments. Expecting a message, a signature, and a public key")
	}

	pkPem, err := base64.StdEncoding.DecodeString(args[2])
	if err != nil {
		fmt.Println(err.Error())
		return "", err
	}
	// 获取国密算法公钥
	pk, err := gmssl.NewPublicKeyFromPEM(string(pkPem))
	if err != nil {
                fmt.Println(err.Error())
		return "", err
	}

	sig, err := base64.StdEncoding.DecodeString(args[1])
	if err != nil {
                fmt.Println(err.Error())
		return "", err
	}

	message := args[0]
	// 计算信息摘要
	zid, err := pk.ComputeSM2IDDigest(DEFAULT_USER_ID)
	if err != nil {
                fmt.Println(err.Error())
		return "", err
	}
	sm3ctx, err := gmssl.NewDigestContext("SM3")
	if err != nil {
                fmt.Println(err.Error())
		return "", err
	}
	sm3ctx.Reset()
	sm3ctx.Update(zid)
	sm3ctx.Update([]byte(message))
	tbs, err := sm3ctx.Final()
	if err != nil {
                fmt.Println(err.Error())
		return "", err
	}
	// 验证签名
	err = pk.Verify("sm2sign", tbs, sig, nil)
	if err == nil {
		fmt.Println("Valid Signature")
		return "Valid Signature.", nil
	} else {
		fmt.Println("Invalid Signature")
		return "Invalid signature:", nil
	}
}
```

