

DynomaDB supports three expression syntax: ConditionExpression, UpdateExpression, and ProjectExpression. Tencent Cloud databases provide compatibility with them as follows:
### ConditionExpression
```
DynamoDBConditionExpressionThe syntax is as follows:
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
Notes:
1. For operand1 comparator operand2 syntax, operand1 must be an attribute field, while operand2 must be a value field. 
2. For operand1 BETWEEN operand2 AND operand3 syntax, operand1 must be an attribute field, while operand2 and operand3 must be value fields. 
3. For operand1 IN ( operand2 (',' operand3 (, ...) )) syntax, operand1 must be an attribute field, while operand2 and operand3 must be value fields.
4. For function syntax, attribute_exists (path), attribute_not_exists (path), begins_with (path, substr), and contains (path, operand) are fully compatible. attribute_type (path, type) supports type-> S, N, B, BOOL, NULL, but type-> SS, NS, BS, L, M. size (path) is not supported.


### UpdateExpression
```
update-expressionThe syntax is as follows:
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
Notes:
[set-action]
1. For SET key = value, key must be an attribute field, while value must be a value field. 
```
SET a =:b    //Supported
SET #a = #b  //Not Supported
```
2. For SET key1 = key2 + value, key1 and key2 must be attribute fields and have the same name, while value must be a value field. 
```
SET a = a + :b //Supported
SET a = b + :b //Not Supported
```
3. For SET key1[NUM] = value, key1 must be an attribute field, while value must be a value field, and num must be a non-negative integer.
4. SET key1[NUM] = key2[NUM] + value, not supported
5. SET key1[NUM] = key2[NUM] - value, not supported
6. SET key1 = if_not_exists(key2, value), not supported
7. For SET key1 = list_append (value, key2), key1 and key2 must be of value type and have the same name, while value must be of attribute type.
8. For SET key1 = list_append (key2, value), key1 and key2 must be of value type and have the same name, while value must be of attribute type.

[remove-action]
1. For REMOVE key, key must be an attribute field, fully compatible
2. REMOVE key[NUM]; not supported

[delete-action]
1. For DELETE key value, key must be of attribute type, while value must be of value type, fully compatible

[add-action]
1. For ADD key value, key must be of attribute type, while value must be of value type, fully compatible 

### ProjectExpression
```
Projec-expressionThe syntax is as follows:
stat ::= sections
sections ::= section, sections
section ::= key|  key[num]
```
Description: All the above syntax is supported except for the two-dimensional array section ::= key[num][num]

