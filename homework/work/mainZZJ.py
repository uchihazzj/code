import mongoZZJ as mg
import randomZZJ as rd
import matplotlibZZJ as mplt
mg.test()
rd.test()
mplt.test()
for data in rd.data_creat():
    mg.insertDB(data)
print('insert finished!')
mg.saveALL()

for data in mg.loadDB():
    mplt.getValues(data)

print('yvalue is sended')
mplt.plotInit()