restore 命令用于取回归档文件。
>! 关于取回归档文件的更多信息，请参见 [POST Object restore - API 文档](https://cloud.tencent.com/document/product/436/12633)。

## 命令格式

```plaintext
./coscli restore cos://<bucket-name>[/prefix/] [flag]
```


restore 命令包含以下参数：

| 参数格式  | 参数用途     | 示例                |
| --------- | ------------- | ------------------------ |
 cos://&lt;bucket-name&gt; | 指定需要访问的存储桶。支持使用 [配置参数](https://cloud.tencent.com/document/product/436/63144#.E9.85.8D.E7.BD.AE.E5.8F.82.E6.95.B0) 中的桶别名，或桶名称进行访问。如使用桶名称访问，需要额外携带 `endpoint` flag。  |使用桶别名访问：cos://example-alias<br>使用桶名称访问：cos://examplebucket-1250000000  |
| /prefix/          | 可选参数。指定某一文件夹 | /picture/ |

restore 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                         |
| --------- | ------------- | --------------------------------- |
| -h |  --help |   查看该命令的具体用法  |
|     无      | --include     | 包含特定模式的文件                |
|     无      | --exclude     | 排除特定模式的文件                |
| -d        | --days        | 指定解冻对象所生成的临时文件的过期时间（默认为3天） |
| -m        | --mode        | 指定恢复模式（默认 Standard）      |
| -r        | --recursive   | 递归遍历文件夹                  |

>?
> - `--include` 和 `--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
> - 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
```
./coscli restore cos://bucket1/example/ -r --include ".*.mp4"
```
>- 关于此命令的其他通用选项（例如切换存储桶、切换用户账号等），请参见 [通用选项](https://cloud.tencent.com/document/product/436/71763) 文档。


## 操作示例

### 以标准取回模式取回 bucket1 桶内的归档文件

```plaintext
./coscli restore cos://bucket1/picture.jpg
```

### 以快速取回模式取回 bucket1 桶内 picture 文件夹下的所有归档文件

```plaintext
./coscli restore cos://bucket1/picture/ -r --mode Expedited
```

>? 在执行此命令前，您需要保证文件夹下所有文件都是相同类型的（例如 ARCHIVE 类型）。如果存在不同类型的文件，请配合使用 `--include` 或 `--exclude` 将相同类型的文件过滤出来。
>

