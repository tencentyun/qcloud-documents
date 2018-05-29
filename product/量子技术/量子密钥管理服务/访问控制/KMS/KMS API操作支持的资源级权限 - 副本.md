在 CAM 中，可对主密钥资源进行以下 API 操作的授权， 具体 API 支持的资源和条件的对应关系如下：

<table border=3D0 cellpadding=3D0 cellspacing=3D0 width=3D504 style=3D'bord=
er-collapse:
 collapse;table-layout:fixed;width:378pt'>
 <col width=3D72 span=3D7 style=3D'width:54pt'>
 <tr height=3D18 style=3D'height:13.5pt'>
  <td height=3D18 width=3D72 style=3D'height:13.5pt;width:54pt'>API 操作</t=
d>
  <td width=3D72 style=3D'width:54pt'>资源</td>
  <td width=3D72 style=3D'width:54pt'>条件</td>
  <td width=3D72 style=3D'width:54pt'>备注</td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>kms:CreateKey
</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/*
</td>
  <td></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'></td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'>kms:ListKey
</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
    qcs::kms:$region:$account:key/*
  </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>kms:Encrypt
</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>creatorUin 表示资源创建者的 uin，资源创建者可为根帐号或子账号。</td>
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'>kms:Decrypt</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>kms::GenerateDataKey</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'></td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>kms::EnableKey</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'></td>
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>kms::DisableKey</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
 
 </tr>
 <tr height=3D108 style=3D'height:81.0pt'>
  <td height=3D108 style=3D'height:81.0pt'>kms::GetKeyAttributes</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'></td>
 </tr>
 <tr height=3D198 style=3D'height:148.5pt'>
  <td height=3D198 style=3D'height:148.5pt'>kms::SetKeyAttributes</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>	
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/$keyid (授权单个资源）<br>
	qcs::kms:$region:$account:key/creatorUin/$creatorUin/* (授权某个创建者的所有资源）<br>
	qcs::kms:$region:$account:key/* (授权某个根帐号的所有资源)
</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'></td>
 </tr>
</table>
