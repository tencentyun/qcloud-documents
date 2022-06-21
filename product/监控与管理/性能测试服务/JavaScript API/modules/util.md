[pts](../README.md) / [Modules](../modules.md) / util

# Module: util

## Table of contents

### Variables

- [default](#default)

## Variables

<span id="default"></span>

### default

• `Const` **default**: `Object`

#### Type declaration

| Name | Type |
| :------ | :------ |
| `base64Decoding` | (`input`: `string`, `encoding?`: ``"std"`` \| ``"rawstd"`` \| ``"url"`` \| ``"rawurl"``, `mode?`: ``"b"``) => `string` \| `ArrayBuffer` |
| `base64Encoding` | (`input`: `string` \| `ArrayBuffer`, `encoding?`: ``"std"`` \| ``"rawstd"`` \| ``"url"`` \| ``"rawurl"``) => `string` |
| `cloudAPISignatureV3` | (`param`: `CloudAPISignatureV3Param`) => `string` |
| `md5Sum` | (`data`: `string` \| `ArrayBuffer`) => `string` |
| `sloginEncrypt` | (`salt`: `number`, `pwd`: `string`, `vcode`: `string`) => `string` |
| `toArrayBuffer` | (`data`: `string` \| `ArrayBuffer`) => `ArrayBuffer` |
| `uuid` | () => `string` |

#### Defined in

typings/util.d.ts:16
