## 简介
EXIF（Exchangeable Image File）是“可交换图像文件”的缩写，可记录数码照片的拍摄参数、缩略图及其他属性信息。
## 接口形式
download_url?imageInfo
## 参数说明 
<table width="1336" border="0" cellpadding="0" cellspacing="0" style='width:1002.00pt;border-collapse:collapse;table-layout:fixed;'>
   <col width="325" style='mso-width-source:userset;mso-width-alt:10400;'/>
   <col width="1011" style='mso-width-source:userset;mso-width-alt:32352;'/>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td class="xl65" height="40" width="325" style='height:30.00pt;width:243.75pt;' x:str>参数</td>
    <td class="xl65" width="1011" style='width:758.25pt;' x:str>含义</td>
   </tr>
   <tr height="40" style='height:30.00pt;mso-height-source:userset;mso-height-alt:600;'>
    <td height="40" style='height:30.00pt;' x:str>|download_url?</td>
    <td x:str>文档的访问链接，具体构成为 &lt;bucket id&gt;-&lt;appid&gt;.&lt;picture region&gt;.&lt;domain&gt;.com/&lt;picture name&gt;<span style='mso-spacerun:yes;'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>
   </tr>
   <![if supportMisalignedColumns]>
    <tr width="0" style='display:none;'>
     <td width="325" style='width:244;'></td>
     <td width="1011" style='width:758;'></td>
    </tr>
   <![endif]>
  </table>

## 示例
```
http://examples-1251000004.picsh.myqcloud.com/sample.jpeg?exif
```
