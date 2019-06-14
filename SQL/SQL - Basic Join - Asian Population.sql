/* https://www.hackerrank.com/challenges/asian-population */

select sum(population) from city where countrycode in (select code from country where continent='Asia');
