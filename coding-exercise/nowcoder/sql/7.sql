/*

题目描述
查找薪水涨幅超过15次的员工号emp_no以及其对应的涨幅次数t
CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));

输出
emp_no				t
10001					17
10004					16
10009					18

注意：结果变量存储为别名t的使用

select s.emp_no , count(emp_no) as t from salaries s group by s.emp_no having t>15;

由于WHERE后不可跟COUNT()函数，故用HAVING语句来限定t>15的条件
用COUNT()函数和GROUP BY语句可以统计同一emp_no值的记录条数
*/

select salaries.emp_no,count(salaries.emp_no) as rel
from salaries group by salaries.emp_no having rel>15;
