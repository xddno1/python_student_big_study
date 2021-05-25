from openpyxl import load_workbook


def getnostudytxt(xlsx_path):
    wb = load_workbook(xlsx_path)
    sheets = wb.worksheets  # 获取当前所有的sheet
    myclassstudent = ['陈荣森', '邓京锐', '邓文凯', '何江伟', '何锦胜', '李春江', '李锦科', '廖金威', '廖钧濠', '林荣添', '刘继洪', '罗炜芊', '麦洋华', '彭浩林', '唐爱萍', '涂骏', '冼东潮', '肖华锋', '谢泽琛', '杨奋发', '张杰森', '郑佳浩', '植美麟', '周天宝']
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
        if i not in studyedstudent:
            unstudyedstudent.append(i)
    file = open('大学习未完成名单.txt', 'w')

    for i in unstudyedstudent:
        file.write(i)
        file.write('\n')
    file.close()
    return unstudyedstudent

