**Cache** 基于 Web APIs 标准 [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache) 进行设计。边缘函数运行时会在全局注入 `caches` 对象，该对象提供了一组缓存操作接口。

>? 缓存的内容仅在当前数据节点有效，不会自动复制到其他数据节点。

## 构造函数
- 使用 `caches.default` 可以获取默认的 cache 实例。

```typescript
// 获取默认 cache 实例
const cache = caches.default;

// 效果等同于 caches.default
await caches.open('default');
```

- 使用 `caches.open` 创建指定命名空间的 cache 实例。

```typescript
// 创建指定命名空间的 cache 实例
const cache = await caches.open(namespace); 
```

### 参数
`caches.open(namespace)` 方法参数说明如下。

<table>
  <thead>
    <tr>
      <th width="10%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="65%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>namespace</td>
      <td>string</td>
      <td>是</td>
      <td>
        缓存命名空间。
        <li>如果该值为 "default" 则表示默认实例，也可直接使用 <code>caches.default</code> 获取默认实例。</li>
      </td>
    </tr>
  </tbody>
</table>

## 实例方法

### match
```typescript
cache.match(request: string | Request, options?: MatchOptions): Promise<Response | undefined>
```

获取 request 关联的缓存 [Response](https://cloud.tencent.com/document/product/1552/81917)。返回一个 Promise 对象。如果缓存存在，则包含 Response 对象，反之包含 undefined。

>! **cache.match** 内部不会主动回源，缓存过期则会抛出 504 错误。

#### 参数
<table>
  <thead>
    <tr>
      <th width="10%">参数名称</th>
      <th width="15%">类型</th>
      <th width="10%">必填</th>
      <th width="65%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>request</td>
      <td>string | <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a></td>
      <td>是</td>
      <td>
        请求对象，headers 说明如下。<br>
        <li>
          <font color="#9ba6b7">GET</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">request 只支持 <code>GET</code> 方法，当类型为 string 时，将被作为 URL 构造 Request 对象。</div>
        </li>
        <li>
          <font color="#9ba6b7">Range</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">request 包含 <code>Range</code> 头部时，如果缓存的 Response 能够支持 Range 范围处理，返回 206 响应。</div>
        </li>
        <li>
          <font color="#9ba6b7">If-Modified-Since</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">request 包含 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since">If-Modified-Since</a> 头部时，如果缓存的 Response 存在 Last-Modified 头部，且 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified">Last-Modified</a> 与 If-Modified-Since 相等，返回 304 响应。</div>
        </li>
        <li>
          <font color="#9ba6b7">If-None-Match</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">request 包含 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match">If-None-Match</a> 头部时，如果缓存的 Response 存在 ETag 头部，且 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag">ETag</a> 与 If-None-Match 相等, 返回 304 响应。</div>
        </li>
      </td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#MatchOptions">MatchOptions</a></td>
      <td>否</td>
      <td>选项。</td>
    </tr>
  </tbody>
</table>

#### MatchOptions[](id:MatchOptions)
<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">示例值</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>ignoreMethod</td>
			<td>boolean</td>
			<td>true</td>
			<td>是否忽略 Request 的 method。为 true 时，会忽略 Request 原来的 method，作为 GET 处理。</td>
		</tr>
	</tbody>
</table>

### put
```typescript
cache.put(request: string | Request, response: Response): Promise<undefined>
```
尝试使用给定的 request 作为缓存 key，将 response 添加到缓存。无论缓存是否成功，均返回 `Promise<undefined>` 对象。

>! 当参数 **response** 对象的 Cache-Control 头部表示不缓存时，抛出 413 错误。 

#### 参数
<table>
	<thead>
		<tr>
			<th width="10%">参数名称</th>
			<th width="15%">类型</th>
			<th width="10%">必填</th>
			<th width="65%">说明</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>request</td>
			<td>string | <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a></td>
			<td>是</td>
			<td>
				缓存 key，说明如下。
				<li>
          <font color="#9ba6b7">GET</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            参数 <code>request</code> 仅支持 GET 方法，其他方法，将抛出参数错误。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">string</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            当参数 <code>request</code> 类型为 string 时，将被作为 URL 构造 <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a> 对象。
          </div>
        </li>
			</td>
		</tr>
		<tr>
			<td>rsponse</td>
			<td><a href="https://cloud.tencent.com/document/product/1552/81917">Response</a></td>
			<td>是</td>
			<td>
        缓存内容，说明如下。<br>
        <li>
          <font color="#9ba6b7">Cache-Control</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            支持 s-maxage、max-age、no-store、no-cache、private；其中 no-store、no-cache、private 均表示不缓存，<code>cache.put</code> 将返回 413 错误。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">Pragma</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            当 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control">Cache-Control</a> 未设置，并且 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Pragma">Pragma</a> 为 no-cache。此时表示不缓存。
          </li>
        <li>
          <font color="#9ba6b7">ETag</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            当 <code>cache.match</code> 参数 <code>request</code> 包含 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-None-Match">If-None-Match</a> 头部时，可关联 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag">ETag</a> 使用。
          </div>
        </li>
        <li>
          <font color="#9ba6b7">Last-Modified</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            当 <code>cache.match</code> 参数 <code>request</code> 包含 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Modified-Since">If-Modified-Since</a> 头部时，可关联 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Last-Modified">Last-Modified</a> 使用。
          </div>
        </li>	
        <li>
          <font color="#9ba6b7">416 Range Not Satisfiable</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            当参数 <code>response</code> 对象为 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/416">416 Range Not Satisfiable</a> 时，暂不缓存。
          </div>
        </li>
			</td>
		</tr>
	</tbody>
</table>

#### 参数限制
`cache.put` 使用以下的参数值，将抛出参数错误：
- 参数 `request` 为 GET 方法之外的其他方法.
- 参数 `response` 状态码为 [206 Partial Content](https://www.webfx.com/web-development/glossary/http-status-codes/what-is-a-206-status-code/)。 
- 参数 `response` 包含 <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary">Vary: *</a> 头部。 


### delete

```typescript
cache.delete(request: string | Request, options?: DeleteOptions): Promise<boolean>
```
删除 request 关联的缓存 response。未发生网络错误时, 总返回 Promise，并包含 true，反之包含 false。

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
      <td>request</td>
      <td>string | <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a></td>
      <td>是</td>
      <td>
        缓存 key，说明如下。
        <li>
          <font color="#9ba6b7">GET</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px">
            参数 <code>request</code> 仅支持 GET 方法
          </div>
        </li>
        <li>
          <font color="#9ba6b7">string</font><br/>
          <div style="padding-left: 20px;padding-bottom: 6px"> 
            当参数 <code>request</code> 类型为 string 时，将被作为 URL 构造 <a href="https://cloud.tencent.com/document/product/1552/81902">Request</a> 对象。
          </div>
        </li>
      </td>
    </tr>
    <tr>
      <td>options</td>
      <td><a href="#DeleteOptions">DeleteOptions</a></td>
      <td>否</td>
      <td>配置选项。</td>
    </tr>
  </tbody>
</table>

#### DeleteOptions[](id:DeleteOptions)

<table>
  <thead>
    <tr>
    <th width="15%">属性名</th>
    <th width="15%">类型</th>
    <th width="10%">示例值</th>
    <th width="60%">说明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ignoreMethod</td>
      <td>boolean</td>
      <td>true</td>
      <td>是否忽略 <code>request</code> 的方法名。为 true 时，会忽略 Request 原来的方法，作为 GET 处理</td>
    </tr>
  </tbody>
</table>

## 相关参考 
- [MDN 官方文档：Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache)
- [示例函数：缓存 POST 请求](https://cloud.tencent.com/document/product/1552/84024)
- [示例函数：Cache API 使用](https://cloud.tencent.com/document/product/1552/84023)
