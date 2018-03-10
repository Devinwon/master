'''
#description:#
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，
逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

###Input description###
将一个英文语句以单词为单位逆序排放。

###Output description###
得到逆序的句子

#example#

###Input###
I am a boy

###Output###
boy a am I
'''

sentence=list(input().split())
sentence=sentence[::-1]
print(' '.join(sentence))