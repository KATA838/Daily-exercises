import jieba
test = '下雨天留客天不留我'
words = jieba.lcut(test)
print(words)