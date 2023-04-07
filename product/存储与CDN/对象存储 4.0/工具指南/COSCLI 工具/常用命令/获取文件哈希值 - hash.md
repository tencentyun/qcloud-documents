hash 命令用于计算本地文件的哈希值或获取对象存储（Cloud Object Storage，COS）文件的哈希值。

## 命令格式


```plaintext
./coscli hash <object-name> [flag]
```

hash 命令包含以下参数：

| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
| &lt;object-name&gt; | 用于指定访问的文件。可以为本地路径或COS文件路径。COS路径支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。|本地路径：~/example.txt<br>使用桶别名指定COS文件路径：cos://bucketalias/example.txt<br>使用桶名称指定COS文件路径：cos://examplebucket-1250000000/example.txt|

hash 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                              |
| --------- | ------------- | -------------------------------------- |
| -h |  --help |   查看该命令的具体用法  |
|     无      | --type        | 哈希类型（md5 或 crc64，默认为 crc64） |

>? 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

## 操作示例

### 计算本地文件的 crc64

```plaintext
./coscli hash ~/test.txt
```

### 获取 COS 文件的 md5

```plaintext
./coscli hash cos://bucket1/example.txt --type=md5
```
