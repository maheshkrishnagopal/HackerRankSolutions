/* https://www.hackerrank.com/challenges/weather-observation-station-16 */

SELECT min(round(lat_n,4)) FROM station WHERE lat_n > 38.7780;
