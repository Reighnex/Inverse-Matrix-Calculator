def Print_Matrix(A):
    for i in A:
        print([round(x, 3) + 0 for x in i])


def Print_Matrices(A, I):
    Print_Matrix(A)
    print()
    Print_Matrix(I)
    print()
    print("----------------------------")
    print()


def Input_A(A, n):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(float(input("a{}{} = ".format(i + 1, j + 1))))
        A.append(row)
    print()
    print("----------------------------")
    print()


def Make_I(I, n):
    for x in range(n):
        row = []
        for y in range(n):
            row.append(float(0))
        I.append(row)

    for x in range(n):
        I[x][x] = float(1)


def Change_Rows(A, I, element, target):
    change_A = 0
    change_I = 0
    for i in range(n):
        change_A = A[element][i]
        A[element][i] = A[target][i]
        A[target][i] = change_A
        change_I = I[element][i]
        I[element][i] = I[target][i]
        I[target][i] = change_I


def Change_Rows_If_Zero(cnt):
    if A[cnt][cnt] == 0:
        for attempt in range(n):
            if attempt > cnt:
                Change_Rows(A, I, cnt, attempt)

                if A[cnt][cnt] == 0:
                    Change_Rows(A, I, cnt, attempt)

                else:
                    print("{}행과 {}행을 교환합니다.".format(cnt + 1, attempt + 1))
                    print()
                    Print_Matrices(A, I)
                    break


def Multiply_Row(A, I, cnt, n):
    d = A[cnt][cnt]
    if d != 1:
        scaler = 1. / d
        for i in range(n):
            A[cnt][i] *= scaler
            I[cnt][i] *= scaler

        print("{}행에 {}을 곱합니다.".format(cnt + 1, round(scaler, 3)))
        print()
        Print_Matrices(A, I)


def Subtract_Row(A, I, cnt, n):
    for x in range(n):
        if x != cnt:
            m = A[x][cnt]
            if m != 0:
                for y in range(n):
                    A[x][y] -= A[cnt][y] * m
                    I[x][y] -= I[cnt][y] * m

                print("{}행에 {}을 곱한 것을 {}행에서 뺍니다.".format(cnt + 1, round(m, 3), x + 1))
                print()
                Print_Matrices(A, I)


def Result(result, I):
    if result == 1:
        print("더 이상 대각성분을 1로 만들 수 없습니다. 역행렬이 존재하지 않습니다!")
    else:
        print("역행렬 계산 결과는 : ")
        print()
        Print_Matrix(I)


###############################################################################################

A = []  # 행렬 A
n = int(input("n차 정사각행렬의 역행렬을 계산합니다. n = "))
Input_A(A, n)  # 행렬의 크기와 원소를 입력받음

I = []  # 단위행렬 I
Make_I(I, n)  # 단위행렬 I를 행렬 A의 크기에 맞춰 생성
Print_Matrices(A, I)
result = 0  # 역행렬이 존재하는지에 대한 신호표지로 사용

for cnt in range(n):  # 대각성분에 차례로 접근
    Change_Rows_If_Zero(cnt)  # 현재 대각성분이 0인지 판별하고 필요시 행 교체

    if A[cnt][cnt] == 0:  # 대각성분을 1로 만들 수 있는지 판별
        result = 1  # 역행렬이 존재하지 않음
        break

    else:  # 대각성분을 1로 만들 수 있으므로 기본행 연산 시행
        Multiply_Row(A, I, cnt, n)  # 대각성분을 1로 만듦
        Subtract_Row(A, I, cnt, n)  # 대각성분 제외 열 원소를 0으로 만듦

Result(result, I)  # 결과 출력