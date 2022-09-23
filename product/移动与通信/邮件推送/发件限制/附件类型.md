通过腾讯云 SES 发送带附件的消息，附件格式需按照表中**支持**类型进行发送。以下为腾讯云 SES 附件类型支持与限制列表：
>!有些 ISP 有其他限制，因此，我们建议您在生产环境发送电子邮件之前，先测试发送主要的 ISP，查看附件是否顺利送达。

<table>
<thead>
<tr>
<th>支持</th>
<td style="word-break: break-all"><code>.xlsx</code>、<code>.xls</code>、<code>.ods</code>、<code>.docx</code>、<code>.docm</code>、<code>.doc</code>、<code>.csv</code>、<code>.pdf</code>、<code>.txt</code>、<code>.gif</code>、<code>.jpg</code>、<code>.jpeg</code>、<code>.png</code>、<code>.tif</code>、<code>.tiff</code>、<code>.rtf</code>、<code>.bmp</code>、<code>.cgm</code>、<code>.css</code>、<code>.shtml</code>、<code>.html</code>、<code>.htm</code>、<code>.zip</code>、<code>.xml</code>、<code>.ppt</code>、<code>.pptx</code>、<code>.tar</code>、<code>.ez</code>、<code>.ics</code>、<code>.mobi</code>、<code>.msg</code>、<code>.pub</code>、<code>.eps</code>、<code>.odt</code>、<code>.mp3</code>、<code>.m4a
</code></td></tr>
</thead>
<tbody><tr>
<th>不支持</th>
<td style="word-break: break-all"><code>.m4v</code>、<code>.wma</code>、<code>.ogg</code>、<code>.flac</code>、<code>.wav</code>、<code>.aif</code>、<code>.aifc</code>、<code>.aiff</code>、<code>.mp4</code>、<code>.mov</code>、<code>.avi</code>、<code>.mkv</code>、<code>.mpeg</code>、<code>.mpg</code>、<code>.wmv</code>、<code>.ade</code>、<code>.adp</code>、<code>.app</code>、<code>.asp</code>、<code>.bas</code>、<code>.bat</code>、<code>.cer</code>、<code>.chm</code>、<code>.cmd</code>、<code>.com</code>、<code>.cpl</code>、<code>.crt</code>、<code>.csh</code>、<code>.der</code>、<code>.exe</code>、<code>.fxp</code>、<code>.gadget</code>、<code>.hlp</code>、<code>.hta</code>、<code>.inf</code>、<code>.ins</code>、<code>.isp</code>、<code>.its</code>、<code>.js</code>、<code>.jse</code>、<code>.ksh</code>、<code>.lib</code>、<code>.lnk</code>、<code>.mad</code>、<code>.maf</code>、<code>.mag</code>、<code>.mam</code>、<code>.maq</code>、<code>.mar</code>、<code>.mas</code>、<code>.mat</code>、<code>.mau</code>、<code>.mav</code>、<code>.maw</code>、<code>.mda</code>、<code>.mdb</code>、<code>.mde</code>、<code>.mdt</code>、<code>.mdw</code>、<code>.mdz</code>、<code>.msc</code>、<code>.msh</code>、<code>.msh1</code>、<code>.msh2</code>、<code>.mshxml</code>、<code>.msh1xml</code>、<code>.msh2xml</code>、<code>.msi</code>、<code>.msp</code></td>
</tr>
</tbody></table>

>?附件命名不能包含以下特殊字符： ? \ * | " < > : / 空格。

