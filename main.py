from openpyxl import load_workbook


def getnostudytxt(xlsx_path):
    wb = load_workbook(xlsx_path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    myclassstudent = [{'name': '邓京锐', 'no': '03'}, {'name': '邓文凯', 'no': '04'}, {'name': '何江伟', 'no': '05'}, {'name': '何锦胜', 'no': '06'}, {'name': '李春江', 'no': '08'}, {'name': '李锦科', 'no': '09'}, {'name': '廖金威', 'no': '11'}, {'name': '廖钧濠', 'no': '12'}, {'name': '林荣添', 'no': '15'}, {'name': '刘继洪', 'no': '16'}, {'name': '罗炜芊', 'no': '17'}, {'name': '麦洋华', 'no': '20'}, {'name': '彭浩林', 'no': '21'}, {'name': '唐爱萍', 'no': '22'}, {'name': '涂骏', 'no': '24'}, {'name': '冼东潮', 'no': '26'}, {'name': '肖华锋', 'no': '27'}, {'name': '谢泽琛', 'no': '28'}, {'name': '杨奋发', 'no': '29'}, {'name': '张杰森', 'no': '31'}, {'name': '郑佳浩', 'no': '33'}, {'name': '植美麟', 'no': '34'}, {'name': '周天宝', 'no': '35'}]
    # 24团员
    # print(len(myclassstudent))
    # 获取第一张sheet
    sheet1 = sheets[0]
    studyedstudent = []
    for col in sheet1['A']:
        studyedstudent.append(col.value)
    # print(studyedstudent)
    unstudyedstudent = []
    for i in myclassstudent:
        if i['name'] not in studyedstudent:
            unstudyedstudent.append(i)
    file = open('大学习未完成名单.txt', 'w')

    for i in unstudyedstudent:
        file.write(i['name'])
        file.write(i['no'])
        file.write('\n')
    file.close()
    return unstudyedstudent

