# 🔢 Résolution de Systèmes Linéaires — Méthodes Numériques

## 📘 Description du projet
Ce projet a pour objectif de résoudre le système linéaire **Ax = b** à l’aide de trois méthodes numériques classiques :

- **Méthode de Jacobi**
- **Méthode de Gauss-Seidel**
- **Méthode de Cholesky**

L’objectif est ensuite de **comparer** ces méthodes en termes de **convergence**, **rapidité** et **précision**.

Ce travail a été réalisé dans le cadre d’un projet universitaire en licence (L2 MPI).

---

## 🧮 Méthodes implémentées

### 🔹 1. Méthode de Jacobi
Méthode itérative utilisant les valeurs de l’itération précédente pour calculer la suivante.  
➡️ Rapide à chaque itération, mais peut **converger lentement**.

### 🔹 2. Méthode de Gauss-Seidel
Méthode itérative améliorée de Jacobi : les valeurs calculées sont **réutilisées immédiatement**.  
➡️ Convergence plus rapide, mais calcul légèrement plus coûteux.

### 🔹 3. Méthode de Cholesky
Méthode directe basée sur la **décomposition matricielle A = H·Hᵗ**, valable pour les matrices **symétriques définies positives**.  
➡️ Très **précise**, mais plus lourde à calculer.

---

## 🧱 Structure du projet
```bash
Projet_Methodes_Numeriques/
│
├── PROJET__KHADIM__NGOM.py # Code principal (toutes les méthodes et tests)
├── README.md # Présentation du projet
```

---

## ⚙️ Exécution

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/kngom427/Projet_Methode_Numerique.git
cd Projet_Methodes_Numeriques
```
### 2️⃣ Lancer le script
```bash
python PROJET__KHADIM__NGOM.py
```
Le programme :

construit la matrice A et le vecteur b,

applique successivement les méthodes de Jacobi, Gauss-Seidel et Cholesky,

affiche les solutions et une comparaison finale des performances.

## 👨‍💻 Auteur

Khadim NGOM
Université Sine Saloum Elhadj Ibrahima Niass — Licence 2

## 🧾 Licence

Projet académique à usage pédagogique — libre d’utilisation à des fins d’apprentissage.
