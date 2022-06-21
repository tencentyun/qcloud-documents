## Table of contents

### Interfaces

- [BatchOption](../interfaces/http.BatchOption.md)
- [BatchResponse](../interfaces/http.BatchResponse.md)
- [File](../interfaces/http.File.md)
- [Request](../interfaces/http.Request.md)
- [Response](../interfaces/http.Response.md)

### Variables

- [default](#default)

## Variables

<span id="default"></span>

### default

• `Const` **default**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `FormData` | () => { `append`: (`key`: `string`, `value`: `string` \| [`File`](../interfaces/http.File.md)) => `void` ; `body`: () => `ArrayBuffer` ; `contentType`: () => `string`  } |
| `batch` | (`requests`: [`Request`](../interfaces/http.Request.md)[], `opt?`: [`BatchOption`](../interfaces/http.BatchOption.md)) => [`BatchResponse`](../interfaces/http.BatchResponse.md)[] |
| `delete` | (`url`: `string`, `request?`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |
| `do` | (`request`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |
| `file` | (`data`: `string` \| `ArrayBuffer`, `name?`: `string`, `contentType?`: `string`) => [`File`](../interfaces/http.File.md) |
| `get` | (`url`: `string`, `request?`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |
| `head` | (`url`: `string`, `request?`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |
| `patch` | (`url`: `string`, `body`: `string`, `request?`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |
| `post` | (`url`: `string`, `body`: `string` \| `object` \| `ArrayBuffer`, `request?`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |
| `put` | (`url`: `string`, `body`: `string`, `request?`: [`Request`](../interfaces/http.Request.md)) => [`Response`](../interfaces/http.Response.md) |

#### Defined in

typings/http.d.ts:157


