/* https://www.hackerrank.com/challenges/more-than-75-marks */

select name from students where marks>75 order by substr(name,-3,3),id asc;
