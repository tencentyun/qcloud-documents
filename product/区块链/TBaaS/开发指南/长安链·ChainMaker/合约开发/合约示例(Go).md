## 智能合约构成

ChainMaker Go语言的智能合约代码主要由以下接口构成：

```go
/*
Copyright (C) BABEC. All rights reserved.
SPDX-License-Identifier: Apache-2.0
一个ChainMaker的GO版本智能合约主要包括以下函数：
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

// sdk代码中，有且仅有一个main()方法
func main() {
// 空，不做任何事。仅用于对tinygo编译支持
}

// 对SDK暴露的函数
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
func main() { // sdk代码中，有且仅有一个main()方法
	// 空，不做任何事。仅用于对tinygo编译支持
}
```

### 对链暴露方法写法为

- //export method_name
- func  method_name(): 不可带参数，无返回值
- 例如：对链暴露init_contract函数

```go
//export init_contract
func init_contract() {

}
```

### 其中init_contract、upgrade方法必须有且对外暴露

- init_contract：创建合约会执行该方法
- upgrade： 升级合约会执行该方法

```go
// 安装合约时会执行此方法，必须。ChainMaker不允许用户直接调用该方法。
//export init_contract
func init_contract() {
}
// 升级合约时会执行此方法，必须。ChainMaker不允许用户直接调用该方法。
//export upgrade
func upgrade() {
}
```

## 智能合约示例

### 存证合约示例，实现功能

1、存储文件哈希、文件名称、时间和该交易的ID。

2、通过文件哈希查询该条记录

```go
package main

// 安装合约时会执行此方法，必须
//export init_contract
func init_contract() {
    // 安装时的业务逻辑，可为空

}
// 升级合约时会执行此方法，必须
//export upgrade
func upgrade() {
    // 升级时的业务逻辑，可为空

}

//export save
func save() {
	// 获取参数
	txId, _ := GetTxId()
	time, _ := Arg("time")
	fileHash, _ := Arg("file_hash")
	fileName, _ := Arg("file_name")

	// 组装
	stone := make(map[string]string,4)
	stone["txId"]=txId
	stone["time"]=time
	stone["fileHash"]=fileHash
	stone["fileName"]=fileName

	// 序列化为json bytes
	bytes,err := Marshal(stone)
	if err!=nil {
		LogMessage("marshal fail")
		ErrorResult("save fail. marshal fail")
		return
	}

	// 存储数据
	PutState("fact", fileHash, string(bytes))
	// 返回结果
	SuccessResult("ok")
}

//export find_by_file_hash
func findByFileHash() {
	// 获取参数
	fileHash, _ := Arg("file_hash")
	// 查询
	if result, resultCode := GetState("fact", fileHash); resultCode != SUCCESS {
		// 返回结果
		ErrorResult("failed to call get_state.")
	} else {
		// 记录日志
		LogMessage("get val:" + result)
		// 返回结果
		SuccessResult(result)
	}
}

func main() {

}

```


### 存证合约代码说明

- init_contract: 合约的初始化函数，在合约部署时被调用，在本合约中为空
- upgrade：合约升级时调用的函数，在本合约中为空
- save：save函数实现将文件相关信息记录到链上的功能
  1. sava函数先通过[**交易信息提取**]API接口`GetTxId`函数拿到交易哈希
  2. 紧接着通过[**参数处理**]API接口`Arg`函数拿到时间，文件哈希和文件名字等信息
  3. 再构造stone结构，序列化为byte数据；且当序列化错误时调用[**其他辅助类**]API接口`LogMessage`函数记录相应日志
  4. 再通过调用[**账本交互**]API接口`PutState`函数将数据记录到链上
  5. 最后通过调用[**其他辅助类**]API接口`SuccessResult`函数将操作结果记录到链上
- findByFileHash：通过文件哈希查询该条记录
  1. findByFileHash通过[**参数处理**]API接口`Arg`函数拿到要查找的文件的文件哈希
  2. 紧接着通过[**账本交互**]API接口`GetState`函数获取文件的信息；若失败则通过[**其他辅助类**]API接口`ErrorResult`函数将操作结果记录到链上，否则，通过[**其他辅助类**]API接口`LogMessage`函数和`SuccessResult`函数记录相关日志和返回结果。
