a = input()
st = []
err = "YES"
for i in a:
    if i in "([{":
        st.append(i)
    else:
        if st and st[-1] + i in ["()", "{}", "[]"]:
            st.pop()
        else:
            err = "NO"
            break
if st:
    err = "NO"
print(err)