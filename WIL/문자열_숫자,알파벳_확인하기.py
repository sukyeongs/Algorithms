# 문자열의 문자들이 모두 대문자인지 확인하기 - isupper()
str1 = 'BDQERacV'
st1_upper = str1.isupper()  # str1_upper == False


# 문자열의 문자들이 모두 소문자인지 확인하기 - islower()
str2 = 'asbvbsd'
str2_lower = str2.islower()  # str2_lower == True


# 문자(열)이 알파벳인지 또는 숫자인지 확인하기 - isalnum()
str3 = 'AB3'
str3_alnum = str3.isalnum()  # str3_alnum == True

str4 = 'BD.23'
str4_alnum = str4.isalnum()  # str4_alnum == False ('.' 때문)


# 문자(열)이 알파벳인지 확인하기 - isalpha()
# 유의할 점: 공백, 숫자가 있으면 False / 한글도 알파벳으로 취급
str5 = 'ABc'
str5_alpha = str5.isalpha()   # str3_alpha == True

str6 = 'Hello World'
str6_alpha = str6.isalpha()   # str4_alpha == False (공백 때문)


# 문자(열)이 숫자인지 확인하기 - isdigit()
str7 = '12543'
str7_digit = str7.isdigit()   # str5_digit == True
