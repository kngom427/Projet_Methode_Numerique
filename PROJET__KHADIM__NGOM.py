######################################################################
##################### KHADIM NGOM L2MPI ##############################
#################### Projet à rendre #################################
#Résolution du systeme lineaire Ax=b par la methode de JACOBI de GAUSS
#SEIDEL et de CHOLESKY,ensuite faire la comparaison entre ces methodes
######################################################################
import numpy as np


#%% Construction de la matrice

def matrice(a,b,c,N):
    U = a*np.ones((N))
    V = b*np.ones((N-1))
    W = c*np.ones((N-1))
    A = (np.diag(U,0) + np.diag(V,1) + np.diag(W,-1))
    return A
A = matrice(2,-1,-1,4) ; print("La matice A est:") ; print(A)


#%% Construction du second membre

def second_membre():
    N = np.shape(A)[0]
    b = np.zeros((N,1))
    for i in range(N):
        if((i+1)%2==0):
            b[i,0] = 1
    return b
b= second_membre() ; print("\nla matrice b est:") ; print(b)
    

#%% METHODE DE JACOBI

def meth_jacobi(A,b,x0,NT,eps):
    N = np.shape(A)[0]
    x1 = np.zeros((N,1))
    for k in range(0,NT):
        for i in range(0,N):
            S = 0
            for j in range(0,N):
                if(i!=j):
                    S = S + A[i,j]*x0[j]
            x1[i] = (1/A[i,i])*(b[i]-S)
        if(max(abs(np.dot(A,x1)-b)) < eps):
            break;
        x0 = x1
    return x1

#%% test du METHODE DE JACOBI

A = matrice(2,-1,-1,2) ; b = second_membre()
x0 = np.zeros((2,1)) ; eps=1e-10 ; NT=100

X = meth_jacobi( A, b, x0, NT, eps) ; print("\nSolution par METH_JACOBI est:")
print(X)


#%% METHODE DE GAUSS SEIDEL

def meth_gauss_seidel(A,b,x0,NT,eps):
    N = np.shape(A)[0]
    x1 = np.zeros((N,1))
    for k in range(0,NT):
        for i in range(0,N):
            S1 = 0
            S2 = 0
            for j in range(0,i):
                S1 = S1 + A[i,j]*x1[j]
            for j in range(i+1,N):
                S2 = A[i,j]*x0[j]
            x1[i] = (1/A[i,i])*(b[i]-S1-S2)
        if(max(abs(np.dot(A,x1)-b)) < eps):
            break;
        x0 = x1
    return x1

#%% test du METHODE DE GAUSS SEIDEL

A = matrice(2,-1,-1,2) ; b = second_membre()
x0 = np.zeros((2,1)) ; eps=1e-10 ; NT=100

X = meth_gauss_seidel( A, b, x0, NT, eps) ; print("\nSolution par METH_GAUSS_SEIDEL est:")
print(X)  


#%% METHODE DE CHOLESKY

def meth_cholesky():
    if (np.allclose(A,np.transpose(A)) and np.all(np.linalg.eigvals(A)>0)):
        N = np.shape(A)[0]
        H = np.zeros((A.shape[1],A.shape[1]))
        h = np.zeros((A.shape[1],A.shape[1]))
        for i in range(A.shape[0]):
            for k in range(i+1):
                S = sum(H[i,j]*H[k,j] for j in range(k))
                if(i==k):
                    H[i,k]=np.sqrt(A[i,i]-S)
                else:
                    H[i,k] = (1/H[k,k])*(A[i,k]-S)
        print("\nLa decomposition de la matrice de CHOLESKY est:") ; print(H)
        h=np.transpose(H)
        x0 = np.linalg.solve(H,b)
        x1 = np.linalg.solve(h,x0)
        return x1
    else:
        print("\nLa matrice n'est pas symetrique ou definie positive.")
        print("Donc la decomposition de CHOLESKY ne peut etre effectué")        
               

#%% test du METHODE DE CHOLESKY

A = matrice(2,-1,-1,2)  ; b = second_membre()
X = meth_cholesky() ; print("\nSolution par METH_CHOLESKY est:") ; print(X)


#%% Compararaison des METHODES
 
print("\nCOMPARAISON:")
print("¤La methode de JACOBI utilise une itération pour resoudre le systeme d'équation,\
 ce qui peut entrainer des erreurs de convergence.Cepandant,cette methode est generalement\
 plus rapide que les autres methodes car elle n'utilise pas de calculs coùteux\n\
 \n¤ La methode de GAUSS SEIDEL est similaire à celle de JACOBI mais elle utilise une\
 itération plus ameliorée.Cela peut entrainer une convergence plus rapides que\
 la methode de JACOBI mais elle est generalement plus lente en termes de vitesse\
 d'éxécution\n\
 \n¤ La methode de CHOLESKY est utiliséé pour résoudre des systemes d'équation lineaires\
 où la matrice est symetrique et definie positive.Elle utilise une décomposition en\
 matrice triangulaire pour résoudre le systeme d'équation,ce qui peut\
 entrainer une précision de solution élevée.Cependant cette methode est\
 generalement plus lente en termes de vitesse d'éxécution que les autres methodes\n\
 \n¤ En résumé,la methode de JACOBI est generalement la plus rapide en termes de vitesse\
 d'éxécution, mais elle peut entrainer des erreurs de convergence.La methode\
 de GAUSS SEIDEL est plus rapide que celle de JACOBI en termes de convergence,\
 mais elle est generalement plus lente en vitesse d'éxécution.La methode\
 de CHOLESKY est generalement la plus précise en terme de solution,mais elle\
 est generalement plus lente en termes de vitesse d'éxécution.")





















