/*
查找所有员工的last_name和first_name以及对应部门编号dept_no，也包括展示没有分配具体部门的员工
CREATE TABLE `dept_emp` (
`emp_no` int(11) NOT NULL,
`dept_no` char(4) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`dept_no`));


CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));


输出描述

last_name		first_name		dept_no
Facello			Georgi				d001

select e.last_name,e.first_name, d.dept_no 
from employees as e left join dept_emp d on e.emp_no=d.emp_no;


join的时候注意from后表的名称，不要多加了

INNER JOIN 两边表同时有对应的数据，即任何一边缺失数据就不显示。 
LEFT JOIN 会读取左边数据表的全部数据，即便右边表无对应数据。 
RIGHT JOIN 会读取右边数据表的全部数据，即便左边表无对应数据。
*/

select employees.last_name,employees.first_name,dept_emp.dept_no
from employees
left join dept_emp on employees.emp_no=dept_emp.emp_no;


select employees.last_name,employees.first_name,dept_emp.dept_no
from dept_emp
right join employees on employees.emp_no=dept_emp.emp_no;