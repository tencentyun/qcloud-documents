## 简介
在有些业务场景中，用户希望在智能合约层增加对国密 SM2，SM3 的支持。TBaaS 在智能合约层引入了国密的能力，方便用户快速在智能合约层使用国密。

TBaaS 智能合约对国密的支持，主要体现在两个方面。
- TBaaS 提供了一个单独的用户业务层工具 gmtool，用户可以使用 gmtool 实现公私钥生成、加密、解密、签名以及验签等功能。
- TBaaS 在 Go 语言智能合约中，额外引入了 gmssl 包，增加 SM2 以及 SM3 算法的 API 接口，用户可以方便的在智能合约中集成国密算法。

以下将分别对 gmtool 和 Go 智能合约的 gmssl 包进行说明。

## 国密算法工具 gmtool 
gmtool 工具是国密算法的用户业务层工具，主要实现了公私钥生成，加密，解密，签名和验签等功能，您可访问 [gmtool 工具](https://main.qcloudimg.com/raw/be234bd141c9422c0f69d95cace32115/gmtool-amd64-1.4.1-tbaas-r050-d002) 进行下载。


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
			<li>pkout：新公钥的文件路径</li>
			<li>skout：新私钥的文件路径</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>encrypt</td>
		<td>加密</td>
		<td>
			<ul class="bottom">
				<li>pkin：用于加密的公钥的文件路径，可以是 genkey 生成的公钥文件路径</li>
				<li>plaintext：要加密的明文文件路径</li>
				<li>cipherout：生成的密文的指定文件路径</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>decrypt</td>
		<td>解密，解密后的明文结果会在控制台展示。</td>
		<td>
			<ul class="bottom">
				<li>skin：解密使用的私钥的文件路径</li>
				<li>cipherin：需要解密的密文文件路径</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>sign</td>
		<td>签名</td>
		<td>
			<ul class="bottom">
				<li>skin：签名使用的私钥的文件路径</li>
				<li>message：需要签发的信息的文件路径</li>
				<li>signature：生成的签名的指定文件路径</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>verify</td>
		<td>验签</td>
		<td>
			<ul class="bottom">
				<li>pkin：验签使用的公钥文件路径</li>
				<li>message：验证的信息所在文件路径</li>
				<li>signature：验证的签名所在文件路径</li>
			</ul>
		</td>
	</tr>
</table>

### 示例
- **genkey**
执行以下命令，生成的新公钥存在 pk.sm2 文件中，新私钥存在 sk.sm2 文件中。公私钥都是用 PKCS8 协议存成 PEM 格式。
```
./gmtool genkey -pkout=pk.sm2 -skout=sk.sm2
```

- **encrypt**
执行以下命令，工具会使用 pk.sm2 中存储的公钥对 plain 文件中的内容进行加密，生成的密文存在文件 cipher.sm2 中。密文经过 base64 编码，需要解码后才能作为国密库解密算法的入参，但可以直接作为 gmtool 工具的解密功能入参。
```
./gmtool encrypt -pkin=pk.sm2 -plaintext=plain -cipherout=cipher.sm2
```

- **decrypt**
执行以下命令，工具会解析文件 sk.sm2 中的私钥，对文件 cipher.sm2 中的密文进行解密，解密结果在控制台展示。
```
./gmtool decrypt -skin=sk.sm2 -cipherin=cipher.sm2
```

- **sign**
执行以下命令，工具会解析文件 sk.sm2 中的私钥，对 message 文件中的内容用 SM2 签名算法和 SM3 哈希算法进行签名，并把签名存在文件 sig.sm2 中。签名已经经过 base64 编码，可以直接被 gmtool 工具的验签功能验证，但需要解码后才能作为国密库验签算法的入参。
工具中的摘要片段固定使用“1234567812345678”与入参 message 拼接，暂不支持自定义。这里与 chaincode 中的接口说明对应。
```
./gmtool sign -skin=sk.sm2 -message=message -signature=sig.sm2
```

- **verify**
执行以下命令，在控制台显示验签结果：通过则为 “Valid Signature”，不通过为 “Invalid Signature”。
```
./gmtool verify -pkin=pk.sm2 -message=message -signature=cipher.sm2
```

## Go 语言智能合约 gmssl 包接口说明
Go 语言智能合约 gmssl包 支持 SM2，SM3 算法的相关接口，用户可以很方便的在智能合约中直接使用相关的接口。

### gmssl 包支持接口
#### 私钥相关函数
- 非成员函数
 - GeneratePrivateKey(alg string, args map[string]string, engine \*Engine)  (\*PrivateKey, error)
 **功能**    
生成私钥。
 **参数**
     - alg：string 类型的算法名称，SM2 算法固定为  “EC”。
     - args：map[string]string 类型算法参数，SM2 算法固定为 ：
			map[string]string{
				"ec_paramgen_curve": "sm2p256v1",
				"ec_param_enc": "named_curve",
			}
		
	-  engine：SM2 加密或签名算法固定入参为 nil。

   **输出**
   - 私钥：用于解密或签名，可导出成员PublicKey作为公钥进行加密
   - 错误信息。

 - NewPrivateKeyFromPEM(pem string, password string) (\*PrivateKey, error)
  **功能：**从 PEM 格式字符串中读取私钥。
	**入参：**
	 - pem：string 类型，符合 PEM 格式的字符串。
	 - password：string 类型，若私钥 PEM 经过加密保护，则在这里传入加密时使用的口令。若没有加密，则传入空字符串`“”`。
	 
	**输出：**
	 - 私钥：用于解密或签名，可导出成员 PublicKey 作为公钥进行加密。
	 - 错误信息。





 <style>
	 .bottom{ margin-bottom:0px !important;}
 </style>




