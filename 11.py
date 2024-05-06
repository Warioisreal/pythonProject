f = open('БД_ученики.csv')
k1, sm, kl, kh = 0, 0, 0, [0, 0, 0]
f.readline()
for i in f:
a = i.split(';')
if a[2] == '9' and int(a[3]) > 250:
k1 += 1
if a[1] == '3':
sm += int(a[3])
kl += 1
if a[1] in ['46', '48', '49']:
kh[int(a[1]) % 4] += 1
f.close()
print(k1)
print('{0:.2f}'.format(sm / kl))
print(f'49 школа: {kh[1]}; 46 школа - {kh[2]} участников; 48 школа - {kh[0]} участников.')
