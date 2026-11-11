sentence = input("Enter sentences: ")

i = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
count_o_tilde = 0
count_a_umlaut = 0
count_o_umlaut = 0
count_u_umlaut = 0

while i < len(sentence):
    char = sentence[i].lower()
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1
    elif char == 'õ':
        count_o_tilde += 1
    elif char == 'ä':
        count_a_umlaut += 1
    elif char == 'ö':
        count_o_umlaut += 1
    elif char == 'ü':
        count_u_umlaut += 1
    i += 1

total_vowels = count_a + count_e + count_i + count_o + count_u + count_o_tilde + count_a_umlaut + count_o_umlaut + count_u_umlaut

print('a: ' + str(count_a))
print('e: ' + str(count_e))
print('i: ' + str(count_i))
print('o: ' + str(count_o))
print('u: ' + str(count_u))
print('õ: ' + str(count_o_tilde))
print('ä: ' + str(count_a_umlaut))
print('ö: ' + str(count_o_umlaut))
print('ü: ' + str(count_u_umlaut))
print('Total vowels: ' + str(total_vowels))