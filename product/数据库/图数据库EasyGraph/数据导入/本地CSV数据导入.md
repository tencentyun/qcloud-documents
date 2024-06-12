# 本地CSV数据导入

## 1 概述

KonisGraph-Importer是 KonisGraph的数据导入组件，能够将多种数据源的数据转换为图的顶点和边，然后批量导入到图数据库中。 目前支持的数据源包括：

- 本地磁盘文件，支持CSV格式的文件

## 2 数据文件准备

CSV文件是带分隔符的文本文件。第一行通常是标题，记录了每一列的名称。其余的每行代表一条记录，会转换为一个顶点或一条边。行的每一列对应一个字段，会转化为顶点或边的id及属性等。
当前KonisGraph-Importer通过在映射文件中指定标题，因些数据源文件如果是带有标题行的，需要将其去掉。

## 3 图库元数据准备

在开始导入点边数据之前，首先要对自己已有的数据和对应的图模型有一个清晰的构想，然后通过可视化页面或者console插入元数据，就完成图模型的构建。用户需要关注的元数据包括

- 属性：导入的点包含哪些属性，导入的边包含哪些属性。**需要注意的是导入点的数据包含了隐含的ID属性，添加属性时容易忘记。**
- 点的元数据：点表示了一个实体对象，构建时需要了解点应该包含除ID外的哪些属性。
- 边的元数据：边表示了实例之间的关系，定义是需要了解关系的主体和客体，以及关系还包含哪些属性。

## 4 数据导入任务

准备好数据源文件、输入源映射文件及构建好图模型后，就可以将数据导入到图数据库中，导入任务由用户通过工具在命令行发起。KonisGraph-Importer参数说明

|参数 |描述信息 |
|:--|:--|
|-addr <arg> |KonisGraph图数据库内网地址:Import端口 |
|-im <arg> |上传并导入数据，如 `-im konws.csv knows.json` 。前者knows.csv表示数据文件，后者knows.json表示映射文件 |
|-lo <arg> |导入数据，如 knows.json |
|-ls |显示已上传文件列表 |
|-p <arg> |KonisGraph图数据库访问密码 |
|-u <arg> |KonisGraph图数据库访问用户 |
|-rm <arg> |删除已上传的文件 |
|-up <arg> |上传文件 |

## 5 数据导入示例

以[tinkerpop的示例](https://tinkerpop.apache.org/docs/3.5.1/tutorials/getting-started/)来说明如何进行数据导入。

## 5.1 获取KonisGraph-Importer

下载最新版本的KonisGraph-Importer包：

```
wget https://...
tar zxvf importer-client-bin.tar.gz
```

解压后会得到下述目录结构：

```
importer-client
    | - bin
    | - conf
    | - lib
    | - logs
```

在 `conf` 目录下提供了一个用于测试的数据源文件及映射文件。

## 5.2 创建图模型

图模型，即图中点/边/属性的模型，创建图模型有两种方式：图可视化的图库管理、gremlin console。

### 5.2.1 通过gremlin console创建

通过gremlin console将属性元数据插入（gremlin console操作图数据库参考)。 tinkerpop示例中包含 `name` ,  `age` ,  `lang`
,  `weight` 等4个显式属性以及 `id` 隐式属性。

```
s.addP("id", "T_LONG", "0")
s.addP("name", "T_STRING", "")
s.addP("age", "T_LONG", "0")
s.addP("lang", "T_STRING", "")
s.addP("weight", "T_DOUBLE", "0.0")
```

示例中包含两类实例：person和software。其中person包含额外的name和age属性，software包含额外的name和lang属性。添加点元数据：

```
s.addV("person", "id", ["name", "age"])
s.addV("software", "id", ["name", "lang"])
```

示例包含两类关系：knows和created。knows表示person与person之间关系，其主体和客体都是person；created表示person和software的之间的关系，主体是person，客体是software。添加边元数据：

```
s.addE("knows", "person", "person", ["weight"])
s.addE("created", "person", "software", ["weight"])
```

### 5.2.2 通过图库管理创建

通过图可视化的图库管理，创建图模型，参考[图库管理](https://cloud.tencent.com/document/product/1366/61205)。

## 5.3 准备数据源文件

### 5.3.1 顶点数据

顶点数据由一行一行数据组成，下面以csv格式进行说明。

- person顶点数据

```
1,marko,29
2,vadas,27
4,josh,32
6,peter,35
```

- software顶点数据

```
3,lop,java
5,ripple,java
```

### 5.3.2 边数据

边数据文件由一行一行数据组成，每一行表示一条边。其中部分列作为源顶点和目标顶点的id，其他列作为边属性

- knows 边数据

```
1,2,0.5
1,4,1.0
```

- created 边数据

```
1,3,0.4
4,3,0.4
6,3,0.2
4,5,1.0
```

### 5.3.3 编写映射文件

映射文件用于描述如何将输入源数据与图的顶点类型或边类型建立映射文件，以json格式组织。

- person顶点映射文件

```json
{
	"type": "VERTEX",
	"graph": "default",
	"label": "person",
	"data_source": {
		"source_type": "CSV",
		"csv_source": {
			"filename": "person.csv",
			"header": [
				"id",
				"name",
				"age"
			],
			"delimiter": ","
		}
	}
}
```

- software顶点映射文件

```json
{
	"type": "VERTEX",
	"graph": "default",
	"label": "software",
	"data_source": {
		"source_type": "CSV",
		"csv_source": {
			"filename": "software.csv",
			"header": [
				"id",
				"name",
				"lang"
			],
			"delimiter": ","
		}
  }
}
```

- knows边映射文件

```json
{
	"type": "EDGE",
	"graph": "default",
	"label": "knows",
	"data_source": {
		"source_type": "CSV",
		"csv_source": {
			"filename": "knows.csv",
			"header": [
				"SID",
				"OID",
				"weight"
			],
			"delimiter": ","
		}
  }
}
```

- created边映射文件

```json
{
	"type": "EDGE",
	"graph": "default",
	"label": "created",
	"data_source": {
		"source_type": "CSV",
		"csv_source": {
			"filename": "created.csv",
			"header": [
				"SID",
				"OID",
				"weight"
			],
			"delimiter": ","
		}
  }
}
```

### 5.3.4 执行命令导入

```bash
sh bin/start.sh -u steven -p rainbow-dash -im person.csv person.json -addr localhost:8180
sh bin/start.sh -u steven -p rainbow-dash -im software.csv software.json -addr localhost:8180
sh bin/start.sh -u steven -p rainbow-dash -im knows.csv knows.json -addr localhost:8180
sh bin/start.sh -u steven -p rainbow-dash -im created.csv created.json -addr localhost:8180
```
