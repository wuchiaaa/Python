# 練習題
'''呈現結果
若失敗五次就會退出遊戲
請輸入一個字串：Python
請輸入-n-的字串： new
錯誤1次,請再輸入-n-的字串
請輸入-n-的字串：new
上一個字串是  Python-new
請輸入-w-的字串：well
上一個字串是  Python-new-well
'''
print('若失敗五次就會退出遊戲')

game = input('請輸入一個字串：')

counter = 0
while counter < 5:
    keyin = input(f'請輸入-{game[-1]}-的字串：')

    if game[-1] == keyin[0]:
        game = game + '-' + keyin
        print(f'上一個字串是：{game}')
    else:
        counter += 1
        print(f'錯誤{counter}次，請再輸入-{game[-1]}-的字串' if counter < 5 else '錯誤已達5次，遊戲結束。')
