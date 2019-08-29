<table>
	<tr>
		<th  colspan=2>接口类型</th>
		<th>函数名</th>
		<th>说明</th>
	</tr>
	<tr>
		<td  rowspan=22>私钥相关函数</td>
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
			<li>私钥：用于解密或签名，可导出成员 PublicKey 作为公钥进行加密</li>
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
				<li>password：string 类型，若私钥 PEM 经过加密保护，则在这里传入加密时使用的口令。若没有加密，则传入空字符串`“”`。</li>
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
					<li>PEM: string类型，公钥的PEM格式字符串，未经加密。</li>
					<li>错误信息。</li>
				</ul>
			</td>
		</tr>
		<tr>
		<td rowspan=3>(*PrivateKey) Decrypt(alg string, ciphertext []byte, engine *Engine) ([]byte, error)</td>
		<td>功能：解密，用私钥sk从密文中获取明文。</td>
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
					<li>alg：string类型，算法名称。SM2 签名算法固定入参为 “sm2sign”。</li>
					<li>dgst：[]byte 类型，信息摘要。将要签名的信息和 ComputeSM2IDDigest 函数生成的部分摘要，用选定的哈希算法算出最终摘要，作为此项入参。</li>
					<li>engine： SM2 算法固定入参为 nil</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td>输出：<br>
				<ul class="bottom">
					<li>签名：[]byte 类型。</li>
					<li>错误信息</li>
				</ul>
			</td>
		</tr>
		<tr>
			<td rowspan=3>(*PrivateKey) ComputeSM2IDDigest(id string) ([]byte, error)</td>
			<td>功能：对公钥和入参 id 生成特定摘要片段，用于签名时与信息生成最终摘要。</td>
		</tr>
		<tr>
				<td>参数：<br>
					id：用户入参 id，可看做用户选择的公钥的一部分，在签名和验签时 id 相同才能正确验证。在 fabric 国密证书系统和 gmtool 工具中，默认使用“1234567812345678”作为 id，目前不支持自定义设置。
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
		<tr>
			<td rowspan=14>公钥相关函数</td>
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
	<tr>
		<td  rowspan=9>哈希算法相关函数</td>
		<td  rowspan=3>非成员函数</td>
		<td  rowspan=3>	NewDigestContext(alg string)  (*DigestContext, error)</td>
		<td>功能：初始化所选哈希算法。</td>
	</tr>
	<tr>
		<td>参数：<br>	alg：string 类型，算法名称，国密 SM3 算法入参为 “SM3”，其他算法按 openssl 管理入参。</td>
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
