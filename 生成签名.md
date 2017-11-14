1. **前置条件：**必须按照 [Access Token获取](https://cloud.tencent.com/document/product/295/10118) 获取 NONCE ticket。
2. 合作方根据本次人脸验证的如下参数生成签名,需要签名的参数信息如下：
<table>
<tr>
<th>参数</th> 
<th>说明</th> 
</tr>
<tr>
<td>appId</td>
<td>腾讯云分配的 app_id</td>
</tr>
<tr>
<td >userId</td>
<td >用户唯一标识</td>
</tr>
<tr>
<td >version</td>
<td >1.0.0</td>
</tr>
<tr>
<td >ticket </td>
<td >合作伙伴服务端缓存的 tikcet。注意是 NONCE 类型，具体见<a href="https://cloud.tencent.com/document/product/295/10118"> Access Token 获取</a>以获取规则。
</td>
</tr>
<tr>
<td >nonceStr</td>
<td >必须是 32 位随机数</td>
</tr>
</table>
3. 生成一个 32 位的随机字符串(字母和数字) nonceStr(登录时也要用到)，将appId、userId、version 连同ticket、nonceStr 共五个参数的值进行字典序排序。
4. 将排序后的所有参数字符串拼接成一个字符串进行 SHA1 编码
5. SHA1 编码后的 40 位字符串作为签名 (sign)
6. 签名算法，示例如下（请参考[签名算法说明](https://cloud.tencent.com/document/product/295/10137)）：
请求参数：
```
appId = TIDA0001
userId= userID19959248596551
	nonceStr = kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T (必须为 32 位)
	version = 1.0.0
	ticket=XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS
```
字典排序后的参数为：
```
[1.0.0,TIDA0001,XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMS，kHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7T, userID19959248596551]
```
拼接后的字符串为：
```
1.0.0TIDA0001XO99Qfxlti9iTVgHAjwvJdAZKN3nMuUhrsPdPlPVKlcyS50N6tlLnfuFBPIucaMSkHoSxvLZGxSoFsjxlbzEoUzh5PAnTU7TuserID19959248596551
```
计算 SHA1 得到签名：
```
4AE72E6FBC2E9E1282922B013D1B4C2CBD38C4BD
```
该字串就是最终生成的签名（40 位），不区分大小写。
