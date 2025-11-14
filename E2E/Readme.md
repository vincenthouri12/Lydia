# Lydia App Automation

## Installer les requirement.txt

### Sur un virtual env (plus facile) ou sur son ordinateur local

## Lancer les tests avec Gherkin

```bash
behave features/wiki.feature
```
### Exécute les scénarios écrits en Gherkin dans le fichier wiki.feature.
### Les étapes sont implémentées en Python avec Appium.

## Lancer avec Appium et Python
```bash
python3 appium_config.py
```
### Lance le script Python standalone pour exécuter les tests sans Behave.
### Utile pour debug rapide ou tests isolés.

## Ouvrir le rapport

```bash
allure open reports/allure-report
```
### Permet de visualiser le rapport interactif avec l’historique des tests, captures d’écran et status Passed/Failed.
### Assurez-vous qu’Allure CLI est installé et dans le PATH.