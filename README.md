# PythonDiscreteControl_TP

Projet Python dédié à l'analyse, la conception et la simulation de systèmes de commande numériques, avec une attention particulière portée aux correcteurs **PID discrets** et aux régulateurs **RST**.

Ce projet a été réalisé dans le cadre d'un travail pratique de commande numérique et fournit un ensemble d'outils modulaires permettant l'étude, la synthèse et la comparaison de différentes stratégies de contrôle.

---

## Objectifs du projet

- Étudier le comportement de systèmes dynamiques discrets.
- Concevoir des correcteurs PID numériques.
- Synthétiser des régulateurs RST par placement de pôles.
- Simuler des boucles de commande en temps discret.
- Évaluer les performances de différentes stratégies de contrôle.
- Comparer les approches PID et RST sur des systèmes de référence.

---

## Fonctionnalités

### Correcteur PID discret

Le projet inclut une implémentation complète d'un correcteur PID numérique permettant :

- Action proportionnelle (P)
- Action intégrale (I)
- Action dérivée (D)
- Représentation sous forme de fonction de transfert discrète
- Conversion vers une représentation RST équivalente
- Simulation pas à pas

### Régulateur RST

Le régulateur RST repose sur la loi de commande :

```math
S(z)u(k)=T(z)r(k)-R(z)y(k)
```

Cette approche permet :

- Le placement explicite des pôles en boucle fermée
- La séparation entre poursuite de consigne et rejet des perturbations
- La synthèse de correcteurs à partir de spécifications dynamiques

Les outils fournis permettent notamment de résoudre les équations diophantiennes nécessaires au calcul des polynômes `R`, `S` et `T`.

### Simulation

Le framework de simulation permet :

- La simulation de systèmes discrets
- L'évaluation de lois de commande PID ou RST
- Le suivi de consigne
- L'enregistrement des données de simulation
- L'analyse des performances temporelles

### Modèle étudié

#### Système Ball & Beam

Le projet contient également un modèle du système Ball & Beam, utilisé pour l'étude de :

- La commande de systèmes instables
- Les modèles non linéaires
- Les approches avancées de régulation

---

## Structure du projet

```text
PythonDiscreteControl_TP
│
├── Control/
│   ├── DiscretePID.py
│   └── RSTController.py
│
├── Models/
│   ├── BallBeam/
│   └── ...
│
├── Simulation/
│   └── simulation.py
│
├── Utils/
│   ├── computeRST.py
│   └── test_computeRST.py
│
├── Metrics_Plotting/
│   ├── Metrics.py
│   ├── Plotting.py
│   └── SimLog.py
│
├── DoubleIntégrateurAnalyse.ipynb
├── CommandeDoubleIntégrateur_PID.ipynb
└── CommandeDoubleIntégrateur_RST.ipynb
```

---

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/Bababoey123/PythonDiscreteControl_TP.git
cd PythonDiscreteControl_TP
```

### Créer un environnement Python

Avec Conda :

```bash
conda create -n discrete-control python=3.12
conda activate discrete-control
```

### Installer les dépendances

```bash
pip install numpy scipy matplotlib control jupyter
```

ou

```bash
conda install numpy scipy matplotlib
conda install -c conda-forge control
```

---

## Notebooks disponibles

### DoubleIntégrateurAnalyse.ipynb

Analyse du système :

- Modélisation
- Discrétisation
- Étude des pôles et des zéros
- Analyse fréquentielle

### CommandeDoubleIntégrateur_PID.ipynb

Conception et validation d'un correcteur PID :

- Réglage des gains
- Simulation en boucle fermée
- Évaluation des performances

### CommandeDoubleIntégrateur_RST.ipynb

Conception d'un régulateur RST :

- Choix de la dynamique désirée
- Résolution de l'équation diophantienne
- Placement de pôles
- Comparaison avec le PID

---

## Évaluation des performances

Les outils intégrés permettent notamment de mesurer :

- Temps de montée
- Temps de réponse
- Dépassement maximal
- Erreur statique
- Effort de commande
- Qualité du suivi de consigne
- Les marges de phase et de gain

---

## Dépendances principales

- Python 3.10+
- NumPy
- SciPy
- Matplotlib
- Python-Control
- Jupyter Notebook

---

## Perspectives d'amélioration

Extensions possibles :

- Observateurs d'état
- Filtre de Kalman
- Commande LQR
- Commande prédictive (MPC)
- Anti-windup pour PID
- Réglage automatique des correcteurs
- Études de robustesse

---

## Contexte pédagogique

Ce projet a été développé dans le cadre di stage de fin de Licence au LAGEPP. Il vise à fournir une base claire et modulaire pour expérimenter différentes méthodes de régulation et approfondir les concepts fondamentaux de la commande discrète.

---
