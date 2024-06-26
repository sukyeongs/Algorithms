-- 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일 / 전화번호 null이면 출력대상에서 제외, 회원ID 오름차순
SELECT MEMBER_ID,
    MEMBER_NAME,
    GENDER,
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE GENDER LIKE 'W' AND
    TLNO IS NOT NULL AND
    DATE_OF_BIRTH LIKE '%-03%'
ORDER BY MEMBER_ID ASC
;