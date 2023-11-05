# Так можно прочитать весь файл
f = open('text.txt', 'w', encoding='utf-8')
text = f.write("'" текстовыми файлами:\n"'")
print(text)
f.close()

"'"\
"r " - "read"
'w ' - 'write'
'a ' - 'append'
"'"а