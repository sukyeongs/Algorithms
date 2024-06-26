-- 각 아이스크림 성분 타입과 성분 타입에 대한 아이스크림 총 주문량
-- 총주문량이 작은 순서대로
-- 총주문량: TOTAL_ORDER
SELECT I.INGREDIENT_TYPE, SUM(F.TOTAL_ORDER) AS TOTAL_ORDER
FROM ICECREAM_INFO I
JOIN FIRST_HALF F ON (I.FLAVOR = F.FLAVOR)
GROUP BY I.INGREDIENT_TYPE
ORDER BY F.TOTAL_ORDER