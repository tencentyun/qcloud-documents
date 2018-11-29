

TiDB optimizer will select the optimal execution plan according to the actual situation of the current data table. The execution plan is composed of a series of operators.

**Optimize SQL Statement Using EXPLAIN**

EXPLAIN can be used with SELECT, DELETE, INSERT, REPLACE, and UPDATE statements, and the returned results provide detailed information on how TiDB executes SQL queries:


> Tips: Executing EXPLAIN, TiDB returns the final physical execution plan processed by optimizer via the EXPLAIN SQL statement. That is to say, EXPLAIN shows the complete information that TiDB executes the SQL statement, such as in what order, how to JOIN two tables, what the expression tree looks like, and so on. By looking at the results of EXPLAIN, you can know how to add index to data tables to allow execution plans to use it and speed up the execution of SQL statements. You can also use EXPLAIN to check whether the optimizer chooses the optimal order to JOIN data tables.

EXPLAIN output format

At present, EXPLAIN of TiDB can output six columns including id, parents, children, task, operator info and count. Each operator in the execution plan is described by these six attributes. Each row in the EXPLAIN result describes an operator. The description of each attribute is explained in detail below:

| Attribute Name | Description |
|------|------|
| id | operator id, used to uniquely identifies an operator throughout the execution plan |
| parents | parent of the operator. The current execution plan can be seen as a tree structure composed of one operator. The data flows from the child to parent and each operator has only one parent |
| children | children of the operator, that is, the data source of the operator |
| task | what kind of task this operator currently belongs to. The current execution plan is divided into two kinds of tasks, one is root task, executed on tidb-server and the other is cop task, executed on tikv in parallel. The topological relationship of the current execution plan at the task level is one root task can be followed by many cop tasks, root task using output result of cop task as input. What executed in cop task are tasks pushed to tikv by tidb. Each cop task distributed in the tikv cluster are executed by multiple processes |
| operator info | details on each operator |
| count	| count of data to be output by the current operator, estimated based on statistics and operator's execution logic |
 
