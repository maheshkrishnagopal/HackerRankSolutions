/* https://www.hackerrank.com/challenges/the-blunder */

select ceil(avg(salary)-avg(replace(salary,'0',''))) from employees;
