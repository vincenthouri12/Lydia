# API Automation

## Installer les dependences necessaire

```bash
pytest
request
allure
```

## Lancer les tests avec pytest

```bash
pytest --alluredir=allure-results
```
### Exécute le scénario de requetes API reqres.
### Les étapes sont implémentées en Python.

## Lancer le serveur pour la doc

```bash
allure serve allure-results
```