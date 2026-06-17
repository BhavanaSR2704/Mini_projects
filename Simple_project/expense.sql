CREATE TABLE expenses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
category TEXT,
expense_name TEXT,
amount INTEGER,
date DATE
);

INSERT INTO expenses
(category,expense_name,amount,date)

VALUES
('Food','Burger',150,'2026-05-26');

SELECT * FROM expenses;

SELECT SUM(amount)
AS MonthlyExpense
FROM expenses;