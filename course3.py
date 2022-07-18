import sys
all_result = {}

def find_direct_cad(line):
    bonus_count = 0
    while True:
        pos = line.find('CAD')
        if pos == -1:
            break
        bonus_count+=1
        line = line[:pos] + line[pos+3:]
    return (line, bonus_count)

def find_cad(str1, length):
    for i in range(length-2):
        if str1[i] != 'C':
            continue
        for j in range(i+1,length-1):
            if str1[j] != 'A':
                continue
            for k in range(j+1,length):
                if (str1[k] == 'D'):
                    return (i,j,k)
                    
    return None

def find_bonus(substr, bonus):
    # print(substr)
    if substr == '':
        return bonus
    cached = all_result.get(substr)
    if cached != None:
        return bonus + cached
    (substr, new_bonus) = find_direct_cad(substr)
    # print(f'1.5: {substr}')
    bonus+=new_bonus
    c_pos = [pos for pos, char in enumerate(substr) if char == 'C']
    a_pos = [pos for pos, char in enumerate(substr) if char == 'A']
    d_pos = [pos for pos, char in enumerate(substr) if char == 'D']
    cad_c = min(len(c_pos),len(a_pos),len(d_pos))
    # print(f'c:{c_pos}, a:{a_pos}, d:{d_pos}')
    if len(c_pos) == 0  or len(a_pos) == 0 or len(d_pos) == 0:
        all_result[substr]=0
        return bonus
    found_pos = find_cad(substr, len(substr))
    if found_pos == None:
        all_result[substr]=0
        return bonus
    # print(f'2: {substr}')
    result = []
    c_prev = -100
    a_prev = -100
    d_prev = -100
    for c in c_pos:
        # print(f'c_prev:{c_prev}, c:{c}')
        if c == c_prev + 1:
            continue
        c_prev = c
        for a in a_pos:
            # print(f'a_prev:{a_prev}, a:{a}')
            if a == a_prev + 1:
                continue
            a_prev = a
            for d in d_pos:
                # print(f'd_prev:{d_prev}, d:{d}')
                if d == d_prev + 1:
                    continue
                d_prev = d
                tmp_bonus = bonus
                if c + 1 == a and a + 1 == d:
                    tmp_bonus+=1
                positions = [c, a, d]
                # print(f'positions: {positions}')
                positions.sort()
                i,j,k = positions
                result.append(find_bonus(substr[:i] + substr[i+1:j] + substr[j+1:k] + substr[k+1:], tmp_bonus))
    final = max(result)
    all_result[substr]=final
    # print(f'final: {final}')
    # print(f'all_result: {all_result}')
    # print()
    return final
    

input = sys.stdin.readlines()
n,x,y = list(map(int,input[0].split(' ')))
line = input[1].rstrip()

bonus_count = 0


c_count = line.count('C')
a_count = line.count('A')
d_count = line.count('D')

(line, bonus_count) = find_direct_cad(line) 

# print(bonus_count)
# print(line)

basic_point = min(c_count,a_count,d_count)
all_cad = basic_point
bonus_count += find_bonus(line, 0)


# print(f'bonus: {bonus_count}')
# print(f'basic: {basic_point}')

print(bonus_count * y + basic_point * x)
