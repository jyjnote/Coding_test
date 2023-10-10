while True:
    n = int(input())
    
    if n == -1:
        break

    ds = []

    for i in range(1, n):
        if n % i == 0:
            ds.append(i)

    s = sum(ds)
  
    if s == n:
        print(f"{n} = " + " + ".join(map(str, ds)))
    else:
        print(f"{n} is NOT perfect.")
