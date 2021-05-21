import matplotlib.pyplot as plt

dni = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21  ]
mass = [109.7, 109.5, 108.4, 107.6, 108.2, 108.6, 108.4, 108.2, 108.7, 108.8, 107.9, 107.5, 107.4, 107.4, 108.0, 107.6, 107.3]
meanmass = []

difkg =mass[0] - mass[-1]

totalkkal = difkg*7716
real_kkal_day = totalkkal/ len(dni)
print(f'с {dni[0]} по {dni[-1]} мая, мой среднесуточный дефицит  составял ',  str(int(real_kkal_day)),  'калории')



for i in range(len(mass)):
    x = difkg/ len(mass)
    z = mass[1] - x*i
    modnum = float('{:.1f}'.format(z))
    meanmass.append(modnum )
    
x_max = int(max(dni)*1.05)
y_max = int(max(mass)*1.02)
y_min = int(min(mass)*0.98)
x_min = int(min(dni)*0.95)


plt.title('Динамика моего веса')    
plt.axis([x_min,x_max,y_min,y_max])
plt.ylabel('Мой вес')
plt.xlabel('Май 2021')
plt.text(6.15, 109.5, r'Красная линия - среднее значение')
plt.plot(dni, mass)

plt.plot(dni, meanmass, 'rd-')
plt.show()
