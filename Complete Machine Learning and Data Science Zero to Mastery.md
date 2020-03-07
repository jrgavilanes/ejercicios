# Complete Machine Learning and Data Science: Zero to Mastery
https://www.udemy.com/course/complete-machine-learning-and-data-science-zero-to-mastery/


## Install miniconda

Descarga en instala en Linux
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```

Crea entorno e instala paquetes
```
$ conda create --prefix ./env pandas numpy matplotlib scikit-learn
```

Añade paquete
```
$ conda install jupyter
```

Ver entornos existentes
```
conda env list
# conda environments:
#
                         /home/janrax/Escritorio/miniconda/env
base                  *  /home/janrax/miniconda3

```

Activar entorno
```
$ conda activate /home/janrax/Escritorio/miniconda/env
```

Desactivar entorno
```
$ conda deactivate
```

Activar Jupyter Notebook
```
$ jupyter notebook
```

Exportar entono a fichero
```
$ conda env export --prefix /home/janrax/Escritorio/miniconda/env > environment.yml
```

Importar entorno desde fichero
```
$ conda env create --file environment.yml --name env_desde_fichero
```

Borrar entorno
```
$ conda remove --name myenv --all
```




