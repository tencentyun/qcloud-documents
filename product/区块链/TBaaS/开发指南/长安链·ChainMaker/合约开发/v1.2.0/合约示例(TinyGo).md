## 智能合约构成

ChainMaker Go (TinyGo) 语言的智能合约代码主要由以下接口构成：

```go
/*
Copyright (C) BABEC. All rights reserved.
SPDX-License-Identifier: Apache-2.0
一个 ChainMaker 的 TinyGO 版本智能合约主要包括以下函数：
*/
package main
// 安装合约时会执行此方法，必须
//export init_contract
func initContract() {
	// 此处可写安装合约的初始化逻辑
}

// 升级合约时会执行此方法，必须
//export upgrade
func upgrade() {
	// 此处可写升级合约的逻辑
}

// sdk 代码中，有且仅有一个 main() 方法
func main() {
// 空，不做任何事。仅用于对 tinygo 编译支持
}

// 对 SDK 暴露的函数
// 对外暴露 test1 方法，供用户由 SDK 调用
//export test1
func test1 () {}
// 对外暴露 test2 方法，供用户由 SDK 调用
//export test2
func test2 () {}

// 其他函数，不对外暴露
func test3 () {}
```

### 代码入口

```go
func main() { // sdk 代码中，有且仅有一个 main() 方法
	// 空，不做任何事。仅用于对 tinygo 编译支持
}
```

### 对链暴露方法写法
```
//export method_name
func  method_name(): 不可带参数，无返回值
```

例如：对链暴露 init_contract 函数。
```go
//export init_contract
func init_contract() {

}
```

其中 init_contract、upgrade 方法必须有且对外暴露。示例如下：
- init_contract：创建合约会执行该方法
- upgrade： 升级合约会执行该方法

```go
// 安装合约时会执行此方法，必须。ChainMaker 不允许用户直接调用该方法。
//export init_contract
func init_contract() {
}
// 升级合约时会执行此方法，必须。ChainMaker 不允许用户直接调用该方法。
//export upgrade
func upgrade() {
}
```

## 智能合约示例

### 存证合约示例

1. 存储文件哈希、文件名称、时间和该交易的 ID。
2. 通过文件哈希查询该条记录。

```go
/*
Copyright (C) BABEC. All rights reserved.

SPDX-License-Identifier: Apache-2.0

一个 文件存证 的存取示例 fact

*/

package main

import (
	"chainmaker-contract-sdk-tinygo/convert"
)

// 安装合约时会执行此方法，必须
//export init_contract
func initContract() {
	// 此处可写安装合约的初始化逻辑

}

// 升级合约时会执行此方法，必须
//export upgrade
func upgrade() {
	// 此处可写升级合约的逻辑

}

// 存证对象
type Fact struct {
	fileHash string
	fileName string
	time     int32 // second
	ec       *EasyCodec
}

// 新建存证对象
func NewFact(fileHash string, fileName string, time int32) *Fact {
	fact := &Fact{
		fileHash: fileHash,
		fileName: fileName,
		time:     time,
	}
	return fact
}

// 获取序列化对象
func (f *Fact) getEasyCodec() *EasyCodec {
	if f.ec == nil {
		f.ec = NewEasyCodec()
		f.ec.AddString("fileHash", f.fileHash)
		f.ec.AddString("fileName", f.fileName)
		f.ec.AddInt32("time", f.time)
	}
	return f.ec
}

// 序列化为json字符串
func (f *Fact) toJson() string {
	return f.getEasyCodec().ToJson()
}

// 序列化为cmec编码
func (f *Fact) marshal() []byte {
	return f.getEasyCodec().Marshal()
}

// 反序列化cmec为存证对象
func unmarshalToFact(data []byte) *Fact {
	ec := NewEasyCodecWithBytes(data)
	fileHash, _ := ec.GetString("fileHash")
	fileName, _ := ec.GetString("fileName")
	time, _ := ec.GetInt32("time")

	fact := &Fact{
		fileHash: fileHash,
		fileName: fileName,
		time:     time,
		ec:       ec,
	}
	return fact
}

// 对外暴露 save 方法，供用户由 SDK 调用
//export save
func save() {
	// 获取上下文
	ctx := NewSimContext()

	// 获取参数
	fileHash, err1 := ctx.Arg("file_hash")
	fileName, err2 := ctx.Arg("file_name")
	timeStr, err3 := ctx.Arg("time")

	if err1 != SUCCESS || err2 != SUCCESS || err3 != SUCCESS {
		ctx.Log("get arg fail.")
		ctx.ErrorResult("get arg fail.")
		return
	}

	time, err := convert.StringToInt32(timeStr)
	if err != nil {
		ctx.ErrorResult(err.Error())
		ctx.Log(err.Error())
		return
	}

	// 构建结构体
	fact := NewFact(fileHash, fileName, time)

	// 序列化：两种方式
	jsonStr := fact.toJson()
	bytesData := fact.marshal()

	//发送事件
	ctx.EmitEvent("topic_vx", fact.fileHash, fact.fileName)

	// 存储数据
	ctx.PutState("fact_json", fact.fileHash, jsonStr)
	ctx.PutStateByte("fact_bytes", fact.fileHash, bytesData)

	// 记录日志
	ctx.Log("【save】 fileHash=" + fact.fileHash)
	ctx.Log("【save】 fileName=" + fact.fileName)
	// 返回结果
	ctx.SuccessResult(fact.fileName + fact.fileHash)
}

// 对外暴露 find_by_file_hash 方法，供用户由 SDK 调用
//export find_by_file_hash
func findByFileHash() {
	ctx := NewSimContext()
	// 获取参数
	fileHash, _ := ctx.Arg("file_hash")
	// 查询Json
	if result, resultCode := ctx.GetStateByte("fact_json", fileHash); resultCode != SUCCESS {
		// 返回结果
		ctx.ErrorResult("failed to call get_state, only 64 letters and numbers are allowed. got key:" + "fact" + ", field:" + fileHash)
	} else {
		// 返回结果
		ctx.SuccessResultByte(result)
		// 记录日志
		ctx.Log("get val:" + string(result))
	}

	// 查询EcBytes
	if result, resultCode := ctx.GetStateByte("fact_bytes", fileHash); resultCode == SUCCESS {
		// 反序列化
		fact := unmarshalToFact(result)
		// 返回结果
		ctx.SuccessResult(fact.toJson())
		// 记录日志
		ctx.Log("get val:" + fact.toJson())
		ctx.Log("【find_by_file_hash】 fileHash=" + fact.fileHash)
		ctx.Log("【find_by_file_hash】 fileName=" + fact.fileName)
	}
}

func main() {

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
    <td>init_contract</td>
    <td>合约的初始化函数，在合约部署时被调用，在本合约中为空。</td>
  </tr>
  <tr>
    <td>upgrade</td>
    <td>合约升级时调用的函数，在本合约中为空。</td>
  </tr>
  <tr>
    <td>save </td>
    <td>save 函数实现将文件相关信息记录到链上的功能。<br>1. save 函数先通过 [交易信息提取]API 接口GetTxId函数拿到交易哈希。<br>2. 通过 [参数处理]API 接口Arg函数拿到时间，文件哈希和文件名字等信息。<br>3. 构造 stone 结构，序列化为 byte 数据；且当序列化错误时调用 [其他辅助类]API 接口 LogMessage 函数记录相应日志。<br>4. 通过调用 [账本交互]API 接口 PutState 函数将数据记录到链上。<br>5. 通过调用 [其他辅助类]API 接口 SuccessResult 函数将操作结果记录到链上。</td>
  </tr>
  <tr>
    <td>findByFileHash</td>
    <td>通过文件哈希查询该条记录。<br>1. findByFileHash 通过 [参数处理]API 接口 Arg 函数拿到要查找的文件的文件哈希。<br>2. 通过 [账本交互]API 接口 GetState 函数获取文件的信息；若失败则通过 [其他辅助类]API 接口 ErrorResult 函数将操作结果记录到链上，否则，通过 [其他辅助类]API 接口 LogMessage 函数和 SuccessResult 函数记录相关日志和返回结果。</td>
  </tr>
</tbody>
</table>
