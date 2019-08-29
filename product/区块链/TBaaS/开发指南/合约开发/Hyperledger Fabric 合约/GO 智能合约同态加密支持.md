<script type="text/javascript"<src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script>

## 简介
在 Fabric 区块链网络中，用户可以把业务数据按照特定的业务逻辑上链。对于链上的数据，多个参与方之间都是透明可见证的。对于不能对链上其他组织直接开放的隐私数据，用户可以直接把相关数据的 hash 值存储在链上做为见证。但是在有些业务领域，有些数据不能直接对于其他组织开放，用户又希望其他组织可以根据链上这些数据进行特定的运算背书。
针对以上场景，TBaaS 引入同态加密的能力，很好的保证了数据隐私性，链上透明性，以及数据可操作性。

## TBaaS 的同态加密能力特点
TBaaS 的同态加密能力，主要体现在以下两个方面：
- TBaaS 提供了一个单独的用户工具 paitoo， 用户可以使用这个工具做一些基本的同态公私钥生成，同态加密和同态解密操作。
- TBaaS 在 Go 语言智能合约中，额外引入了 paillier 包，增加了同态算法的 API 接口。用户可以通过 API 接口，实现同态公私钥生成、同态加密、同态解密、同态加法、同态减法以及部分同态乘法（密文和明文相乘）。

下面将分别对 paitool 和 Go 智能合约的 paillier 包进行说明。

## 同态加密算法工具 paitool 
paitool 工具是同态加密 Paillier 算法的用户工具，主要实现了生成同态算法公私钥对，同态加密，同态解密3个功能，您可访问 [paitoo 工具](https://main.qcloudimg.com/raw/d0dd6f0b2303a19cf55a76a6cb0d8061/paitool-amd64-1.4.1-tbaas-r050-d002) 进行下载。

### 使用说明
<table>
	<tr>
		<th>命令</th>
		<th>描述</th>
		<th>参数</th>
	</tr>
	<tr>
		<td>genkey</td>
		<td>生成 Paillier 算法的公私钥对</td>
		<td>
				<ul class="bottom">
					<li>length：公钥长度，即安全等级，可选，默认为2048。</li>
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
				<li>plaintext: 要加密的明文数字，十进制形式的数字，假设公钥值为N，长度为n bit，该数字范围只能取 (-N \over 2,N \ over 2]，即明文的安全长度为 n-2 bit (不算符号的长度)。</li>
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



