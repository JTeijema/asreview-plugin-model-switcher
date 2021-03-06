# ASReview Model Switcher

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5084863.svg)](https://doi.org/10.5281/zenodo.5084863)

This repository contains a plugin for [ASReview](https://github.com/asreview) ![logo](https://raw.githubusercontent.com/asreview/asreview-artwork/e2e6e5ea58a22077b116b9c3d2a15bc3fea585c7/SVGicons/IconELAS/ELASeyes24px24px.svg "ASReview"). This plugin adds a model that switches between two models during runtime. It can be useful for when later stages of data classification require different models.

This plugin contains a base model and an implementation of a switching model. The current implemented switching model uses SVM and a convolutional neural network, and needs doc2vec or [wide doc2vec](https://github.com/JTeijema/asreview-plugin-wide-doc2vec/) as feature extractor. 

The point at which the classification model is set to 100 and is easily changed in the code. This setting is found in the `asreviewcontrib.models.config` module.


## Getting started

Run install the new classifier with:

```bash
pip install .
```
from the download folder or run the follow to install directly

```bash
python -m pip install git+https://github.com/JTeijema/asreview-plugin-model-switcher.git
```


## Usage

The new base switcher is defined in
[`asreviewcontrib/models/model_switcher.py`](asreviewcontrib/models/model_switcher.py).

The new classifier `svm_nn` is defined in
[`asreviewcontrib/models/svm_nn.py`](asreviewcontrib/models/svm_nn.py) 
and can be used in a simulation.

The models can be used like this:
```bash
asreview simulate benchmark:van_de_Schoot_2017 -m svm_nn -e doc2vec
```

### CNN
If the [CNN plugin](https://github.com/JTeijema/asreview-plugin-model-cnn-17-layer) is installed, it can be used in switching too, using the new classifier `svm_cnn`, defined in
[`asreviewcontrib/models/svm_cnn.py`](asreviewcontrib/models/svm_cnn.py).

The models can be used like this:
```bash
asreview simulate benchmark:van_de_Schoot_2017 -m svm_cnn -e doc2vec
```

### Switch point
Currently the switch point is set manually in model_switcher.py, named ``switchpoint``. It is set to switch after 100 iterations.

## License
Apache-2.0 License 
