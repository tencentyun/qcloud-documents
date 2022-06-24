## Table of contents（目录）

### Interfaces（接口）
- [BatchOption](https://cloud.tencent.com/document/product/1484/75820)
- [BatchResponse](https://cloud.tencent.com/document/product/1484/75821)
- [File](https://cloud.tencent.com/document/product/1484/75822)
- [Request](https://cloud.tencent.com/document/product/1484/75823)
- [Response](https://cloud.tencent.com/document/product/1484/75819)

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)
### default
- `Const` **default**: `Object`

```
Defined in typings/http.d.ts:157
```

#### Type declaration
| Name       | Type                                                         |
| :--------- | :----------------------------------------------------------- |
| FormData | () => { `append`: (`key`: `string`, `value`: `string` \| [`File`](https://cloud.tencent.com/document/product/1484/75822)) => `void` ; `body`: () => `ArrayBuffer` ; `contentType`: () => `string`  } |
| batch    | (`requests`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)[], `opt?`: [`BatchOption`]https://cloud.tencent.com/document/product/1484/75820)) => [`BatchResponse`](https://cloud.tencent.com/document/product/1484/75821)[] |
| delete   | (`url`: `string`, `request?`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
|do       | (`request`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
| file    | (`data`: `string` \| `ArrayBuffer`, `name?`: `string`, `contentType?`: `string`) => [`File`](https://cloud.tencent.com/document/product/1484/75822) |
| get     | (`url`: `string`, `request?`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
| head     | (`url`: `string`, `request?`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
| patch  | (`url`: `string`, `body`: `string`, `request?`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
| post     | (`url`: `string`, `body`: `string` \| `object` \| `ArrayBuffer`, `request?`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
| put     | (`url`: `string`, `body`: `string`, `request?`: [`Request`](https://cloud.tencent.com/document/product/1484/75823)) => [`Response`](https://cloud.tencent.com/document/product/1484/75819) |
