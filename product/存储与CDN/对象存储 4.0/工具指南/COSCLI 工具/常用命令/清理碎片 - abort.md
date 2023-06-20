abort 命令用于清理分块上传过程中产生的文件碎片。

## 命令格式

```plaintext
./coscli abort cos://<bucket-name>[/prefix/] [flag]
```

abort 命令包含以下参数：

| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucket-name&gt;/&lt;key&gt;  | 指定需要存储桶中的对象。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。  |使用桶别名访问：cos://example-alias<br>使用桶名称访问：cos://examplebucket-1250000000   |
| /prefix/          | 可选参数。指定某一文件夹 | /picture/ |


abort 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                |
| --------- | ------------- | ------------------------ |
| -h |  --help |   查看该命令的具体用法  |
|     无      | --include     | 包含特定模式的文件       |
|     无      | --exclude     | 排除特定模式的文件       |

>? 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。
>

## 操作示例

### 清除 bucket1 桶内的所有文件碎片

```plaintext
./coscli abort cos://bucket1
```

### 清除 bucket1 桶内 picture 文件夹下的所有碎片

```plaintext
./coscli abort cos://bucket1/picture/
```

