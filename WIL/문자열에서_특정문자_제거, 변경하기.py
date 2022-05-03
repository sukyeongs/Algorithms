# 문자열에서 특정문자 제거, 변경하기 - replace()
str1 = "google"
str1 = str1.replace("oo", "")  # str1 = "ggle"

str2 = "naver"
str2 = str2.replace("a", "A")  # str2 = "nAver"


# 문자열에서 양 끝의 문자 제거 - strip(), lstrip(): 왼쪽 제거, rstrip(): 오른쪽 제거
str3 = "hihellohi"
str3 = str3.strip("hi")   # str3 = "hello"

str4 = "  hi  "
str4 = str4.strip()  # 괄호 안의 값 지정X => 공백 제거 => str4 = "hi"

str5 = "...hello,,,"
str5 = str5.strip("."",")  # 여러개 문자 지정 가능
