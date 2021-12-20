YAML 专门用来写配置文件的语言。


## 语法规则

YAML 的基本语法规则如下：
- 大小写敏感。
- 使用缩进表示层级关系。
- 缩进时**不允许**使用 Tab 键，只允许使用空格。
- 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可。



## 数据结构

YAML 支持三种数据结构：对象、数组和纯量。

- 对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
- 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
- 纯量（scalars）：单个的、不可再分的值



### 对象

简单对象

```yaml
foo: whatever
bar: stuff
```

复杂对象 
<dx-codeblock>
:::  yaml
foo: whatever 
bar: 
 - 
   fruit: apple 
   name: steve 
   sport: baseball 
 - more 
 - 
   python: rocks 
   perl: papers 
   ruby: scissorses
:::
</dx-codeblock>


转换为 JavaScript 代码后：
<dx-codeblock>
:::  javascript
{ foo: 'whatever',
  bar: 
   [ { fruit: 'apple', name: 'steve', sport: 'baseball' },
     'more',
     { python: 'rocks', perl: 'papers', ruby: 'scissorses' } ] }
:::
</dx-codeblock>


### 数组

```yaml
- Cat
- Dog
- Goldfish
```

### 纯量

纯量是最基本的、不可再分的值。

```
- 字符串
- 布尔值
- 整数
- 浮点数
- Null
- 时间
- 日期
```



#### 字符串

字符串是比较复杂的类型，举例说明：

```
str: 这是一行字符串
```

如果字符串之中包含空格或特殊字符，需要放在引号之中。

```
str: '内容: 字符串'
```

单引号和双引号都可以使用，双引号不会对特殊字符转义。

```yaml
s1: '内容\n字符串' # 会对 \n 字符转义
s2: "内容\n字符串" # 不会对 \n 字符转义
```

多行字符串可以使用 `|` 保留换行符，也可以使用 `>` 折叠换行。
<dx-codeblock>
:::  yaml
this: |
  Foo
  Bar
that: >
  Foo
  Bar
:::
</dx-codeblock>


转换为 JavaScript 代码：

```javascript
{ this: 'Foo\nBar\n', that: 'Foo Bar\n' }
```



## 工具

- 提供了一个 [YAML 的格式校验工具](https://www.bejson.com/validators/yaml_editor/)，供参考
- [YAML 和 Properties 格式互转工具](http://www.toyaml.com/)

## 参考

- [YAML 语言教程 - 阮一峰](http://www.ruanyifeng.com/blog/2016/07/yaml.html)
- [Yaml Cookbook](http://yaml.org/YAML_for_ruby.html)：提供了很多典型的 YAML 用例
- [YAML Syntax - Ansible](http://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)：写了一些 YAML 的常见陷阱
