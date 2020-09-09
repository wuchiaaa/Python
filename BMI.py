"""
標準體重，其計算公式：
男性： （身高cm－80）×70﹪
女性： （身高cm－70）×60﹪
身體質量指數（Body Mass Index，縮寫為BMI），其計算公式：
    BMI = 體重 (kg) / 身高 (m2)

    BMI ＜ 18.5      體重過輕
    18.5≦BMI＜24     正常範圍
    24≦BMI＜27       過重
    27≦BMI＜30       輕度肥胖
    30≦BMI＜35      中度肥胖
    BMI≧35          重度肥胖　
<資料來源：衛生福利部國民健康署>
"""
gender = int(input('性別(1)男性 (2)女性：'))

if (gender == 1) or (gender == 2):
    height = float(input('身高(公分)：'))
    weight = float(input('目前體重(公斤)：'))
    '''
    身高輸入範圍限制130公分~250公分
    體重輸入範圍限制2公斤~400公斤
    '''
    print('<結果>：')
    if (130 <= height <= 250) and (2 <= weight <= 400):
        if gender == 1:
            sw = (height - 80) * 0.7
        else:
            sw = (height - 70) * 0.6

        BMI = weight / (height / 100) ** 2

        if BMI < 18.5:
            result = '體重過輕'
        elif 18.5 <= BMI < 24:
            result = '正常範圍'
        elif 24 <= BMI < 27:
            result = '過重'
        elif 27 <= BMI < 30:
            result = '輕度肥胖'
        elif 30 <= BMI < 35:
            result = '中度肥胖'
        else:
            result = '重度肥胖'

        print(f'''您的性別：{'男' if gender == 1 else '女'}  身高：{height}公分  體重：{weight}公斤
-----------------------------------------------
標準體重：{sw:.2f}公斤
您的BMI：{BMI:.2f}
判定結果：{result}
''')
    else:
        print('身高輸入範圍限制130公分~250公分\n體重輸入範圍限制2公斤~400公斤\n請依範圍輸入!')
else:
    print('性別輸入錯誤，請重新輸入！')
