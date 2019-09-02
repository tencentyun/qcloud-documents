You can write an SCF to process timed tasks. Timer can automatically trigger the SCF at a specified time. Timer trigger has the following features:

- **Pull model**: Timer directly calls the Invoke API of a function at a specified time to trigger the function. The event source mapping relation is stored in SCF.
- **Asynchronous call**: Timer always calls the function asynchronously, and does not return the result to the caller. For more information about call types, please see [Call Types](https://cloud.tencent.com/document/product/583/9694#.E8.B0.83.E7.94.A8.E7.B1.BB.E5.9E.8B).

## Attribute of Timer Trigger

- (Required) Timer name: Its length should be limited to 60 characters. `a-z`, `A-Z`, `0-9`, `-` and `_` are supported. It must begin with a letter. Multiple timer triggers with the same name are not supported for a function.
- (Required) Triggering cycle: A specified time at which the function is triggered. You can use the default value on the console, or choose a custom standard CRON expression to determine when to trigger the function. For more information on the CRON expression, please see below.

## CRON Expression
When creating a timer trigger, you can use a standard CRON expression to customize the time to trigger function.

## CRON Expression Syntax
CRON expression contains five required fields separated by spaces.

| First | Second | Third | Fourth | Fifth |
|--|--|--|--|--|
| Minute | Hour | Day | Month | Week |

Each field corresponds to a value range:

| Field | Value | Wildcard |
|--|--|--|
| Minute | 	0-59	| , - * / |
| Hour | 	0-23	| , - * / |
| Day | 1-31 |  , - * / |
| Month | 1-12 or JAN-DEC | 	, - * /|
| Week | 1-7 or MON-SUN |  , - * / |


The wildcard has the following meaning:

| Wildcard | Meaning |
|--|--|
| , (comma) | A set of characters separated by commas. For example, in the "Hour" field, "1, 2, 3" refers to 1, 2 and 3 am/pm |
| - (dash) | Includes all values within a specified range. For example, in the "Day" field, "1-15" contains the 1st to 15th days of a specified month |
| * (asterisk) | All values. In the "Hour" field, * refers to each hour |
| / (slash) | Specified increment. In the "Minute" field, entering 1/10 means to repeat every 10 minutes from the first minute. For example, the 11th minute, 21st minute, 31st minute, and so on |


### Note

- When "Day" and "Week" fields are specified at the same time in a CRON expression, the relation between them is "OR", and the function is triggered when either of them is met.

### Example
The following examples show some CRON expressions and their meanings:

- `15 23 * * *`	Run at 23:15 every night
- `0 18 * * MON-FRI`	Run at 6:00 pm on each work day
- `0 8 1 * *`	Run at 8:00 am on the 1st day of each month
- `0/15 * * * *`	Run every 15 minutes

## Input Parameters of Timer Trigger

No input parameter is specified when a timer trigger triggers a function, which means the event is empty. This allows you to determine whether the trigger source is a timer trigger.

