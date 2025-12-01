# 📘 TP ChessLab - Backend Django avec WebSockets

## 🎯 Introduction

Bienvenue dans ce TP où vous allez créer une application web de jeu d'échecs en temps réel ! Ce projet vous permettra de maîtriser les concepts avancés du développement backend avec Django, en particulier la communication temps réel via WebSockets.

---

## 🎓 Objectifs Pédagogiques

À la fin de ce TP, vous serez capable de :

✅ **Modéliser** des données complexes avec Django ORM (relations, contraintes)

✅ **Configurer** Django Channels pour supporter les WebSockets

✅ **Implémenter** la communication bidirectionnelle en temps réel

✅ **Gérer** l'état partagé entre plusieurs utilisateurs connectés

✅ **Comprendre** la différence entre WSGI (synchrone) et ASGI (asynchrone)

✅ **Créer** des Consumers pour gérer les événements WebSocket

✅ **Synchroniser** des données entre plusieurs clients en temps réel

## 📦 Le Starter GitHub

Pour vous concentrer sur le backend, nous vous fournissons un **starter complet** contenant :

### 📁 Structure du Starter

```
chesslab-starter/
├── 📄 README.md              ← Instructions de setup
├── 📄 requirements.txt       ← Dépendances Python
├── 📄 manage.py
│
├── 📂 chess_project/
│   ├── settings.py          ✅ Fourni (pré-configuré)
│   ├── urls.py              ✅ Fourni (structure de base)
│   ├── asgi.py              ✅ Fourni
│   └── wsgi.py              ✅ Fourni
│
├── 📂 chess_app/
│   ├── models.py            ✏️ TODO PARTIE 1
│   ├── admin.py             ✏️ TODO PARTIE 1
│   ├── views.py             ✏️ TODO PARTIE 2
│   ├── urls.py              ✏️ TODO PARTIE 2
│   ├── consumers.py         ✏️ TODO PARTIE 3 
│   ├── routing.py           ✅ Fourni
│   └── migrations/
│
├── 📂 templates/             ✅ Fourni (complet)
│   ├── base.html
│   ├── home.html
│   └── play_game.html
	└── online_players.html

```
