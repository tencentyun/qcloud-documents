Users can write SCF to handle timer tasks. Timer can automatically trigger the SCF at a specified time. Timer trigger has the following features:

- Pull model: Timer directly calls Invoke API of relevant function at a specified time to trigger the function. The event source mapping relation is stored in SCF.
- Asynchronous call: Timer always uses asynchronous call type to call the function, and the result is not returned to the caller. For more information about the call type, please see [Call Type](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## Attribute of Timer Trigger

- Timer name (required): It contains a maximum of 60 characters. `a-z`, `A-Z`, `0-9`, `-` and `_` are supported. It must begin with a letter. Multiple timer triggers with the same name are not supported for one function.
- Triggering period (required): A specified time at which the function is triggered. You can determine when to trigger the function using the default value in the console or selecting the custom standard CRON expression. For more information about the CRON expression, please see below.

## CRON Expression
When creating a timer trigger, you can use standard CRON expression to customize the time to trigger function.

## CRON Expression Syntax
CRON expression contains six required fields separated by spaces.

| First | Second | Third | Fourth | Fifth | Sixth |
|--|--|--|--|--|--|
| Minute | Hour | Day | Month | Week | Year |

Each field corresponds to a value range:

| Field | Value | Wildcard |
|--|--|--|
| Minute |	0-59	| , - * / |
| Hour |	0-23	| , - * / |
| Day |	1-31 | , - * ? / |
| Month |	1-12 or JAN-DEC |	, - * / |
| Week | 1-7 or SUN-SAT	| , - * ? / |
| Year | 1970-2199 | , - * / |

The wildcard has the following meaning:

| Wildcard | Meaning |
|--|--|
| , (comma) | A set of characters separated by commas. For example, in "Hour" field, "1, 2, 3" refers to 1, 2 and 3 am/pm |
| - (dash) | Include all values within a specified range. For example, in "Day" field, "1-15" contains 1st to 15th day of a specified month |
| * (asterisk ) | All values. In "Hour" field, * refers to each hour |
| / (slash) | Specified increment. In "Minute" field, entering 1/10 means to repeat every 10 minutes from the first minute. For example, the 11th minute, 21st minute, 31st minute, and so on |
| ? (question mark) | Ignore the corresponding field. For example, if you enter 7 in "Day" field and want to execute command on 7th no matter what day of the week it is, you can enter ? in "Week" field |

### Note

- The Cron expression faster than 5 minutes is not supported
- "Day" and "Week" fields are not allowed to be specified with values at the same time in Cron expression. If you specify a value in one field, you must use ? in another field.

### Example
The following examples show some Cron expressions and their meanings:

- `15	23	*	*	?	*`	Run at 23:15 every night
- `0	18	?	*	MON-FRI	*`	Run at 6:00 pm on each work day
- `0	8	1	*	?	*`	Run at 8:00 am on the 1st day of each month
- `0/15	*	*	*	?	*`	Run every 15 minutes
