#Indi Knighton
#30/09/2014
#Conversion of text characters into ASCII code

ASCII_code = int(input("Please enter a code in ASCII here: "))
Text_code = input("Please enter your text here: ")

ASCII_conversion = chr(ASCII_code)
Text_conversion = ord(Text_code)

print("Your ASCII code in text is {0}".format(ASCII_conversion))
print("Your Text code is {0}".format(Text_conversion))
