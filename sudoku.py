f = (input("Давайте поиграем в судоку! Нажмите 1, чтобы начать "))
while True:
     p = [[0, 4, 9, 2, 5, 6, 1, 0, 3],
          [5, 2, 7, 1, 3, 9, 8, 4, 6],
          [6, 1, 3, 7, 8, 4, 5, 2, 9],
          [9, 6, 2, 8, 4, 1, 3, 5, 7],
          [0, 5, 1, 3, 6, 7, 2, 9, 8],
          [3, 7, 8, 9, 2, 5, 6, 1, 4],
          [7, 8, 5, 6, 9, 2, 4, 3, 1],
          [1, 3, 4, 5, 7, 8, 9, 6, 2],
          [2, 9, 6, 4, 1, 3, 7, 8, 5]]
     while f != "1":
          f = input("Я вас не понимаю. Нажмите 1, чтобы начать ")
     while 0 in [p[i][j] for i in range(len(p)) for j in range(len(p))]:
          for i in range(len(p)):
               print(*p[i])
          column = (input("Введите номер столбца "))
          while column.isdigit() == False:
               column = input("Введите число, а не букву ")
          column = int(column)
          while column>9 or column<1:
               column = (input("Я вас не понимаю. Введите число от 1 до 9 "))
               while column.isdigit() == False:
                    column = input("Введите число, а не букву ")
               column = int(column)
          row = (input("Введите номер строки "))
          while row.isdigit() == False:
               row = input("Введите число, а не букву ")
          row = int(row)
          while row>9 or row<1:
               row = (input("Я вас не понимаю. Введите число от 1 до 9 "))
               while row.isdigit() == False:
                    row = input("Введите число, а не букву ")
               row = int(row)
          n = (input("На какое число заменяете? "))
          while n.isdigit() == False:
               n = input("Введите число, а не букву ")
          n = int(n)
          while n>9 or n<1:
               n = (input("Я вас не понимаю. Введите число от 1 до 9 "))
               while n.isdigit() == False:
                    n = input("Введите число, а не букву ")
               n = int(n)
          p[row-1][column-1] = n
     flag1 = True
     for i in p:
          if len(set(i)) != 9:
               flag1 = False
               break
     flag2 = True
     for i in range(len(p)):
          s = []
          for j in range(len(p)):
               s.append(p[j][i])
          if len(set(s)) != 9:
               flag2 = False
               break
     flag3 = True
     for i in range(0, 9, 3):
          for j in range(0, 9, 3):
               k = []
               for i1 in range(i, i+3):
                    for j1 in range(j, j+3):
                         k.append(p[i1][j1])
               if len(set(k)) != 9:
                    flag3 = False
                    break
     if flag1 and flag2 and flag3:
          print("Вы выиграли!")
     else:
          print("Вы проиграли!")
     ans = input("Хотите сыграть ещё раз? (Если да, нажмите 1) ")
     if ans != "1":
          break