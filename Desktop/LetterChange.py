'''
Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. '''
#Using python to solve problem:
def LetterChange(x):
 store=[]
 vowels=['a','e','i','o','u']
 for i in x:
   if i.isalpha():
     nextLetter=chr(ord(i)+1)#output is next letter
     if (nextLetter.lower() in vowels):
       store.extend([nextLetter.upper()])#change to upper of vowels
     else:
       store.append(nextLetter)
   else:
     store.append(i)
 y="".join(store)#get rid off list things i,e[] & ''
 return y
t="hello*3"
#Input: "fun times!"
#Output: gvO Ujnft!
# Input: "hello*3"
# Output: Ifmmp*3
print(LetterChange(t))

