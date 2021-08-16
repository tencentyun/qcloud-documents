
DBMS_JOB 主要用来对 JOB QUEUE 中的 JOB 做管理。该包已经被 DBMS_SCHEDULER 包所取代。如果您正在管理 JOB 以控制系统负载，建议通过收回用户在该包上的执行权限，以禁止 DBMS_JOB 包。

示例：
```
declare
jobno number;
begin dbms_job.submit(
job=>jobno, 
what=>'proc_job(2);',
next_date=>sysdate,
interval=>'sysdate+1/1440'); 
COMMIT;
dbms_output.put_line(jobno);
end;
/
```
