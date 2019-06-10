/* https://www.hackerrank.com/challenges/weather-observation-station-7 */

select distinct city from station where substr(city,-1,1) in ('a','e','i','o','u');
