## 目录

### Interfaces（接口）
- [DialOption](https://cloud.tencent.com/document/product/1484/75816)
- [Info](https://cloud.tencent.com/document/product/1484/75817)
- [InvokeOption](https://cloud.tencent.com/document/product/1484/75818)
- [Response](https://cloud.tencent.com/document/product/1484/75819)

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)
### default
- `Const` **default**: `Object`

```
 Defined in typings/grpc.d.ts:69
```

#### Type declaration
| Name     | Type                                                         |
| :------- | :----------------------------------------------------------- |
| `Client` | () => { `close`: () => `void` ; `connect`: (`target`: `string`, `option?`: [`DialOption`](https://cloud.tencent.com/document/product/1484/75816)) => `void` ; `invoke`: (`method`: `string`, `request`: `any`, `option?`: [`InvokeOption`](https://cloud.tencent.com/document/product/1484/75818) => [`Response`](https://cloud.tencent.com/document/product/1484/75819)） ; `load`: (`importPaths`: `string`[], ...`filenames`: `string`[]) => `void`  } |
