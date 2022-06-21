## Table of contents

### Interfaces

- [DialOption](../interfaces/grpc.DialOption.md)
- [Info](../interfaces/grpc.Info.md)
- [InvokeOption](../interfaces/grpc.InvokeOption.md)
- [Response](../interfaces/grpc.Response.md)

### Variables

- [default](#default)

## Variables

<span id="default"></span>

### default

• `Const` **default**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `Client` | () => { `close`: () => `void` ; `connect`: (`target`: `string`, `option?`: [`DialOption`](../interfaces/grpc.DialOption.md)) => `void` ; `invoke`: (`method`: `string`, `request`: `any`, `option?`: [`InvokeOption`](../interfaces/grpc.InvokeOption.md)) => [`Response`](../interfaces/grpc.Response.md) ; `load`: (`importPaths`: `string`[], ...`filenames`: `string`[]) => `void`  } |

#### Defined in

typings/grpc.d.ts:69
