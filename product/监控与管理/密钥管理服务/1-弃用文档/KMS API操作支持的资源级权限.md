在 CAM 中，可对主密钥资源进行以下 API 操作的授权， 具体 API 支持的资源和条件的对应关系如下：

<table>
   <tr>
      <th>API 操作</th>
      <th>资源</th>
      <th>备注</th>
   </tr>
   <tr>
      <td>kms:CreateKey</td>
      <td>qcs::kms:$region:$account:key/*</td>
      <td rowspan="23">creatorUin 表示资源创建者的 uin，资源创建者可为根帐号或子账号。</td>
   </tr>
   <tr>
      <td>kms:ListKey</td>
      <td>qcs::kms:$region:$account:key/*</td>
   </tr>
   <tr>
      <td>kms:ListKeys</td>
      <td>qcs::kms:$region:$account:key/*</td>
   </tr>
   <tr>
      <td>kms:ListKeyDetail</td>
      <td>qcs::kms:$region:$account:key/*</td>
   </tr>
   <tr>
      <td>kms:GetServiceStatus</td>
      <td>qcs::kms:$region:$account:key/*</td>
   </tr>
   <tr>
      <td>kms:Encrypt</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:Decrypt</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms::GenerateDataKey</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms::EnableKey</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms::DisableKey</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms::GetKeyAttributes</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms::SetKeyAttributes</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:GetKeyRotationStatus</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:ReEncrypt</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:DescribeKey</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:UpdateKeyDescription</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:UpdateAlias</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:DisableKeyRotation</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:EnableKeyRotation</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:EnableKeys</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:DisableKeys</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/*（授权某个创建者的所有资源） qcs::kms:$region:$account:key/*（授权某个根帐号的所有资源）</td>
   </tr>
   <tr>
      <td>kms:DescribeKeys</td>
      <td>qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid（授权单个资源） qcs::kms:$region:$account:key/creatorUin/$creatorUin/* （授权某个创建者的所有资源） qcs::kms:$region:$account:key/* （授权某个根帐号的所有资源）</td>
   </tr>
</table>
