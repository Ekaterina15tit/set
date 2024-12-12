b = input().split()
st = set()
for i in b:
    if i in st:
        print('YES')
    else:
        print('NO')
    st.add(i)