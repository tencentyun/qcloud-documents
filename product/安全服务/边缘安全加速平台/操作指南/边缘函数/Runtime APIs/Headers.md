HTTP 头部，可用于 HTTP 请求和响应的各种操作，包括查询、设置、添加和删除。

## 语法
```typescript
class Headers {
  constructors(init?: object | Array<[string, string]> | Headers);
  append(name: string, value: string): void;
  delete(name: string): void;
  entries(): iterator;
  forEach(cb: (name: string, value: string) => void | number): void;
  get(name: string): string;
  has(name: string): boolean;
  keys(): iterator;
  set(name: string, value: string): void;
  values(): iterator;
}
```

### 构造方法
- init  可选<br>用于初始化新创建的 Headers 对象，取值有：
  - 普通的 Object：构造函数将会枚举 Object 包含的所有可枚举属性，设置到 Headers 对象中。
  - 数组 Array：数组的每一个成员均是 key/value 对，构造函数遍历数组包含的所有 key/value 对，并设置到 Headers 对象中。
  - 已存在的 Headers 对象：拷贝传入的 Headers 对象的所有字段到新的 Headers 对象中。

### 属性
无

### 方法
- append(name: string, value: string):  void
  - 追加一个新的值到该 header 中，若该 header 不存在，则直接添加。
  - name 和 value 都不允许为空字符串。
- delete(name: string):  void<br>从 Headers 对象中删除指定 header；name 不允许为空字符串。
- entries():  iterator<br>获取 Headers 对象所有的 key/value 对数组。
- forEach(cb: (name: string, value: string) => void | number):  void
  - 遍历 Headers 对象所有的 header，若 cb 返回非零值，表示终止遍历。
  - <b>非标准方法, 添加此方法是为了高效的遍历 header。</b><br>
- get(name: string):  string<br>从 Headers 对象中获取指定 header 的值；name 不允许为空字符串。<br>
- has(name: string):  boolean<br>判断 Headers 对象是否包含该 header；name 不允许为空字符串。<br>
- keys():  iterator<br>获取 Headers 对象包含的所有 key。
- set(name: string, value: string):  void
  - 设置 Headers 对象的指定 header 值，若该 header 不存在，则直接添加一个新的 key/value 对。
  - name 和 value 都不允许为空字符串。
- values():  iterator<br>获取 Headers 对象包含的所有 value。

## 示例
### Headers 对象的创建
- 通过普通的 object 对象创建
```js
let h = new Headers({
  k1: 1,
  k2: "v2",
});
log(h.get("k1"));
log(h.get("k2"));

h.delete("k1");
log(h.has("k1"));

h.set("k1", 1);
log(h.has("k1"));

h.append("k1", 1);
log(h.get("k1"));
```

- 通过 Array 创建
```js
let h = new Headers([
  ["k1", 1],
  ["k2", "v2"],
]);
```

- 通过已有的 Headers 对象创建
```js
let h1 = new Headers({
  k1: 1,
  k2: "v2",
});

let h2 = new Headers(h1);
h2.set("k2", 2);

log(h2.get("k2"));
log(h1.get("k2"));
```

### 拷贝 Headers
- 通过 entries() 方法
```js
function clone(h1) {
  let h2 = new Headers();
  for (let entry of h1.entries()) {
    h2.set(entry[0], entry[1]);
  }
  return h2;
}
```

- 通过 keys() 方法
```js
function clone(h1) {
  let h2 = new Headers();
  for (let name in h1.keys()) {
    h2.set(name, h1.get(name));
  }
}
```

- 通过 forEach() 方法
```js
function clone(h1) {
  let h2 = new Headers();
  h1.forEach((name, value) => {
    h2.set(name, value);
  });
}
```

- append 与 set 的区别
```js
let h = new Headers({
  k1: "v1",
});

h.set("k1", "v2");
log("k1"); // v2

h.append("k1", "v3");
log("k1"); // v2, v3
```

## 参考
- [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers)
