# Mejoras implementadas

He implementado varias mejoras, ahora en el `README.md` solo se queda el ultimo estado de los test, mientras que el historial de test anteriores realizados estan en el `report.md`. En este historial cada línea sale con su fecha y hora aparte de que en el inicio hay un contador con cuantos test se han realizado y cuantos de ellos han fallado y cuantos han pasado correctamente.

Para implementar estas mejores he creado dos funciones, una para escribir el `report.md`  que es `update_reportmd()` que hace un funcionamiento parecido al `update_readmemd()` solo que este en vez de sustituir la ultima linea por una nueva lo que hace es añadir al final el nuevo test. Aparte de que al principio se utiliza la otra función que he creado que es `leerhistorial()`, que su funcion es leer el historial que hay en el `report.md` contando por cada linea si a fallado el test o ha pasado el test, esta devuelve el conteo de todos y aparte de los correctos y los fallados.

# Workflow

He configurado un workflow que se llama `CI con AutoCommit` que automatiza la ejecución de test y actualiza los archivos `README.md` y `report.md` cada vez que se hace un push a la rama `main`.

Primero el workflow le da permiso de escritura a Github para que pueda realizar commits automáticos. Despues se descarga el repositorio, se configura python y se instala la líbreria `pytest`. Luego se ejecuta el script de python `update_readme.py` que ejecuta los test y actualiza los archivos. Y por ultimo con `stefanzweifel/git-auto-commit-action@v5` hace un commit con los cambios en los archivos, y el nombre del commit.