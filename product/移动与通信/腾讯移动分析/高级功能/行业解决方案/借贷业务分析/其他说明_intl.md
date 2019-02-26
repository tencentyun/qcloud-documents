### Key Loan Metric Concepts
**New/Old User**
Whether a user has borrowed money successfully is the criterion to judge new/old user. If a user has borrowed money successfully, he/she will be regarded as an old user when applying for another loan.

**Number of orders**
When a loan is made, an order will be generated for this loan. The orders are counted based on the ID (order number).

**Number of bills**
Generally, each installment generates a bill ID (bill number), and the bills are counted based on the bill IDs. Repayments are made based on bills (for non-installment loan, only one bill is uploaded).

**Final repayment date**
It refers to the final repayment date specified on the bill. It is a fixed date (such as the 15th of each month) and generated in the first loan of a user, and is bound to the user's account. If the user does not make repayment after the final repayment date, it will be deemed as an overdue repayment.

**Number of overdue days**
If the current date - the final repayment date > 90 days, the loan will be regarded as the bad debt. Only overdue repayments within 180 days is taken.

**Overdue amount**
It refers to the total remaining amount of the borrower who has not repaid since the overdue date indicated by the overdue bill.
