# Curso-Basico-Pythoin
Script de practicas de curso de Python

Proyecto que se ejecuta siguiendo el curso del canal de Youtube
EL PROFESOR IMPEDANTE en el curso de "Curso de Python de cero a experto"

https://www.youtube.com/watch?v=aiubGNWw-JU&list=PLadPjjC02xXGwhDQVmTV5_rj23NBPd-L5


Pasos para subir un repositoria a github desde git bash por primera vez
1.	git init
2.	git status (opcional)
3.	git add .
4.	git commit  -m  “cual es el cambio” (si no esta autenticado seguir los literales a-c)
a.	git config –global user.email marioalexis.2007@gmail.com
b.	git config –global user.name mariomunoz82
c.	git commit -m “cual es el cambio”
5.	git branch  -M main
6.	git remote add origin https://github.com/mariomunoz82/Curso-Basico-Pythoin.git (laruta es la ruta del nuevo repositorio)
7.	git push -u origin main
Pasos para guardar un cambio al repositorio
1.	git status (para ver los cambios a guardar)
2.	git add .
3.	git commit -m “Cambios a guardad”
4.	git push -u origin main


Para corregir error : fatal: detected dubious ownership in repository at 'E:/Curso de R y Python/Curso de Python/Hola'
•	git config --global --add safe.directory '*'
Para corregir error: failed to push some refs to 'https://github.com/mariomunoz82/Curso-Basico-Pythoin'
•	git pull --rebase origin master
Para corregir error: interactive rebase in progress; onto 0a34601
•	git rebase --continue
