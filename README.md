# openBF-hub
Repository of vascular networks for [openBF](https://github.com/INSIGNEO/openBF).

## How to use models
All the different networks are in `models/` folder. In each folder, an archive containing the openBF configuration files is provided. Download the archive and run it with the [latest openBF release](https://github.com/INSIGNEO/openBF/releases).

## Models list
- [Circle of Willis](https://github.com/alemelis/openBF-hub/tree/master/models/alastruey2007modelling)

## Contribute
You are welcome to submit your own models developed with openBF. This can be done through a pull request for the `models/` directory. Your submission should consist of a folder containing openBF configurations files and a readme describing the network with relevant references and plots (inlet BC and results) of the obtained results. The main readme should be updated accordingly. Example files are provided in `models/template/`.

<!--
### openBF installation
- copia `openBF/` in `~/.julia/vX.X.X/`
- crea una cartella `BTypes/src/BTypes.src` e copiala in `~/.julia/vX.X.X/`
A questo punto `using openBF` funziona senza `push!`

- crea un alias in `~/.profile`
```bash
alias openBF='cp ~/.julia/v0.6/openBF/main.jl ./main.jl && julia main.jl $1'
```
e poi `source ~/.profile`
in questo modo le simulazioni dovrebbero partire con `openBF project_name`. -->
