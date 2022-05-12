## 简介
在 Fabric 区块链网络中，用户可以把业务数据按照特定的业务逻辑上链。链上存储 hash 数据具备了隐私性强的特点，但存在参与方难以对链上的 hash 数据直接操作的问题。存在如下场景，用户数据不能直接向其他组织直接开放，但其他组织又需要根据链上数据进行特定的运算背书，同时其他组织需要确定链上的数据在特定的数值范围内。例如，在用户转账场景中，对于加密的用户账户，参与方需要判断用户的余额大于等于转账金额，同时可以直接利用链上的加密数据进行加减操作。

针对以上问题，TBaaS 引入 Bulletproofs 零知识范围证明的能力，保证了数据隐私性、链上透明性和数据可操作性。Bulletproofs 零知识范围证明可以利用 Pedersen 承诺算法将明文数值隐藏，实现数据加密。同时 Pedersen 承诺是一个支持同态加法、减法、部分乘法运算的算法，因此在对已经制成承诺的数据进行运算时，不使用“解密-运算-加密”流程，而是直接对承诺进行计算。



## TBaaS 的零知识范围证明能力特点
TBaaS 的零知识范围证明能力，主要体现在以下两个方面：
- TBaaS 提供了零知识范围证明使用的两个工具 [Bulletproofs](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/bulletproofs) 和 [Pedersen](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/pedersen)。Bulletproofs 工具提供生成范围证明、验证范围证明与承诺的有效性、范围证明的同态运算（加、减、乘）等功能。Pedersen 工具提供生成承诺、验证承诺、致盲因子的随机生成、同态加法、减法、乘法及求相反数运算。
- TBaaS 在 Go 语言智能合约中，额外引入了 Bulletproofs 包，增加了零知识范围证明 API 接口。用户可以通过在智能合约中使用 API 接口，实现验证范围证明与承诺的有效性、范围证明的同态运算（加、减、乘）等功能。

下面将分别对零知识范围证明工具 Bulletproofs 和 Pedersen 进行说明。

## 零知识范围证明工具 Bulletproofs
Bulletproofs 工具是零知识范围证明 Bulletproofs 算法的用户端工具。零知识范围证明算法在提供验证一个数值属于 [0，2<sup>64</sup>) 的同时，不向验证者泄露此数值。该工具提供生成范围证明、验证范围证明与承诺的有效性、范围证明的同态运算（加、减、乘）等功能。您可访问 [Bulletproofs](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/bulletproofs) 进行下载。

### 使用说明
<table>
	<tr>
		<th>命令</th>
		<th>描述</th>
		<th>输入参数</th>
		<th>输出</th>
	</tr>
	<tr>
		<td>prove</td>
		<td>为输入的数字生成零知识证明，证明其为非负整数。</td>
		<td>
				<ul class="indentation">
				<li>value：无符号整数，证明该整数是非负数。</li>
				<li>opening：用于在 Pedersen 承诺和 Bulletproofs 证明中隐藏整数 value 的随机数，也用来验证某个 Pedersen 承诺中隐藏的整数是否是某个给定值时用到的致盲因子。（可选，若不给出则使用一个密码学随机数）</li>
				</ul>
				</td>
				<td>
				<ul class="indentation">
				<li>proof：{proof}类型的字符串，是零知识范围证明的内容。</li>
				<li>commitment：{commitment}类型的字符串，是对应 proof 的承诺。</li>
				<li>opening：{opening}类型的字符串，用在 commitment 中作为致盲因子的部分，需要用户自行保存，在核对 commitment 中的数值时使用。</li>
				</td>
	</tr>
	<tr>
		<td>verify</td>
		<td>验证已输入 Bulletproofs 证明和 Pedersen 承诺的有效性。</td>
		<td>
			<ul class="indentation">
				<li>proof：{proof}类型的数据，由 prove 或者 add、sub、mul 等同态运算命令生成的零知识范围证明。</li>
				<li>commitment：{commitment}类型数据，由 pedersen 工具、prove 命令或者 add、sub、mul 等同态运算命令生成的 Pedersen 承诺。</li>
			</ul>
		</td>
		<td>若 proof 与 commitment 相符，并且 commitment 中隐藏的值为非负整数，则显示 “Valid proof”，否则显示 “Invalid proof”。</td>
	</tr>
	<tr>
		<td>add</td>
		<td>证明的同态加法计算。支持“承诺 + 承诺”、“承诺 + 数值”两种模式。</td>
		<td>
			<ul class="indentation">
				<li>value1、value2：数字，分别在commitment1、commitment2两个承诺中。</li>
				<li>commitment1、commitment2：相加的两个承诺。</li>
				<li>opening1、opening2：分别为 commitment1和 commitment2的致盲因子。</li>
			</ul>其中，commitment2、opening2是可选入参，如果同时给出了这两个入参，则使用“承诺 + 承诺”模式，否则使用“承诺 + 数值”模式。
		</td>
		<td>
		<li>proof：value1 + value2为非负整数的证明。</li>
		<li>commitment：value1 + value2的承诺。</li>
		<li>opening：commitment 的致盲因子。</li>
    </td>
	</tr>
	<tr>
		<td>sub</td>
		<td>证明的同态减法计算。支持“承诺 - 承诺”、“承诺 - 数值”两种模式。</td>
		<td>
			<ul class="indentation">
				<li>value1、value2：数字，分别在commitment1、commitment2两个承诺中。</li>
				<li>commitment1、commitment2：相减的两个承诺。</li>
				<li>opening1、opening2：分别为 commitment1和 commitment2的致盲因子。</li>
			</ul>其中，commitment2、opening2是可选入参，如果同时给出了这两个入参，则使用“承诺 - 承诺”模式，否则使用“承诺 - 数值”模式。
		</td>
		<td>
		<li>proof：value1 - value2为非负整数的证明。</li>
		<li>commitment：value1 - value2的承诺。</li>
		<li>opening：commitment 的致盲因子。</li>
    </td>
	</tr>
	<tr>
		<td>mul</td>
		<td>证明的同态乘法计算。只有“承诺 * 数值”的模式。</td>
		<td>
			<ul class="indentation">
				<li>value1、value2：相乘的两个值。</li>
				<li>commitment1：包含 value1的承诺。</li>
				<li>opening1：commitment1的致盲因子。</li>
			</ul>
		</td>
		<td>
		<li>proof：value1 * value2为非负整数的证明。</li>
		<li>commitment：value1 * value2的承诺。</li>
		<li>opening：commitment 的致盲因子。</li>
		</td>
	</tr>
</table>




## 零知识范围证明工具 Pedersen
Pedersen 工具是 Pedersen 承诺的用户端工具。Pedersen 承诺是一个同态加密算法，可以隐藏明文，且与目标明文绑定。但 Pedersen 承诺不能进行解密，作为替代，它支持对明文、承诺（密文）关联性的验证。Pedersen 承诺中用于生成承诺和验证明文、承诺关联性的组件被称为致盲因子，又叫做 opening。该工具提供生成承诺、验证承诺及致盲因子的随机生成、同态加法、减法、乘法、求相反数运算的工具。您可访问 [Pedersen](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/pedersen) 进行下载。

### 使用说明
<table>
	<tr>
		<th>命令</th>
		<th>描述</th>
		<th>输入参数</th>
		<th>输出</th>
	</tr>
	<tr>
		<td>commit</td>
		<td>生成承诺。</td>
		<td>
				<ul class="indentation">
				<li>value：在承诺中绑定及隐藏的目标值。</li>
				<li>opening：用于隐藏 value 的随机数。若不给出则随机生成一个致盲因子。</li>
				</ul>
				</td>
				<td>
				<ul class="indentation">
				<li>commitment：绑定了 value 的承诺。</li>
				<li>opening：用于生成 commitment 的致盲因子。</li>
				</td>
	</tr>
	<tr>
		<td>verify</td>
		<td>验证 Pedersen 承诺的有效性。</td>
		<td>
			<ul class="indentation">
				<li>commitment：绑定了 Value 的 Pedersen 承诺。</li>
				<li>value：在承诺中绑定及隐藏的目标值。</li>
				<li>opening：用于隐藏 value 的随机数。若不给出则随机生成一个致盲因子。</li>
			</ul>
		</td>
		<td>Valid or Invalid。</td>
	</tr>
	<tr>
		<td>genOpening</td>
		<td>生成随机致盲因子。</td>
		<td> - </td>
		<td>opening：一个随机生成的44-byte 的 base64字符串（32-byte 二进制串）。该随机字符串可用于在生成承诺 <code>./pedersen commit</code> 或生成证明 <code>./bulletproofs prove</code> 命令中作为指定的随机数入参。</td>
	</tr>
	<tr>
		<td>openingAdd</td>
		<td>在 Pedersen 承诺的 “承诺 + 承诺” 同态加法运算中更新致盲因子。</td>
		<td>opening1、opening2：两个相加的致盲因子。</td>
		<td>opening：opening1 + opening2</td>
	</tr>
		<tr>
		<td>openingSub</td>
		<td>在 Pedersen 承诺的 “承诺 - 承诺” 同态减法运算中更新致盲因子。</td>
		<td>opening1、opening2：两个相减的致盲因子。</td>
		<td>opening：opening1 - opening2</td>
	</tr>
	<tr>
		<td>openingMul</td>
		<td>在 Pedersen 承诺的 “承诺 * 数值” 同态乘法运算中更新致盲因子。</td>
		<td>
			<ul class="indentation">
				<li>value：参与乘法的数值。</li>
				<li>opening：参与乘法的致盲因子。</li>
			</ul>
		</td>
		<td>opening：opening * value</td>
	</tr>
		<tr>
		<td>openingNeg</td>
		<td>计算 opening 的相反数（mod p 数域内的相反数，其中 p 是一个大质数）。</td>
		<td>opening：需要求相反数的目标致盲因子。</td>
		<td>opening：- opening</td>
	</tr>
</table>


## Go 语言智能合约 Bulletproofs 包接口说明

用户在 TBaaS 平台中使用 Go 语言智能合约时，可直接 import bulletproofs 包，使用相关的接口。当前接口支持验证范围证明与承诺的有效性，同态加法、减法、乘法、求相反数运算。

### Bulletproofs 包支持接口
<table>
	<tr>
		<th>接口</th>
		<th>功能</th>
		<th>参数</th>
		<th>输出</th>
	</tr>
	<tr>
		<td>BulletproofsVerify(proof []byte, commitment []byte) (bool, error)</td>
		<td>验证范围证明与承诺的有效性。</td>
		<td>
			<ul class="bottom">
				<li>proof：672 - byte 二进制串，证明内容。</li>
				<li>commitment：32 - byte 二进制串，与 proof 对应的 Pedersen 承诺。</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>证明有效性：若证明与承诺通过验证，即 x 在[0, 2<sup>64</sup>) 范围内，则返回 true，否则为 false。</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>PedersenAddNum(commitment []byte, value uint64)  ([]byte, error)</td>
		<td>进行“承诺 + 数值”的同态运算，该运算不涉及致盲因子变化，链上、线下皆适用。</td>
		<td>
			<ul class="bottom">
				<li>commitment：32 - byte 二进制串，原承诺。</li>
				<li>value：无符号64位整数，参与同态运算的数值。</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>新承诺：32 - byte 二进制串，假设 commitment 所绑定值为 x，则新承诺绑定值为 “x + value”，致盲因子不变。</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>PedersenAddCommitment(commitment1, commitment2  []byte) ([]byte, error)</td>
		<td>进行“承诺 + 承诺”的同态运算，仅返回新承诺，虽然致盲因子发生变化，但运算过程及结果中不出现新旧致盲因子，适用于链上数据更新。</td>
		<td>
			<ul class="bottom">
				<li>commitment1：32 - byte 二进制串，绑定值为 x、致盲因子为 r 的承诺。</li>
				<li>commitment2：32 - byte 二进制串，绑定值为 y、致盲因子为 s 的承诺。</li>
			</ul> 
		</td>
		<td>
			<ul class="bottom">
				<li>新承诺：32 - byte 二进制串，绑定值为 x + y、致盲因子为 r + s 的承诺。 </li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>PedersenSubNum(commitment []byte, value uint64)  ([]byte, error)</td>
		<td>进行“承诺 - 数值”的同态运算，该运算不涉及致盲因子变化，链上、线下皆适用。</td>
		<td>
			<ul class="bottom">
				<li>commitment：32 - byte 二进制串，原承诺。 </li>
				<li>value：无符号64位整数，参与同态运算的数值。</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>新承诺：32 - byte 二进制串，假设 commitment 所绑定值为 x，则新承诺绑定值为 x - value，致盲因子不变。</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>PedersenSubCommitment(commitment1, commitment2  []byte) ([]byte, error)</td>
		<td>进行“承诺 - 承诺”的同态运算，仅返回新承诺，虽然致盲因子发生了变化，但运算过程及结果中不出现新旧致盲因子，适用于链上数据更新。</td>
		<td>
			<ul class="bottom">
				<li>commitment1：32 - byte 二进制串，绑定值为 x、致盲因子为 r 的承诺。</li>
				<li>commitment2：32 - byte 二进制串，绑定值为 y、致盲因子为 s 的承诺。</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>新承诺：32 - byte 二进制串，绑定值为 x - y、致盲因子为 r - s 的承诺。 </li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>PedersenMulNum(commitment1 []byte, value uint64)  ([]byte, error)</td>
		<td>进行“承诺 * 数值”的同态运算，仅返回新承诺，虽然致盲因子发生了变化，但运算过程及结果中不出现新旧致盲因子，适用于链上数据更新。</td>
		<td>
			<ul class="bottom">
				<li>commitment：32 - byte 二进制串，原承诺。</li>
				<li>value：无符号64位整数，参与同态运算的数值。</li>
			</ul>
		</td>
		<td>
			<ul class="bottom">
				<li>新承诺：32  -byte 二进制串，假设 commitment 所绑定值为 x、致盲因子为 r，则新承诺绑定值为 x * value，致盲因子为 r * value。</li>
				<li>错误信息</li>
			</ul>
		</td>
	</tr>
</table>

<style> .bottom{ margin-bottom:0px !important;} </style>


