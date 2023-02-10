**Web Crypto API** 基于 Web APIs 标准 [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API) 进行设计。提供了一组常见的加密操作接口，相比纯 JavaScript 实现的加密接口，`Web Crypto API` 的性能更高。

>! 不支持直接构造 `Crypto` 对象，边缘函数运行时会在全局注入，直接使用全局 crypto 实例即可。

## 描述
```typescript
// 编码
const encodeContent = new TextEncoder().encode('hello world');
// 使用 crypto，生成 SHA-256 哈希值 Promise<ArrayBuffer>
const sha256Content = await crypto.subtle.digest(
  { name: 'SHA-256' },
  encodeContent 
);
const result = new Uint8Array(sha256Content); 
```

## 属性
```typescript
// crypto.subtle
readonly subtle: SubtleCrypto;
```
提供常见的加密操作, 例如: 哈希、签名/验签、加解密等，详情参见 [SubtleCrypto](#SubtleCrypto)。

## 方法
### getRandomValues
```typescript
crypto.getRandomValues(buffer: TypedArray): TypedArray;
```

生成随机数填充 buffer, 并返回 buffer。

#### 参数

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="20%">类型</th>
			<th width="10%">必填</th>
			<th width="60%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>buffer</td>
			<td>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int8Array">Int8Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8Array">Uint8Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint8ClampedArray">Uint8ClampedArray</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int16Array">Int16Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint16Array">Uint16Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Int32Array">Int32Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Uint32Array">Uint32Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt64Array">BigInt64Array</a> |<br>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigUint64Array">BigUint64Array</a>
      </td>
			<td>是</td>
			<td>
        随机数缓冲区，不超过 65536 字节。详情参见 <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray">TypedArray</a>。
      </td>
		</tr>
	</tbody>
</table>

### randomUUID
```typescript
crypto.randomUUID(): string;
```

返回随机 UUID(v4)。

## SubtleCrypto[](id:SubtleCrypto)
提供常见的加密操作, 例如: 哈希、签名/验签、加解密等，详情参见 [MDN 官方文档：SubtleCrypto](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto#Methods)。

>? **SubtleCrypto** 加密接口按功能分为两类：
- **加密功能**，包含 `encrypt/decrypt`、`sign/verify`、`digest`, 可以用来实现隐私和身份验证等安全功能。
- **密钥管理功能**，包含 `generateKey`、`deriveKey`、`importKey/exportKey`, 可以用来管理密钥。

### digest
```typescript
crypto.subtle.digest(algorithm: string | object, data: ArrayBuffer): Promise<ArrayBuffer>;
```

返回 Promise 对象，包含生成的数据摘要（hash），详情参见 [MDN 官方文档：SubtleCrypto.digest](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/digest)。

### encrypt 
```typescript
crypto.subtle.encrypt(algorithm: object, key: CryptoKey, data: ArrayBuffer): Promise<ArrayBuffer>;
```

返回 Promise 对象，包含加密数据，详情参见 [MDN 官方文档：SubtleCrypto.encrypt](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt)。

### decrypt
```typescript
crypto.subtle.decrypt(algorithm: object, key: CryptoKey, data: ArrayBuffer): Promise<ArrayBuffer>;
```

返回 Promise 对象，包含解密数据，详情参见 [MDN 官方文档：SubtleCrypto.decrypt](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/decrypt)。

### sign
```typescript
crypto.subtle.sign(algorithm: string | object, key: CryptoKey, data: ArrayBuffer): Promise<ArrayBuffer>;
``` 

返回 Promise 对象，包含数据签名，详情参见 [MDN 官方文档：SubtleCrypto.sign](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/sign)。

### verify
```typescript
crypto.subtle.verify(algorithm: string | object, key: CryptoKey, signature: BufferSource, data: ArrayBuffer): Promise<boolean>;
```

返回 Promise 对象，包含签名验证结果，详情参见 [MDN 官方文档：SubtleCrypto.verify](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/verify)。

### generateKey[](id:generateKey)
```typescript
crypto.subtle.generateKey(algorithm: object, extractable: boolean, keyUsages: Array<string>): Promise<CryptoKey | CryptoKeyPair>;
```

返回 Promise 对象，包含密钥 [CryptoKey](id:CryptoKey) 或密钥对 [CryptoKeyPair](id:CryptoKeyPair)，详情参见 [MDN 官方文档：SubtleCrypto.generateKey](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/generateKey)。

### deriveKey[](id:deriveKey)
```typescript
crypto.subtle.deriveKey(algorithm: object, baseKey: CryptoKey, derivedKeyAlgorithm: object, extractable: boolean, keyUsages: Array<string>): Promise<CryptoKey>;
```

返回 Promise 对象，包含密钥 [CryptoKey](id:CryptoKey)，详情参见 [MDN 官方文档：SubtleCrypto.deriveKey](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveKey)。

### importKey[](id:importKey)
```typescript
crypto.subtle.importKey(format: string, keyData: BufferSource, algorithm: string | object, extractable: boolean, keyUsages: Array<string>): Promise<CryptoKey>;
```

返回 Promise 对象，包含密钥 [CryptoKey](id:CryptoKey)，详情参见 [MDN 官方文档：SubtleCrypto.importKey](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey)。

### exportKey
```typescript
crypto.subtle.exportKey(format: string, key: CryptoKey): Promise<ArrayBuffer>;
```

返回 Promise 对象，包含导出密钥 ArrayBuffer，详情参见 [MDN 官方文档：SubtleCrypto.exportKey](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/exportKey)。

### deriveBits
```typescript
crypto.subtle.deriveBits(algorithm: object, baseKey: CryptoKey, length: integer): Promise<ArrayBuffer>;
```

返回 Promise 对象，包含伪随机字节 ArrayBuffer，详情参见 [MDN 官方文档：SubtleCrypto.deriveBits](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/deriveBits)。

### wrapKey 
```typescript
crypto.subtle.wrapKey(format: string, key: CryptoKey, wrappingKey: CryptoKey, wrapAlgo: string | object): Promise<ArrayBuffer>;;
```

返回 Promise 对象，包含封装密钥 ArrayBuffer，详情参见 [MDN 官方文档：SubtleCrypto.wrapKey](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/wrapKey)。

### unwrapKey[](id:unwrapKey)
```typescript
crypto.subtle.unwrapKey(format: string, wrappedKey: ArrayBuffer, unwrappingKey: CryptoKey, unwrapAlgo: string | object, unwrappedKeyAlgo: string | object, extractable: boolean, keyUsages: Array<string>): Promise<CryptoKey>;
```

返回 Promise 对象，包含解封密钥 [CryptoKey](id:CryptoKey)，详情参见 [MDN 官方文档：SubtleCrypto.unwrapKey](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/unwrapKey)。

## CryptoKey[](id:CryptoKey)
`CryptoKey` 表示用加密算法生成的密钥，详细参见 [MDN 官方文档 CryptoKey](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey)。不支持直接构造 CryptoKey 对象，使用下述接口生成密钥：

- [crypto.subtle.generateKey](#generateKey)
- [crypto.subtle.importKey](#importKey)
- [crypto.subtle.deriveKey](#deriveKey)
- [crypto.subtle.unwrapKey](#unwrapKey)

`CryptoKey` 属性描述如下。

<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">只读</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>type</td>
			<td>string</td>
			<td>是</td>
			<td>密钥类型。</td>
		</tr>
    <tr>
			<td>extractable</td>
			<td>boolean</td>
			<td>是</td>
			<td>密钥是否可导出。</td>
		</tr>
    <tr>
			<td>algorithm</td>
			<td>object</td>
			<td>是</td>
			<td>算法相关, 包含算法需要的字段。</td>
		</tr>
    <tr>
			<td>usages</td>
			<td>Array&lt;string&gt;</td>
			<td>是</td>
			<td>密钥的用途。</td>
		</tr>
	</tbody>
</table>

## CryptoKeyPair[](id:CryptoKeyPair)
`CryptoKeyPair` 表示用加密算法生成的密钥对，详细参见 [MDN 官方文档：CryptoKeyPair](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKeyPair)。不支持直接构造 CryptoKeyPair 对象，使用下述接口生成密钥对：

- [crypto.subtle.generateKey](#generateKey)

`CryptoKeyPair` 属性描述如下。


<table>
	<thead>
		<tr>
			<th width="10%">属性名</th>
			<th width="15%">类型</th>
			<th width="10%">只读</th>
			<th width="65%">说明</th>
	</tr>
	</thead>
	<tbody>
		<tr>
			<td>privateKey</td>
			<td><a href="#CryptoKey">CryptoKey</a></td>
			<td>是</td>
			<td>对于加解密算法, 私钥用于解密。对于签名算法, 私钥用于签名。</td>
		</tr>
    <tr>
			<td>publicKey</td>
			<td><a href="#CryptoKey">CryptoKey</a></td>
			<td>是</td>
			<td>对于加解密算法, 公钥用于加密。对于签名算法, 公钥用于验签。</td>
		</tr>
	</tbody>
</table>

## 支持算法
边缘函数支持 Web APIs 标准 [WebCrypto](https://www.w3.org/TR/WebCryptoAPI/) 定义的所有算法，详细如下表所示。
<table>
<thead>
<tr>
<th width="12%">lgorithm</th>
<th width="11%">encrypt() decrypt()</th>
<th width="11%">sign() verify()</th>
<th width="11%">wrapKey() unwrapKey()</th>
<th width="11%">deriveKey() deriveBits()</th>
<th width="11%">generateKey()</th>
<th width="11%">importKey()</th>
<th width="11%">exportKey()</th>
<th width="11%">digest()</th>
</tr>
</thead>
<tbody><tr>
<td>RSASSA-PKCS1-v1_5</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>RSA-PSS</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>RSA-OAEP</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>ECDSA</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>ECDH</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>HMAC</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>AES-CTR</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>AES-CBC</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>AES-GCM</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>AES-KW</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td>✓</td>
<td>✓</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>HKDF</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>PBKDF2</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td>✓</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
</tr>
<tr>
<td>SHA-1</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
</tr>
<tr>
<td>SHA-256</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
</tr>
<tr>
<td>SHA-384</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
</tr>
<tr>
<td>SHA-512</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
</tr>
<tr>
<td>MD5</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td style="color:#aaa">-</td>
<td>✓</td>
</tr>
</tbody></table>

## 示例代码
```typescript
function uint8ArrayToHex(arr) {
	return Array.prototype.map.call(arr, (x) => ((`0${x.toString(16)}`).slice(-2))).join('');
}

async function handleEvent(event) {
	const encodeArr = TextEncoder().encode('hello world');
	// 执行 md5
	const md5Buffer = await crypto.subtle.digest({ name: 'MD5' }, encodeArr);
	// 输出十六进制字符串
	const md5Str = uint8ArrayToHex(new Uint8Array(md5Buffer));
	
	const response = new Response(md5Str);
	return response;
}
  
addEventListener('fetch', async (event) => {    
  event.respondWith(handleEvent(event));
});
```

## 相关参考 
- [MDN 官方文档：Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API)
- [MDN 官方文档：SubtleCrypto](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto#Methods)
- [MDN 官方文档：CryptoKey](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey)
- [MDN 官方文档：CryptoKeyPair](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKeyPair)
- [示例函数：防篡改校验](https://cloud.tencent.com/document/product/1552/84081)
- [示例函数：m3u8 改写与鉴权](https://cloud.tencent.com/document/product/1552/84086)
- [示例函数：缓存 POST 请求](https://cloud.tencent.com/document/product/1552/84079)
