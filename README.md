# openBF-hub
Repository of vascular networks for [openBF](https://github.com/INSIGNEO/openBF).

## Models list
- [Ascending aorta](https://github.com/alemelis/openBF-hub/tree/master/models/boilleau2015benchmark/aorta)
- [Common carotid](https://github.com/alemelis/openBF-hub/tree/master/models/boilleau2015benchmark/common_carotid)
- [Iliac bifurcation](https://github.com/alemelis/openBF-hub/tree/master/models/boilleau2015benchmark/iliac_bifurcation)
- Systemic circulation:
  <!-- - [ADAN56](https://github.com/alemelis/openBF-hub/tree/master/models/boilleau2015benchmark/adan56) -->
  - [In vitro model](https://github.com/alemelis/openBF-hub/tree/master/models/matthys2007pulse)
- [Circle of Willis](https://github.com/alemelis/openBF-hub/tree/master/models/alastruey2007modelling)

## How to use models
Clone this repository and run the [latest openBF release](https://github.com/INSIGNEO/openBF/releases) within the chosen model directory.

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
