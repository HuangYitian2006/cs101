haab = {'pop': 1, 'no': 2, 'zip': 3, 'zotz': 4, 'tzec': 5, 'xul': 6,
        'yoxkin': 7, 'mol': 8, 'chen': 9, 'yax': 10, 'zac': 11, 'ceh': 12,
        'mac': 13, 'kankin': 14, 'muan': 15, 'pax': 16, 'koyab': 17, 'cumhu': 18, 'uayet': 19}
tz=['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik',
    'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben',
    'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
n = int(input())
print(n)
for _ in range(n):
    a = input().split()
    s=int(a[2])*365+int(a[0][0:len(a[0])-1])+(haab[a[1]]-1)*20
    y=s//260
    b=s%260
    print(s%13+1,tz[s%20],y)
