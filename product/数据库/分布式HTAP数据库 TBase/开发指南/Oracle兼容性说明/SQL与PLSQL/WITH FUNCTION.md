在子查询的 `WITH` 子句中定义函数，并在普通 SQL 语句中使用。

## 语法
```
WITH
  FUNCTION <NAME_FUNCTION>
  BEGIN
    ...
  END;
SELECT <NAME_FUNCTION>
FROM <TABLE>;
/
```
    
## 示例
```
create table tw(t1 int, t2 int);
insert into tw values(3, 4);
insert into tw values(1, 2);
    
WITH FUNCTION raise_test_wf(int) returns int as $$
begin
raise notice 'This message has too many parameters %', $1;
return $1 + 1;
end;
$$ language plpgsql;
FUNCTION raise_test_wf2(int) returns int as $$
begin
raise notice 'This message has too many parameters %', $1;
return $1 + 1000;
end;
$$ language plpgsql;
select raise_test_wf2(t2), raise_test_wf(t1) from tw where raise_test_wf(t2) > 0 order by 1;
/
```
