## 目录

### Variables（变量）
- [default](#default)

## Variables（变量）

[](id:default)
### default
`Const` **default**: `Object`
```
 Defined in typings/util.d.ts:16
```

#### Type declaration
| Name                  | Type                                                         |
| :-------------------- | :----------------------------------------------------------- |
| base64Decoding      | (`input`: `string`, `encoding?`: ``"std"`` \| ``"rawstd"`` \| ``"url"`` \| ``"rawurl"``, `mode?`: ``"b"``) => `string` \| `ArrayBuffer` |
| base64Encoding      | (`input`: `string` \| `ArrayBuffer`, `encoding?`: ``"std"`` \| ``"rawstd"`` \| ``"url"`` \| ``"rawurl"``) => `string` |
| cloudAPISignatureV3 | (`param`: `CloudAPISignatureV3Param`) => `string`            |
| md5Sum              | (`data`: `string` \| `ArrayBuffer`) => `string`              |
| sloginEncrypt       | (`salt`: `number`, `pwd`: `string`, `vcode`: `string`) => `string` |
| toArrayBuffer       | (`data`: `string` \| `ArrayBuffer`) => `ArrayBuffer`         |
| uuid                | () => `string`                                               |
