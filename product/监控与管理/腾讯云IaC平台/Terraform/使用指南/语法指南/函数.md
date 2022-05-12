
## 数值函数
<table>
<thead>
<tr>
<th width="25%">函数名称</th>
<th width="30%">功能</th>
<th width="30%">示例</th>
<th width="15%">结果</th>
</tr>
</thead>
<tbody><tr>
<td>abs</td>
<td>取绝对值</td>
<td>abs(-1024)</td>
<td>1024</td>
</tr>
<tr>
<td>ceil</td>
<td>向上取整</td>
<td>ceil(5.1)</td>
<td>6</td>
</tr>
<tr>
<td>floor</td>
<td>向下取整</td>
<td>floor(4.9)</td>
<td>4</td>
</tr>
<tr>
<td>log</td>
<td>计算对数</td>
<td>log(16, 2)</td>
<td>4</td>
</tr>
<tr>
<td>pow</td>
<td>计算指数幂</td>
<td>pow(3,2)</td>
<td>9</td>
</tr>
<tr>
<td>max</td>
<td>取最大值</td>
<td>max(12,54,3)</td>
<td>54</td>
</tr>
<tr>
<td>min</td>
<td>取最小值</td>
<td>min(12, 54, 3)</td>
<td>3</td>
</tr>
</tbody></table>

## 字符串函数
<table>
<thead>
<tr>
<th width="25%">函数名称</th>
<th width="30%">功能</th>
<th width="30%">示例</th>
<th width="15%">结果</th>
</tr>
</thead>
<tbody><tr>
<td>chomp</td>
<td>删除字符串末尾换行符</td>
<td>chomp("hello\n")</td>
<td>"hello"</td>
</tr>
<tr>
<td>format</td>
<td>格式化字符串</td>
<td>format("Hello, %s!", "Ander")</td>
<td>"Hello, Ander!"</td>
</tr>
<tr>
<td>lower</td>
<td>字符串转小写</td>
<td>lower("HELLO")</td>
<td>"hello"</td>
</tr>
<tr>
<td>upper</td>
<td>字符串转大写</td>
<td>upper("hello")</td>
<td>"HELLO"</td>
</tr>
<tr>
<td>join</td>
<td>将字符串列表使用指定分隔符拼接</td>
<td>join(", ", ["foo", "bar", "baz"])</td>
<td>"foo, bar, baz"</td>
</tr>
<tr>
<td>replace</td>
<td>替换字符串中的指定字符</td>
<td>replace("1 + 2 + 3", "+", "-")</td>
<td>"1 - 2 - 3"</td>
</tr>
</tbody></table>

更多函数信息请参见 [Terraform 官网](https://www.terraform.io/language/functions)。
