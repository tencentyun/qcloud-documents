## 简介
在业务场景中，用户希望在智能合约层增加对国密算法 SM2，SM3 的支持。TBaaS 已在智能合约层引入了国密算法的能力，方便用户快速在智能合约层使用国密算法。

TBaaS 智能合约对国密算法的支持，主要体现在以下两个方面：
- TBaaS 提供了一个单独的用户业务层工具 gmtool，用户可以使用 gmtool 实现公私钥生成、加密、解密、签名以及验签等功能。
- TBaaS 在 Go 语言智能合约中，额外引入了 gmssl 包，增加 SM2 以及 SM3 算法的 API 接口，用户可以方便的在智能合约中集成国密算法。

以下将分别对 gmtool 和 Go 智能合约的 gmssl 包进行说明。

## 国密算法工具 gmtool 
Gmtool 工具是国密算法的用户业务层工具，主要实现了公私钥生成、加密、解密、签名、验签等功能，您可访问 [gmtool](https://main.qcloudimg.com/raw/be234bd141c9422c0f69d95cace32115/gmtool-amd64-1.4.1-tbaas-r050-d002) 进行下载。


### 使用说明
<table>
	<tr>
		<th>命令</th>
		<th>描述</th>
		<th>参数</th>
	</tr>
	<tr>
		<td>genkey</td>
		<td>生成 SM2 算法的公私钥对（加密、签名的公私钥对使用同一个算法）</td>
		<td> 
			<ul class="bottom">
			<li>pkout：新公钥的文件路径。</li>
			<li>skout：新私钥的文件路径。</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>encrypt</td>
		<td>加密</td>
		<td>
			<ul class="bottom">
				<li>pkin：用于加密的公钥的文件路径，可以是 genkey 生成的公钥文件路径。</li>
				<li>plaintext：要加密的明文文件路径。</li>
				<li>cipherout：生成的密文的指定文件路径。</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>decrypt</td>
		<td>解密</td>
		<td>
			<ul class="bottom">
				<li>skin：解密使用的私钥的文件路径。</li>
				<li>cipherin：需要解密的密文文件路径。</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>sign</td>
		<td>签名</td>
		<td>
			<ul class="bottom">
				<li>skin：签名使用的私钥的文件路径。</li>
				<li>message：需要签发的信息的文件路径。</li>
				<li>signature：生成的签名的指定文件路径。</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>verify</td>
		<td>验签</td>
		<td>
			<ul class="bottom">
				<li>pkin：验签使用的公钥文件路径。</li>
				<li>message：验证的信息所在文件路径。</li>
				<li>signature：验证的签名所在文件路径。</li>
			</ul>
		</td>
	</tr>
</table>

### 示例
- **genkey**
执行以下命令，生成的新公钥存在 pk.sm2 文件中，新私钥存在 sk.sm2 文件中。公私钥均使用 PKCS8 协议存成 PEM 格式。
>?本示例使用同一套公私钥来执行加解密以及签名验签。在生产环境中，加密和签名的公私钥对必须都单独生成，不能混用。
>
```
./gmtool genkey -pkout=pk.sm2 -skout=sk.sm2
```

- **encrypt**
执行以下命令，工具会使用 pk.sm2 中存储的公钥对 plain 文件中的内容进行加密，生成的密文存在文件 cipher.sm2 中。密文经过 base64 编码，需要解码后才能作为国密算法库解密算法的入参，但可以直接作为 gmtool 工具的解密功能入参。
```
./gmtool encrypt -pkin=pk.sm2 -plaintext=plain -cipherout=cipher.sm2
```

- **decrypt**
执行以下命令，工具会解析文件 sk.sm2 中的私钥，对文件 cipher.sm2 中的密文进行解密，解密结果在控制台展示。
```
./gmtool decrypt -skin=sk.sm2 -cipherin=cipher.sm2
```

- **sign**
执行以下命令，工具会解析文件 sk.sm2 中的私钥，对 message 文件中的内容用 SM2 签名算法和 SM3 哈希算法进行签名，并把签名存在文件 sig.sm2 中。签名已经过 base64 编码，可以直接被 gmtool 工具的验签功能验证，但需要解码后才能作为国密算法库验签算法的入参。
工具中的摘要片段固定使用“1234567812345678”与入参 message 拼接，暂不支持自定义。这里与 chaincode 中的接口说明对应。
>?根据GM/T 0009-2012《SM2密码算法使用规范》，用户身份标识ID的长度为16字节，其默认值从左到右依次为1234567812345678。
>
```
./gmtool sign -skin=sk.sm2 -message=message -signature=sig.sm2
```

- **verify**
执行以下命令，在控制台显示验签结果。通过则为 “Valid Signature”，不通过为 “Invalid Signature”。
```
./gmtool verify -pkin=pk.sm2 -message=message -signature=sig.sm2
```

## Go 语言智能合约 gmssl 包接口说明
Go 语言智能合约 gmssl 包 支持 SM2，SM3 算法的相关接口，用户可以很方便的在智能合约中直接 import gmssl 包，使用相关的接口。

### gmssl 包支持接口
#### 私钥相关函数
<table>
	<tr>
		<th width="12%">接口类型</th>
		<th width="39%">函数名</th>
		<th width="53%">说明</th>
	</tr>
	<tr>
		<td rowspan=6>非成员函数</td>
		<td rowspan=3>GeneratePrivateKey(alg string, args map[string]string, engine *Engine)  (*PrivateKey, error)</td>
		<td>功能：生成私钥。</td>
		</tr>
		<tr><td>
		参数：<br>
		<ul class="bottom">
			<li>alg：string 类型的算法名称，SM2 算法固定为  “EC”。</li>
			<li>args：map[string]string 类型算法参数，SM2 算法固定为 ：<br><pre>map[string]string{
				"ec_paramgen_curve": "sm2p256v1",
				"ec_param_enc": "named_curve",
			}</pre></li>
			<li>engine：SM2 加密或签名算法固定入参为 nil。</li>
		</ul>
		</td></tr>
		<tr><td>输出：<br>
		<ul class="bottom">
			<li>私钥：用于解密或签名，可导出成员 PublicKey 作为公钥进行加密。</li>
			<li>错误信息。</li>
		</ul>
		</td></tr>
		<tr>
			<td rowspan=3>NewPrivateKeyFromPEM(pem string, password string) (*PrivateKey, error)</td>
			<td>功能：从 PEM 格式字符串中读取私钥。</td>
		</tr>
		<tr>
		<td>参数：<br>
			<ul class="bottom">
				<li>pem：string 类型，符合 PEM 格式的字符串。</li>
				<li>password：string 类型，若私钥 PEM 经过加密保护，则在这里传入加密时使用的口令。若没有加密，则传入空字符串<code>“”</code>。</li>
			</ul>
		</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>私钥：用于解密或签名，可导出成员 PublicKey 作为公钥进行加密。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
		<td rowspan=16>成员函数</td>
		<td  rowspan=3>(*PrivateKey) GetPEM(cipher string, password string) (string, error)</td>
		<td>功能：生成加密保护的私钥 PEM 格式字符串。</td>
		</tr>
		<tr>
			<td>参数：<br>
				<ul class="bottom">
					<li>cipher：string 类型，加密私钥 PEM 的算法，可选 “SM4”、 “AES256” 及其它 openssl 支持的对称加密算法。</li>
					<li>password：string 类型，加密私钥使用的口令，用于扩展生成对称加密的密钥。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>PEM：string 类型。</li>
					<li>错误信息。</li>
				</ul>
			<td>
		</tr>
		<tr>
			<td rowspan=2>(*PrivateKey) GetUnencryptedPEM() (string, error)</td>
			<td>功能： 生成不加密的私钥 PEM 格式字符串。</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>PEM：string 类型。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
		<td rowspan=2>(*PrivateKey) GetPublicKeyPEM() (string, error)</td>
		<td>功能：从私钥中抽取对应的公钥。</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>PEM：string 类型，公钥的 PEM 格式字符串，未经加密。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
		<td rowspan=3>(*PrivateKey) Decrypt(alg string, ciphertext []byte, engine *Engine) ([]byte, error)</td>
		<td>功能：解密，用私钥 sk 从密文中获取明文。</td>
		</tr>
		<tr>
		<td>参数：<br>
			<ul class="bottom">
				<li>alg：string 类型，算法名称。SM2 加密算法固定入参为 “sm2encrypt-with-sm3”。</li>
				<li>ciphertext：[]byte 类型，密文（由 gmtool 工具或者调用公钥成员函数 Encrypt 生成）。</li>
				<li>engine：SM2 算法固定入参 nil。</li>
			</ul>
		</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li> 明文：[]byte 类型明文字符串。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td rowspan=3>(*PrivateKey) Sign(alg string, dgst []byte, engine *Engine) ([]byte, error)</td>
			<td>功能：针对入参中的信息摘要 dgst 生成签名。</td>
		</tr>
		<tr>
			<td>参数：<br>
				<ul class="bottom">
					<li>alg：string 类型，算法名称。SM2 签名算法固定入参为 “sm2sign”。</li>
					<li>dgst：[]byte 类型，信息摘要。将要签名的信息和 ComputeSM2IDDigest 函数生成的部分摘要，用选定的哈希算法算出最终摘要，作为此项入参。</li>
					<li>engine： SM2 算法固定入参为 nil。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>签名：[]byte 类型。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td rowspan=3>(*PrivateKey) ComputeSM2IDDigest(id string) ([]byte, error)</td>
			<td>功能：对公钥和入参 id 生成特定摘要片段，用于签名时与信息生成最终摘要。</td>
		</tr>
		<tr>
				<td>参数：<br>
					id：用户入参 id，可看做用户选择的公钥的一部分，在签名和验签时 id 相同才能正确验证。在 fabric 国密算法证书系统和 gmtool 工具中，默认使用“1234567812345678”作为 id，目前不支持自定义设置。
			</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>摘要片段：[]byte 类型，一对特定公私钥对通常只有一个特定的摘要片段，可以预先算好，后续使用时直接取用结果。该摘要片段在签名时与被签名的信息拼接后使用哈希算法算出完整摘要。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
</table>

#### 公钥相关函数
<table>
	<tr>
		<th width="11%">接口类型</th>
		<th width="39%">函数名</th>
		<th width="53%">说明</th>
	</tr>
		<tr>
			<td rowspan=3>非成员函数</td>
			<td rowspan=3>NewPublicKeyFromPEM(pem string) (*PublicKey, error)</td>
			<td>功能：从 PEM 格式的字符串中读取解析出公钥。</td>
		</tr>
		<tr>
			<td>参数：<br>pem：string 类型，PEM 格式的公钥字符串。</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>公钥：可用于加密或验签。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td rowspan=11>成员函数</td>
			<td rowspan=2>(*PublicKey) GetPEM() (string, error)</td>
			<td>功能：生成存有公钥信息的 PEM 格式字符串。</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>PEM：string 类型，可用于公钥的传输和保存。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td rowspan=3>(*PublicKey) Encrypt(alg string, plaintext []byte, engine *Engine) ([]byte, error)</td>
			<td>功能：加密，生成密文。</td>
		</tr>
		<tr>
			<td>参数：<br>
				<ul class="bottom">
					<li>alg：string 类型，算法名称，SM2 加密算法固定入参为 “sm2encrypt-with-sm3”。</li>
					<li>plaintext：[]byte 类型，明文字符串。</li>
					<li>engine：SM2 算法固定入参为 nil。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>密文：[]byte 类型。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td rowspan=3>(*PublicKey) Verify(alg string, dgst []byte, sig []byte, engine *Engine) error</td>
			<td>功能：验证摘要 dgst、签名 sig 是否与调用的公钥对应。</td>
		</tr>
		<tr>
			<td>参数：<br>
				<ul class="bottom">
					<li>alg：string 类型，算法名称。SM2 签名算法固定入参为 “sm2sign”。</li>
					<li>dgst：[]byte 类型，信息摘要。</li>
					<li>sig：[]byte 类型，签名。</li>
					<li>engine：SM2 签名算法固定入参 nil。</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>输出：<br>	错误信息：若错误信息为 nil，则验证通过，否则验签不通过。</td>
		</tr>
		<tr>
			<td rowspan=3>(*PublicKey) ComputeSM2IDDigest(id string) ([]byte, error)</td>
			<td>功能：对公钥和入参 id 生成特定摘要片段，用于签名时与信息生成最终摘要。与私钥的同名成员函数相同。</td>
		</tr>
		<tr>
			<td>参数：<br>id：string 类型，默认入参“1234567812345678”，暂不支持自定义。</td>
		</tr>
	<tr>
		<td>输出：<br>
			<ul class="bottom">
				<li>摘要片段：[]byte 类型。</li>
				<li>错误信息。</li>
			</ul>
		</td>
	</tr>
	</table>
	

#### 哈希算法相关函数
<table>
		<tr>
		<th width="11%">接口类型</th>
		<th width="39%">函数名</th>
		<th width="53%">说明</th>
	</tr>
	<tr>
		<td  rowspan=3>非成员函数</td>
		<td  rowspan=3>	NewDigestContext(alg string)  (*DigestContext, error)</td>
		<td>功能：初始化所选哈希算法。</td>
	</tr>
	<tr>
		<td>参数：<br>	alg：string 类型，算法名称，国密算法 SM3 算法入参为 “SM3”，其他算法按 openssl 管理入参。</td>
	</tr>
	<tr>
		<td>输出：哈希算法实例。</td>
	</tr>
	<tr>
		<td rowspan=5>成员函数</td>
		<td>(*DigestContext) Reset() error</td>
		<td>功能：充值哈希算法，清除接入算法的字符串。</td>
	</tr>
	<tr>
		<td rowspan=2>(*DigestContext) Update(data []byte) error</td>
		<td>功能：把 data 拼接到输入的数据末尾。</td>
	</tr>
	<tr>
		<td>参数：<br>data：要拼接的新数据。</td>
	</tr>
	<tr>
		<td rowspan=2>(*DigestContext) Final() ([]byte, error)</td>
		<td>功能：用已经用 Update 拼接入得数据生成摘要。</td>
	</tr>
	<tr>
		<td>输出：<br>
			<ul class="bottom">
				<li>摘要：[]byte 类型，使用 Update 传入的所有数据生成的摘要。</li>
				<li>错误信息。</li>
			</ul>
		</td>
	</tr>
</table>


 <style>
	 .bottom{ margin-bottom:0px !important;}
 </style>





