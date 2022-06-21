# Interface: File

[http](../modules/http.md).File

## Table of contents

### Properties

- [contentType](#contenttype)
- [data](#data)
- [name](#name)

## Properties

<span id="contentType"></span>

### contentType

• **contentType**: `string`

contentType 表示内容类型，默认为 application/octet-stream。

#### Defined in

typings/http.d.ts:154

___

<span id="data"></span>

### data

• **data**: `string` \| `ArrayBuffer`

data 表示文件内容。通常使用 open() 的返回值。

#### Defined in

typings/http.d.ts:146

___

<span id="name"></span>

### name

• **name**: `string`

name 表示文件名，默认为纳秒级时间戳。

#### Defined in

typings/http.d.ts:150
