rm 命令用于删除文件。

## 命令格式

```plaintext
./coscli rm cos://<bucketAlias>[/prefix/] [cos://<bucket-name>[/prefix/]...] [flag]
```

>? 有关 bucketAlias 的说明，请参见 [配置](https://cloud.tencent.com/document/product/436/63144#alias)。
>

rm 命令包含以下可选 flag：

| flag 简写 | flag 全称     | flag 用途                            |
| --------- | ------------- | ------------------------------------ |
| -h        | --help        | 输出帮助信息                         |
| -c        | --config-path | 指定要使用的配置文件路径             |
|     无      | --include     | 包含特定模式的文件                   |
|     无      | --exclude     | 排除特定模式的文件                   |
| -r        | --recursive   | 是否递归地遍历文件夹下所有文件       |
| -f        | --force       | 强制删除（删除文件前不弹出确认信息） |

>?
> - `--include` 和 `--exclude` 支持标准正则表达式的语法，您可以使用它来过滤出符合特定条件的文件。
> - 使用 zsh 时，您可能需要在 pattern 串的两端加上双引号。
```
./coscli rm cos://bucket1/example/ -r --include ".*.mp4"
```

## 操作示例

### 删除文件

```plaintext
./coscli rm cos://bucket1/fig1.png
```

### 删除 pictrue 文件夹下的所有文件

```plaintext
./coscli rm cos://bucket1/pictrue/ -r
```
