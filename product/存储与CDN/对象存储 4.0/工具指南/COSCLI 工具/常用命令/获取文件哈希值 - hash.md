hash 命令用于计算本地文件的哈希值或获取对象存储（Cloud Object Storage，COS）文件的哈希值。

## 命令格式


```plaintext
./coscli hash <object-name> [flag]
```

>? 
>- 有关 bucketAlias 的说明，请参见 [下载与安装配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

hash 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                              |
| --------- | ------------- | -------------------------------------- |
|     无      | --type        | 哈希类型（md5 或 crc64，默认为 crc64） |

## 操作示例

### 计算本地文件的 crc64

```plaintext
./coscli hash ~/test.txt
```

### 获取 COS 文件的 md5

```plaintext
./coscli hash cos://bucket1/example.txt --type=md5
```
