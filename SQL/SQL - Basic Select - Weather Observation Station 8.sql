/* https://www.hackerrank.com/challenges/weather-observation-station-8 */

select distinct city from station where substr(lower(city),0,1) in ('a','e','o','i','u') and substr(city,-1,1) in ('a','e','o','i','u');
