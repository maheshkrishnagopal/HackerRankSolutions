# https://www.hackerrank.com/challenges/the-report

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/

select 
  case when grade<8 then 'NULL' else s.name end,g.grade,s.marks 
from 
  students s,grades g 
where 
  s.marks between g.min_mark and g.max_mark 
order by 
  grade desc,s.name;
