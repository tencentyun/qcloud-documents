
## Python 原生类型方法
为了方便用户对 Python 原生类型的操作，Dataway 支持 Python 原生类型的常用方法：
<table>
    <tr>
        <th>数据类型</th>
        <th>方法</th>
				<th>方法类型</th>
				<th>功能</th>
				<th>输出类型</th>
    </tr>
		<tr>
        <td rowspan="15">str</td>
        <td>endswith(suffix[, start[, end]])</td>
				<td>方法</td>
				<td>后缀对比</td>
				<td>bool</td>
    </tr>
		<tr>
        <td>split(sep=None, maxsplit=-1)</td>
				<td>方法</td>
				<td>分割</td>
				<td>list</td>
    </tr>
		<tr>
        <td>startswith(prefix[, start[, end]])</td>
				<td>方法</td>
				<td>前缀对比</td>
				<td>bool</td>
    </tr>
		<tr>
        <td>count(sub[, start[, end]])</td>
				<td>方法</td>
				<td>统计子串数量</td>
				<td>int</td>
    </tr>
		<tr>
        <td>find(sub[, start[, end]])</td>
				<td>方法</td>
				<td>查找匹配子串</td>
				<td>int</td>
    </tr>
		<tr>
        <td>format(*args, **kwargs)</td>
				<td>方法</td>
				<td>格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td>index(sub[, start[, end]])</td>
				<td>方法</td>
				<td>索引匹配子串</td>
				<td>int</td>
    </tr>
		<tr>
        <td>isascii()</td>
				<td>方法</td>
				<td>返回全是 ASCII 字符</td>
				<td>bool</td>
    </tr>
		<tr>
        <td>isspace()</td>
				<td>方法</td>
				<td>返回是否非空且全是空白字符</td>
				<td>bool</td>
    </tr>
		<tr>
        <td>encode(encoding="utf-8", errors="strict")</td>
				<td>方法</td>
				<td>编码</td>
				<td>bytes</td>
    </tr>
		<tr>
        <td>join(iterable)</td>
				<td>方法</td>
				<td>拼接</td>
				<td>str</td>
    </tr>
		<tr>
        <td>lower()</td>
				<td>方法</td>
				<td>小写</td>
				<td>str</td>
    </tr>
		<tr>
        <td>replace(old, new[, count])</td>
				<td>方法</td>
				<td>替换</td>
				<td>str</td>
    </tr>
		<tr>
        <td>strip([chars])</td>
				<td>方法</td>
				<td>移除特定字符组成的前后缀</td>
				<td>str</td>
    </tr>
		<tr>
        <td>upper()</td>
				<td>方法</td>
				<td>大写</td>
				<td>str</td>
		</tr>
		<tr>
        <td rowspan="10">bytes</td>
        <td>count(sub[, start[, end]])</td>
				<td>方法</td>
				<td>统计子串数量</td>
				<td>int</td>
    </tr>
		<tr>
        <td>find(sub[, start[, end]])</td>
				<td>方法</td>
				<td>查找匹配子串</td>
				<td>int</td>
    </tr>
		<tr>
        <td>index(sub[, start[, end]])</td>
				<td>方法</td>
				<td>索引匹配子串</td>
				<td>int</td>
    </tr>
		<tr>
        <td>decode(encoding="utf-8", errors="strict")</td>
				<td>方法</td>
				<td>解码</td>
				<td>str</td>
    </tr>
		<tr>
        <td>replace(old, new[, count])</td>
				<td>方法</td>
				<td>替换</td>
				<td>bytes</td>
    </tr>
		<tr>
        <td>rstrip([chars])</td>
				<td>方法</td>
				<td>移除特定字符集合组成的后缀</td>
				<td>bytes</td>
    </tr>
		<tr>
        <td>strip([chars])</td>
				<td>方法</td>
				<td>移除特定字符集合组成的前后缀</td>
				<td>bytes</td>
    </tr>
		<tr>
        <td>split(sep=None, maxsplit=-1)</td>
				<td>方法</td>
				<td>分割</td>
				<td>list</td>
    </tr>
		<tr>
        <td>startswith(prefix[, start[, end]])</td>
				<td>方法</td>
				<td>前缀对比</td>
				<td>bool</td>
    </tr>
		<tr>
        <td>endswith(prefix[, start[, end]])</td>
				<td>方法</td>
				<td>后缀对比</td>
				<td>bool</td>
    </tr>
		<tr>
        <td>float</td>
        <td>is_integer()</td>
				<td>方法</td>
				<td>是否整数</td>
				<td>bool</td>
    </tr>
		<tr>
        <td rowspan="2">list</td>
        <td>count(x)</td>
				<td>方法</td>
				<td>统计元素数量</td>
				<td>int</td>
    </tr>
		<tr>
        <td>index(sub[, start[, end]])</td>
				<td>方法</td>
				<td>索引元素</td>
				<td>int</td>
    </tr>
		<tr>
        <td rowspan="2">tuple</td>
        <td>count(x)</td>
				<td>方法</td>
				<td>统计元素数量</td>
				<td>int</td>
    </tr>
		<tr>
        <td>index(sub[, start[, end]])</td>
				<td>方法</td>
				<td>索引元素</td>
				<td>int</td>
    </tr>
		<tr>
        <td rowspan="2">dict</td>
        <td>get(key[, default])</td>
				<td>方法</td>
				<td>获取 key 对应值</td>
				<td>any</td>
    </tr>
		<tr>
        <td>items</td>
				<td>方法</td>
				<td>获取键值对列表</td>
				<td>list</td>
    </tr>
		<tr>
        <td>set</td>
        <td>union(*others)</td>
				<td>方法</td>
				<td>返回求并集后的新集合</td>
				<td>set</td>
    </tr>
		<tr>
        <td rowspan="7">datetime.datetime</td>
        <td>today()</td>
				<td>类方法</td>
				<td>无时区当前时间</td>
				<td>datetime.datetime</td>
		</tr>
		<tr>
        <td>fromtimestamp(timestamp, tz=None)</td>
				<td>类方法</td>
				<td>从时间戳构造时间</td>
				<td>datetime.datetime</td>
    </tr>
		<tr>
        <td>now()</td>
				<td>类方法</td>
				<td>带时区当前时间</td>
				<td>datetime.datetime</td>
    </tr>
		<tr>
        <td>strptime(date_string, format)</td>
				<td>类方法</td>
				<td>从格式化构造时间</td>
				<td>datetime.datetime</td>
    </tr>
		<tr>
        <td>time()</td>
				<td>方法</td>
				<td>转换为时钟</td>
				<td>datetime.time</td>
    </tr>
		<tr>
        <td>date()</td>
				<td>方法</td>
				<td>转换为日期</td>
				<td>datetime.date</td>
    </tr>
		<tr>
        <td>strftime(format)</td>
				<td>方法</td>
				<td>格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td rowspan="2">datetime.date</td>
        <td>today()</td>
				<td>类方法</td>
				<td>当前日期</td>
				<td>datetime.date</td>
		</tr>
		<tr>
        <td>strftime(format)</td>
				<td>方法</td>
				<td>格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td rowspan="1">datetime.time</td>
        <td>strftime(format)</td>
				<td>方法</td>
				<td>格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td rowspan="3">DataSet</td>
        <td>id()</td>
				<td>方法</td>
				<td>获取数据集 ID</td>
				<td>int</td>
    </tr>
		<tr>
        <td>partitions()</td>
				<td>方法</td>
				<td>获取数据集分区数</td>
				<td>int</td>
    </tr>
		<tr>
        <td>schema()</td>
				<td>方法</td>
				<td>获取数据集 schema</td>
				<td>Schema</td>
    </tr>
		<tr>
        <td rowspan="3">Record</td>
        <td>data()</td>
				<td>方法</td>
				<td>以列表形式返回各项数据</td>
				<td>list</td>
    </tr>
		<tr>
        <td>get(name, default=None)</td>
				<td>方法</td>
				<td>获取字段名对应数据</td>
				<td>any</td>
    </tr>
		<tr>
        <td>schema()</td>
				<td>方法</td>
				<td>获取数据集 schema</td>
				<td>Schema</td>
    </tr>
</table>


## 内置常量和函数
表达式模式支持常量：None、True 和 False。除此之外，为了方便用户使用，表达式模式内置了许多函数，用户可以调用相关函数，快速实现对应的功能，获取所需数据。

| 内置函数 | 函数说明 | 
|---------|---------|
| abs(x) | 返回绝对值（整数、浮点数） |
| all(iterable) | 返回是否所有元素为真或为空 |
| any(iterable) | 返回是否存在元素为真 |
| ascii(object) | 打印 object 但不处理非 ASCII 字母 |
| bool([x]) | 转换为 bool |
| bytes([source[,encoding[,errors]]]) | 转换为 bytes |
| chr(i) | 返回 int 对应的 unicode |
| dict(kwarg)/dict(mapping,kwarg)/dict(iterable,kwarg) | 转换为 dict |
| float([x]) | 转换为 float | 
| int(x)/int(x,base) | 转换为 int |
| len(s) | 返回长度 |
| list([iterable]) | 转换为list |
| max(iterable,[,key,default])/max(arg1,arg2,args[,key]) | 返回最大值 |
| min(iterable,[,key,default])/min(arg1,arg2,args[,key]) | 返回最小值 |
| ord(c) | 返回 char 对应编码 | 
| pow(x,y[,z]) | 返回指数 |
| range(stop)/(start,stop[,step]) | 返回不可改列表 |
| repr(object) | 返回可打印对象信息 |
| round(number[,ndigits]) | 四舍五入偏偶数 |
| set([iterable]) | 转换为集合 |
| str(object)/(object,encoding,errors) | 转换为 str |
| sum(iterable[,start]) | 求和 |
| tuple([iterable]) | 转换为 tuple |
| type(object) | 返回数据类型 |



## 其他第三方模块
表达式模式支持部分常见 Python 第三方模块。

<table>
    <tr>
        <th>模块</th>
				<th>特性</th>
				<th>特性类型</th>
				<th>特性描述</th>
				<th>特性输出</th>
		</tr>
		<tr>
        <td rowspan="9">time</td>
        <td>asctime([t])</td>
				<td>函数</td>
				<td>struct_time 格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td>ctime([secs])</td>
				<td>函数</td>
				<td>时间戳格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td>gmtime([secs])</td>
				<td>函数</td>
				<td>生成 UTC 时区的struct_time</td>
				<td>struct_time</td>
    </tr>
		<tr>
        <td>localtime([secs])</td>
				<td>函数</td>
				<td>生成本地 struct_time</td>
				<td>struct_time</td>
    </tr>
		<tr>
        <td>mktime(t)</td>
				<td>函数</td>
				<td>struct_time 生成时间戳</td>
				<td>float</td>
    </tr>
		<tr>
        <td>strftime(format[,t])</td>
				<td>函数</td>
				<td>struct_time 定制格式化</td>
				<td>str</td>
    </tr>
		<tr>
        <td>strptime(string[,format])</td>
				<td>函数</td>
				<td>字符串构建 struct_time</td>
				<td>struct_time</td>
    </tr>
		<tr>
        <td>time()</td>
				<td>函数</td>
				<td>生成当前时间戳</td>
				<td>float</td>
    </tr>
		<tr>
        <td>time_ns()</td>
				<td>函数</td>
				<td>生成当前时间戳（纳秒）</td>
				<td>int</td>
    </tr>
    <tr>
        <td rowspan="13">math</td>
        <td>e</td>
				<td>常量</td>
				<td>自然对数</td>
				<td>float</td>
    </tr>
		<tr>
        <td>pi</td>
				<td>常量</td>
				<td>圆周率</td>
				<td>float</td>
    </tr>
		<tr>
        <td>sqrt(x)</td>
				<td>函数</td>
				<td>开方</td>
				<td>float</td>
    </tr>
		<tr>
        <td>log(x[,base])</td>
				<td>函数</td>
				<td>对数</td>
				<td>float</td>
    </tr>
		<tr>
        <td>ceil(x)</td>
				<td>函数</td>
				<td>向上取整</td>
				<td>int</td>
    </tr>
		<tr>
        <td>floor(x)</td>
				<td>函数</td>
				<td>向下取整</td>
				<td>int</td>
    </tr>
		<tr>
        <td>cos(x)</td>
				<td>函数</td>
				<td>余弦</td>
				<td>float</td>
    </tr>
		<tr>
        <td>fabs(x)</td>
				<td>函数</td>
				<td>绝对值</td>
				<td>float</td>
    </tr>
		<tr>
        <td>log2(x)</td>
				<td>函数</td>
				<td>以2为底对数</td>
				<td>float</td>
    </tr>
		<tr>
        <td>log10(x)</td>
				<td>函数</td>
				<td>以10为底对数</td>
				<td>float</td>
    </tr>
		<tr>
        <td>pow(x,y)</td>
				<td>函数</td>
				<td>指数</td>
				<td>float</td>
    </tr>
		<tr>
        <td>sin(x)</td>
				<td>函数</td>
				<td>正弦</td>
				<td>float</td>
    </tr>
		<tr>
        <td>tan(x)</td>
				<td>函数</td>
				<td>正切</td>
				<td>float</td>
    </tr>
		<tr>
        <td rowspan="2">json</td>
        <td>dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)</td>
				<td>函数</td>
				<td>json 编码</td>
				<td>str</td>
    </tr>
		<tr>
        <td>loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)</td>
				<td>函数</td>
				<td>json 解码</td>
				<td>any</td>
    </tr>
		<tr>
        <td rowspan="2">base64</td>
        <td>b64encode(s, altchars=None)</td>
				<td>函数</td>
				<td>base64 编码</td>
				<td>bytes</td>
    </tr>
		<tr>
        <td>b64decode(s, altchars=None, validate=False)</td>
				<td>函数</td>
				<td>base64 解码</td>
				<td>bytes</td>
    </tr>
		<tr>
        <td rowspan="2">random</td>
        <td>randint(a, b)</td>
				<td>函数</td>
				<td>[a,b]随机整数</td>
				<td>int</td>
    </tr>
		<tr>
        <td>random()</td>
				<td>函数</td>
				<td>[0,1)随机浮点数</td>
				<td>float</td>
    </tr>
		<tr>
        <td rowspan="2">urllib</td>
        <td>parse.quote(string, safe='/', encoding=None, errors=None)</td>
				<td>函数</td>
				<td>特殊字符转码</td>
				<td>str</td>
    </tr>
		<tr>
        <td>parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None)</td>
				<td>函数</td>
				<td>url 编码</td>
				<td>float</td>
    </tr>
</table>
