from matplotlib import pyplot as plt

minutes=[0,1,2,3,4,5,6,7,8,9]
player1=[2,1,0,3,5,4,1,5,4,2]
player2=[1,0,0,1,3,5,2,1,3,2]
#player3=[3,4,1,3,5,2,1,0,4,1]
labels=['player 1','player 2']
plt.stackplot(minutes,player1,player2,labels=labels)
plt.legend()
plt.show()
