## 函数形态

Golang 函数形态一般如下所示：

``` go
package main

import (
    "context"
    "fmt"
    "github.com/tencentyun/scf-go-lib/cloudfunction"
)

type DefineEvent struct {
    // test event define
    Key1 string `json:"key1"`
    Key2 string `json:"key2"`
}

func hello(ctx context.Context, event DefineEvent) (string, error) {
    fmt.Println("key1:", event.Key1)
    fmt.Println("key2:", event.Key2)
    return fmt.Sprintf("Hello %s!", event.Key1), nil
}

func main() {
    // Make the handler available for Remote Procedure Call by Cloud Function
    cloudfunction.Start(hello)
}
```



代码开发时，请注意以下几点：

- 需要使用 package main 包含 main 函数。
- 引用 `github.com/tencentyun/scf-go-lib/cloudfunction` 库，在编译打包之前，执行 `go get github.com/tencentyun/scf-go-lib/cloudfunction`。
- 入口函数入参可选0 - 2参数，如包含参数，需 context 在前，event 在后，入参组合有 （），（event），（context），（context，event），具体说明请参见 [入参](#Participation)。
- 入口函数返回值可选0 - 2参数，如包含参数，需返回内容在前，error 错误信息在后，返回值组合有 （），（ret），（error），（ret，error），具体说明请参见 [返回值](#ReturnValue)。
- 入参 event 和返回值 ret，均需要能够兼容 `encoding/json` 标准库，可以进行 Marshal、Unmarshal。
- 在 main 函数中使用包内的 Start 函数启动入口函数。

## 执行方法

在创建 SCF 云函数时，均需要指定执行方法。使用 Golang 开发语言时，执行方法类似 `main`，此处 `main` 表示执行的入口文件为编译后的 `main` 二进制文件。

在使用本地 ZIP 文件上传、COS 上传等方法提交代码 ZIP 包时，请确认 ZIP 包的根目录下包含指定的二进制文件，避免因为无法查找到执行文件导致函数创建或执行失败。

### package 与 main 函数

在使用 Golang 开发云函数时，需要确保 main 函数位于 main package 中。在 main 函数中，通过使用 cloudfunction 包中的 Start 函数，启动实际处理业务的入口函数。

通过 `import "github.com/tencentyun/scf-go-lib/cloudfunction"`，可以在 main 函数中使用包内的 Start 函数。

### 入口函数

入口函数为通过 cloudfunction.Start 来启动的函数，通常通过入口函数来处理实际业务。入口函数的入参和返回值都需要根据一定的规范编写。

#### 入参

入口函数可以带有0 - 2个入参，例如：

```go
func hello()
func hello(ctx context.Context)
func hello(event DefineEvent)
func hello(ctx context.Context, event DefineEvent)
```

在带有2个入参时，需要确定 context 参数在前，自定义参数在后。

自定义参数可以为 Golang 自带基础数据结构，例如 string，int，也可以为自定义的数据结构，如示例中的 DefineEvent。在使用自定义的数据结构时，需要确定数据结构可以兼容 `encoding/json` 标准库，可以进行 Marshal、Unmarshal 操作，否则在送入入参时会因为异常而出错。

自定义数据结构对应的 JSON 结构，通常与函数执行时的入参对应。在函数调用时，入参的 JSON 数据结构将会转换为自定义数据结构变量并传递和入口函数。

> ! 部分触发器传递的入参事件结构目前已有一部分已定义，可直接使用。您可通过 [cloud event 定义](https://github.com/tencentyun/scf-go-lib/tree/master/events) 获取 golang 的库并使用。通过在代码中引用 `import "github.com/tencentyun/scf-go-lib/events"` 来直接使用。如果使用过程中发现问题，可以通过 [提交 issue ](https://github.com/tencentyun/scf-go-lib/issues/new) 或 [提交工单](https://console.cloud.tencent.com/workorder/category) 说明。

#### 返回

入口函数可以带有0 - 2个返回值，例如：
```go
func hello()()
func hello()(error)
func hello()(string, error)
```

在定义2个返回值时，需要确定自定义返回值在前，error 返回值在后。

自定义返回值可以为 Golang 自带基础数据结构，例如 string，int，也可以为自定义的数据结构。在使用自定义的数据结构时，需要确定数据结构可以兼容 `encoding/json` 标准库，可以进行 Marshal、Unmarshal 操作，否则在返回至外部接口时会因为异常转换而出错。

自定义数据结构对应的 JSON 结构，通常会在函数调用完成返回时，在平台内转换为对应的 JSON 数据结构，作为运行响应传递给调用方函数。

