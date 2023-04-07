bucket-tagging 命令用于创建（修改）、获取、删除存储桶标签。每个存储桶下最多支持50组标签。

## 命令格式

```plaintext
./coscli bucket-tagging --method [method] cos://<bucket-name> [tag_key]#[tag_value]
```


bucket-tagging 命令包含以下参数：

| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucket-name&gt; | 指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。  |使用桶别名访问：cos://example-alias<br>使用桶名称访问：cos://examplebucket-1250000000 |

bucket-tagging 命令包含以下可选 flag：

|flag 简写|flag 全称| flag 用途|
|----|----|----|
| -h |  --help |   查看该命令的具体用法  |
|无|--method|指定需要进行的操作，包括 put（添加标签）、get（查询标签）、delete（删除标签）   |

>? 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>


## 添加或修改存储桶标签

存储桶标签用一组健值对（Key-Value）来表示，只有存储桶所有者及拥有 PutBucketTagging 权限的用户才可以添加或修改存储桶标签，否则会返回错误码 403 AccessDenied。

### 命令格式

```plaintext
./coscli bucket-tagging --method put cos://bucketAlias key1#value1 key2#value2
```
其中，`key#value`表示标签键值对 Key-Value，key 和 value 之间以`#`分割。若存储桶未设置标签，此命令将为存储桶添加指定的标签；若存储桶已设置标签，此命令将覆盖原有的标签。

### 操作示例

为桶别名为 example-alias 的存储桶配置两组标签，其中一组标签的 key 为1，value 为111，一组标签的 key 为2，value 为222。命令如下：

```plaintext
./coscli bucket-tagging --method put cos://exmaple-alias 1#111 2#222
```

## 查询存储桶标签
### 命令格式

```plaintext
./coscli bucket-tagging --method get cos://bucketAlias
```

### 操作示例

```plaintext
./coscli bucket-tagging --method get cos://exmaple-alias
```

以下输出结果表明桶别名为 exmaple-alias 的存储桶配置了两组标签，其中一组标签的 key 为1，value 为111，一组标签的 key 为2，value 为222。

```plaintext
  KEY | VALUE  
------+--------
    1 |   111  
    2 |   222 
```

## 删除存储桶标签

### 命令格式

```plaintext
./coscli bucket-tagging --method delete cos://bucketAlias
```

### 操作示例

```plaintext
./coscli bucket-tagging --method delete cos://exmaple-alias
```
