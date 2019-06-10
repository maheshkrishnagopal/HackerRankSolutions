/* https://www.hackerrank.com/challenges/weather-observation-station-6 */

select distinct city from station where substr(upper(city),0,1) in ('A','E','I','O','U');
