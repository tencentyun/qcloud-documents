在 CAM 中，可对主密钥资源进行以下 API 操作的授权， 具体 API 支持的资源和条件的对应关系如下：

| API 操作 | 资源 | 条件 | 备注 |
|---------|---------|---------|---------|
| kms:CreateKey | qcs::kms:$region:$account:key/ |   |  |
| kms:ListKey | qcs::kms:$region:$account:key/ |  |  |
| kms:Encrypt | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |  | creatorUin 表示资源创建者的 uin，资源创建者可为根帐号或子账号 |
| kms:Decrypt | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |  |  |
| kms::GenerateDataKey | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |   |  |
| kms::EnableKey | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |   |  |
| kms::DisableKey | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |   |  |
| kms::GetKeyAttributes | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |   |   |
| kms::SetKeyAttributes | qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>qcs::kms:$region:$account:key/creatorUin/$creatorUin/ (授权某个创建者的所有资源）<br>qcs::kms:$region:$account:key/ (授权某个根帐号的所有资源) |  <br>  |  <br>  |
 
