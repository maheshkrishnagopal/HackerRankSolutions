/* https://www.hackerrank.com/challenges/weather-observation-station-11 */

select distinct city from station where substr(lower(city),0,1) not in ('a','e','i','o','u') or substr(lower(city),-1,1) not in ('a','e','i','o','u');
