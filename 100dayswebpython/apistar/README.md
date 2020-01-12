Instalar VENV
```bash
$ apt-get install python3-venv
```

Crear Entorno Virtual
```bash
cd /myApp
$ python3 -m venv venv
```

Activar Entorno Virtual
```bash 
$ source venv/bin/activate
```

Instalar dependencias
```bash
$ pip install -r requirements.txt
```

Congelar dependencias
```bash
$ pip freeze > requirements.lock
```


Ejemplo Python Debugger
```python
import pdb
pdb.set_trace()
coches = ['uno', 'dos', 'tres']
```

Ejecuta tests
```bash
$ pytest -v

```
