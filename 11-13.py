mtStr='파이썬은 재밌어요.'
strPosList=[]
index=0

while True:
    try:
        index = myStr.index('파이썬', index)
        strPosList.append(index)
        index = index+1     #다음 위치부터 찾음
    except:
        break

print('파이썬 글자 위치 -->.',strPosList)
