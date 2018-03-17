/*
题目描述
查找各个部门当前(to_date='9999-01-01')领导当前薪水详情以及其对应部门编号dept_no

CREATE TABLE `dept_manager` (
`dept_no` char(4) NOT NULL,
`emp_no` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));

CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));

输出描述：
emp_no

salary

from_date

to_date

dept_no

from 语法错误
*/

select * from salaries,dept_no from dept_manager where salaries.emp_no==dept_manager.emp_no order by dept_no;



