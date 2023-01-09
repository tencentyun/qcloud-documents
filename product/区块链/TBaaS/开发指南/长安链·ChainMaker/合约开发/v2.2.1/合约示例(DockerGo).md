## 智能合约构成

ChainMaker Go (DockerGo) 语言的智能合约代码主要由以下接口构成：

```go
package main

// sdk 代码中，有且仅有一个 main() 方法
func main() {  
   // main() 方法中，下面的代码为必须代码，不建议修改 main() 方法当中的代码
   // 其中，TestContract 为用户实现合约的具体名称
	err := shim.Start(new(TestContract))
	if err != nil {
		log.Fatal(err)
	}
}

// 合约结构体，合约名称需要写入 main() 方法当中
type TestContract struct {
}

// 合约必须实现下面两个方法：
// InitContract(stub shim.CMStubInterface) protogo.Response
// InvokeContract(stub shim.CMStubInterface) protogo.Response

// 用于合约的部署和升级
// @param stub: 合约接口
// @return: 	合约返回结果，包括 Success 和 Error
func (t *TestContract) InitContract(stub shim.CMStubInterface) protogo.Response {

	return shim.Success([]byte("Init Success"))

}

// 用于合约的调用
// @param stub: 合约接口
// @return: 	合约返回结果，包括 Success 和 Error
func (t *TestContract) InvokeContract(stub shim.CMStubInterface) protogo.Response {

	return shim.Success([]byte("Invoke Success"))

}
```

### 代码入口

代码入口包名必须为 main

```go
package main

// sdk 代码中，有且仅有一个 main() 方法
func main() {  
   // main() 方法中，下面的代码为必须代码，不建议修改 main() 方法当中的代码
   // 其中，TestContract 为用户实现合约的具体名称
	err := shim.Start(new(TestContract))
	if err != nil {
		log.Fatal(err)
	}
}
```

## 智能合约示例

### 存证合约示例

1. 存储文件哈希、文件名称、时间。
2. 通过文件哈希查询该条记录。

<dx-alert infotype="notice" title="">
- 实现合约接口的结构体不能包含任何字段，例如存证合约中的 FactContract；
- 合约中不能定义全局变量；
因为在一个 vm-docker-go 合约实例的生命周期中，可能会处理多笔交易，这些交易共用全局变量和一个 Contract 接口实例（该示例中的 FactContract），不同交易之间会相互产生不可控的影响，导致合约业务不能正常运行。
</dx-alert>

```go
package main

import (
	"encoding/json"
	"log"
	"strconv"

	"chainmaker.org/chainmaker-contract-sdk-docker-go/pb/protogo"
	"chainmaker.org/chainmaker-contract-sdk-docker-go/shim"
)

type FactContract struct {
}

// 存证对象
type Fact struct {
	FileHash string `json:"FileHash"`
	FileName string `json:"FileName"`
	Time     int32  `json:"time"`
}

// 新建存证对象
func NewFact(FileHash string, FileName string, time int32) *Fact {
	fact := &Fact{
		FileHash: FileHash,
		FileName: FileName,
		Time:     time,
	}
	return fact
}

func (f *FactContract) InitContract(stub shim.CMStubInterface) protogo.Response {

	return shim.Success([]byte("Init Success"))

}

func (f *FactContract) InvokeContract(stub shim.CMStubInterface) protogo.Response {

	// 获取参数
	method := string(stub.GetArgs()["method"])

	switch method {
	case "save":
		return f.save(stub)
	case "findByFileHash":
		return f.findByFileHash(stub)
	default:
		return shim.Error("invalid method")
	}

}

func (f *FactContract) save(stub shim.CMStubInterface) protogo.Response {
	params := stub.GetArgs()

	// 获取参数
	fileHash := string(params["file_hash"])
	fileName := string(params["file_name"])
	timeStr := string(params["time"])
	time, err := strconv.Atoi(timeStr)
	if err != nil {
		msg := "time is [" + timeStr + "] not int"
		stub.Log(msg)
		return shim.Error(msg)
	}

	// 构建结构体
	fact := NewFact(fileHash, fileName, int32(time))

	// 序列化
	factBytes, _ := json.Marshal(fact)

	// 发送事件
	stub.EmitEvent("topic_vx", []string{fact.FileHash, fact.FileName})

	// 存储数据
	err = stub.PutStateByte("fact_bytes", fact.FileHash, factBytes)
	if err != nil {
		return shim.Error("fail to save fact bytes")
	}

	// 记录日志
	stub.Log("[save] FileHash=" + fact.FileHash)
	stub.Log("[save] FileName=" + fact.FileName)

	// 返回结果
	return shim.Success([]byte(fact.FileName + fact.FileHash))

}

func (f *FactContract) findByFileHash(stub shim.CMStubInterface) protogo.Response {
	// 获取参数
	FileHash := string(stub.GetArgs()["file_hash"])

	// 查询结果
	result, err := stub.GetStateByte("fact_bytes", FileHash)
	if err != nil {
		return shim.Error("failed to call get_state")
	}

	// 反序列化
	var fact Fact
	_ = json.Unmarshal(result, &fact)

	// 记录日志
	stub.Log("[find_by_file_hash] FileHash=" + fact.FileHash)
	stub.Log("[find_by_file_hash] FileName=" + fact.FileName)

	// 返回结果
	return shim.Success(result)
}

func main() {

	err := shim.Start(new(FactContract))
	if err != nil {
		log.Fatal(err)
	}
}
```

### 存证合约代码说明

<table>
<thead>
  <tr>
    <th>参数名称</th>
    <th>描述</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>InitContract</td>
    <td>合约的初始化函数，在合约部署时被调用，在本合约中为空。</td>
  </tr>
  <tr>
    <td>save</td>
    <td>save 函数实现将文件相关信息记录到链上的功能。步骤如下：<br>1. save 函数先通过 [参数处理]API 接口 GetArgs 函数拿到时间，文件哈希和文件名字等信息。<br>2. 构造 Fact 结构，序列化为 byte 数据；且当序列化错误时调用 [其他辅助类]API 接口 Log 函数记录相应日志。<br>3. 通过调用 [账本交互]API 接口 PutStateByte 函数将数据记录到链上。<br>4. 最后通过调用 [其他辅助类]API 接口 Success 函数将操作结果记录到链上。</td>
  </tr>
  <tr>
    <td>findByFileHash</td>
    <td>通过文件哈希查询该条记录。步骤如下：<br>1. findByFileHash 通过 [参数处理]API 接口 GetArgs 函数拿到要查找的文件的文件哈希。<br>2. 通过 [账本交互]API 接口 GetStateByte 函数获取文件的信息；若失败则通过 [其他辅助类]API 接口 Error 函数将操作结果记录到链上，否则，通过 [其他辅助类]API 接口 Log 函数和 Success 函数记录相关日志和返回结果。</td>
  </tr>
</tbody>
</table>
