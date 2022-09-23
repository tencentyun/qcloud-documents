
## 操作场景
用户可以利用 TBaaS 提供的同态加密的能力，便捷的在智能合约中使用同态加密。使用同态加密可以分为以下三个步骤：
1.  使用 TBaaS 提供的 paitool 生成同态公私钥，同时使用生成的公钥对用户数据线下加密。
2.  使用 TBaaS 提供的 Go 语言智能合约包 paillier，编写同态相关的业务层操作，例如同态加、同态减、部分同态乘等。
3.  当业务逻辑完成后，用户可以从智能合约中获取到对应的同态加密数据，线下使用对应的同态私钥进行数据解密，从而可以获取链上业务操作完成后的真实数据。

## 操作步骤
### Paitool 同态公私钥生成以及数据加密
1. 依次执行以下命令，使用 paitool 生成两组同态加密的公私钥对。
```
./paitool genkey -length=2048 -pkout=pk1.pai -skout=sk1.pai
./paitool genkey -length=2048 -pkout=pk2.pai -skout=sk2.pai
```
其中，pk1.pai, pk2.pai 是同态加密公钥文件，sk1.pai, sk2.pai 是同态加密私钥文件。
2. 依次执行以下命令，使用 paitool 对数字100和200分别用不同的公钥进行同态加密。
```
./paitool encrypt -pkin=pk1.pai -plaintext=100 -cipherout=cipher1.pai
./paitool encrypt -pkin=pk2.pai -plaintext=200 -cipherout=cipher2.pai
```
其中，cipher1.pai 是数字100同态加密后的密文数据，cipher2.pai 是数字200加密后的密文数据。

### 智能合约同态加密示例
Hyperledger Fabric 提供了很多官方的智能合约样例，具体请参考 [fabric 官方示例](https://github.com/hyperledger/fabric/tree/release-1.4/examples/chaincode/go) 。本示例以 Hyperledger Fabric 官方提供的 example02 样例为例进行同态修改。该示例的 Init 函数用于初始化两个 key/value 键值对，其中 value 是用同态加密后的数据，Invoke 函数用于根据不同业务逻辑进行细分调用，最终调用以下业务逻辑接口：
- invoke：用于 key 之间的 value 转移。
- query：用于查询 key 所对应的值。

您可以访问 [智能合约代码](https://main.qcloudimg.com/raw/9d62832aa7f04218c795a2624176a7fc/pai_base64_demo.go) 获得完整代码，以下将对代码中的重要函数进行分析。

#### Init 函数示例
Init 函数主要用于在智能合约实例化和升级的时候默认调用。在实现 Init 函数的过程中，可以使用 [Go 语言版本的合约 API](https://cloud.tencent.com/document/product/663/36243) 来对参数和账本进行操作。在这个示例中，通过调用 API GetFunctionAndParameters 获取到用户输入参数。在获取用户输入参数后，通过调用 API PutState 将数据写到账本中。
```
// Init函数用于初始化两个键值对，用户输入的参数为KEY1_NAME, VALUE1, KEY2_NAME, VALUE2,其中VALUE1和VALUE2都是同态加密后的数据
// 在例子中，VALUE1是cipher1.pai的内容， VALUE2是ciphe2.pai的内容
func (t *SimpleChaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("ex02 Init")
	// 调用API GetFunctionAndParameters 获取用户输入参数
	_, args := stub.GetFunctionAndParameters()
	var A, B string    // Entities
	var Aval, Bval string // Asset holdings
	var err error

	if len(args) != 4 {
		return shim.Error("Incorrect number of arguments. Expecting 4")
	}

	// Initialize the chaincode
	A = args[0]
	Aval = args[1]

	B = args[2]
	Bval = args[3]

	// 调用API PutState把数据写入账本
	// Write the state to the ledger
	err = stub.PutState(A, []byte(Aval))
	if err != nil {
		return shim.Error(err.Error())
	}

	err = stub.PutState(B, []byte(Bval))
	if err != nil {
		return shim.Error(err.Error())
	}

	return shim.Success(nil)
}
```

#### Invoke 函数示例
Invoke 函数可以对用户的不同的智能合约业务逻辑进行拆分。本示例通过调用 API GetFunctionAndParameters 获取到用户的具体业务类型和参数，再分别调用不同的函数，如 invoke 和 query 函数。
```
// Invoke把用户调用的function细分到几个子function, 包含invoke和query
func (t *SimpleChaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("ex02 Invoke")
	// 调用API GetFunctionAndParameters获取用户输入的业务类型和参数
	function, args := stub.GetFunctionAndParameters()
	if function == "invoke" {
		// Make payment of X units from A to B
		return t.invoke(stub, args)
	} else if function == "query" {
		// the old "Query" is now implemtned in invoke
		return t.query(stub, args)
	} 
	return shim.Error("Invalid invoke function name")
}
```

#### 业务逻辑 invoke 函数示例
业务逻辑 invoke 函数主要用于实现业务逻辑中的资产转移。本示例中通过调用 API GetState 获取到 KEY 对应的同态加密资产总值，通过调用用户业务逻辑实现资产转移，通过调用 API PutState 将用户最终资产写入账本。
在此过程中，调用了同态加密的接口 GetPublicKeyFromHex 用于获取同态公钥，GetCiphertextFromHex 用于获取同态加密数据，Sub 用于同态密文和明文相减，Add 用于同态密文和明文相加以及 GetCiphertextHex 用于获取同态加密后的16进制密文数据。
```
// invoke实现两个键之间的value转移，输入为KEY1_NAME, KEY1_PUBKEYINHEX, KEY2_NAME，KEY2_PUBKEYINHEX，VALUE
// 在例子中，KEY1_PUBKEYINHEX是pk1.pai内容的base64, KEY2_PUBKEYINHEX是pk2.pai的内容base64
func (t *SimpleChaincode) invoke(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	var A, B string    // Entities
	var Apkpem, Bpkpem []byte //public key in hex 

	var Aval, Bval string // Asset encrypted holdings
	var X *big.Int          // Transaction value
	var err error

	if len(args) != 5 {
		return shim.Error("Incorrect number of arguments. Expecting 5")
	}

	A = args[0]
	Apkpem, err = base64.StdEncoding.DecodeString(args[1])
	if err != nil {
		return shim.Error("Failed to get Apkpem in hex")
	}

	B = args[2]
	Bpkpem, err = base64.StdEncoding.DecodeString(args[3])
	if err != nil{
		return shim.Error("Failed to get Bpkpem in hex")
	}
	X, isOK := new(big.Int).SetString(args[4], 10)
	if !isOK {
		return shim.Error("Fail to get X")
	}

	// Get the state from the ledger
	// API GetState获取对应账户的资产，这里的资产是同态加密后的数据
	Avalbytes, err := stub.GetState(A)
	if err != nil {
		return shim.Error("Failed to get state")
	}
	if Avalbytes == nil {
		return shim.Error("Entity not found")
	}
	Aval = string(Avalbytes)

	Bvalbytes, err := stub.GetState(B)
	if err != nil {
		return shim.Error("Failed to get state")
	}
	if Bvalbytes == nil {
		return shim.Error("Entity not found")
	}
	Bval = string(Bvalbytes)
  
	// 执行具体业务逻辑，这里是对应资产进行转移
	// Perform the execution
	// 调用同态接口GetPublicKeyFromHex获取公钥信息
	Apk, err := paillier.GetPublicKeyFromHex(string(Apkpem))
	if err != nil {
		return shim.Error("Fail to get A public key in PublicKey")
	}
	// 调用同态接口GetCiphertextFromHex获取同态密文信息
	Acipher, err := paillier.GetCiphertextFromHex(Aval)
	if err != nil {
		return shim.Error("Fail to get Ciphertext for A")
	}


	// 调用同态接口Sub执行密文和明文相减
	Aciphernew, err := paillier.Sub(Apk, Acipher, X.Text(10))
	if err != nil {
		return shim.Error("Fail to compute Aciphernew")
	}
	// 调用同态接口GetCiphertextHex获取同态密文16进制string
	Avalnew, err := paillier.GetCiphertextHex(Aciphernew)
	if err != nil {
		return shim.Error("Fail to get Avalnew")
	}

	Bpk, err := paillier.GetPublicKeyFromHex(string(Bpkpem))
	if err != nil {
		return shim.Error("Fail to get B public key in PublicKey")
	}

	Bcipher, err := paillier.GetCiphertextFromHex(Bval)
	if err != nil {
		return shim.Error("Fail to get Ciphertext for B")
	}
	// 调用同态接口Add执行密文和明文相加
	Bciphernew, err := paillier.Add(Bpk, Bcipher, X.Text(10))
	if err != nil {
		return shim.Error("Fail to compute Bciphernew")
	}

	Bvalnew, err := paillier.GetCiphertextHex(Bciphernew)
	if err != nil {
		return shim.Error("Fail to get Bvalnew")
	}

	// API PutState将对应资产写入账本
	// Write the state back to the ledger
	err = stub.PutState(A, []byte(Avalnew))
	if err != nil {
		return shim.Error(err.Error())
	}

	err = stub.PutState(B, []byte(Bvalnew))
	if err != nil {
		return shim.Error(err.Error())
	}

	return shim.Success(nil)
}
```

#### 业务逻辑 query 函数示例
业务逻辑 query 函数主要用于实现业务逻辑中的账户查询功能，本示例通过调用 API GetState 查询对应账户的资产。
```
// query主要是查询键对应的值，输入为KEY_NAME
// query callback representing the query of a chaincode
func (t *SimpleChaincode) query(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	var A string // Entities
	var err error

	if len(args) != 1 {
		return shim.Error("Incorrect number of arguments. Expecting name of the person to query")
	}

	A = args[0]

	// Get the state from the ledger
	Avalbytes, err := stub.GetState(A)
	if err != nil {
		jsonResp := "{\"Error\":\"Failed to get state for " + A + "\"}"
		return shim.Error(jsonResp)
	}

	if Avalbytes == nil {
		jsonResp := "{\"Error\":\"Nil amount for " + A + "\"}"
		return shim.Error(jsonResp)
	}

	return shim.Success(Avalbytes)
}
```

### Paitool 同态数据解密
依次执行以下命令，通过智能合约从链上获取到最新的业务逻辑操作过的同态密文数据。拥有对应同态私钥的用户，可以解密出相应的明文。
```
./paitool decrypt -skin=sk1.pai -cipherin=cipher1new.pai
./paitool decrypt -skin=sk2.pai -cipherin=cipher2new.pai
```
其中，cipher1new.pai 对应的是智能合约中 KEY1_NAME 存储的值，cipher2new.pai 对应的是智能合约中 KEY2_NAME 存储的值。





