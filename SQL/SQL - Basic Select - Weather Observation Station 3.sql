/* https://www.hackerrank.com/challenges/weather-observation-station-3 */

select 
  distinct(city) 
from 
  station 
where 
  mod(id,2)=0;
