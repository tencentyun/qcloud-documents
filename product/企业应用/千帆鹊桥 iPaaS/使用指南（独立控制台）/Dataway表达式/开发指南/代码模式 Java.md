为了降低熟练使用 Java 的用户接入腾讯云数据连接器的门槛，Dataway 代码模式提供对 Java 脚本的支持。

## IDE 使用

1. 对于任意 Dataway 编辑文本框，将鼠标移至文本框，会自动弹出模式选择按钮，单击**代码**进入代码模式。
![](https://qcloudimg.tencent-cloud.cn/raw/09857e2a0b5ca72761d9f5a57997f06d.png)
2. 单击编辑文本框，弹出代码编辑器，单击**Java**，进入 Java 脚本编辑器。
<img src="https://qcloudimg.tencent-cloud.cn/raw/f790705d53b448dc41d7f16b053f43f4.png" alt="Java编辑器" style="zoom:50%;" />
3. 编辑完成后，单击**确定**进行保存。

代码模式 Java 支持 [集成流数据面板](https://cloud.tencent.com/document/product/1270/73950#dataref)引用。

## 脚本结构
Java 脚本需符合 JDK8 语法规定。

类名必须为 Handler，且必须定义一个签名为 Object eval(Message msg) 的函数作为入口函数。
```java
import com.tencent.ipaas.dataway.common.message.Message; 
import com.tencent.ipaas.dataway.common.message.DataRef; 
```

不能删除，其它 import 语句可以根据类型使用需求在下面新增。
```java
// 这行 import 固定，不能删除
import com.tencent.ipaas.dataway.common.message.Message;
import com.tencent.ipaas.dataway.common.message.DataRef; 

/**
 * dataway-java入口类，名称必须为 Handler
 */
public class Handler {
    /**
     * 入口函数，签名必须为 Object eval(Message msg)
     * @param msg 输入 Message 对象
     * @return 任意 dataway 支持的数据对象
     */
    public Object eval(Message msg) {
        return msg.getPayload();
    }
}
```

## 数据类型
代码模式 Java 对各数据类型提供充足支持，方便用户对各数据类型进行操作。

<table>
    <tr>
        <th>类型名</th>
        <th>类型描述</th>
        <th>对应 Python 类型</th>
        <th>类型举例</th>
        <th>类型方法</th>
    </tr>
    <tr>
        <td>null</td>
        <td>Java 中的空值 null</td>
        <td>None</td>
        <td>null</td>
        <td>略</td>
    </tr>
    <tr>
        <td>String</td>
        <td>字符串，即 Java 原生的字符串 String</td>
        <td>str</td>
        <td>“abc”</td>
        <td>略</td>
    </tr>
    <tr>
        <td>Boolean</td>
        <td>布尔值，即 Java 原生布尔值 bool</td>
        <td>bool</td>
        <td>true/false</td>
        <td>略</td>
    </tr>
    <tr>
        <td>float/Float</td>
        <td>浮点数，即 Java 原生浮点数 float</td>
        <td>float</td>
        <td>123.456</td>
        <td>略</td>
    </tr>
    <tr>
        <td>int/Integer</td>
        <td>整数，即 Java 原生整型 int</td>
        <td rowspan="3">int</td>
        <td>123</td>
        <td>略</td>
    </tr>
    <tr>
        <td>long/Long</td>
        <td>长整数，即 Java 原生长整型 Long</td>
        <td>123L</td>
        <td>略</td>
    </tr>
    <tr>
        <td>short/Short</td>
        <td>短整数，即 Java 原生短整型 Short</td>
        <td>123</td>
        <td>略</td>
    </tr>
    <tr>
        <td>byte[]</td>
        <td>字节数组，即 Java 字节数组类型 byte[]</td>
        <td>bytes</td>
        <td>byte[]{1,2,3}</td>
        <td>略</td>
    </tr>
    <tr>
        <td>java.util.List</td>
        <td>列表，序列类型容器，即 Java 原生 List 类型</td>
        <td>list</td>
        <td>new java.util.ArrayList&lt;&gt;()</td>
        <td>详情可参考 <a href="https://docs.oracle.com/javase/8/docs/api/java/util/List.html">官方文档</a></td>
    </tr>
    <tr>
        <td>java.util.Map</td>
        <td>字典，kv 类型容器，即 Java 原生 Map 类型</td>
        <td>dict</td>
        <td>new java.util.HashMap&lt;&gt;()</td>
        <td>详情可参考 <a href="https://docs.oracle.com/javase/8/docs/api/java/util/Map.html">官方文档</a></td>
    </tr>
    <tr>
        <td>java.time.OffsetDateTime</td>
        <td>时间，即 Java 原生的 OffsetDateTime</td>
        <td>datetime.datetime</td>
        <td>java.time.OffsetDateTime.now()</td>
        <td>详情可参考 <a href="https://docs.oracle.com/javase/8/docs/api/java/time/OffsetDateTime.html">官方文档</a></td>
    </tr>
    <tr>
        <td>java.time.LocalDate</td>
        <td>日期，即 Java 原生的 LocalDate</td>
        <td>datetime.date</td>
        <td>java.time.LocalDate.now()</td>
        <td>详情可参考 <a href="https://docs.oracle.com/javase/8/docs/api/java/time/LocalDate.html">官方文档</a></td>
    </tr>
    <tr>
        <td>java.time.OffsetTime</td>
        <td>时钟，即 Java 原生的 OffsetTime</td>
        <td>datetime.time</td>
        <td>java.time.OffsetTime.now()</td>
        <td>详情可参考 <a href="https://docs.oracle.com/javase/8/docs/api/java/time/OffsetTime.html">官方文档</a></td>
    </tr>
    <tr>
        <td>java.math.BigDecimal</td>
        <td>十进制数，即 Java 原生的 BigDecimal</td>
        <td>decimal.Decimal</td>
        <td>new java.math.BigDecimal("1") </td>
        <td>详情可参考 <a href="https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html">官方文档</a></td>
    </tr>
    <tr>
        <td>com.tencent.ipaas.dataway.common.message.Entity（数据连接器特有类型）</td>
        <td>即数据连接器中的实体数据，用于代表一个二进制对象，以 Entity 类型进行访问，包括blob、mimeType、encoding 等信息</td>
        <td>Entity</td>
        <td>HTTP-listener 构造消息中的 payload</td>
        <td>详见“使用 Entity 对象”</td>
    </tr>
    <tr>
        <td rowspan="6">com.tencent.ipaas.dataway.common.message.Multimap（数据连接器特有类型）</td>
        <td rowspan="6">多值 map，类似于 xml 而与 dict 不同，该类型可以支持重复的 key，继承自 HashMap&lt;String, List&gt;</td>
        <td rowspan="6">MultiMap</td>
        <td rowspan="6">application/www-form-urlencoded 格式的数据解析之后得到的对象</td>
        <td>构建方法：Multimap(Map dict)</td>
    </tr>
    <tr>
        <td>构建静态方法：Multimap fromSetEntry(Set&lt;Map.Entry&gt; set)</td>
    </tr>
    <tr>
        <td>获取特定键对应的第一个值：Object getFirst(Object key)</td>
    </tr>
    <tr>
        <td>获取特定键对应的所有值组成的列表：List getAll(Object key)</td>
    </tr>
    <tr>
        <td>获取键值对集合：Set&lt;Map.Entry&gt; toSetEntry()</td>
    </tr>
    <tr>
        <td>继承自 HashMap 的方法</td>
    </tr>
    <tr>
        <td rowspan="3">com.tencent.ipaas.dataway.common.message.FormDataParts（数据连接器特有类型）</td>
        <td rowspan="3">数组+列表的数据结构，类似于 Python 中的 orderDict 结构，继承自 LinkedHashMap&lt;String, Object&gt;</td>
        <td rowspan="3">FormDataParts</td>
        <td rowspan="3">multipart/form-data 格式的数据解析后得到的对象</td>
        <td>构建方法：FormDataParts(String boundary)</td>
    </tr>
    <tr>
        <td>获取特定关键词对应值（当关键词为 int /long时，关键词作为键的序号；其余情况，关键词即为键）：Object get(Object key)</td>
    </tr>
    <tr>
        <td>继承自 LinkedHashMap 的方法</td>
    </tr>
    <tr>
        <td rowspan="4">com.tencent.ipaas.dataway.common.message.Message（数据连接器特有类型，不可通过 dataway  构建）</td>
        <td rowspan="4">即数据连接器中的集成流消息，以 Message 类型进行访问</td>
        <td rowspan="4">Message</td>
        <td rowspan="4">public Object eval(Message msg) 入口函数中的 msg 参数</td>
        <td>获取 payload：Object getPayload()</td>
    </tr>
    <tr>
        <td>获取 Attributes：Map getAttrs()</td>
    </tr>
    <tr>
        <td>获取 Variables：Map&lt;Object, Object&gt; getVars() 或者 Object getVar(String name)</td>
    </tr>
    <tr>
        <td>获取 Error：DataWayError getError()</td>
    </tr>
    <tr>
        <td rowspan="3">com.tencent.ipaas.dataway.common.message.DataSet（数据连接器特有类型，不可通过 dataway  构建）</td>
        <td rowspan="3">数据集成中的数据集，通过数据集成组件生成</td>
        <td rowspan="3">RecordSet</td>
        <td rowspan="3">Builder 组件的输出</td>
        <td>获取 id：Long getId()</td>
    </tr>
    <tr>
        <td>获取 schema：Schema getSchema()</td>
    </tr>
    <tr>
        <td>获取 partitions：Long getPartitions()</td>
    </tr>
    <tr>
        <td rowspan="5">com.tencent.ipaas.dataway.common.message.Record（数据连接器特有类型，不可通过 dataway  构建）</td>
        <td rowspan="5">数据集成中的单条数据，附有 schema </td>
        <td rowspan="5">Record</td>
        <td rowspan="5">可通过 Foreach 组件遍历 DataSet 获取</td>
        <td>获取所有数据：List getData()</td>
    </tr>
    <tr>
        <td>获取 schema：Schema getSchema()</td>
    </tr>
    <tr>
        <td>获取特定关键词对应数据（当关键词为 int / long时，关键词为列序号；其余情况，关键词为字段名）：Object get(Object key)</td>
    </tr>
    <tr>
        <td>是否包含字段名：boolean contains(String name)</td>
    </tr>
    <tr>
        <td>获取字段名迭代器：Iterator&lt;String&gt; getIterator()</td>
    </tr>
    <tr>
        <td rowspan="3">com.tencent.ipaas.dataway.common.message.Schema（数据连接器特有类型，不可通过 dataway  构建）</td>
        <td rowspan="3">数据集成中的数据字典，描述数据的元信息 </td>
        <td rowspan="3">Schema</td>
        <td rowspan="3">可通过 Record 的 getSchema() 方法获取，对应于各项数据</td>
        <td>获取所有字段信息：RecordField[] getFields()</td>
    </tr>
    <tr>
        <td>获取特定字段名对应字段信息：RecordField getField(String name)</td>
    </tr>
    <tr>
        <td>转化为类似 {"Fields":[{"Name":"name","Type":"string"}]} 的字典形式：Map&lt;?,?&gt; toMap()</td>
    </tr>
    <tr>
        <td rowspan="2">com.tencent.ipaas.dataway.common.message.RecordField（数据连接器特有类型，不可通过 dataway 构建）</td>
        <td rowspan="2">数据集成中的字段信息，描述单个字段的元信息 </td>
        <td rowspan="2">Schema</td>
        <td rowspan="2">可通过 Schema 的 getField(name) 方法获取 RecordField</td>
        <td>获取字段名：String getName()</td>
    </tr>
    <tr>
        <td>获取字段类型：String getType()</td>
    </tr>
</table>

## 使用 Entity 对象

### 基础方法
在代码模式 Java 中， 用 Entity 类型来表示数据连接器集成流中的实体数据，表示二进制数据的封装对象，其主要组成部分包括 blob、mimeType 以及 encoding。

| 组成部分 | 说明 | 
|---------|---------|
| blob  |  原始的二进制数据。|
| mimeType  |  表示二进制数据的内容格式，例如：application/json、application/www-form-urlencoded  |  multipart/form-data 等。  |  
| encoding  |  表示二进制数据的字符编码格式，例如：utf-8、gbk 等。  |  


可以通过如下方式访问 Entity 中的内容：

| 访问方式 | 说明 | 
|---------|---------|
|   byte[] getBlob() |  获取该消息对象的负载数据，返回 byte[] 类型的对象。 |  
|   String getMimeType() |  获取该消息对象的 MIME 类型，返回 String 对象。
|   String getEncoding() |  获取该消息对象的编码类型，返回 String 对象。 |  
|   Object getValue() |  根据 MIME 类型和编码类型，对负载数据 blob 进行反序列化，并返回其结果，该类型为代码模式 Java 类型系统中定义的类型之一。 |  
|   Object get(Object key) |  根据 MIME 类型和编码类型对 message 的内容进行反序列化，并获取其中指定 key 的值。 |   

当前反序列化支持的 MIME 类型及其反序列化后的值类型如下：
- text/plain → String
- application/json →  Object，与 GSON 一致
- application/x-www-form-urlencoded → Multimap
- application/xml → Map
- application/csv → List&lt;Map&lt;String,String&gt;&gt;，即字段名与取值映射的列表
- multipart/form-data → FormDataParts



### 构造方法
#### Entity.fromValue 静态方法
用于将值类型 data 封装为 Entity 类型，并返回。如下所示：
```java
Entity.fromValue(Object value, String mimeType, String encoding)
```
在 fromValue 函数内部，会先根据给定的 MIME 类型和编码类型尝试对 value 进行序列化得到 byte[] 类型的数据，然后再封装为 Entity 类型进行返回。

- mimeType 参数必传，且目前支持的 MIME 类型有 text/plain、application/json、application/x-www-form-urlencoded、application/csv、 application/xml 和 multipart/form-data 六种。
- encoding 参数必传，且支持任意合法的编码类型。

#### Entity.fromBytes 静态方法
用于将 String 或者 byte[] 类型数据封装为 Entity 类型，并返回。如下所示：
```java
Entity.fromBytes(Object data, String mimeType, String encoding)
```
fromBytes 函数中的 MIME 类型和编码类型参数校验规则与 fromValue 函数相似，不同的是不会对 MIME 类型的参数值进行限制，可以为任意的 MIME 类型。

- 如果传递给 fromBytes 函数的 data 参数类型为 byte[] 类型，该函数会直接返回一个以 data、mimeType、encoding 作为参数构造的 Entity 对象。
- 如果传递的 data 是 String 数据，则会尝试根据 encoding 参数将其编码为 byte[] 类型，并构造成 Entity 对象。

### 使用限制
Entity 对象在本质上是一个对二进制数据的封装对象，为方便使用，提供 entity.get() 等访问对象内容的方法。在使用这些功能时，需要注意的是，有些特殊操作下系统会尝试先对 Entity 中的二进制数据进行反序列化解析，如果解析失败则会导致运行时错误。这些特殊操作包括：

- 用 entity.getValue() 来获取解析后的结构化结果。
- 用 entity.get(key) 来获取结构化结果中的某项内容。

在不符合条件的 Entity 对象上执行上述特殊操作，将会导致运行时错误。
