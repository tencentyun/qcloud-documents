

DynomaDB支持三种表达式语法ConditionExpression，UpdateExpression，ProjectExpression，腾讯云数据库对其兼容情况如下
### ConditionExpression
```
DynamoDBConditionExpression语法如下：
condition-expression ::=
    | operand comparator operand
    | operand BETWEEN operand AND operand
    | operand IN ( operand (',' operand (, ...) ))
    | function 
    | condition AND condition 
    | condition OR condition
    | NOT condition 
    | ( condition )

comparator ::=
    | = 
    | <>
    | <
    | <= 
    | >
    | >=

function ::=
    | attribute_exists (path) 
    | attribute_not_exists (path) 
    | attribute_type (path, type) 
    | begins_with (path, substr) 
    | contains (path, operand)
    | size (path)

```
说明：
1.operand1 comparator operand2语法中，operand1必须是属性字段，operand2必须是值字段 
2.operand1 BETWEEN operand2 AND operand3语法中，operand1必须是属性字段， operand2和operand3必须是值字段 
3.operand1 IN ( operand2 (',' operand3 (, ...) ))语法中，operand1 必须是属性字段，operand2和operand3必须是值字段
4.function语法中，attribute_exists (path)，attribute_not_exists (path)，begins_with (path, substr)，contains (path, operand)完全兼容。attribute_type (path, type)对type->S,N, B, BOOL,NULL支持 ，但type->SS, NS, BS, L,M 不支持。size (path)不支持


### UpdateExpression
```
update-expression语法如下：
update-expression ::=
    | SET set-action , ... 
    | REMOVE remove-action , ...  
    | ADD add-action , ... 
    | DELETE delete-action , ...

set-action ::=
path = value

value ::=
    | operand
    | operand '+' operand 
    | operand '-' operand

operand ::=
path | function

remove-action ::=
path

add-action ::=
path value

delete-action ::=
path value 

function ::=
if_not_exists (path, operand) | list_append (operand, operand)
```
说明：
[set-action]
1.SET key = value，key必须是属性字段 ，value必须是值字段 
```
SET a =:b    //支持
SET #a = #b  //不支持
```
2.SET key1 = key2 + value,key1 与key2 必须是属性字段，且key1 与key2 必须同名 ，value必须是值字段 
```
SET a = a + :b //支持
SET a = b + :b //不支持
```
3.SET key1[NUM] = value,key1必须是属性字段  ，value必须是值字段  ，num必须是非负整数
4.SET key1[NUM] = key2[NUM] + value ，不支持
5.SET key1[NUM] = key2[NUM] - value ，不支持
6.SET key1 = if_not_exists(key2, value) ，不支持
7.SET key1 = list_append(value, key2)，key1与key2 必须是值类型且key1 与key2 同名 ，value必须是属性类型
8.SET key1 = list_append(key2, value)，key1与key2 必须是值类型且key1 与key2 同名 ，value必须是属性类型

[remove-action]
1.REMOVE key，key必须是属性字段，完全兼容
2.REMOVE key[NUM]，不支持

[delete-action]
1.DELETE key value，key必须是属性类型，value必须是值类型，完全兼容

[add-action]
1.ADD key value，key必须是属性类型，value必须是值类型 

### ProjectExpression
```
Projec-expression语法如下：
stat ::= sections
sections ::= section, sections
section ::= key|  key[num]
```
说明：以上语法都支持，除二维数组section ::= key[num][num]不支持
