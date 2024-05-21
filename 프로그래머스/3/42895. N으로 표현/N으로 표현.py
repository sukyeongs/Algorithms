def solution(N, number):
    answer = -1
    can_make = []
    
    for i in range (1,9):
        case = set()
        case.add(int(str(N) * i))
        for j in range(i-1):
            for num1 in can_make[j]:
                for num2 in can_make[i-j-2]:
                    case.add(num1 - num2)
                    case.add(num1 + num2)
                    case.add(num1 * num2)
                    if num2 != 0:
                        case.add(num1 // num2)

        if number in case:
            answer = i
            break
            
        can_make.append(case)
        
    return answer