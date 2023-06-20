signurl 命令用于获取某个对象的预签名 URL，可以通过此 URL 匿名访问对象。

## 命令格式

```plaintext
./coscli signurl cos://<bucket-name>/<key> [flag]
```


signurl 命令包含以下参数：

| 参数格式          | 参数用途       | 示例                 |
| ----------------- | -------------- | -------------------- |
 cos://&lt;bucket-name&gt;/&lt;key&gt;  | 指定需要存储桶中的对象。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。  |使用桶别名访问：cos://example-alias/test.txt<br>使用桶名称访问：cos://examplebucket-1250000000/test.txt  |


signurl 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                    |
| --------- | ------------- | ---------------------------- |
| -h |  --help |   查看该命令的具体用法  |
| -t        | --time        | 设置 URL 过期时间（默认1000s） |

>? 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

## 操作示例

### 获取 bucket1 桶内 picture.jpg 的预签名 URL

```plaintext
./coscli signurl cos://bucket1/picture.jpg
```

### 获取 bucket2 桶内 picture.jpg 的预签名 URL，并设置 URL 的过期时间为1314秒

```plaintext
./coscli signurl cos://bucket2/picture.jpg --time 1314
```

