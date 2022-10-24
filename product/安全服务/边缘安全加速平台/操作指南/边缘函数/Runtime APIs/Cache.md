# Cache

Cache 提供了一组缓存操作接口。  
Cache API 在全球范围内可用，但缓存的内容仅在当前数据中心有效，不会自动复制到其他数据中心。

## 语法

```typescript
class CacheStorage {
  readonly default: Cache;
  static open(name: string): Promise<Cache>;
}
```

```typescript
class Cache {
  static match(req: string | Request, options?: object): Promise<Response | undefined>;
  static put(req: Request, rsp: Response): Promise<undefined>;
  static delete(req: string | Request, options?: object): Promise<boolean>;
}
```

### 属性
- CacheStorage.default: <br>
&emsp;默认 cache 实例.

### 方法
- CacheStorage.open(name: string):  Promise&lt;Cache&gt;<br>
&emsp;创建指定 name 的 cache 实例.

- Cache.match(req: string | Request, options?: object):  Promise&lt;Response | undefined&gt;<br>
&emsp;获取 req 关联的缓存 Response. 返回 Promise 对象, 如果缓存 Response 存在, 则包含缓存 Response,
&emsp;反之则包含 undefined.
- Cache.put(req: string | Request, rsp: Response):  Promise&lt;undefined&gt;<br>
&emsp;设置 req 关联的缓存 Response. 返回 Promise 对象, 包含 undefined.<br>
- Cache.delete(req: string | Request, options?: object):  Promise&lt;boolean&gt;<br>
&emsp;删除 req 关联的缓存 Response. 返回 Promise 对象, 如果删除成功, 则包含 true, 反之则包含 false.

*Cache.match, Cache.delete 方法中 options 参数说明:*
 - ignoreMethod: boolean 是否忽略 Request 的方法名

## Cache.match 补充说明
- 参数 req 只支持 GET 方法, 当类型为 string 时, 将被作为 URL 构造 Request 对象.
- 参数 options 只支持 ignoreMethod, 为 true 时, 会忽略 Request 原来的方法, 做为 GET 处理.
- 当参数 req 包含 Range 头部时, 如果缓存的 Response 能够支持 Range 范围处理, 返回 206 响应.
- 当参数 req 包含 If-Modified-Since 头部时, 如果缓存的 Response 存在 Last-Modified 头部, 且 Last-Modified == If-Modified-Since, 返回 304 响应.
- 当参数 req 包含 If-None-Match 头部时, 如果缓存的 Response 存在 ETag 头部, 且 ETag == If-None-Match, 返回 304 响应.
- match 接口底层实现不主动回源, 缓存过期抛出 504 错误.

## Cache.put 补充说明
- 参数 Response 支持的一些头部处理:
 - Cache-Control: s-maxage,max-age,no-store,no-cache,private, 其中 no-store,no-cache,private 均表示不缓存.
 - Pragma: no-cache. 当 Cache-Control 未设置时, 该头部表示不缓存.
 - ETag: 当 match 接口参数 req 包含 If-None-Match 头部时使用.
 - Last-Modified: 当 match 接口参数 req 包含 If-Modified-Since 头部时使用.
- 当参数 req 类型为 string 时, 将被作为 URL 构造 Request 对象.
- 以下几类限制如果不满足, 将抛出参数错误:
 - 参数 req 不支持 GET 方法之外的其他方法.
 - 参数 rsp 不支持 206 Partial Content.
 - 参数 rsp 不支持 Vary: * 头部.
- 当 Response 对象的 Cache-Control 头部表示不缓存时, 抛出 413 错误.
- 暂未对 body 大小做出限制.
- 当 Response 对象为 416 Range Not Satisfiable 时, 暂不缓存.

## Cache.delete 补充说明
- 参数 req 只支持 GET 方法, 当类型为 string 时, 将被作为 URL 构造 Request 对象.
- 未发生网络错误时, 总返回 true.

## 示例

### 获取默认 cache 实例

```js
let cache = caches.default; // await caches.open("default");

// do something ...
```

### 创建指定 name 的 cache 实例

```js
let cache = await caches.open("non-default");

// do something ...
```

### match, put, delete使用
```js
async function handleRequest(event) {
    const request = event.request;

    const cacheKey = new Request("http://www.baidu.com");

    const cache = caches.default;

    return cache.match(cacheKey).then(async (response) => {
        if (!response) {
            console.log(
                `Response for request url: ${cacheKey.url} not present in cache. Fetching and caching request.`
            );
            response = await fetch(cacheKey);

            response = new Response(response.body, response);

            response.headers.append('Cache-Control', 's-maxage=300');

            event.waitUntil(cache.put(cacheKey, response.clone()));
        } else {
            console.log(`Cache hit for: ${cacheKey.url}.`);
        }
        return response;
    }).catch(async (err) => {
        console.log(`Cache expired: ${err}.`);

        let ret = await cache.delete(cacheKey);
        console.log(`Cache delete: ${ret}.`);

        return new Response(null, { status: parseInt(err.message) });
    });
}

addEventListener('fetch', async (event) => {
    try {
        let response = await handleRequest(event);
        return event.respondWith(response);
    } catch (e) {
        return event.respondWith(new Response('Error thrown ' + e.message));
    }
});
```

