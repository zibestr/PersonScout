import numpy as np





def util(a):
    types = {(1,-1,-1,-1):["Inspector","Инспектор"], (1,-1,1,-1):["Protector","Защитник"], (1, 1, 1, -1):["Counselor","Советник"], (1, 1, -1, -1):["Mastermind","Вдохновитель"], 
         (1, -1, -1, 1):["Crafter","Делец"], (1, -1, 1, 1):["Composer","Развлекатель"], (1, 1, 1, 1):["Healer","Виртуоз"], (1, 1, -1, 1):["Architect","Артист"],
         (-1, -1, -1, 1):["Promoter","Полемист"], (-1, -1, 1, 1):["Performer","Стратег"], (-1, 1, 1, 1):["Champion","Командир"], (-1, 1, -1, 1):["Invertor","Учёный"],
         (-1, -1, -1, -1):["Supervisor","Активист"], (-1, -1, 1, -1):["Provider","Посредник"], (-1, 1, 1, -1):["Teacter","Тренер"], (-1, 1, -1, -1):["Fieldmarshal","Борец"]}
    return types[a]



def OCEAN2MBTI(ocean):
    matrix = [
            [-0.74, 0.03, -0.03, 0.08, 0.16],
            [0.1, 0.72, 0.04, -0.15, -0.06],
            [0.19, 0.02, 0.44, -0.15, 0.06],
            [0.15, 0.3, -0.06, -0.49, 0.11]
    ]

    mat=np.array([np.array(xi) for xi in matrix])
    ocean[1], ocean[-1] = ocean[-1], ocean[1]
    a = np.dot(mat,ocean)
    ret = []
    for i in a:
        if i<0:
            ret.append(-1)
        else:
            ret.append(1)
    return util(tuple(ret))
