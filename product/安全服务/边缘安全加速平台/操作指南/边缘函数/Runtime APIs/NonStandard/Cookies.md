Cookies 提供了一组 cookie 操作接口。

## 语法
```typescript
class Cookie {
  readonly name: string;
  readonly value: string;
  readonly domain: string;
  readonly path: string;
  readonly expires: string;
  readonly max_age: string;
  readonly samesite: string;
  readonly httponly: boolean;
  readonly secure: boolean;
}

class Cookies {
  static get(name?: string): null | Cookie | [Cookie];
  static set(name: string, value: string, options?: object): boolean;
  static append(name: string, value: string, options?: object): boolean;
  static remove(name: string, options?: object): boolean;
}
```

## 构造方法
Cookie 对象暂不支持构造生成。
```typescript
let cookies = new Cookies(cookie_str?: string, is_setcookie?: boolean)
```

### 参数
- cookie_str Optional<br>Cookie 字符串或者 Set-Cookie 字符串。
- is_setcookie Optional<br>表示 cookie_str 是 Set-Cookie 字符串，默认为 false。

>?
>- 如果构造函数不带参数，会创建空的 Cookies 对象。
>- 如果构造函数只带 cookie_str 参数或者两个参数都带，并且 is_setcookie 为 false，会按照 Cookie 格式解析字符串，创建的 Cookies 对象将包含解析出的 Cookie 对象集。
>- 如果构造函数两个参数都带，并且 is_setcookie 为 true，会按照 Set-Cookie 格式解析字符串，创建的 Cookies 对象将包含解析出的 Cookie 对象。
>- 相关匹配特殊字符将会自动转义，解析出错将会抛出异常。

### 属性
- Cookie.name: string<br>cookie name。
- Cookie.value: string<br>cookie value。
- Cookie.domain: string<br>cookie 属性。指定该 cookie 的作用域名。
- Cookie.path: string<br>cookie 属性。指定该 cookie 的作用路径。
- Cookie.expires: string<br>cookie 属性。指定该 cookie 的最长有效时间，应符合 [HTTP Date首部](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Date) 标准。
- Cookie.max_age: string<br>cookie 属性。指定该 cookie 失效之前需要经过的秒数。
- Cookie.samesite: string<br>cookie 属性。指定该 cookie 是否仅限于第一方或者同一站点上下文。
- Cookie.httponly: boolean<br>cookie 属性。指定是否限制 cookie 的作用范围在 HTTP 请求内。
- Cookie.secure: boolean<br>cookie 属性。指定 cookie 的安全属性。

### 方法
- Cookies.get(name?: string): null | Cookie | [Cookie]<br>获取指定 Cookie 对象。
 - 参数 name 缺省，表示获取所有 Cookie 对象；否则表示获取指定 name 的 Cookie 对象。
 - 返回 null，表示无对应 Cookie 对象。
 - 返回 Cookie，表示只存在一个匹配的 Cookie 对象。
 - 返回 Cookie 数组，表示存在多个匹配的 Cookie 对象。
- Cookies.set(name: string, value: string, options?: object): boolean<br>覆盖添加 cookie。 
 - options 对象可以指定任意 Cookie 对象属性值。 
 - httponly 和 secure 默认值为 false，如果显式指定 false 无意义，将被忽略。
 - 返回 true，表示添加成功；返回 false，表示添加失败, 超过了 Cookie 数量限制。
- Cookies.append(name: string, value: string, options?: object): boolean<br>追加 cookie，针对相同 name, 多个 value 的场景。
 - options 对象可以指定任意 Cookie 对象属性值。
 - httponly 和 secure 默认值为 false，如果显式指定 false 无意义，将被忽略。
 - 返回 true，表示添加成功，返回 false，表示添加失败，value 重复 或者 超过了 Cookie 数量限制。
- Cookies.remove(name: string, options?: object): boolean<br>删除 cookie. options 对象指定的属性 domian 和 path 可支持*，表示匹配所有。

#### 补充说明
- Cookies 对象以 name+domain+path 为唯一 key，来管理 Cookie 对象集。
- Cookies.set 接口，以 name+domain+path 为 key 覆盖添加 cookie. 不区分 options 缺省和空 domain + 空 path。
- Cookies.append 接口，以 name+domain+path 为 key 追加 cookie. 不区分 options 缺省和空 domain + 空 path。
- Cookies.delete 接口，以 name+domain+path 为 key 删除 cookie. 不区分 options 缺省和空 domain + 空 path。
- name 不能为空，value，domain，path，expires，max_age，samesite 字段可能为空。
- 对于 name，其中" ", """, "(", ")", ",", "/", ":", ";", "?", "<", "=", ">", "?", "@", "[", "]", "\", "{", "}", 0x00-0x1F, 0x7F-0xFF 将会被自动转义。
- 对于 value，其中" ", ",", ";", """, "\", 0x00-0x1F, 0x7F-0xFF 将会被自动转义。
- 对于 domain，path，expires，max_age，samesite，其中0x00-0x1F，0x7F-0xFF，";" 将会被自动转义。
- Pivot-JS 限制 name 不超过64B，value，domain，path，expires，max_age，samesite 不超过1KB，转义之后所有字段总长度不超过4KB，Cookie 对象不超过64个。


## 示例
### Cookies 对象构造
```js
// empty
let cookies = new Cookies();
log.info("typeof:", typeof(cookies));  // typeof: object

// parse Cookie
cookies = new Cookies("k1=v1; k2=; %00k3=%00v3");
log.info("typeof:", typeof(cookies));  // typeof: object
let ck1 = cookies.get("k1");
let ck2 = cookies.get("k2");
let ck3 = cookies.get("%00k3");
log.info("k1 val:", ck1.value, "k2 val:", ck2.value, "%00k3 val:", ck3.value);  // k1 val: v1 k2 val:  %00k3 val: %00v3

// parse Set-Cookie
cookies = new Cookies("k1=%00v1; Domain=http://www.qq.com; Path=/; HttpOnly", true);
log.info("typeof:", typeof(cookies));  // typeof: object
ck1 = cookies.get("k1");
log.info("value:", ck1.value, "domain:", ck1.domain, "path:", ck1.path, "httponly:", ck1.httponly);  // value: %00v1 domain: http://www.qq.com path: / httponly: true
```

### Cookies.get

```js
let cookies = new Cookies();
cookies.set("k1", "v1");
cookies.append("k1", "v1-append");
cookies.set("k2", "v2");

let cks1 = cookies.get("k1");
// name: k1 value: v1
// name: k1 value: v1-append
for (let i = 0; i < cks1.length; i++) {
   log.info("name:", cks1[i].name, "value:", cks1[i].value);
}

let cks2 = cookies.get();
// name: k2 value: v2
// name: k1 value: v1
// name: k1 value: v1-append
for (let i = 0; i < cks2.length; i++) {
   log.info("name:", cks2[i].name, "value:", cks2[i].value);
}
```

### Cookies.set

```js
let cookies = new Cookies();
cookies.set("k1", "v1");
cookies.set("k1", "v1-override");

let ck = cookies.get("k1");
log.info("k1 val:", ck.value);  // k1 val: v1-override

cookies = new Cookies();
cookies.set("k1", "v1", {"domain":"http://qq.com","path":"/"});
cookies.set("k1", "v1-override", {"domain":"http://qq.com","path":"/"});
cookies.set("k1", "v1-not-override", {"domain":"http://sub.qq.com","path":"/"});

let cks = cookies.get("k1");
// name: k1 value: v1-not-override domain: http://sub.qq.com path: /
// name: k1 value: v1-override domain: http://qq.com path: /
for (let i = 0; i < cks.length; i++) {
   log.info("name:", cks[i].name, "value:", cks[i].value, "domain:", cks[i].domain, "path:", cks[i].path);
}
```

### Cookies.append

```js
let cookies = new Cookies();
cookies.set("k1", "v1");
cookies.append("k1", "v1-append");
let cks = cookies.get("k1");
// name: k1 value: v1
// name: k1 value: v1-append
for (let i = 0; i < cks.length; i++) {
   log.info("name:", cks[i].name, "value:", cks[i].value);
}

cookies = new Cookies();
cookies.set("k1", "v1", {"domain":"http://qq.com","path":"/"});
cookies.append("k1", "v1-append", {"domain":"http://qq.com","path":"/"});
cks = cookies.get("k1");
// name: k1 value: v1 domain: http://qq.com path: /
// name: k1 value: v1-append domain: http://qq.com path: /
for (let i = 0; i < cks.length; i++) {
   log.info("name:", cks[i].name, "value:", cks[i].value, "domain:", cks[i].domain, "path:", cks[i].path);
}
```

### Cookies.remove

```js
let cookies = new Cookies();
cookies.set("k1", "v1", {"domain":"http://qq.com","path":"/"});
cookies.set("k1", "v2", {"domain":"http://sub.qq.com","path":"/"});

cookies.remove("k1", {"domain":"http://qq.com","path":"/"});
let cks = cookies.get();
log.info("name:", cks.name, "value:", cks.value, "domain:", cks.domain, "path:", cks.path);  // name: k1 value: v2 domain: http://sub.qq.com path: /

cookies.remove("k1", {"domain":"*"});
cks = cookies.get();
log.info("cks:", cks);  // cks: null
```
