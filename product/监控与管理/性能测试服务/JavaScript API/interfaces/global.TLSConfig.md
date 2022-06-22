# Interface: TLSConfig

[global](../modules/global.md).TLSConfig

## Table of contents

### Properties

- [certificates](#certificates)
- [insecureSkipVerify](#insecureskipverify)
- [rootCAs](#rootcas)

## Properties

<span id="certificates"></span>

### certificates

• **certificates**: [`Certificate`](global.Certificate.md)[]

客户端证书列表

#### Defined in

typings/global.d.ts:404

___

<span id="insecureSkipVerify"></span>

### insecureSkipVerify

• **insecureSkipVerify**: `boolean`

控制客户端是否验证服务器的证书链和主机名。如果为真，crypto/tls 接受服务器提供的任何证书以及该证书中的任何主机名。

#### Defined in

typings/global.d.ts:396

___

<span id="rootCAs"></span>

### rootCAs

• **rootCAs**: `string`[]

根证书

#### Defined in

typings/global.d.ts:400
