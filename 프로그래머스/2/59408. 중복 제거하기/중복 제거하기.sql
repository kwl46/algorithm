-- 코드를 입력하세요
SELECT Count(Name) as count from (select distinct NAME from ANIMAL_INS group by NAME) AS T