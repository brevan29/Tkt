# exercice 3.3
print(x==0 or (x>0 and 1/x>y) or (x<0 and 1/x<y))

# exercice 4
if m/d**2<=18:
    print("vous êtes en sous-poids")
elif m/d**2>=25:
    print("vous êtes en surpoids")

# exercice 5
somme_partielle=0
n=1
while 1/(n**2)<epsilon:
    n+=1
print(n)

# exercice 6
def ecriture_n(n,b):
    p=0
    while b**p<n:
        p+=1
    n_dans_b=[]
    for i in range(p,-1,-1):        
        n_dans_b.append(n%b**i)
        n=n//b**i
    return n_dans_b

def est_un_palindrome(n,b):
    n_b=ecriture_n(n,b)
    for i in range(len(n_b)//2):
        if n_b[i]!=n_b[len(n_b)-(i+1)]:
            return False
    return True

def recherche():
    n=range(10,10000)
    nombre_palindrome=[1,1] #Nombre en base 10, nombre de bases dans lequel il est palindrome
    for nombre in n:
        bases_palindrome=0
        for b in range(2,10):
            if est_un_palindrome(nombre,b):
                bases_palindrome+=1
        if bases_palindrome>nombre_palindrome[1]:
            nombre_palindrome=[nombre,bases_palindrome]
    return nombre_palindrome[1]
