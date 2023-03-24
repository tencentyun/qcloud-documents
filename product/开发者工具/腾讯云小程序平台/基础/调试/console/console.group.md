### .group

#### console.group(string label)

在调试面板中创建一个新的分组。随后输出的内容都会被添加一个缩进，表示该内容属于当前分组。调用 [console.groupEnd](./console.groupEnd.md)之后分组结束。

#### 参数

##### string label

分组标记，可选。

#### 注意

仅在工具中有效，在 vConsole 中为空函数实现。
