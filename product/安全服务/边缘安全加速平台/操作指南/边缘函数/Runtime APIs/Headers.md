**Headers** 基于 Web APIs 标准 [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers) 进行设计。可用于 HTTP request 和 response 的头部操作。

## 构造函数

```typescript
const headers = new Headers(init?: object | Array<[string, string]> | Headers);
```

### 参数
<table>
  <thead>
    <tr>
      <th width="10%">参数名称</th>
      <th width="20%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>init</td>
      <td>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object">object</a> | </br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array">Array&lt;[string, string]&gt;</a> | </br>
        Headers
      </td>
      <td>否</td>
      <td>
        初始化 Headers 对象，参数类型说明如下：<br/>
        <li>
          <font color="#9ba6b7">object</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            构造函数将会枚举 Object 包含的所有可枚举属性，并初始化到新的 Headers 对象中。
          </div> 
        </li>
        <li>
          <font color="#9ba6b7">Array&lt;[string, string]&gt;</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            数组的每一个元素为 <code>key/value</code> 的键值对（如：[key, value]），构造函数遍历数组，并初始化到新的 Headers 对象中。
          </div> 
        </li>
        <li>
          <font color="#9ba6b7">Headers</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            拷贝 Headers 对象，并把所有字段初始化到新的 Headers 对象中。
          </div> 
        </li>
      </td>
    </tr>
  </tbody>
</table>

## 方法
### append

```typescript
headers.append(name: string, value: string): void;
```

在 `headers` 对象指定的 header 上追加一个新值，若 header 不存在，则直接添加。

#### 参数
<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>name</td>
			<td>string</td>
			<td>是</td>
			<td>header 名</td>
		</tr>
    <tr>
			<td>value</td>
			<td>string</td>
			<td>是</td>
			<td>追加的新值</td>
		</tr>
	</tbody>
</table>

### delete
```typescript
headers.delete(name: string): void;
```

从 `headers` 对象中删除指定 header。

#### 参数
<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>name</td>
			<td>string</td>
			<td>是</td>
			<td>header 名</td>
		</tr>
	</tbody>
</table>


### entries
```typescript
headers.entries(): iterator;
```

获取 `headers` 对象所有的键值对（[name, value]）数组，返回值参考 [MDN 官方文档：iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)。

### forEach
```typescript
headers.forEach(callback: (name: string, value: string) => void | number): void;
```

遍历 `headers` 对象所有的 header。若 `callback` 返回非零值，表示终止遍历。

>! `forEach` 为非 Web APIs 标准方法。为了提供高效遍历 headers 的方式，边缘函数基于 Web APIs 标准进行了扩展实现。

### get
```typescript
headers.get(name: string): string;
```

从 `headers` 对象中获取指定 header 的值。

### has
```typescript
headers.has(name: string): boolean;
```
判断 `headers` 对象是否包含该指定 header。

### keys
```typescript
headers.keys(): iterator;
```

获取 `headers` 对象包含的所有 key，返回值参考 [MDN 官方文档：iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)。

### set
```typescript
headers.set(name: string, value: string): void;
```
设置 `headers` 对象的指定 header 值，若该 header 不存在，则添加一个新的 <code>key/value</code> 键值对。

### values
```typescript
headers.values(): iterator;
```
获取 `headers` 对象包含的所有 value，返回值参考 [MDN 官方文档：iterator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols)。

## 示例代码
```typescript
function handleEvent() {
  const headers = new Headers({
    'my-header-x': 'hello world',
  });

  const response =  new Response('hello world', {
    headers,
  });
  return response;
}

addEventListener('fetch', (event) => {
  event.respondWith(handleEvent(event));
});
```

## 相关参考
- [MDN 官方文档：Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers)
- [示例函数：防篡改校验](https://cloud.tencent.com/document/product/1552/84081)
- [示例函数：请求头鉴权](https://cloud.tencent.com/document/product/1552/81940)
- [示例函数：修改响应头](https://cloud.tencent.com/document/product/1552/81937)
