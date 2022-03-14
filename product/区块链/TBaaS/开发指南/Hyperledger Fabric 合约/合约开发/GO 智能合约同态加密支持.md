## 简介
在 Fabric 区块链网络中，用户可以把业务数据按照特定的业务逻辑上链。对于链上的数据，多个参与方之间均透明可见证。对于不能对链上其他组织直接开放的隐私数据，用户可以直接把相关数据的 hash 值存储在链上作为见证。但是存在如下情形，用户数据不能直接向其他组织直接开放，但其他组织又需要根据链上这些数据进行特定的运算背书。

针对以上场景，TBaaS 引入同态加密的能力，很好的保证了数据隐私性，链上透明性，以及数据可操作性。

## TBaaS 的同态加密能力特点
TBaaS 的同态加密能力，主要体现在以下两个方面：
- TBaaS 提供了一个单独的用户工具 paitool， 用户可以使用这个工具做一些基本的同态公私钥生成，同态加密和同态解密操作。
- TBaaS 在 Go 语言智能合约中，额外引入了 paillier 包，增加了同态算法的 API 接口。用户可以通过 API 接口，实现同态公私钥生成、同态加密、同态解密、同态加法、同态减法以及部分同态乘法（密文和明文相乘）。

下面将分别对 paitool 和 Go 智能合约的 paillier 包进行说明。

## 同态加密算法工具 paitool 
paitool 工具是同态加密 Paillier 算法的用户工具，主要实现了生成同态算法公私钥对，同态加密，同态解密3个功能，您可访问 [paitool](https://main.qcloudimg.com/raw/d0dd6f0b2303a19cf55a76a6cb0d8061/paitool-amd64-1.4.1-tbaas-r050-d002) 进行下载。

### 使用说明
<table>
	<tr>
		<th>命令</th>
		<th>描述</th>
		<th width="68%">参数</th>
	</tr>
	<tr>
		<td>genkey</td>
		<td>生成 Paillier 算法的公私钥对</td>
		<td>
				<ul class="indentation">
				<li>length：公钥长度，即安全等级，<code>[]</code>代表可选，默认为2048</li>
					<li>pkout：新公钥的文件路径</li>
					<li>skout：新私钥的文件路径</li>
				</ul>
				</td>
	</tr>
	<tr>
		<td>encrypt</td>
		<td>加密</td>
		<td>
			<ul class="indentation">
				<li>pkin：用于加密的公钥的文件路径，可以是 genkey 生成的公钥文件路径</li>
				<li>plaintext：要加密的明文数字，十进制形式的数字。假设公钥值为 N，长度为 n bit，该数字范围只能取 <code>(-N/2,N/2]</code>，即明文的安全长度为 <code>n - 2</code> bit（不算符号的长度）</li>
				<li>cipherout：生成的密文的指定文件路径</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>decrypt</td>
		<td>解密</td>
		<td>
			<ul class="indentation">
				<li>skin：解密使用的私钥的文件路径</li>
				<li>cipherin：需要解密的密文文件路径</li>
			</ul>
		</td>
	</tr>
</table>

### 示例
- genkey
执行以下命令，生成的新公钥存在 pk.pai 文件中，新私钥存在 sk.pai 文件中。
公钥是一行16进制字符串，私钥是两行16进制字符串。示例中的公钥是 2048-bit 长的二进制串，16进制编码后为512位字符串。私钥是两段 1024-bit 长的二进制串，16进制编码后为两段256位字符串。
```
./paitool genkey [-length=2048] -pkout=pk.pai -skout=sk.pai
```

- encrypt
执行以下命令，工具会使用 pk.pai 中存储的公钥对数字10进行加密，生成的密文存在文件 cipher.pai 中。
密文是一个16进制字符串，可以直接作为 paitool 工具的解密功能入参，或者在调用 Paillier chaincode 的解密、同态运算接口时作为密文入参。
```
./paitool encrypt -pkin=pk.pai -plaintext=10 -cipherout=cipher.pai
```

- decrypt
执行以下命令，工具会解析文件 sk.pai 中的私钥，对文件 cipher.pai 中的密文进行解密，解密后的明文结果会直接输出。
```
./paitool decrypt -skin=sk.pai -cipherin=cipher.pai
```


## Go 语言智能合约 paillier 包接口说明
Go 语言智能合约 paillier 包是根据轻量同态加密 Paillier 算法实现的，该算法是由 Paillier Pascal 于1999年提出。用户在 TBaaS 平台中使用 Go 语言智能合约时，可直接 import paillier 包，使用相关的接口。该算法支持加法、减法、部分乘法，但对运算的输入和输出有范围限制，**即参与运算的数和运算结果的长度都不能比公钥长，否则会溢出**。

### paillier 包支持接口
<table>
	<tr>
		<th>接口</th>
		<th>功能</th>
		<th>参数</th>
		<th>输出</th>
	</tr>
	<tr>
		<td>GenerateKey(rand io.Reader, length int) (*PrivateKey, error)</td>
		<td>生成私钥</td>
		<td>
			<ul class="bottom">
				<li>rand：io.Reader，是随机数生成器，推荐使用 crypto/rand 库中的 rand.Reader</li>
				<li>length：int，是公钥长度，也代表安全性，推荐使用大于2048的整数</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>私钥：用于解密，可导出成员 PublicKey 作为公钥进行加密</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Encrypt(pk *PublicKey, plaintext string) (string, error)</td>
		<td>加密，生成密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>plaintext：string 类型明文，格式需要是以 string 表示的整数，可以是负数</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Decrypt(sk *PrivateKey, ciphertext string) (string, error)</td>
		<td>解密，用私钥 sk 从密文中获取明文</td>
		<td>
			<ul class="bottom">
				<li>sk：私钥</li>
				<li>ciphertext：string 类型密文</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>明文：string 类型表示的数字</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Neg(pk *PublicKey, ciphertext string) (string, error)</td>
		<td>计算密文中被加密数字的相反数，生成其相反数的密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>ciphertext：string 类型密文</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型，其内容为原信息的相反数</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>AddCipher(pk *PublicKey, cipher1 string, cipher2 string) (string, error)</td>
		<td>计算 cipher1 和 cipher2 中明文的和，并生成和的新密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>cipher1，cipher2：string 类型的密文</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Add(pk *PublicKey, cipher string, plain string) (string, error)</td>
		<td>计算密文 cipher 中被加密的数与明文数字 plain 的和，并生成和的新密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>cipher：string 类型密文</li>
				<li>plain：string 类型明文，以 tring 表示的一个数，可以为负数</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>SubCipher(pk *PublicKey, cipher1 string, cipher2 string) (string, error)</td>
		<td>计算 cipher1 和 cipher2 中明文的差（cipher1 - cipher2），并生成差的新密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>cipher1，cipher2：string 类型的密文</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Sub(pk *PublicKey, cipher string, plain string) (string, error)</td>
		<td>计算密文 cipher 中被加密的数与明文数字 plain 的差（cipher - plain），并生成差的新密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>cipher：string 类型密文</li>
				<li>plain：string 类型明文，以 string 表示的一个数，可以为负数</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>Mul(pk *PublicKey, cipher string, plain string) (string, error)</td>
		<td>计算密文 cipher 中被加密的数与明文数字 plain 的乘积，并生成积的新密文</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>cipher：string 类型密文</li>
				<li>plain：string 类型明文，以 string 表示的一个数，可以为负数</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>密文：string 类型</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>GetPublicKeyHex(pk *PublicKey) string</td>
		<td>生成公钥的16进制字符串表达方式</td>
		<td>
			pk：公钥
		</td>
		<td>string 类型的公钥字符串</td>
	</tr>
	<tr>
		<td>GetPublicKeyFromHex(hex string) (*PublicKey, error)</td>
		<td>从16进制字符串中恢复出公钥</td>
		<td>string：16进制字符串</td>
		<td>公钥</td>
	</tr>
	<tr>
		<td>WritePublicKeyToFile(pk *PublicKey, file string) error</td>
		<td>将公钥写入文件</td>
		<td>
			<ul class="bottom">
				<li>pk：公钥</li>
				<li>file：文件名</li>
			</ul>
		</td>
		<td>错误信息</td>
	</tr>
	<tr>
		<td>ReadPublicKeyFromFile(file string) (*PublicKey, error)</td>
		<td>从文件中读取公钥</td>
		<td>file：文件名</td>		
		<td>
			<ul class="bottom">
				<li>公钥</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>GetPrivateKeyHex(sk *PrivateKey) string</td>
		<td>生成私钥的16进制字符串表达方式</td>
		<td>sk：私钥</td>
		<td>string 类型的私钥字符串</td>
	</tr>
	<tr>
		<td>GetPrivateKeyFromHex(hex string) (*PrivateKey, error)</td>
		<td>从16进制字符串中恢复出私钥</td>
		<td>string：16进制字符串</td>
		<td>私钥</td>
	</tr>
	<tr>
		<td>WritePrivateKeyToFile(sk *PrivateKey, file string) error</td>
		<td>将私钥写入文件</td>
		<td>
			<ul class="bottom">
				<li>sk：私钥</li>
				<li>file：文件名</li>
			</ul>
		</td>
		<td>错误信息</td>
	</tr>
	<tr>
		<td>ReadPrivateKeyFromFile(file string) (*PrivateKey, error)</td>
		<td>从文件中读取私钥</td>
		<td>file：文件名</td>
		<td>
			<ul class="bottom">
				<li>私钥</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>GetCiphertextHex(cipher string) string</td>
		<td>生成密文的16进制字符串表达方式</td>
		<td>cipher：密文</td>
		<td>string类型的密文字符串</td>
	</tr>
	<tr>
		<td>GetCiphertextFromHex(hex string) string</td>
		<td>从16进制字符串中恢复出密文</td>
		<td>string：16进制字符串</td>
		<td>密文</td>
	</tr>
	<tr>
	<td>WriteCiphertextToFile(cipher string, file string) error</td>
	<td>将密文写入文件</td>
	<td>
		<ul class="bottom">
			<li>cipher：密文</li>
			<li>file：文件名</li>
		</ul>
	</td>
	<td>错误信息</td>
</tr>
<tr>
	<td>ReadCiphertextFromFile(file string) (string, error)</td>
	<td>从文件中读取密文</td>
	<td>file：文件名</td>
	<td>
		<ul class="bottom">
			<li>密文</li>
			<li>错误信息</li>
		</ul>
	</td>
</tr>
</table>

<style> .bottom{ margin-bottom:0px !important;} </style>



