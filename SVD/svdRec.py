
from numpy import *
from numpy import linalg as la

def loadExData():
    return[[4,4,0,2,2],
           [4,0,0,3,3],
           [4,0,0,1,1],
           [1,1,1,2,0],
           [2,2,2,0,0],
           [1,1,1,0,0],
           [5,5,5,0,0]
        ]

def loadExData2():
    return[[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
           [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
           [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
           [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
           [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
           [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
           [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
           [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
           [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
           [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
           [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

def eulidSim(inA,inB):
    return 1.0/(1.0+la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5*corrcoef(inA,inB,rowvar = 0)[0][1]

def cosSim(inA,inB):
    num = float(inA.T * inB)
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * (num/denom)

#这个算法的目的是通过从左到右遍历每一个物品，如果找到用户评价过的物品，
#就计算与目标物品的相似度，通过对用户其他评价过的物品的比较，得出用户对目标物品可能的喜爱程度
def standEst(dataMat,user,simMeas,item):
    n = shape(dataMat)[1]     #得到物品数目
    simTotal = 0.0
    ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]  #用户的评分
        if userRating == 0:continue    #评分为0，跳过循环
        #dataMat[:,item],dataMat[:,j]中同时都大于0的那个元素的行下标
        overLap = nonzero(logical_and(dataMat[:,item].A>0,dataMat[:,j].A>0))[0]
        #两列元素没有在同一行元素都大于0的行，说明这两列向量正交，相似度为0
        if len(overLap) == 0:similarity = 0
        #计算相似度，overlap是一个行下标向量
        else:similarity = simMeas(dataMat[overLap,item],dataMat[overLap,j])
        print ('the %d and %d similarity is: %f' % (item,j,similarity))
        simTotal += similarity
        ratSimTotal += similarity * userRating   #用户评分越高权重越大
    if simTotal ==0:return 0
    else : return ratSimTotal/simTotal    #归一化

#得出估计评分前三的物品
def recommend(dataMat,user,N=3,simMeas=cosSim,estMethod=standEst):
    unratedItems = nonzero(dataMat[user,:].A==0)[1]      #找出所有未评分物品
    if len(unratedItems) == 0:return 'you rated everything'
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat,user,simMeas,item)
        itemScores.append((item,estimatedScore))
    #jj表示待排序元祖，jj[1]按照jj的第二列排序，reverse=True，降序
    return sorted(itemScores,key=lambda jj: jj[1],reverse=True)[:N]
    
#基于SVD的评分估计
def svdEst(dataMat,user,simMeas,item):
    n = shape(dataMat)[1]    #列数，既物品数
    simTotal = 0.0
    ratSimTotal = 0.0
    U,Sigma,VT = la.svd(dataMat)
    Sig4 = mat(eye(4)*Sigma[:4])    #找出包含90%能量的奇异值，建立对角矩阵
    xformedItems = dataMat.T * U[:,:4] * Sig4.I   # 利用U矩阵将物品转换到低维空间中，即降成4维
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 or j == item:continue   #用户没有评分或遇到目标物品，结束本次循环
        similarity = simMeas(xformedItems[item,:].T,xformedItems[j,:].T)
        print( 'the %d and %d similarity is: %f' % (item,j,similarity))
        simTotal += similarity * userRating
        ratSimTotal += similarity * userRating
    if simTotal ==0:return 0
    else:return ratSimTotal/simTotal

def printMat(inMat,thresh=0.8):
    a = [0]*32
    for i in range(32):
        for k in range(32):
            if float(inMat[i,k]) > thresh:
                a[k] = 1
            else: a[k] = 0
        print (a)
        print ('')

def imgCompress(numSV=3,thresh=0.8):
    myl = []
    for line in open('0_5.txt').readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)
    myMat = mat(myl)
    print ("****original matrix******")
    printMat(myMat,thresh)
    U,Sigma,VT = la.svd(myMat)
    SigRecon = mat(zeros((numSV,numSV)))
    for k in range(numSV):
        SigRecon[k,k] = Sigma[k]
    reconMat = U[:,:numSV] * SigRecon * VT[:numSV,:]
    print ("****reconstructed matrix using %d singular values******" %numSV)
    printMat(reconMat,thresh)

imgCompress(2)



























































    
