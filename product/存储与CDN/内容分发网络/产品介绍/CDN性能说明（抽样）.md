## 测试说明


### 测试工具

主机（单核1G），腾讯云 CDN。

### 测试方法

采用业内通用的基调测速方法，服务提供商为听云。

### 测试参数

| 测试时间   | 2019-05-21 07:45 ~ 2019-05-21 19:15           |
| ---------- | --------------------------------------------- |
| 测试城市   | 全部                                          |
| 测试运营商 | 中国联通, 中国电信, 中国移动                  |
| 源站链接   | http://*/simptab-wallpaper-20190520181120.png |
| CDN 链接   | http://*/simptab-wallpaper-20190520181120.png |

## 结果分析

### 时延性能曲线

单位：秒

![时延性图](https://main.qcloudimg.com/raw/523e221c3a7bbf5853d5ed3e17ff3689.png)

### 可用性曲线

单位：%

![可用性图new](https://main.qcloudimg.com/raw/f3b7b6f9483045e9fd0797f1d2c90632.png)

### 图表分析

<table>
   <tr>
      <td rowspan="2">监测任务</td>
      <td rowspan="2">监测点数</td>
      <td colspan="5">性能(秒)</td>
      <td colspan="5">可用性(%)</td>
   </tr>
   <tr>
      <td colspan="1">均值</td>
      <td colspan="2">最好</td>
      <td colspan="2">最差</td>
      <td colspan="1">均值</td>
      <td colspan="2">最好</td>
      <td colspan="2">最差</td>
   </tr>
   <tr>
      <td>CDN</td>
      <td>2235</td>
      <td>  0.196</td>
      <td>05月21日 07:45</td>
      <td>  0.117</td>
      <td>05月21日 12:15</td>
      <td>  0.313</td>
      <td> 99.996</td>
      <td>05月21日 07:45</td>
      <td>100.00</td>
      <td>05月21日 08:45</td>
      <td> 99.91</td>
   </tr>
   <tr>
      <td>源站</td>
      <td>2177</td>
      <td>  0.933</td>
      <td>05月21日 10:45</td>
      <td>  0.635</td>
      <td>05月21日 08:15</td>
      <td>  1.827</td>
      <td> 99.035</td>
      <td>05月21日 07:45</td>
      <td>100.00</td>
      <td>05月21日 11:15</td>
      <td> 97.65</td>
   </tr>
</table>

### 数据明细

<table>
   <tr>
      <td rowspan="2">时间</td>
      <td colspan="3">CDN</td>
      <td colspan="3">源站</td>
   </tr>
   <tr>
      <td>性能(秒)</td>
      <td>可用性(%)</td>
      <td>监测点数</td>
      <td>性能(秒)</td>
      <td>可用性(%)</td>
      <td>监测点数</td>
   </tr>
   <tr>
      <td>05月21日 07:45</td>
      <td>  0.117</td>
      <td>100.00</td>
      <td> 98</td>
      <td>  0.945</td>
      <td>100.00</td>
      <td> 98</td>
   </tr>
   <tr>
      <td>05月21日 08:15</td>
      <td>  0.160</td>
      <td>100.00</td>
      <td> 91</td>
      <td>  1.827</td>
      <td> 98.86</td>
      <td> 88</td>
   </tr>
   <tr>
      <td>05月21日 08:45</td>
      <td>  0.135</td>
      <td> 99.91</td>
      <td> 92</td>
      <td>  0.645</td>
      <td>100.00</td>
      <td> 88</td>
   </tr>
   <tr>
      <td>05月21日 09:15</td>
      <td>  0.240</td>
      <td>100.00</td>
      <td> 97</td>
      <td>  0.821</td>
      <td> 98.95</td>
      <td> 95</td>
   </tr>
   <tr>
      <td>05月21日 09:45</td>
      <td>  0.190</td>
      <td>100.00</td>
      <td> 95</td>
      <td>  1.315</td>
      <td> 98.80</td>
      <td> 83</td>
   </tr>
   <tr>
      <td>05月21日 10:15</td>
      <td>  0.158</td>
      <td>100.00</td>
      <td> 95</td>
      <td>  0.745</td>
      <td> 98.95</td>
      <td> 95</td>
   </tr>
   <tr>
      <td>05月21日 10:45</td>
      <td>  0.170</td>
      <td>100.00</td>
      <td> 90</td>
      <td>  0.635</td>
      <td>100.00</td>
      <td> 89</td>
   </tr>
   <tr>
      <td>05月21日 11:15</td>
      <td>  0.123</td>
      <td>100.00</td>
      <td> 90</td>
      <td>  0.692</td>
      <td> 97.65</td>
      <td> 85</td>
   </tr>
   <tr>
      <td>05月21日 11:45</td>
      <td>  0.246</td>
      <td>100.00</td>
      <td> 96</td>
      <td>  0.653</td>
      <td>100.00</td>
      <td> 98</td>
   </tr>
   <tr>
      <td>05月21日 12:15</td>
      <td>  0.313</td>
      <td>100.00</td>
      <td> 89</td>
      <td>  0.763</td>
      <td> 97.83</td>
      <td> 92</td>
   </tr>
   <tr>
      <td>05月21日 12:45</td>
      <td>  0.258</td>
      <td>100.00</td>
      <td> 92</td>
      <td>  1.181</td>
      <td>100.00</td>
      <td> 93</td>
   </tr>
   <tr>
      <td>05月21日 13:15</td>
      <td>  0.175</td>
      <td>100.00</td>
      <td> 95</td>
      <td>  1.122</td>
      <td> 97.67</td>
      <td> 86</td>
   </tr>
   <tr>
      <td>05月21日 13:45</td>
      <td>  0.173</td>
      <td>100.00</td>
      <td> 97</td>
      <td>  1.148</td>
      <td> 98.89</td>
      <td> 90</td>
   </tr>
   <tr>
      <td>05月21日 14:15</td>
      <td>  0.257</td>
      <td>100.00</td>
      <td> 81</td>
      <td>  1.083</td>
      <td>100.00</td>
      <td> 81</td>
   </tr>
   <tr>
      <td>05月21日 14:45</td>
      <td>  0.214</td>
      <td>100.00</td>
      <td>103</td>
      <td>  1.044</td>
      <td>100.00</td>
      <td> 97</td>
   </tr>
   <tr>
      <td>05月21日 15:15</td>
      <td>  0.240</td>
      <td>100.00</td>
      <td> 92</td>
      <td>  0.737</td>
      <td> 97.98</td>
      <td> 99</td>
   </tr>
   <tr>
      <td>05月21日 15:45</td>
      <td>  0.169</td>
      <td>100.00</td>
      <td> 94</td>
      <td>  0.969</td>
      <td> 98.85</td>
      <td> 87</td>
   </tr>
   <tr>
      <td>05月21日 16:15</td>
      <td>  0.146</td>
      <td>100.00</td>
      <td> 93</td>
      <td>  0.769</td>
      <td> 98.86</td>
      <td> 88</td>
   </tr>
   <tr>
      <td>05月21日 16:45</td>
      <td>  0.269</td>
      <td>100.00</td>
      <td> 91</td>
      <td>  0.724</td>
      <td>100.00</td>
      <td> 86</td>
   </tr>
   <tr>
      <td>05月21日 17:15</td>
      <td>  0.181</td>
      <td>100.00</td>
      <td> 91</td>
      <td>  1.072</td>
      <td> 98.02</td>
      <td>101</td>
   </tr>
   <tr>
      <td>05月21日 17:45</td>
      <td>  0.208</td>
      <td>100.00</td>
      <td> 96</td>
      <td>  1.000</td>
      <td>100.00</td>
      <td> 90</td>
   </tr>
   <tr>
      <td>05月21日 18:15</td>
      <td>  0.219</td>
      <td>100.00</td>
      <td> 94</td>
      <td>  0.744</td>
      <td> 98.86</td>
      <td> 88</td>
   </tr>
   <tr>
      <td>05月21日 18:45</td>
      <td>  0.119</td>
      <td>100.00</td>
      <td> 81</td>
      <td>  0.841</td>
      <td> 98.84</td>
      <td> 86</td>
   </tr>
   <tr>
      <td>05月21日 19:15</td>
      <td>  0.212</td>
      <td>100.00</td>
      <td>102</td>
      <td>  0.981</td>
      <td> 97.87</td>
      <td> 94</td>
   </tr>
   <tr>
      <td>平均 / 汇总</td>
      <td>  0.196</td>
      <td> 99.996</td>
      <td>2235</td>
      <td>  0.933</td>
      <td> 99.04</td>
      <td>2177</td>
   </tr>
   <tr>
      <td>排除点数</td>
      <td colspan="3">  0</td>
      <td colspan="3">  0</td>
   </tr>
</table>
