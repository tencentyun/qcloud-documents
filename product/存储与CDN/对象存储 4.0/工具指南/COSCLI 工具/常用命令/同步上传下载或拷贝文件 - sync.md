## 命令格式

sync 命令用于同步上传、下载或拷贝文件，与 cp 命令不同的是：sync 命令首先会对比同名文件的 crc64，如果 crc64 值相同则不进行传输。

```plaintext
./coscli sync <source_path> <destination_path> [flag]
```


sync 命令包含以下参数：

| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
|  source_path | 源文件路径。可以为本地路径或 COS 文件路径。COS 路径支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。|本地路径：~/example.txt<br>使用桶别名指定 COS 文件路径：cos://bucketalias/example.txt<br>使用桶名称指定 COS 文件路径：cos://examplebucket-1250000000/example.txt|
|   destination_path | 目的文件路径。可以为本地路径或 COS 文件路径。COS 路径支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。|本地路径：~/example.txt<br>使用桶别名指定 COS 文件路径：cos://bucketalias/example.txt<br>使用桶名称指定 COS 文件路径：cos://examplebucket-1250000000/example.txt|

sync 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                      |
| --------- | ------------- | ------------------------------ |
|    无       | --include     | 包含特定模式的文件             |
|   无         | --exclude     | 排除特定模式的文件             |
| -r        | --recursive   | 是否递归遍历文件夹下所有文件 |
|   无       | --storage-class | 指定上传文件的存储类型（默认 STANDARD），更多存储类型，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417) |
|   无       | --part-size     | 文件分块大小（默认32MB，最大支持5GB）     |
|   无       | --thread-num    | 并发线程数（默认并发5）      |
|   无       | --rate-limiting | 单链接速率限制（0.1 - 100MB/s）       |
| 无 | --snapshot-path | 指定保存上传或者下载文件时的快照信息所在的目录。在下一次上传或者下载文件时，coscli 会读取指定目录下的快照信息进行增量上传或者下载。本选项用来加速目录文件同步。 |
| 无 | --meta | 上传文件的元信息。包括部分 HTTP 标准属性（HTTP Header）以及以 `x-cos-meta-` 开头的用户自定义元数据（User Meta）。文件元信息格式为 `header:value#header:value`，示例为 `Expires:2022-10-12T00:00:00.000Z#Cache-Control:no-cache#Content-Encoding:gzip#x-cos-meta-x:x`。 |


>?
> - sync 命令在上传和下载大文件时会自动启用并发上传/下载。
> - 当文件大于 `--part-size` 时，COSCLI 会先将文件按 `--part-size` 进行切块，之后用 `--thread-num` 个线程并发地执行上传/下载任务。
> - 每个线程都会维护一个链接，对于每个链接，您可以使用 `--rate-limiting` 参数对单链接进行限速，当启用并发上传/下载时，总速率为 `--thread-num * --rate-limiting`。
> - 当以分块形式上传/下载文件时，会默认开启断点续传。
> - `--include` 和 `--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
> - 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
> - snapshot-path 不要设置到为待迁移目录或其子目录。coscli 不会主动删除 snapshot-path 文件夹中的快照信息。为避免快照信息过多，请定期删除 snapshot-path 文件夹内无用的快照。
```
./coscli sync ~/test/ cos://bucket1/example/ -r --include ".*.txt" --snapshot-path=/path/snapshot-path  --meta=x-cos-meta-a:a#ContentType:text#Expires:2022-10-12T00:00:00.000Z
```
> - 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。


## 操作示例

### 同步上传文件

```plaintext
./coscli sync ~/example.txt cos://bucket1/example.txt
```

### 同步下载文件

```plaintext
./coscli sync cos://bucket1/example.txt ~/example.txt
```

### 桶内同步拷贝文件

```plaintext
./coscli sync cos://bucket1/example.txt cos://bucket1/example_copy.txt
```

### 跨桶同步拷贝文件

```plaintext
./coscli sync cos://bucket1/example.txt cos://bucket2/example_copy.txt
```
