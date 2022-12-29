**Cookies** 提供了一组 cookie 操作接口。

>! Cookies 对象以 `name + domain + path` 为唯一 key, 管理 Cookie 对象集。

## 构造函数
```typescript
const cookies = new Cookies(cookieStr?: string, isSetCookie?: boolean);
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
      <td>cookieStr</td>
      <td>string</td>
      <td>否</td>
      <td>Cookie 字符串或者 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie">Set-Cookie</a> 字符串。</td>
    </tr>
    <tr>
      <td>isSetCookie</td>
      <td>boolean</td>
      <td>否</td>
      <td>参数 cookieStr 是否是 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie">Set-Cookie</a> 字符串，默认为 false。</td>
    </tr>
  </tbody>
</table>

## 方法
### get
```typescript
cookies.get(name?: string): null | Cookie | Array<Cookie>;
```

获取指定名称的 [Cookie](#Cookie) 对象。存在多个 `name` 匹配时，返回 [Cookie](#Cookie) 数组。

#### 参数

<table>
  <thead>
    <tr>
      <th width="15%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>string</td>
      <td>否</td>
      <td>
        <code>Cookie</code> 名称，取值说明如下。
        <li>
          <font color="#9ba6b7">缺省 name </font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            表示获取所有 Cookie 对象。
          </div> 
        </li>
        <li>
          <font color="#9ba6b7">指定 name </font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            表示获取指定 name 的 Cookie 对象，存在多个匹配时，返回 <a href="#Cookie">Cookie</a> 数组。
          </div> 
        </li>
      </td>
    </tr>
  </tbody>
</table>

#### Cookie[](id:Cookie)
`Cookie` 对象属性如下，详细参见 [MDN 官方文档 Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)。

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">只读</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>name</td>
			<td>string</td>
			<td>是</td>
			<td><code>Cookie</code> 名称。</td>
		</tr>
    <tr>
			<td>value</td>
			<td>string</td>
			<td>是</td>
			<td><code>Cookie</code> 值。</td>
		</tr>
    <tr>
			<td>domain</td>
			<td>string</td>
			<td>是</td>
			<td><code>Cookie</code> 的作用域名。</td>
		</tr>
    <tr>
			<td>path</td>
			<td>string</td>
			<td>是</td>
			<td><code>Cookie</code> 的作用路径。</td>
		</tr>
    <tr>
			<td>expires</td>
			<td>string</td>
			<td>是</td>
			<td>
        <code>Cookie</code> 最长有效时间, 取值符合 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date">HTTP Date</a> 首部标准。
      </td>
		</tr>
    <tr>
			<td>max_age</td>
			<td>string</td>
			<td>是</td>
			<td><code>Cookie</code> 经过 max_age 秒失效，单位秒（s）。</td>
		</tr>
    <tr>
			<td>samesite</td>
			<td>string</td>
			<td>是</td>
			<td>控制 <code>Cookie</code> 跨站点请求伪造攻击（CSRF）的保护。</td>
		</tr>
    <tr>
			<td>httponly</td>
			<td>boolean</td>
			<td>是</td>
			<td>禁止 JavaScript 访问 <code>Cookie</code>，仅限 HTTP 请求携带。</td>
		</tr>
    <tr>
			<td>secure</td>
			<td>boolean</td>
			<td>是</td>
			<td><code>Cookie</code> 仅限 HTTPS 请求协议携带。</td>
		</tr>
	</tbody>
</table>


### set
```typescript
cookies.set(name: string, value: string, options?: Cookie): boolean;
```

覆盖添加 Cookie。返回 true，表示添加成功，返回 false，表示添加失败（超过了 cookies 数量限制，详细参见 [cookies 大小限制](#CookiesLimit)）。

>! 以 `name + domain + path` 为唯一 key，覆盖添加 Cookie。

#### 参数

<table>
  <thead>
    <tr>
      <th width="15%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>string</td>
      <td>是</td>
      <td><code>Cookie</code> 名称。</td>
    </tr>
    <tr>
      <td>value</td>
      <td>string</td>
      <td>是</td>
      <td><code>Cookie</code> 值。</td>
    </tr>
    <tr>
      <td>Cookie</td>
      <td>string</td>
      <td>否</td>
      <td><a href="#Cookie">Cookie</a> 属性配置项。</td>
    </tr>
  </tbody>
</table>

### append
```typescript
cookies.append(name: string, value: string, options?: Cookie): boolean;
```

追加 Cookie，用于相同 name, 多个 value 的场景。返回 true，表示添加成功，返回 false，表示添加失败（value 重复或超过了 cookies 数量限制，详细参见 [cookies 大小限制](#CookiesLimit)）。

>! 以 `name + domain + path` 为唯一 key 追加 Cookie。

### remove
```typescript
cookies.remove(name: string, options?: Cookie): boolean;
```

删除 Cookie。

>! 以 `name + domain + path` 为唯一 key 删除 Cookie。

#### 参数

<table>
  <thead>
    <tr>
      <th width="15%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>string</td>
      <td>是</td>
      <td><code>Cookie</code> 名称。</td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#Cookie">Cookie</a></td>
      <td>是</td>
      <td>
        <a href="#Cookie">Cookie</a> 属性配置项，其中属性 domian 和 path 可支持 *, 表示匹配所有。
      </td>
    </tr>
  </tbody>
</table>

## 使用限制
### 特殊字符自动转义
- name 值包含字符 ` " ( ) , / : ; ? < = > ? @ [ ] \ { }`，`0x00～0x1F`， `0x7F~0xFF` 将被自动转义。

- value 值包含字符 ` , ， ; " \`，`0x00~0x1F`，`0x7F~0xFF` 将被自动转义。

### cookies 大小限制[](id:CookiesLimit)
- Cookie 属性 name 大小不超过 64B。

- Cookie 属性 `value, domain, path, expires, max_age, samesite` 累计大小不超过 1KB。

- cookies 转义后所有字段总长度不超过 4KB。

- cookies 中包含的 Cookie 对象总数不超过 64个。

## 示例代码
```typescript
function handleEvent(event) {
  const response = new Response('hello world');
    
  // 生成 cookies 对象
  const cookies = new Cookies('ssid=helloworld; expires=Sun, 10-Dec-2023 03:10:01 GMT; path=/; domain=.tencentcloud.com; samesite=.tencentcloud.com', true);
  
  // 设置响应头 Set-Cookie
  response.setCookies(cookies);

  return response;
}

addEventListener('fetch', (event) => {    
  event.respondWith(handleEvent(event));
});
```

## 相关参考 
- [MDN 官方文档：Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
- [示例函数：AB测试](https://cloud.tencent.com/document/product/1552/81934)
- [示例函数：设置 Cookie](https://cloud.tencent.com/document/product/1552/84080)
