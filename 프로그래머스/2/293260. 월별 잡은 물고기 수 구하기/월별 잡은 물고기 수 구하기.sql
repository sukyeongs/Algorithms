-- 월별 잡은 물고기 수, 월
-- 잡은 물고기 수: FISH_COUNT, 월: MONTH
-- 월 기준 오름차순, 잡은 물고기 없는 월 출력 X
SELECT COUNT(ID) AS FISH_COUNT, MONTH(TIME) AS MONTH
FROM FISH_INFO
GROUP BY MONTH
ORDER BY MONTH