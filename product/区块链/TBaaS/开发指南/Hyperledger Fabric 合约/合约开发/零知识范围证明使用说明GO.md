## 操作场景
用户可以利用 TBaaS 提供的零知识范围证明的能力，便捷的在智能合约中使用零知识证明。在智能合约中使用零知识范围证明，可以分为以下四个步骤：
1. 使用 TBaaS 提供的零知识范围证明工具 Bulletproofs，对特定的数字生成零知识证明，证明其为非负整数。
2. 使用 TBaaS 提供的零知识范围证明工具 Bulletproofs，对步骤1的数字执行同态减法操作，并生成证明，确保对应的数字为非负整数。
3. 使用 TBaaS 智能合约将步骤1生成的承诺和证明存储到链上。
4. 使用 TBaaS 智能合约对特定的数字执行同态减法计算，并验证步骤2生成的证明和同态减承诺的有效性。





## 操作步骤
本文以使用零知识范围证明一个隐藏的值满足特定的条件为例，例如“大于等于18岁”。
1. [](id:stepone)执行以下命令，使用 Bulletproofs 对特定的数字生成零知识证明，证明其为非负数。
```
bulletproofs prove -value=18
```
以返回成功为例，示例代码如下：
```
bulletproofs prove -value=18
proof: jM0+O70Z0nBQJif0BBQHTkWqKskk06FkwwNqTv3B9RcqcElZXezAkhEaMdFwpZKLX09PS8ZOhNsOoGvpCizxTiKxyEmbsNJvuUZVuyMzQq26voz1GRgn31oVk/oo8Voe8FavZiX1F9wwsBWzloAfaRrKvbgeNN2Tq7BCGVIvMi/1AddDWBv32aa4h18iYKYrE8OAixUh57lN5mujdfUYCA6cZL0c8NccVJ5ila1E4dBgXAlxWPAaAC3LlJV4Tf0JaVjluYCw8PRGfO3u6AIjAVfJXkDfNOiOR9jjiUEVTgL6KipHY6EHAZV+4hSKGoD0K2+fSMFkK0+4BC+bokedS1pD2ZiNSxBlUJ9psWa+FBOKHnesHp9N6WwypnIclKQ6Qu8O2Qtw7l/UE+lXswTO3/1SeTTbMtQKxGLdYeEoM2rGZy9GQ3A/fq1H1H9410VlUGzjzVaez8wrtgMa/dwKJj7WHtZ8lhWdzcMsoBo3XuO7OZ6YN3XxdWH1AOjn4yU7AA0IokI6lBIVRKZSVBVRyngxiQb7eulPH10xXW/OOzWwUCm6v/Iw5j3+OQR5y/AfT+2cm/Ar6AAqptnp8mLzId4NYm7QhsOAWvUuUgQFFHnyVff4GBUFXdLOKJb9oJZOThmy4VeMWz5fL6Jwm0Mcn+uaGENZw4gwPtlg4dy3OHV6suIGykFUdK7eqWuP3+Sumf96NyGQRWpa+1Qk1tU8aAAy5jlmcmlPToL9ST8DGqOBFNXyLr7GcdKS5aB+vQsGFtLOeh46A61jiYi7QzTbaDwj6tVRZdvNwkjUl36kWRloG2KqiQe4YR/PIw6sWrj0Aj0H9l2lgZGw5ph34jQdDEWSYibDh4Xr9h0q4yw0ZpBagy8pgVIxYVE3N39BCU4C
commitment: QAlb0rww7GFQF3IGj0osBrj9VdWCV8JG+bSfFX3GlhI=
opening: 04QToSmCYt3KaFqB6VMYDhh/aMKXh1G2b+xnS0IwYAY=
```
2. [](id:steptwo)执行以下命令，使用 Bulletproofs 对 [步骤1](#stepone) 的数字执行同态减法操作，并生成证明，确保对应的数字为非负整数。
```
bulletproofs sub -value1=18 -commitment1=QAlb0rww7GFQF3IGj0osBrj9VdWCV8JG+bSfFX3GlhI= -opening1=04QToSmCYt3KaFqB6VMYDhh/aMKXh1G2b+xnS0IwYAY= -value2=18
```
以返回成功为例，示例代码如下：
```
bulletproofs sub -value1=18 -commitment1=QAlb0rww7GFQF3IGj0osBrj9VdWCV8JG+bSfFX3GlhI= -opening1=04QToSmCYt3KaFqB6VMYDhh/aMKXh1G2b+xnS0IwYAY= -value2=18
proof: GG1kmQGw6ENSmhaG7LfApsixeJIxAfe5Bmns2x6Gwhq2uFWkiWyLYo5EjnRX14wvjHcpchjp9eE1uQh6X3r/Y3Iy53hw7VjIkO8GcJx+11t5iYxWfaquM0iVQcRy1OQ1BkELjeIT6alkXi0qnBnlq4Z1fOcw/ouFg7Se4vX+I2dT5CaxJq++ZBbhx7hjBRPsDZCsDmEoXJcCVTT1uccKAU0yoV+Vm1/11hzbhlWEbQoFGWAqn8w8IoRHF1J4BTkEtdcYtWuM7I1ZDYaY8IpyJzzSAAMHk65/nQgARppB9A8CAZ8FBEU6Oj/iKUQwaILjGG6xY8DngaFM3jg8A7PgOww9Hv7ao0hK26rIpnTF3/m6ezEcWBchdhR6JkDuBIIhqgbtShcZ0iQoUn1ZpOSQ6aC25mHqBnq3/eJfzp5q/nwgBZObeEppGLk+KvcPUlmYElyVjNWZBkfqnDx+MRSME1Y2enysm2hxvjkr+/hpW56y75l2JS9QxWcQHVFFVzVHOnDdSraHARDNHq5bZiinlz8n98fmYVCDyXq+y36JK3BGrljuuBeRNSeZZqhKy/JpyH+vsaeDQLLW7FualiXbNgwsZMNtnO4w53vGyfTps/w9uhh1jmUDi/obK3czP5c6lHDBkUv7i6uzvLz5+tYzvamv/zUOdSHoNn1gcPS7XnCkHEnQzW0rCLHv38MVYeboe10n52Tj2+aTuyeGUEa5IgDiFQJhLx/w6v0DUWl5lNGC/Ma6WjH47TOf4jDEIzVLWB5VIfWNLW9PPFxlfhckJ23iPBZZEFNpjInUNQqnJCAYB9BQkyreyFHYlNHeNl6g6YJEQ1zmZBrGguewH8fbAKY1OJV6fuPfi6xG5aIqfik/o4TNNVa6K2sdNkKDBkAP
commitment: CIXe8Nptv/3VJrgu9xlRHSGC7HB5DGqIGis+HlUipWw=
opening: 04QToSmCYt3KaFqB6VMYDhh/aMKXh1G2b+xnS0IwYAY=
```
3. 使用 TBaaS 智能合约将 [步骤1](#stepone) 生成的承诺和证明存储到链上，您可访问 [Go 语言版本智能合约代码](https://tbaasdoc-1259695942.cos.ap-guangzhou.myqcloud.com/bulletproofs.go) 进行下载。合约需存储用户在 [步骤1](#stepone) 生成的承诺和证明。输入参数分别为 key，步骤1承诺，步骤1证明。
以返回成功为例，示例代码如下：
```
func set(stub shim.ChaincodeStubInterface, args []string) (string, error) {
	if len(args) != 3 {
		return "", fmt.Errorf("incorrect arguments: expecting a user name, a committed value, and a proof")
	}

	userName := args[0]
	commitment := args[1]
	proof := args[2]

	commitmentRaw, err := base64.StdEncoding.DecodeString(commitment)
	if err != nil {
		return "invalid input", fmt.Errorf("invalid input: fail to parse commitment")
	}
	proofRaw, err := base64.StdEncoding.DecodeString(proof)
	if err != nil {
		return "invalid input", fmt.Errorf("invalid input: fail to parse proof")
	}

	isValid, err := bulletproofs.BulletproofsVerify(proofRaw, commitmentRaw)
	if !isValid {
		return "invalid proof", fmt.Errorf("invalid proof")
	}

	err = stub.PutState(userName, []byte(commitment))
	if err != nil {
		return "", fmt.Errorf("failed to set asset: %s", args[0])
	}

	err = stub.PutState(userName + proofSuffix, []byte(proof))
	if err != nil {
		return "", fmt.Errorf("failed to set asset: %s", args[0] + proofSuffix)
	}
	return "success", nil
}
```
4. 使用 TBaaS 智能合约对特定的数字执行同态减法计算，减去特定的数字，例如18，并验证 [步骤2](#steptwo) 生成的证明和智能合约中同态减承诺的有效性，从而可以在链上数据加密的情况下，得到链上数据大于等于18。输入参数分别为 key，要比较的数字18，步骤2生成的 proof。
以返回成功为例，示例代码如下：
```
func subNumber(stub shim.ChaincodeStubInterface, args []string) (string, error) {
	if len(args) != 3 {
		return "", fmt.Errorf("incorrect arguments: expecting a user name, a number, and a proof")
	}

	proof, err := base64.StdEncoding.DecodeString(args[2])
	if err != nil {
		return "", fmt.Errorf("fail to parse the input proof")
	}

	commitment1, err := stub.GetState(args[0])
	if err != nil {
		return "", fmt.Errorf("failed to get asset: %s with error: %s", args[0], err)
	}
	if commitment1 == nil {
		return "", fmt.Errorf("asset not found: %s", args[0])
	}

	proof1, err := stub.GetState(args[0] + proofSuffix)
	if err != nil {
		return "", fmt.Errorf("failed to get asset: %s with error: %s", args[0] + proofSuffix, err)
	}
	if proof1 == nil {
		return "", fmt.Errorf("asset not found: %s", args[0] + proofSuffix)
	}

	num, err := strconv.ParseInt(args[1], 10, 64)
	if err != nil {
		return "", fmt.Errorf("fail to recognize the number")
	}

	commitment1Raw, err := base64.StdEncoding.DecodeString(string(commitment1))
	if err != nil {
		return "", fmt.Errorf("fail to parse commitment1: " + err.Error())
	}
	proof1Raw, err := base64.StdEncoding.DecodeString(string(proof1))
	if err != nil {
		return "", fmt.Errorf("fail to parse proof1: " + err.Error())
	}

	ret, err := bulletproofs.BulletproofsVerify(proof1Raw, commitment1Raw)
	if err != nil {
		return "", fmt.Errorf("invalid proof1: " + err.Error())
	}
	if !ret {
		return "", fmt.Errorf("invalid proof1")
	}

	commitment, err := bulletproofs.PedersenSubNum(commitment1Raw, uint64(num))
	if err != nil {
		return "", fmt.Errorf("fail to compute sum of commitments: " + err.Error())
	}

	ret, err = bulletproofs.BulletproofsVerify(proof, commitment)
	if err != nil {
		return "", fmt.Errorf("invalid proof new: " + err.Error())
	}
	if !ret {
		return "", fmt.Errorf("invalid proof new")
	}

	return "success", nil
}
```
