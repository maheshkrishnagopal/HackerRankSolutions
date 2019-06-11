/* 

select 
  case 
    when (A+B)>C 
  then 
    case 
      when (A=B and B=C) 
    then 'Equilateral' 
  when (A=B or B=C or C=A) 
    then 'Isosceles' 
  when (A!=B and B!=C and C!=A) 
    then 'Scalene' 
  end 
  else 
  'Not A Triangle' 
  end 
  Triangle 
from 
  triangles;
