
import re
a = '[<Word: c++>, <Word: java>, <Word: python>, <Word: php>, <Word: ruby>, <Word: c#>]'
# b = a.replace('<Word: ','\'').replace('>','\'')
# print(b)
p=re.compile(r'Word:(.+)>')
c=re.search(r'Word:(.+)>',a).group(1)
print(c)
d=p.findall(a)
print(d)