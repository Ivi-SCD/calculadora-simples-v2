# GITFLOW

O projeto contém 3 branches (2 remotas e 1 local):

- main (Principal)
- develop
    - feature/calculadora

Os códigos utilizados foram o seguinte:

```bash
git init .
git clone https://github.com/Ivi-SCD/calculadora-simples-v2
git switch -c develop
git switch -c feature/calculadora
git add .
git commit -m "<mensagem do commit>"
git switch develop
git merge feature/calculadora
git tag -a v1.0 -m "<mensagem da tag>"
git push --set-upstream origin develop
```
