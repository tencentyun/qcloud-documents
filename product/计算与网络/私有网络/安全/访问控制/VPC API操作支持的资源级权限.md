在CAM中，可对私有网络资源进行以下API操作的授权， 具体API支持的资源和条件的对应关系如下：
**重要：**在表格中没有出现VPC API不支持资源级权限，但您可向用户授予使用不在该列表中的VPC API，但是必须为策略语句的资源元素指定： *。

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
  <td height=3D180 style=3D'height:135.0pt'>AcceptVp<span style=3D'display:=
none'>cPeeringConnection</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:region<br>
    vpc:requester_vpc</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId(接收方vpcId)</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'>AcceptVp<span style=3D'display:=
none'>cPeeringConnectionEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:accepter_vpc_region<br>
    vpc:requester_vpc<br>
    vpc:requester_vpc_region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:accepter_vpc_region表示接收方地域。<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:requester_vpc_region表示发起方地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>AddVpnCo<span style=3D'display:=
none'>nnEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn网关资源<br>
    qcs::vpc:$region:$account:vpngw/*<br>
    qcs::vpc:$region:$account:vpngw/$vpnGwId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D108 style=3D'height:81.0pt'>
  <td height=3D108 style=3D'height:81.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对端网关资源<br>
    qcs::vpc:$region:$account:cgw/*</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D198 style=3D'height:148.5pt'>
  <td height=3D198 style=3D'height:148.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn通道资源<br>
    qcs::vpc:$region:$account:vpnx/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:vpngw<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:vpngw表示开发商下的vpn网关<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>AssignPr<span style=3D'display:=
none'>ivateIpAddresses</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>Associat<span style=3D'display:=
none'>eVip</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>Associat<span style=3D'display:=
none'>eRouteTable</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网资源<br>
    qcs::vpc:$region:$account:subnet/*<br>
    qcs::vpc:$region:$account:subnet/$subnetId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>路由表资源<br>
    qcs::vpc:$region:$account:rtb/*<br>
    qcs::vpc:$region:$account:rtb/$routeTableId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>AttachCl<span style=3D'display:=
none'>assicLinkVpc</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>云主机资源<br>
    qcs::cvm:$region:$account:instance/*<br>
    qcs::cvm:$region:$account:instance/$instanceId</td>
  <td>cvm:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D4 style=3D'mso-ignore:colspan'>cvm:region表示云主机所在地域。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>AttachNe<span style=3D'display:=
none'>tworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>云主机资源<br>
    qcs::cvm:$region:$account:instance/*<br>
    qcs::cvm:$region:$account:instance/$instanceId</td>
  <td>cvm:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D4 style=3D'mso-ignore:colspan'>cvm:region表示云主机所在地域
。</td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateAn<span style=3D'display:=
none'>dAttachNetworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>云主机资源<br>
    qcs::cvm:$region:$account:instance/*<br>
    qcs::cvm:$region:$account:instance/$instanceId</td>
  <td>cvm:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D4 style=3D'mso-ignore:colspan'>cvm:region表示云主机所在地域
。</td>
 </tr>
 <tr height=3D198 style=3D'height:148.5pt'>
  <td height=3D198 style=3D'height:148.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateDi<span style=3D'display:=
none'>rectConnectGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D126 style=3D'height:94.5pt'>
  <td height=3D126 style=3D'height:94.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>CreateLo<span style=3D'display:=
none'>calDestinationIPPortTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>CreateLo<span style=3D'display:=
none'>calIPTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>CreateLo<span style=3D'display:=
none'>calIPTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>CreateLo<span style=3D'display:=
none'>calSourceIPPortTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>CreateLo<span style=3D'display:=
none'>calSourceIPPortTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>CreatePe<span style=3D'display:=
none'>erIPTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateNa<span style=3D'display:=
none'>tGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D126 style=3D'height:94.5pt'>
  <td height=3D126 style=3D'height:94.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>nat网关资源<br>
    qcs::vpc:$region:$account:nat/*<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateNe<span style=3D'display:=
none'>tworkAcl</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D126 style=3D'height:94.5pt'>
  <td height=3D126 style=3D'height:94.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>网络acl资源<br>
    qcs::vpc:$region:$account:acl/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateNe<span style=3D'display:=
none'>tworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网资源<br>
    qcs::vpc:$region:$account:subnet/*<br>
    qcs::vpc:$region:$account:subnet/$subnetId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:subnet表示开发商子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>CreateRo<span style=3D'display:=
none'>ute</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>路由表资源<br>
    qcs::vpc:$region:$account:rtb/*<br>
    qcs::vpc:$region:$account:rtb/$routeTableId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateRo<span style=3D'display:=
none'>uteTable</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D126 style=3D'height:94.5pt'>
  <td height=3D126 style=3D'height:94.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>路由表资源<br>
    qcs::vpc:$region:$account:rtb/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateSu<span style=3D'display:=
none'>bnet</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D126 style=3D'height:94.5pt'>
  <td height=3D126 style=3D'height:94.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网网关资源<br>
    qcs::vpc:$region:$account:subnet/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>CreateSu<span style=3D'display:=
none'>bnetAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>网络acl资源<br>
    qcs::vpc:$region:$account:acl/*<br>
    qcs::vpc:$region:$account:acl/$networkAclId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D126 style=3D'height:94.5pt'>
  <td height=3D126 style=3D'height:94.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网网关资源<br>
    qcs::vpc:$region:$account:subnet/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D198 style=3D'height:148.5pt'>
  <td height=3D198 style=3D'height:148.5pt'>CreateVp<span style=3D'display:=
none'>cPeeringConnection</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源(发起方)<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:requester_vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>CreateVp<span style=3D'display:=
none'>cPeeringConnectionEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:accepter_vpc_region<br>
    vpc:requester_vpc<br>
    vpc:requester_vpc_region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:accepter_vpc_region表示接收方地域。<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:requester_vpc_region表示发起方地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteDi<span style=3D'display:=
none'>rectConnectGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteLo<span style=3D'display:=
none'>calDestinationIPPortTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteLo<span style=3D'display:=
none'>calIPTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteLo<span style=3D'display:=
none'>calIPTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteLo<span style=3D'display:=
none'>calSourceIPPortTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeletePe<span style=3D'display:=
none'>erIPTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteLo<span style=3D'display:=
none'>calSourceIPPortTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>DeleteNa<span style=3D'display:=
none'>tGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>nat网关资源<br>
    qcs::vpc:$region:$account:nat/*<br>
    qcs::vpc:$region:$account:nat/$natId<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>DeleteNe<span style=3D'display:=
none'>tworkAcl</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>网络acl资源<br>
    qcs::vpc:$region:$account:acl/*<br>
    qcs::vpc:$region:$account:acl/$networkAclId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DeleteNe<span style=3D'display:=
none'>tworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>DeleteRo<span style=3D'display:=
none'>ute</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>路由表资源<br>
    qcs::vpc:$region:$account:rtb/*<br>
    qcs::vpc:$region:$account:rtb/$routeTableId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>DeleteRo<span style=3D'display:=
none'>uteTable</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>路由表资源<br>
    qcs::vpc:$region:$account:rtb/*<br>
    qcs::vpc:$region:$account:rtb/$routeTableId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>DeleteSu<span style=3D'display:=
none'>bnet</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网资源<br>
    qcs::vpc:$region:$account:subnet/*<br>
    qcs::vpc:$region:$account:subnet/$subnetId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D198 style=3D'height:148.5pt'>
  <td height=3D198 style=3D'height:148.5pt'>DeleteUs<span style=3D'display:=
none'>erGw</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对端网关资源<br>
    qcs::vpc:$region:$account:cgw/*<br>
    qcs::vpc:$region:$account:cgw/$userGwId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>DeleteVpc</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:region<br>
    vpc:vpc<br>
    </td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'>DeleteVp<span style=3D'display:=
none'>cPeeringConnection</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:region<br>
    vpc:requester_vpc<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'>DeleteVp<span style=3D'display:=
none'>cPeeringConnectionEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:accepter_vpc_region<br>
    vpc:requester_vpc<br>
    vpc:requester_vpc_region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:accepter_vpc_region表示接收方地域。<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:requester_vpc_region表示发起方地域。</td>
 
 </tr>
 <tr height=3D270 style=3D'height:202.5pt'>
  <td height=3D270 style=3D'height:202.5pt'>DeleteVp<span style=3D'display:=
none'>nConn</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn通道资源<br>
    qcs::vpc:$region:$account:vpnx/*<br>
    qcs::vpc:$region:$account:vpnx/$vpnConnId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:vpngw<br>
    vpc:usergw<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:vpngw表示开发商下的网关<br>
    vpc:usergw表示开发商下的对端网关<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>DetachCl<span style=3D'display:=
none'>assicLinkVpc</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
    <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:region<br>
    vpc:vpc<br>
    </td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>云主机资源<br>
    qcs::cvm:$region:$account:instance/*<br>
    qcs::cvm:$region:$account:instance/$instanceId</td>
  <td>cvm:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D4 style=3D'mso-ignore:colspan'>cvm:region表示云主机所在地域
。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>DetachNe<span style=3D'display:=
none'>tworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>云主机资源<br>
    qcs::cvm:$region:$account:instance/*<br>
    qcs::cvm:$region:$account:instance/$instanceId</td>
  <td>cvm:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D4 style=3D'mso-ignore:colspan'>cvm:region表示云主机所在地域
。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>DeteleSu<span style=3D'display:=
none'>bnetAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网资源<br>
    qcs::vpc:$region:$account:subnet/*<br>
    qcs::vpc:$region:$account:subnet/$subnetId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>网络acl资源<br>
    qcs::vpc:$region:$account:acl/*<br>
    qcs::vpc:$region:$account:acl/$networkAclId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>EipBindN<span style=3D'display:=
none'>atGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>nat网关资源<br>
    qcs::vpc:$region:$account:nat/*<br>
    qcs::vpc:$region:$account:nat/$natId<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>EipUnBin<span style=3D'display:=
none'>dNatGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>nat网关资源<br>
    qcs::vpc:$region:$account:nat/*<br>
    qcs::vpc:$region:$account:nat/$natId<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>EnableVp<span style=3D'display:=
none'>cPeeringConnection</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:region<br>
    vpc:requester_vpc<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>EnableVp<span style=3D'display:=
none'>cPeeringConnectionEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:accepter_vpc_region<br>
    vpc:requester_vpc<br>
    vpc:requester_vpc_region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:accepter_vpc_region表示接收方地域。<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:requester_vpc_region表示发起方地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>MigrateN<span style=3D'display:=
none'>etworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D288 style=3D'height:216.0pt'>
  <td height=3D288 style=3D'height:216.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>云主机资源<br>
    qcs::cvm:$region:$account:instance/*<br>
    qcs::cvm:$region:$account:instance/$instanceId(迁移前后的都需要授权)</t=
d>
  <td>cvm:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D4 style=3D'mso-ignore:colspan'>cvm:region表示云主机所在地域
。</td>
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>MigrateP<span style=3D'display:=
none'>rivateIpAddress</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyDi<span style=3D'display:=
none'>rectConnectGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyLo<span style=3D'display:=
none'>calDestinationIPPortTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyLo<span style=3D'display:=
none'>calIPTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyLo<span style=3D'display:=
none'>calIPTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyLo<span style=3D'display:=
none'>calSourceIPPortTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyPe<span style=3D'display:=
none'>erIPTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyLo<span style=3D'display:=
none'>calSourceIPPortTranslationNatRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>ModifyNa<span style=3D'display:=
none'>tGateway</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>nat网关资源<br>
    qcs::vpc:$region:$account:nat/*<br>
    qcs::vpc:$region:$account:nat/nat-dc7cdf<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>ModifyNe<span style=3D'display:=
none'>tworkAcl</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>网络acl资源<br>
    qcs::vpc:$region:$account:acl/*<br>
    qcs::vpc:$region:$account:acl/$networkAclId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>ModifyNe<span style=3D'display:=
none'>tworkAclEntry</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>网络acl资源<br>
    qcs::vpc:$region:$account:acl/*<br>
    qcs::vpc:$region:$account:acl/$networkAclId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyNe<span style=3D'display:=
none'>tworkInterface</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>ModifyPr<span style=3D'display:=
none'>ivateIpAddress</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>ModifyRo<span style=3D'display:=
none'>uteTableAttribute</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>路由表资源<br>
    qcs::vpc:$region:$account:rtb/*<br>
    qcs::vpc:$region:$account:rtb/$routeTableId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>ModifySu<span style=3D'display:=
none'>bnetAttribute</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>子网资源<br>
    qcs::vpc:$region:$account:subnet/*<br>
    qcs::vpc:$region:$account:subnet/$subnetId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D198 style=3D'height:148.5pt'>
  <td height=3D198 style=3D'height:148.5pt'>ModifyUs<span style=3D'display:=
none'>erGw</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对端网关资源<br>
    qcs::vpc:$region:$account:cgw/*<br>
    qcs::vpc:$region:$account:cgw/$userGwId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>ModifyVp<span style=3D'display:=
none'>cAttribute</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:Regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>ModifyVp<span style=3D'display:=
none'>cPeeringConnection</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:region<br>
    vpc:requester_vpc<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>ModifyVp<span style=3D'display:=
none'>cPeeringConnectionEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:accepter_vpc_region<br>
    vpc:requester_vpc<br>
    vpc:requester_vpc_region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:accepter_vpc_region表示接收方地域。<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:requester_vpc_region表示发起方地域。</td>
 
 </tr>
 <tr height=3D270 style=3D'height:202.5pt'>
  <td height=3D270 style=3D'height:202.5pt'>ModifyVp<span style=3D'display:=
none'>nConnEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn通道资源<br>
    qcs::vpc:$region:$account:vpnx/*<br>
    qcs::vpc:$region:$account:vpnx/$vpnConnId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:vpngw<br>
    vpc:usergw<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:vpngw表示开发商下的网关<br>
    vpc:usergw表示开发商下的对端网关<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>ModifyVp<span style=3D'display:=
none'>nGw</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn网关资源<br>
    qcs::vpc:$region:$account:vpngw/*<br>
    qcs::vpc:$region:$account:vpngw/$vpnGwId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>RejectVp<span style=3D'display:=
none'>cPeeringConnection</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D324 style=3D'height:243.0pt'>
  <td height=3D324 style=3D'height:243.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:region<br>
    vpc:requester_vpc<br>
    </td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D180 style=3D'height:135.0pt'>
  <td height=3D180 style=3D'height:135.0pt'>RejectVp<span style=3D'display:=
none'>cPeeringConnectionEx</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc资源<br>
    qcs::vpc:$region:$account:vpc/*<br>
    qcs::vpc:$region:$account:vpc/$vpcId</td>
  <td>vpc:regi<span style=3D'display:none'>on</span></td>
  <td colspan=3D3 style=3D'mso-ignore:colspan'>vpc:region表示vpc所在地域。</td>
 </tr>
 <tr height=3D432 style=3D'height:324.0pt'>
  <td height=3D432 style=3D'height:324.0pt'></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>对等连接资源<br>
    qcs::vpc:$region:$account:pcx/*<br>
    qcs::vpc:$region:$account:pcx/$peeringConnectionId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc<br>
    vpc:accepter_vpc_region<br>
    vpc:requester_vpc<br>
    vpc:requester_vpc_region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>
    vpc:accepter_vpc_region表示接收方地域。<br>
    vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>
    vpc:requester_vpc_region表示发起方地域。</td>
 
 </tr>
 <tr height=3D270 style=3D'height:202.5pt'>
  <td height=3D270 style=3D'height:202.5pt'>ResetVpn<span style=3D'display:=
none'>ConnSA</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn通道资源<br>
    qcs::vpc:$region:$account:vpnx/*<br>
    qcs::vpc:$region:$account:vpnx/$vpnConnId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:vpngw<br>
    vpc:usergw<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:vpngw表示开发商下的网关<br>
    vpc:usergw表示开发商下的对端网关<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>SetLocal<span style=3D'display:=
none'>IPTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>SetLocal<span style=3D'display:=
none'>SourceIPPortTranslationAclRule</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>专线网关资源<br>
    qcs::vpc:$region:$account:dcg/*<br>
    qcs::vpc:$region:$account:dcg/$directConnectGatewayId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D216 style=3D'height:162.0pt'>
  <td height=3D216 style=3D'height:162.0pt'>SetSSLVp<span style=3D'display:=
none'>nDomain</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpn网关资源<br>
    qcs::vpc:$region:$account:vpngw/*<br>
    qcs::vpc:$region:$account:vpngw/$vpnGwId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商VPC<br>
    vpc:region表示vpc所在地域。</td>
 
 </tr>
 <tr height=3D234 style=3D'height:175.5pt'>
  <td height=3D234 style=3D'height:175.5pt'>Unassign<span style=3D'display:=
none'>PrivateIpAddresses</span></td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>弹性网卡资源<br>
    qcs::vpc:$region:$account:eni/*<br>
    qcs::vpc:$region:$account:eni/$networkInterfaceId</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc<br>
    vpc:subnet<br>
    vpc:region</td>
  <td class=3Dxl65 width=3D72 style=3D'width:54pt'>vpc:vpc表示开发商的VPC<b=
r>
    vpc:subnet表示开发商下的子网<br>
    vpc:region表示vpc所在地域。</td>
 </tr>
</table>

| API 操作|	资源 |	条件	|备注|
|-------|-------|--------|-------|
|AcceptVpcPeeringConnection	| vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId	|vpc:region	|vpc:region表示vpc所在地域。|
|  | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | 	vpc:accepter_vpc<br>vpc:region<br>vpc:requester_vpc	| vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:region表示vpc所在地域。|
|  | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId(接收方vpcId) | vpc:region | 	vpc:region表示vpc所在地域。|
| AcceptVpcPeeringConnectionEx | 对等连接资源 <br>qcs::vpc:$region:$account:pcx/* <br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:accepter_vpc_region<br>vpc:requester_vpc<br>vpc:requester_vpc_region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:accepter_vpc_region表示接收方地域。<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:requester_vpc_region表示发起方地域。|
|  |  vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | 	vpc:region表示vpc所在地域。|
| AddVpnConnEx |  vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId |  vpc:region | 	vpc:region表示vpc所在地域。|
|  |  vpn网关资源<br>qcs::vpc:$region:$account:vpngw/*<br>qcs::vpc:$region:$account:vpngw/$vpnGwId | vpc:vpc <br>vpc:region | 	vpc:vpc表示开发商VPC <br> vpc:region表示vpc所在地域。|
|  |  对端网关资源<br>qcs::vpc:$region:$account:cgw/* | vpc:region | vpc:region表示vpc所在地域。|
|   | vpn通道资源<br>qcs::vpc:$region:$account:vpnx/* | vpc:vpc <br> vpc:vpngw <br> vpc:region | vpc:vpc表示开发商VPC <br> vpc:vpngw表示开发商下的vpn网关 <br> vpc:region表示vpc所在地域。|
| AssignPrivateIpAddresses | 	弹性网卡资源 <br> qcs::vpc:$region:$account:eni/* <br> qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc <br> vpc:subnet <br> vpc:region | vpc:vpc表示开发商的VPC <br> vpc:subnet表示开发商下的子网 <br> vpc:region表示vpc所在地域。|
| AssociateVip | vpc资源 <br> qcs::vpc:$region:$account:vpc/* <br> qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:vpc <br> vpc:region |
| AssociateRouteTable | 	子网资源 <br> qcs::vpc:$region:$account:subnet/* <br> qcs::vpc:$region:$account:subnet/$subnetId | vpc:vpc <br> vpc:region | 	vpc:vpc表示开发商VPC <br> vpc:region表示vpc所在地域。|
|  |  路由表资源 <br> qcs::vpc:$region:$account:rtb/* <br> qcs::vpc:$region:$account:rtb/$routeTableId | vpc:vpc <br> vpc:region |  vpc:vpc表示开发商VPC <br> vpc:region表示vpc所在地域。|
| AttachClassicLinkVpc | vpc资源 <br> qcs::vpc:$region:$account:vpc/* <br> qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 	云主机资源 <br> qcs::cvm:$region:$account:instance/* <br> qcs::cvm:$region:$account:instance/$instanceId | cvm:region | cvm:region表示云主机所在地域。|
| AttachNetworkInterface | 	弹性网卡资源 <br> qcs::vpc:$region:$account:eni/* <br> qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc <br> vpc:subnet <br> vpc:region | vpc:vpc表示开发商的VPC <br> vpc:subnet表示开发商下的子网 <br> vpc:region表示vpc所在地域。|
|  |  云主机资源 <br> qcs::cvm:$region:$account:instance/* <br> qcs::cvm:$region:$account:instance/$instanceId | cvm:region | cvm:region表示云主机所在地域 。|
| CreateAndAttachNetworkInterface | vpc资源 <br> qcs::vpc:$region:$account:vpc/* <br> qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | 	vpc:region表示vpc所在地域。|
|  | 云主机资源<br>qcs::cvm:$region:$account:instance/* <br> qcs::cvm:$region:$account:instance/$instanceId | cvm:region | 	cvm:region表示云主机所在地域 。|
|  | 弹性网卡资源 <br> qcs::vpc:$region:$account:eni/* | vpc:vpc<br> vpc:subnet <br>vpc:region| vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
| CreateDirectConnectGateway | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br> qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | 	vpc:region表示vpc所在地域。|
|  | 	专线网关资源<br>qcs::vpc:$region:$account:dcg/* | 	vpc:vpc<br> vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateLocalDestinationIPPortTranslationNatRule | 	专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br> vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateLocalIPTranslationAclRule | 	专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br> vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateLocalIPTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateLocalSourceIPPortTranslationAclRule | 	专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateLocalSourceIPPortTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreatePeerIPTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br> vpc:region表示vpc所在地域。|
| CreateNatGateway | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | nat网关资源<br>qcs::vpc:$region:$account:nat/* | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateNetworkAcl | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | 	vpc:region表示vpc所在地域。 |
|  | 	网络acl资源<br>qcs::vpc:$region:$account:acl/* | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。| 
| CreateNetworkInterface | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 子网资源<br>qcs::vpc:$region:$account:subnet/*<br>qcs::vpc:$region:$account:subnet/$subnetId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
|  | 弹性网卡资源<br>qcs::vpc:$region:$account:eni/* | vpc:vpc<br>vpc:subnet<br>vpc:region |
| CreateRoute | 	路由表资源<br>qcs::vpc:$region:$account:rtb/*<br>qcs::vpc:$region:$account:rtb/$routeTableId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateRouteTable | 	vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 路由表资源<br>qcs::vpc:$region:$account:rtb/* | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateSubnet | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 子网网关资源<br>qcs::vpc:$region:$account:subnet/* | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateSubnetAclRule | 网络acl资源<br>qcs::vpc:$region:$account:acl/*<br>qcs::vpc:$region:$account:acl/$networkAclId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
|  | 子网网关资源<br>qcs::vpc:$region:$account:subnet/* | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| CreateVpcPeeringConnection | vpc资源(发起方)<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。| 
|  | 对等连接资源<br>qcs::vpc:$region:$account:pcx/* | vpc:accepter_vpc<br>vpc:requester_vpc<br>vpc:region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:region表示vpc所在地域。|
| CreateVpcPeeringConnectionEx | 	vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|   | 	对等连接资源<br>qcs::vpc:$region:$account:pcx/* | vpc:accepter_vpc<br>vpc:accepter_vpc_region<br>vpc:requester_vpc<br>vpc:requester_vpc_region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:accepter_vpc_region表示接收方地域。<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:requester_vpc_region表示发起方地域。|
| DeleteDirectConnectGateway | 专线网关资源<br>qcs::vpc:$region:$account:dcg/* <br>qcs::vpc$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteLocalDestinationIPPortTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteLocalIPTranslationAclRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteLocalIPTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteLocalSourceIPPortTranslationAclRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc$region:$account:dcg/$directConnectGatewayId |  vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeletePeerIPTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteLocalSourceIPPortTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteNatGateway | nat网关资源<br>qcs::vpc:$region:$account:nat/*<br>qcs::vpc:$region:$account:nat/$natId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteNetworkAcl | 网络acl资源<br>qcs::vpc:$region:$account:acl/*<br>qcs::vpc:$region:$account:acl/$networkAclId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| DeleteNetworkInterface | 	弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
| DeleteRoute | 	路由表资源<br>qcs::vpc:$region:$account:rtb/*<br>qcs::vpc:$region:$account:rtb/$routeTableId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域 | 
| DeleteRouteTable | 路由表资源<br>qcs::vpc:$region:$account:rtb/*<br>qcs::vpc:$region:$account:rtb/$routeTableId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域 | 
| DeleteSubnet | 子网资源<br>qcs::vpc:$region:$account:subnet/*<br>qcs::vpc:$region:$account:subnet/$subnetId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域 | 
| DeleteUserGw | 对端网关资源<br>qcs::vpc:$region:$account:cgw/*<br>cs::vpc:$region:$account:cgw/$userGwId | vpc:region | 	vpc:region表示vpc所在地域。|
| DeleteVpc | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region<br>vpc:vpc | vpc:region表示vpc所在地域。|
| DeleteVpcPeeringConnection | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:region<br>vpc:requester_vpc | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:region表示vpc所在地域。|
| DeleteVpcPeeringConnectionEx | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:accepter_vpc_region<br>vpc:requester_vpc<br>vpc:requester_vpc_region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:accepter_vpc_region表示接收方地域。<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:requester_vpc_region表示发起方地域。|
| DeleteVpnConn | vpn通道资源<br>qcs::vpc:$region:$account:vpnx/*<br>qcs::vpc:$region:$account:vpnx/$vpnConnId | vpc:vpc<br>vpc:vpngw<br>vpc:usergw<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:vpngw表示开发商下的网关<br>vpc:usergw表示开发商下的对端网关<br>vpc:region表示vpc所在地域。|
| DetachClassicLinkVpc | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region<br>vpc:vpc | vpc:region表示vpc所在地域。|
|  | 云主机资源<br>qcs::cvm:$region:$account:instance/*<br>qcs::cvm:$region:$account:instance/$instanceId | cvm:region | 	cvm:region表示云主机所在地域 。|
| DetachNetworkInterface | 云主机资源<br>qcs::cvm:$region:$account:instance/*<br>qcs::cvm:$region:$account:instance/$instanceId | cvm:region | 	cvm:region表示云主机所在地域 。|
|  | 弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
| DeteleSubnetAclRule | 子网资源<br>qcs::vpc:$region:$account:subnet/*<br>qcs::vpc:$region:$account:subnet/$subnetId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
|  | 网络acl资源<br>qcs::vpc:$region:$account:acl/*<br>qcs::vpc:$region:$account:acl/$networkAclId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| EipBindNatGateway | nat网关资源<br>qcs::vpc:$region:$account:nat/*<br>qcs::vpc:$region:$account:nat/$natId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| EipUnBindNatGateway | nat网关资源<br>qcs::vpc:$region:$account:nat/*<br>qcs::vpc:$region:$account:nat/$natId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| EnableVpcPeeringConnection | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:region<br>vpc:requester_vpc | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:region表示vpc所在地域。|
| EnableVpcPeeringConnectionEx | 	vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|   | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:accepter_vpc_region<br>vpc:requester_vpc<br>vpc:requester_vpc_region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:accepter_vpc_region表示接收方地域。<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:requester_vpc_region表示发起方地域。|
| MigrateNetworkInterface | 弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
|   | 云主机资源<br>qcs::cvm:$region:$account:instance/*<br>qcs::cvm:$region:$account:instance/$instanceId(迁移前后的都需要授权) | cvm:region | cvm:region表示云主机所在地域 。|
| MigratePrivateIpAddress | 弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
| ModifyDirectConnectGateway | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyLocalDestinationIPPortTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyLocalIPTranslationAclRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyLocalIPTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyLocalSourceIPPortTranslationAclRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyPeerIPTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyLocalSourceIPPortTranslationNatRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyNatGateway | nat网关资源<br>qcs::vpc:$region:$account:nat/*<br>qcs::vpc:$region:$account:nat/nat-dc7cdf | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyNetworkAcl | 网络acl资源<br>qcs::vpc:$region:$account:acl/*<br>qcs::vpc:$region:$account:acl/$networkAclId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。| 
| ModifyNetworkAclEntry | 网络acl资源<br>qcs::vpc:$region:$account:acl/*<br>qcs::vpc:$region:$account:acl/$networkAclId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyNetworkInterface | 弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
| ModifyPrivateIpAddress |弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|
| ModifyRouteTableAttribute |  路由表资源<br>qcs::vpc:$region:$account:rtb/*<br>qcs::vpc:$region:$account:rtb/$routeTableId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifySubnetAttribute | 子网资源<br>qcs::vpc:$region:$account:subnet/*<br>qcs::vpc:$region:$account:subnet/$subnetId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| ModifyUserGw | 对端网关资源<br>qcs::vpc:$region:$account:cgw/*<br>qcs::vpc:$region:$account:cgw/$userGwId | vpc:region | vpc:region表示vpc所在地域。|
| ModifyVpcAttribute | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
| ModifyVpcPeeringConnection |  vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|   | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:region<br>vpc:requester_vpc | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:region表示vpc所在地域。|
| ModifyVpcPeeringConnectionEx | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:accepter_vpc_region<br>vpc:requester_vpc<br>vpc:requester_vpc_region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:accepter_vpc_region表示接收方地域。<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:requester_vpc_region表示发起方地域。|
| ModifyVpnConnEx | vpn通道资源<br>qcs::vpc:$region:$account:vpnx/*<br>qcs::vpc:$region:$account:vpnx/$vpnConnId | vpc:vpc<br>vpc:vpngw<br>vpc:usergw<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:vpngw表示开发商下的网关<br>vpc:usergw表示开发商下的对端网关<br>vpc:region表示vpc所在地域。| 
| ModifyVpnGw | vpn网关资源<br>qcs::vpc:$region:$account:vpngw/*<br>qcs::vpc:$region:$account:vpngw/$vpnGwId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| RejectVpcPeeringConnection | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId | vpc:region | vpc:region表示vpc所在地域。|
|  | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:region<br>vpc:requester_vpc | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:region表示vpc所在地域。| 
| RejectVpcPeeringConnectionEx | vpc资源<br>qcs::vpc:$region:$account:vpc/*<br>qcs::vpc:$region:$account:vpc/$vpcId |  vpc:region | vpc:region表示vpc所在地域。|
|  | 对等连接资源<br>qcs::vpc:$region:$account:pcx/*<br>qcs::vpc:$region:$account:pcx/$peeringConnectionId | vpc:accepter_vpc<br>vpc:accepter_vpc_region<br>vpc:requester_vpc<br>vpc:requester_vpc_region | vpc:accepter_vpc接收方VPC，取值为接收方VPC；<br>vpc:accepter_vpc_region表示接收方地域。<br>vpc:requester_vpc表示发起方VPC，取值为发起方VPC；<br>vpc:requester_vpc_region表示发起方地域。|
| ResetVpnConnSA | vpn通道资源<br>qcs::vpc:$region:$account:vpnx/*<br>qcs::vpc:$region:$account:vpnx/$vpnConnId | vpc:vpc<br>vpc:vpngw<br>vpc:usergw<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:vpngw表示开发商下的网关<br>vpc:usergw表示开发商下的对端网关<br>vpc:region表示vpc所在地域。|
| SetLocalIPTranslationAclRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。 |
| SetLocalSourceIPPortTranslationAclRule | 专线网关资源<br>qcs::vpc:$region:$account:dcg/*<br>qcs::vpc:$region:$account:dcg/$directConnectGatewayId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| SetSSLVpnDomain | vpn网关资源
qcs::vpc:$region:$account:vpngw/*
qcs::vpc:$region:$account:vpngw/$vpnGwId | vpc:vpc<br>vpc:region | vpc:vpc表示开发商VPC<br>vpc:region表示vpc所在地域。|
| UnassignPrivateIpAddresses | 弹性网卡资源<br>qcs::vpc:$region:$account:eni/*<br>qcs::vpc:$region:$account:eni/$networkInterfaceId | vpc:vpc<br>vpc:subnet<br>vpc:region | vpc:vpc表示开发商的VPC<br> vpc:subnet表示开发商下的子网<br>vpc:region表示vpc所在地域。|















