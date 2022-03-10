本文介绍如何使用 Go 语言连接和操作图数据库 KonisGraph。以 [Gremlin-console tutorials](https://tinkerpop.apache.org/docs/3.5.1/tutorials/getting-started/#_the_first_five_minutes) 中的人和软件的关系图为示例。
![enter image description here](https://main.qcloudimg.com/raw/51a52aabf2b24289aa61f713a8cd1eb4.png)
如图所示，整个图包含2类点 person 和 software，2类边 knows 和 created，和几类属性 id、name、age、lang、weight。

## 环境准备
1. 安装 Go 语言环境，参考 [Go 语言官网](https://go.dev/doc/install)。
2. 获取图数据库的连接参数。在 [控制台](https://console.cloud.tencent.com/konisgraph) 实例详情页中可以查看实例的 VIP 和 PORT，即内网地址和 Gremlin 端口。

## 示例程序
### 新建一个 demo 目录，并初始化 module
```
mkdir graph_demo
cd graph_demo
go mod init demo
```

#### 示例项目目录结构
```
|- graph_demo
	|- go.mod
	|- go.sum
	|- main.go
	|- model
		|- meta.go
		|- property.go
		|- vertex.go
		|- edge.go
```

### 定义点、边及属性等模型
#### meta.go: 属性、点边等对应的元数据定义
```go
package model

type PropertyType string

const (
	PropertyLong   = "T_LONG"
	PropertyInt    = "T_INT"
	PropertyInt64  = "T_INT64"
	PropertyString = "T_STRING"
	PropertyDouble = "T_DOUBLE"
)

type PropertyMeta struct {
	Label   string
	Type    PropertyType
	Default string
}

type VertexMeta struct {
	Label      string
	Primary    string
	Properties []string
}

type EdgeMeta struct {
	Label          string
	SrcVertexLabel string
	DstVertexLabel string
	Properties     []string
}
```

#### property.go: 属性模型定义
```go
package model

type Property struct {
	Type  string        `json:"@type"`
	Value PropertyValue `json:"@Value"`
}

type PropertyValue struct {
	Key   string      `json:"key"`
	Value interface{} `json:"value"`
}
```

#### vertex.go: 点模型定义
```go
package model

import "encoding/json"

type VertexList struct {
	listOfVertices List
	Vertices       []Vertex
}

type List struct {
	Type  string        `json:"@type"`
	Value []interface{} `json:"@value"`
}

type Vertex struct {
	Type  string      `json:"@type"`
	Value VertexValue `json:"@value"`
}

type VertexValue struct {
	ID         interface{}           `json:"id"`
	Label      string                `json:"label"`
	Properties map[string][]Property `json:"properties,omitempty"`
}

func (vl *VertexList) UnmarshalJSON(data []byte) error {
	if err := json.Unmarshal(data, &vl.listOfVertices); err == nil {
		if data, err = json.Marshal(vl.listOfVertices.Value); err != nil {
			return err
		}
	}

	return json.Unmarshal(data, &vl.Vertices)
}
```

#### edge.go: 边模型定义
```go
package model

import "encoding/json"

type EdgeList struct {
	listOfEdges List
	Edges       []Edge
}

type Edge struct {
	Type  string    `json:"@type"`
	Value EdgeValue `json:"@value"`
}

type EdgeValue struct {
	ID         interface{}           `json:"id"`
	Label      string                `json:"label"`
	InVLabel   string                `json:"inVLabel,omitempty"`
	OutVLabel  string                `json:"outVLabel,omitempty"`
	InV        interface{}           `json:"inV,omitempty"`
	OutV       interface{}           `json:"outV,omitempty"`
	Properties map[string][]Property `json:"properties,omitempty"`
}

func (el *EdgeList) UnmarshalJSON(data []byte) error {
	if err := json.Unmarshal(data, &el.listOfEdges); err == nil {
		if data, err = json.Marshal(el.listOfEdges.Value); err != nil {
			return err
		}
	}

	return json.Unmarshal(data, &el.Edges)
}
```

### 数据库操作
```go
package main

import (
	"fmt"
	"log"
	"strings"
	"tutorial/model"

	"github.com/northwesternmutual/grammes"
)

type Tutorial struct {
	*grammes.Client
}

func New(host string, port int, username, password string) (*Tutorial, error) {
	url := fmt.Sprintf("ws://%s:%d", host, port)
	c, err := grammes.DialWithWebSocket(url, grammes.WithAuthUserPass(username, password))
	if err != nil {
		return nil, err
	}
	return &Tutorial{Client: c}, nil
}

func (t *Tutorial) CreatePropertyMetas(metas ...model.PropertyMeta) error {
	for _, meta := range metas {
		expr := fmt.Sprintf(`s.addP("%s", "%s", "%s")`, meta.Label, meta.Type, meta.Default)
		_, err := t.ExecuteStringQuery(expr)
		if err != nil {
			return err
		}
	}
	return nil
}

func (t *Tutorial) CreateVertexMetas(metas ...model.VertexMeta) error {
	for _, meta := range metas {
		expr := fmt.Sprintf(`s.addV("%s", "%s", ["%s"])`, meta.Label, meta.Primary, strings.Join(meta.Properties, "\",\""))
		_, err := t.ExecuteStringQuery(expr)
		if err != nil {
			return err
		}
	}
	return nil
}

func (t *Tutorial) CreateEdgeMetas(metas ...model.EdgeMeta) error {
	for _, meta := range metas {
		expr := fmt.Sprintf(`s.addE("%s", "%s", "%s", ["%s"])`, meta.Label, meta.SrcVertexLabel, meta.DstVertexLabel,
			strings.Join(meta.Properties, "\",\""))
		_, err := t.ExecuteStringQuery(expr)
		if err != nil {
			return err
		}
	}

	return nil
}

func createMetas(tutorial *Tutorial) {
	propMetas := []model.PropertyMeta{
		{Label: "id", Type: model.PropertyLong, Default: "0"},
		{Label: "name", Type: model.PropertyString, Default: ""},
		{Label: "age", Type: model.PropertyInt, Default: "0"},
		{Label: "weight", Type: model.PropertyDouble, Default: "0.0"},
		{Label: "lang", Type: model.PropertyString, Default: ""},
	}
	if err := tutorial.CreatePropertyMetas(propMetas...); err != nil {
		log.Fatal("create property meta err ", err)
	}

	vertexMetas := []model.VertexMeta{
		{Label: "person", Primary: "id", Properties: []string{"name", "age"}},
		{Label: "software", Primary: "id", Properties: []string{"name", "lang"}},
	}
	if err := tutorial.CreateVertexMetas(vertexMetas...); err != nil {
		log.Fatal("create vertex meta err ", err)
	}

	edgeMetas := []model.EdgeMeta{
		{Label: "knows", SrcVertexLabel: "person", DstVertexLabel: "person", Properties: []string{"weight"}},
		{Label: "created", SrcVertexLabel: "person", DstVertexLabel: "software", Properties: []string{"weight"}},
	}
	if err := tutorial.CreateEdgeMetas(edgeMetas...); err != nil {
		log.Fatal("create edge meta err ", err)
	}
}

func addVertexAndEdge(tutorial *Tutorial) {
	g := grammes.Traversal()

	tutorial.ExecuteQuery(g.AddV("person").Property("id", 1).Property("name", "marko").Property("age", 29))
	tutorial.ExecuteQuery(g.AddV("person").Property("id", 2).Property("name", "vadas").Property("age", 27))
	tutorial.ExecuteQuery(g.AddV("person").Property("id", 4).Property("name", "josh").Property("age", 32))
	tutorial.ExecuteQuery(g.AddV("person").Property("id", 6).Property("name", "peter").Property("age", 35))

	tutorial.ExecuteQuery(g.AddV("software").Property("id", 3).Property("name", "lop").Property("lang", "java"))
	tutorial.ExecuteQuery(g.AddV("software").Property("id", 5).Property("name", "ripple").Property("lang", "java"))

	tutorial.ExecuteQuery(g.AddE("knows").From(g.V(1)).To(g.V(2)))
	tutorial.ExecuteQuery(g.AddE("knows").From(g.V(1)).To(g.V(4)))
	tutorial.ExecuteQuery(g.AddE("created").From(g.V(1)).To(g.V(3)).Property("weight", 0.4))
	tutorial.ExecuteQuery(g.AddE("created").From(g.V(6)).To(g.V(3)).Property("weight", 0.2))
	tutorial.ExecuteQuery(g.AddE("created").From(g.V(4)).To(g.V(3)).Property("weight", 0.4))
	tutorial.ExecuteQuery(g.AddE("created").From(g.V(4)).To(g.V(5)).Property("weight", 1.0))
}

func main() {
	tutorial, err := New("KONISGRAPH_VIP", KONISGRAPH_PORT, "your useranme", "your password")
	//KONISGRAPH_VIP 图数据库 KonisGraph 实例的内网地址 vip，如 10.xx.xx.107
	//KONISGRAPH_PORT 图数据库 KonisGraph 实例的 Gremlin 端口，如 8186
	if err != nil {
		log.Fatal("open gremlin connection err ", err)
	}

	// 创建属性、点、边等元数据
	createMetas(tutorial)

	// 添加点和边
	addVertexAndEdge(tutorial)

	// 做一些查询
	g := grammes.Traversal()
	// 查看 marko 的信息
	data, _ := tutorial.ExecuteQuery(g.V().HasLabel("person").Has("name", "marko").ValueMap())
	for _, item := range data {
		log.Println(string(item))
	}

	// 查找 marko 都认识哪些人
	data, _ = tutorial.ExecuteQuery(g.V().HasLabel("person").Has("name", "marko").Out("knows"))
	for _, item := range data {
		var vertices model.VertexList
		if err := vertices.UnmarshalJSON(item); err != nil {
			log.Fatal("unmarshal resp err: ", err)
		}
		var names []interface{}
		for _, vertex := range vertices.Vertices {
			names = append(names, vertex.Value.Properties["name"][0].Value.Value)
		}
		log.Print("Who marko knows: ", names)
	}

	// 查找哪些人创建了软件 lop
	data, _ = tutorial.ExecuteQuery(g.V().HasLabel("software").Has("name", "lop").In("created"))
	for _, item := range data {
		var vertices model.VertexList
		if err := vertices.UnmarshalJSON(item); err != nil {
			log.Fatal("unmarshal resp err: ", err)
		}
		var names []interface{}
		for _, vertex := range vertices.Vertices {
			names = append(names, vertex.Value.Properties["name"][0].Value.Value)
		}
		log.Println("Who creates software lop: ", names)
	}
}
```

## 运行示例程序
```shell
go run main.go
```
