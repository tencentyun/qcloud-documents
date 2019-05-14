## 互动直播的费用类型
A.基础网络费用
•	付费周期：
（1）按月计费，每个月1-5号月结时，从腾讯云费用账户扣除上个月实际使用费用，并按照上个月费用的120%进行费用冻结；
（2）下个月结算时会对冻结的费用先解冻，再进行扣除。
B.附加能力费用(可选)
•	旁路直播使用的是云直播的能力，如果客户使用了旁路直播的能力，其费用将按照旁路直播所小号的的月OC峰值带宽来计算，OC峰值带宽的价格详见以下的说明

## 基础网络费用
###  计算公式
 ![](//mccdn.qcloud.com/static/img/e045f054cc19ceb13344f2c8c0b7fc03/image.jpg)
 
友情提示：如果您有较大的业务量或单独接入服务需求，可通过腾讯云客户经理进一步协商定制相关价格

### 定价
<div class="mod-price">
    
    <div class="tab-content-detail column-4">
       
        </div>
        <div class="slide-text"></div>
        <div class="text-content">
        </div>
        <div class="slide-text"> </div>
        <div class="price-content">
            <table>
                <colgroup>
                    <col class="col1">
                    <col class="col2">
                    <col class="col3">
                    <col class="col4">
                    <col class="col5">
                </colgroup>
                <thead>
                    <tr>
                        <th colspan="2">核心机房带宽</th>
                        <th colspan="2">边缘节点带宽</th>
                        <th rowspan="2">费用(元)</th>
                    </tr>
                    <tr>
                        <th>月带宽峰值</th>
                        <th>单价(元/Mbps/月)</th>
                        <th>月带宽峰值</th>
                        <th>单价(元/Mbps/月)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td rowspan="6">
                            <span>X</span>
                        </td>
                        <td rowspan="6">
                            <span>120</span>
                        </td>
                        <td>
                            <span>Y ＜ 5Gbps</span>
                        </td>
                        <td>
                            <span>23</span>
                        </td>
                        <td>
                            <span>X * 120 + Y * 23</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>5 ≤ Y ＜ 50Gbps</span>
                        </td>
                        <td>
                            <span>21.5</span>
                        </td>
                        <td>
                            <span>X * 120 + Y * 21.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>50 ≤ Y ＜ 100Gbps</span>
                        </td>
                        <td>
                            <span>20.5</span>
                        </td>
                        <td>
                            <span>X * 120 + Y * 20.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>100 ≤ Y ＜ 300Gbps</span>
                        </td>
                        <td>
                            <span>19.5</span>
                        </td>
                        <td>
                            <span>X * 120 + Y * 19.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>300 ≤ Y ＜ 500Gbps</span>
                        </td>
                        <td>
                            <span>18.5</span>
                        </td>
                        <td>
                            <span>X * 120 + Y * 18.5</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <span>500Gbps ≤ Y</span>
                        </td>
                        <td>
                            <span>17.5</span>
                        </td>
                        <td>
                            <span>X * 120 + Y * 17.5</span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

### 每月基础网络费用计算公式

<iframe src="https://avc.qcloud.com/calculator/index.html" width=400px height=400px border=0 style=border:none></iframe>

## 注解：
### 月带宽峰值：
•	核心机房(DC)和边缘机房(OC)每5分钟统计一个带宽峰值（单位Mbps），取当月最高点作为核心机房月带宽峰值，作为结算标准；
### 核心机房（DC）
•	可以上下行音视频数据，适用于多人音视频互动
#### 需要大比率用到DC的情况：
(1)当观众端有上行音视频权限时 (【注意】观众端是否上麦是由开发者进行设定切换的，设定错误会导致大量流量走DC，请务必认真阅读具体设定方法：[点击此处查看](https://cloud.tencent.com/doc/product/268/3227))
(2)如果没有上行音视频流量，当房间人数较少(比如小于等于5人)由于流程是主播--->DC--->OC--->观众，使用OC会导致 DC-->OC 流量浪费，所以也直接用DC流量下行)

### 边缘节点(OC)
•	只能下行音视频数据，适用于纯观看，如观众等角色。
(如图所示，没有观众端上行视频、房间在线人数>5人， 大部分都会是OC流量，但也有一定带宽比率是DC-->OC的带宽，这部分将近是10%)）

### 流量图解
#### 无上麦，且房间人数大于5人的图解
![](//mccdn.qcloud.com/static/img/1cb95629a1101c5381ce64194b478fbd/image.png)

#### 无上麦，且房间人数小于等于5人的图解
当房间人数较少，使用OC会导致 DC-->OC 流量浪费，所以直接通过DC下行
 ![](//mccdn.qcloud.com/static/img/3dd9c91f847457a5d456256d895f56d4/image.jpg)
 
####  有观众上麦的图解
 ![](//mccdn.qcloud.com/static/img/1e463c571da0514f6c01e3aa3b6f9bf5/image.jpg)