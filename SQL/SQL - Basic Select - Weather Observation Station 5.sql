/* https://www.hackerrank.com/challenges/weather-observation-station-5 */

select 
  city, length(city) city_length 
from 
  (select 
      city, length(city) city_length 
   from 
      station
   order by 
      city_length, city
  ) 
where 
  rownum = 1 
union 
select 
  city, length(city) city_length 
from 
  (select 
      city, length(city) city_length 
   from 
      sation 
   order by 
      city_length desc, city) 
where 
  rownum = 1;
