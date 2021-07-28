
DBMS_UTILITY 包含一个接口： FORMAT_CALL_STACK，这个内置函数返回一个格式化的字符串，它显示了执行调用堆栈，直至此函数的调用点处的所有过程或者函数的调用顺序。

示例：
```
create or replace function dbms_uti_func() returns text as
declare
v_str1 text;
v_str2 text;
v_str3 text;
v_str4 text;
begin
   v_str1 := dbms_utility.format_call_stack();
   select regexp_replace(v_str1,'[ 0-9a-fA-F]{4}[0-9a-fA-F]{4}','   0','g') into v_str1;
   select regexp_replace(v_str1,'[45()]','','g') into v_str1;
   v_str2 := dbms_utility.format_call_stack('o');
   select regexp_replace(v_str2,'[ 0-9a-fA-F]{4}[0-9a-fA-F]{4}','   0','g') into v_str2;
   select regexp_replace(v_str2,'[45()]','','g') into v_str2;
   v_str3 := dbms_utility.format_call_stack('p');
   select regexp_replace(v_str3,'[ 0-9a-fA-F]{4}[0-9a-fA-F]{4}','   0','g') into v_str3;
   select regexp_replace(v_str3,'[45()]','','g') into v_str3;
   v_str4 := dbms_utility.format_call_stack('s');
   select regexp_replace(v_str4,'[ 0-9a-fA-F]{4}[0-9a-fA-F]{4}','   0','g') into v_str4;
   select regexp_replace(v_str4,'[45()]','','g') into v_str4;
   return 'v_str1:
'||v_str1 || '
v_str2:
'|| v_str2|| '
v_str3:
'|| v_str3|| '
v_str4:
'|| v_str4;
end;
/
select dbms_uti_func();
```
   
