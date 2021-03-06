/*
查找所有员工入职时候的薪水情况，给出emp_no以及salary， 并按照emp_no进行逆序
CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` char(1) NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`));


CREATE TABLE `salaries` (
`emp_no` int(11) NOT NULL,
`salary` int(11) NOT NULL,
`from_date` date NOT NULL,
`to_date` date NOT NULL,
PRIMARY KEY (`emp_no`,`from_date`));

emp_no			salary

10011				25828

10001				60117


据说存在涨薪的形式，造成salaries.emp_no不唯一，故需要加上日期的判断
*/

select employees.emp_no,salaries.salary from employees, salaries
where employees.emp_no=salaries.emp_no and employees.hire_date=salaries.from_date
order by employees.emp_no desc;