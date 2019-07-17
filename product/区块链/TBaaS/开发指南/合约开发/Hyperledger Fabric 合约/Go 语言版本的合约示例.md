## 智能合约构成
Go 语言的智能合约代码主要由以下接口构成：
```
// Chaincode interface must be implemented by all chaincodes. The fabric runs
// the transactions by calling these functions as specified.
type Chaincode interface {
        // Init is called during Instantiate transaction after the chaincode container
        // has been established for the first time, allowing the chaincode to
        // initialize its internal data
        Init(stub ChaincodeStubInterface) pb.Response
        // Invoke is called to update or query the ledger in a proposal transaction.
        // Updated state variables are not committed to the ledger until the
        // transaction is committed.
        Invoke(stub ChaincodeStubInterface) pb.Response
}
```
- 接口 Init 主要用于智能合约初始化和升级智能合约时调用此接口，初始化相关的数据。
- 接口 Invoke 主要用于实现智能合约中的内部业务逻辑。用户可以根据实际需求，实现自己相关的业务。
- 在实现过程中，用户还可以调用 ChaincodeStubInterface 的 API 接口和链上进行交互。

## 智能合约示例

### 基本示例
本示例以一个基本的智能合约用例为例，只包含智能合约的必须部分，没有实现任何业务逻辑。
```
package main
import (
    "github.com/hyperledger/fabric/core/chaincode/shim"
    "github.com/hyperledger/fabric/protos/peer"
)
// SimpleAssetDemo implements a simple chaincode to manage an asset
type SimpleAssetDemo struct {
}
// Init is called during chaincode instantiation to initialize any data.
func (t *SimpleAssetDemo) Init(stub shim.ChaincodeStubInterface) peer.Response {
	return shim.Success(nil)
}
// Invoke is called per transaction on the chaincode. Each transaction is
// either a 'get' or a 'set' on the asset created by Init function. The 'set'
// method may create a new asset by specifying a new key-value pair.
func (t *SimpleAssetDemo) Invoke(stub shim.ChaincodeStubInterface) peer.Response {
	return shim.Success(nil)
}
func main() {
	err := shim.Start(new(SimpleAssetDemo))
	if err != nil {
		fmt.Printf("Error starting SimpleAssetDemo chaincode: %s", err)
	}
}
```

### 官方示例
Hyperledger Fabric 提供了大量的官方智能合约样例，具体请参考 [fabric 官方示例](https://github.com/hyperledger/fabric/tree/release-1.3/examples/chaincode/go) 。本示例以一个 Hyperledger Fabric 官方提供的 example02 样例为例。该示例的 Init 函数用于初始化两个 key/value 键值对，同时提供以下接口：
- invoke：用于 key 之间的 value 转移。
- delete：用于删除一个键值对。
- query：用于查询 key 所对应的值。

```
package example02
import (
	"fmt"
	"strconv"
	"github.com/hyperledger/fabric/core/chaincode/shim"
	pb "github.com/hyperledger/fabric/protos/peer"
)
// SimpleChaincode example simple Chaincode implementation
type SimpleChaincode struct {
}
//Init函数用于初始化两个键值对，用户输入的参数为KEY1_NAME, VALUE1, KEY2_NAME, //VALUE2
func (t *SimpleChaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("ex02 Init")
	_, args := stub.GetFunctionAndParameters()
	var A, B string    // Entities
	var Aval, Bval int // Asset holdings
	var err error
	if len(args) != 4 {
		return shim.Error("Incorrect number of arguments. Expecting 4")
	}
	// Initialize the chaincode
	A = args[0]
	Aval, err = strconv.Atoi(args[1])
	if err != nil {
		return shim.Error("Expecting integer value for asset holding")
	}
	B = args[2]
	Bval, err = strconv.Atoi(args[3])
	if err != nil {
		return shim.Error("Expecting integer value for asset holding")
	}
	fmt.Printf("Aval = %d, Bval = %d\n", Aval, Bval)
	// Write the state to the ledger
	err = stub.PutState(A, []byte(strconv.Itoa(Aval)))
	if err != nil {
		return shim.Error(err.Error())
	}
	err = stub.PutState(B, []byte(strconv.Itoa(Bval)))
	if err != nil {
		return shim.Error(err.Error())
	}
	return shim.Success(nil)
}
//Invoke把用户调用的function细分到几个子function, 包含invoke, delete和query
func (t *SimpleChaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
	fmt.Println("ex02 Invoke")
	function, args := stub.GetFunctionAndParameters()
	if function == "invoke" {
		// Make payment of X units from A to B
		return t.invoke(stub, args)
	} else if function == "delete" {
		// Deletes an entity from its state
		return t.delete(stub, args)
	} else if function == "query" {
		// the old "Query" is now implemtned in invoke
		return t.query(stub, args)
	}
	return shim.Error("Invalid invoke function name. Expecting \"invoke\" \"delete\" \"query\"")
}
//invoke实现两个键之间的value转移，输入为KEY1_NAME, KEY2_NAME，VALUE
// Transaction makes payment of X units from A to B
func (t *SimpleChaincode) invoke(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	var A, B string    // Entities
	var Aval, Bval int // Asset holdings
	var X int          // Transaction value
	var err error
	if len(args) != 3 {
		return shim.Error("Incorrect number of arguments. Expecting 3")
	}
	A = args[0]
	B = args[1]
	// Get the state from the ledger
	// TODO: will be nice to have a GetAllState call to ledger
	Avalbytes, err := stub.GetState(A)
	if err != nil {
		return shim.Error("Failed to get state")
	}
	if Avalbytes == nil {
		return shim.Error("Entity not found")
	}
	Aval, _ = strconv.Atoi(string(Avalbytes))
	Bvalbytes, err := stub.GetState(B)
	if err != nil {
		return shim.Error("Failed to get state")
	}
	if Bvalbytes == nil {
		return shim.Error("Entity not found")
	}
	Bval, _ = strconv.Atoi(string(Bvalbytes))
	// Perform the execution
	X, err = strconv.Atoi(args[2])
	if err != nil {
		return shim.Error("Invalid transaction amount, expecting a integer value")
	}
	Aval = Aval - X
	Bval = Bval + X
	fmt.Printf("Aval = %d, Bval = %d\n", Aval, Bval)
	// Write the state back to the ledger
	err = stub.PutState(A, []byte(strconv.Itoa(Aval)))
	if err != nil {
		return shim.Error(err.Error())
	}
	err = stub.PutState(B, []byte(strconv.Itoa(Bval)))
	if err != nil {
		return shim.Error(err.Error())
	}
	return shim.Success(nil)
}
//Delete用于从账本中删除指定的键，输入为KEY_NAME
// Deletes an entity from state
func (t *SimpleChaincode) delete(stub shim.ChaincodeStubInterface, args []string) pb.Response {
	if len(args) != 1 {
		return shim.Error("Incorrect number of arguments. Expecting 1")
	}
	A := args[0]
	// Delete the key from the state in ledger
	err := stub.DelState(A)
	if err != nil {
		return shim.Error("Failed to delete state")
	}
	return shim.Success(nil)
}
//query主要是查询键对应的值，输入为KEY_NAME
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
	jsonResp := "{\"Name\":\"" + A + "\",\"Amount\":\"" + string(Avalbytes) + "\"}"
	fmt.Printf("Query Response:%s\n", jsonResp)
	return shim.Success(Avalbytes)
}
```
