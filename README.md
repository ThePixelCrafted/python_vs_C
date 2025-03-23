# Python vs C: Performance Benchmark

Ce projet démontre qu'un code Python bien optimisé peut rivaliser, voire surpasser, le C en termes de performances pour certaines tâches spécifiques.

## Benchmark : Création d'un tableau de 1 milliard de nombres aléatoires

### Environnement
- **Système d'exploitation** : Linux (WSL2)
- **Compilateur C** : GCC 11.4.0
- **Interpréteur Python** : Python 3.10.12

### Résultats du benchmark

| Langage  | Temps d'exécution |
|----------|------------------|
| **C**    | 11.32 secondes   |
| **Python** | 0.52 secondes   |

### Explication
Contrairement aux idées reçues, Python peut être extrêmement performant lorsqu'on utilise les bonnes bibliothèques et les bonnes pratiques d'optimisation (par ex. NumPy, multiprocessing, JIT compilation avec Numba, etc.).

## Objectif du Projet
L'objectif est d'analyser et de démontrer comment, avec les bonnes techniques, Python peut atteindre des performances comparables à C.

## Comment exécuter le benchmark ?

### Exécution du benchmark (C et Python simultanément)
```bash
python3 benchmark.py
```
