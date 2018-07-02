## Example of CMQ Trigger

Assume that CMQ trigger is configured for SCF. 3 messages are sent to CMQ per second. A memory of 128 MB is configured for SCF. It takes 760 ms (calculated by 800 ms) for SCF to process messages and put in to a message queue per run.

Resource usage per day = (128/1024) x (800/1000) x 3 x 3600 x 24 = 25920 GBs

Number of calls per day = 3 x 3600 x 24 = 259200

Fees per month (calculated by 30 days):

Resource usage fee per month = (25920 x 30 - 400000) x 0.000115 = 43.42 CNY

Fee of number of calls per month = (259200 x 30/1000000 - 1) x 1.38 = 9.35 CNY

In this case, the total cost = 43.42 CNY (resource usage fee) + 9.35 CNY (fee of number of calls) = 52.77 CNY

## Example of File Upload

Assume that a user uses a cloud API to call SCF. The number of calls is 50 per minute. A memory of 256 MB is configured for SCF. It takes 3680 ms (calculated by 3700 ms) for SCF to generate a 5 KB file and upload it to a user-built external site.

Resource usage per day = (256/1024) x (3700/1000) x 50 x 60 x 24 = 66600 GBs

Number of calls per day = 50 x 60 x 24 = 72000

Traffic per day = 5 x 50 x 60 x 24 = 360000 KB = 351.5625 MB

Fees per month (calculated by 30 days):

Resource usage fee per month = (66600 x 30 - 400000) x 0.000115 = 183.77 CNY

Fee of number of calls per month = (72000 x 30/1000000 - 1) x 1.38 = 2.98 CNY

Fee of public network outbound traffic = (351.5625 x 30/1024) x 0.8 = 8.24 CNY

In this case, the total cost = 183.77 CNY (resource usage fee) + 2.98 CNY (fee of number of calls) + 8.24 CNY (fee of public network outbound traffic) = 194.99 CNY

