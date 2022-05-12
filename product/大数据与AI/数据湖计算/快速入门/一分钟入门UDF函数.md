## UDF 说明
用户可通过编写 UDF 函数，打包为 JAR 文件后，在数据湖计算定义为函数在查询分析中使用。目前数据湖计算 DLC 的 UDF 为 HIVE 格式，继承 org.apache.hadoop.hive.ql.exec.UDF，实现 evaluate 方法。
示例：简单数组 UDF 函数
```
public class MyDiff extends UDF {   
    public ArrayList<Integer> evaluate(ArrayList<Integer> input) {
        ArrayList<Integer> result = new ArrayList<Integer>();     
        result.add(0, 0);        
        for (int i = 1; i < input.size(); i++) {              
        result.add(i, input.get(i) - input.get(i - 1));        
        }      
        return result;    
    }
}
```
pom 文件参考
```
<dependencies>          
    <dependency>        
        <groupId>org.slf4j</groupId>        
			<artifactId>slf4j-log4j12</artifactId>       
			<version>1.7.16</version>        
			<scope>test</scope>    
        </dependency>    
        <dependency>        
            <groupId>org.apache.hive</groupId>        
            <artifactId>hive-exec</artifactId>        
            <version>1.2.1</version>    
        </dependency>
</dependencies>
```
## 创建函数
若您了解 SQL 语法，可通过**数据探索**执行 [CREATE FUNCTION](https://cloud.tencent.com/document/product/1342/61808) 语法完成函数创建，或通过可视化界面创建，流程如下：
>? 数据湖计算 DLC 的数据管理页目前处于邀测阶段，如需免费体验可 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行申请。

1. 登录 [数据湖计算控制台](https://console.cloud.tencent.com/dlc) ，选择服务地域。
2. 通过左侧导航菜单进入**数据管理**，选择需要创建的函数的数据库，如果需要创建新的数据库，可参见 [数据库管理](https://cloud.tencent.com/document/product/1342/71246)。
3. 单击**函数**进入函数管理页面。
4. 单击**创建函数**进行创建。
![](https://qcloudimg.tencent-cloud.cn/raw/5446396913571924e3990c819225c511.png)
UDF 的程序包支持本地上传或选择 COS 路径（需具备 COS 相关权限），示例为选择 cos 路径创建。
函数类名包含“包信息”及“函数的执行类名”。

## 函数使用
1. 登录 [数据湖计算控制台](https://console.cloud.tencent.com/dlc)，选择服务地域。
2. 通过左侧导航菜单进入数据探索，选择计算引擎后即可使用 SQL 调用函数。
![](https://qcloudimg.tencent-cloud.cn/raw/ca767b6999bd74df6d0b165c113c38f4.png)









