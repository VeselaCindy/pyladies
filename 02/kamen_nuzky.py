tah_pocitace = 'kámen'
tah_cloveka = input('kámen, nůžky, nebo papír? ')

if (tah_cloveka == 'kámen' and tah_pocitace == 'kámen') or (tah_cloveka == 'nůžky' and tah_pocitace == 'nůžky') or (tah_pocitace == 'papír' and tah_cloveka == 'papír'):
     print('Plichta.')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'nůžky') or (tah_cloveka == 'nůžky' and tah_pocitace == 'papír') or (tah_cloveka == 'papír'and tah_pocitace == 'kámen'):
        print('Vyhrála jsi!')
elif(tah_pocitace == 'papír' and tah_cloveka == 'kámen') or (tah_cloveka == 'nůžky' and tah_pocitace == 'kámen') or (tah_cloveka == 'papír' and tah_pocitace == 'nůžky'):
    print('Počítač vyhrál.')
else:
    print('Nerozumím.')