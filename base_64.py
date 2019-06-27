import textwrap

#BASE64 Dictionary
base64_dict = {"0":"A", "1":"B", "2":"C", "3":"D", "4":"E", "5":"F", "6":"G", "7":"H", "8":"I", "9":"J", "10":"K", "11":"L", "12":"M", "13":"N", "14":"O", "15":"P", "16":"Q", "17":"R", "18":"S", "19":"T", "20":"U", "21":"V", "22":"W", "23":"X", "24":"Y", "25":"Z",
"26":"a", "27":"b", "28":"c", "29":"d", "30":"e", "31":"f", "32":"g", "33":"h", "34":"i", "35":"j", "36":"k", "37": "l", "38":"m", "39":"n", "40":"o", "41":"p", "42":"q", "43":"r", "44":"s", "45":"t", 
"46":"u", "47":"v", "48":"w", "49":"x", "50":"y", "51":"z", "52":"0", "53":"1", "54":"2", "55":"3", "56":"4", "57":"5", "58":"6", "59":"7", "60":"8", "61":"9", "62":"+", "63":"/"}

test_input = "how utterly fascinating"
test_input_list = list(test_input)

for i in range(0, len(test_input_list)):
    test_input_list[i] = format(ord(test_input_list[i]), '08b')

binary_string = ''.join(test_input_list)
temp = textwrap.wrap(binary_string,6)
last_element_length = len(temp[len(temp)-1])

if(last_element_length < 6):
    print("True!")
    last_element = temp[len(temp)-1]

    for j in range(0, 6 - last_element_length):
        last_element += '0'
        temp[len(temp)-1] = last_element
        
for k in range(0, len(temp)):
    temp[k] = int(temp[k],2) 
    temp[k] = base64_dict.get(str(temp[k]))

equals = 6 - last_element_length
for x in range(0, int(equals / 2)):
    temp.append("=")
    
binary_string = ''.join(temp
print("The base64 encoding of the string",test_input, "is",binary_string)