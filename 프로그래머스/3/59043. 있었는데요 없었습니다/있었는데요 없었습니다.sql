-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디, 이름 (보호 시작일이 빠른 순으로 조회)
SELECT I.ANIMAL_ID, I.NAME
FROM ANIMAL_INS I
INNER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.DATETIME > O.DATETIME
ORDER BY I.DATETIME ASC
;