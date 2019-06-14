/* https://www.hackerrank.com/challenges/average-population-of-each-continent */

select a.continent,floor(avg(b.population)) from country a, city b where a.code=b.countrycode group by a.continent;
