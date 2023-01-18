使用边缘函数生成 JSON，并在浏览器端访问预览该 JSON。

## 示例代码

```typescript
const data = {
  content: 'hello world',
};

async function handleRequest(request) {
  // JSON 转为字符串
  const result = JSON.stringify(data, null, 2);

  return new Response(result, {
    headers: {
      'content-type': 'application/json; charset=UTF-8',
    },
  });
}

addEventListener('fetch', event => {
  return event.respondWith(handleRequest(event.request));
});
```

## 示例预览

在浏览器地址栏中输入匹配到边缘函数触发规则的 URL，即可预览到示例效果。
<img src="https://qcloudimg.tencent-cloud.cn/raw/100dee7845fcef3db6a2300eac803846.png" width=609px>

## 相关参考
- [Runtime APIs: addEventListener](https://cloud.tencent.com/document/product/1552/81928)
- [Runtime APIs: Response](https://cloud.tencent.com/document/product/1552/81917)
