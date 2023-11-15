# Conda
---

## Entorno
---

### Crear Entorno
```sh
conda create --name <name>
```

#### Especificando la versión de python
```sh
conda create --name <name> python=x.x
```

### Activar entorno
```sh
conda activate <name>
```

### Desactivar entorno
```sh
conda deactivate
```

### Información del entorno virtual
```sh
conda info
```
### Lista de los entornos
```sh
conda info --envs
```

### Instalar paquetes
```sh
conda install <package>
```

### Eliminar ambiente virtual
```sh
conda remove --name <name> --all
```

### Exporta el anviente
```sh
1. conda env export
2. conda env export --no-builds
3. conda env export --from-history --> Está es la más aconsejable|solo muestra lo instalado y no los paquetes base
4. 
```
Exportar en un archivo
```sh
conda env export --from-history --file <name_file>.yml
```

### Importar el entorno 
Normalmente el archivo tiene que ser tipo yml
```sh
conda env create --file <name_file>.yml
```

### Ejecutar Jupyter
```sh
jupyter-notebook
```

### Listar todos los paquetes que están instalados
```sh
conda list
```

### Eliminar paquetes
```sh
conda remove <library>
```
### Verifica las revisiones, esto son las versiones de los paquetes instalados
```sh
conda list --revision
```

Las versiones son cambios que se producen cuando se instala o desinstala un paquete, se puede retornar a las versiones anteriores
```sh
conda install --revision <numero de la version>
```

# Mamba
Permite realizar funciones de conda más rapido, como instalar o crear entornos de manera muy rapida.
### Install
```sh
conda install --channel conda-forge mamba
```
