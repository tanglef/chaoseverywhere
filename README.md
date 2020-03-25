![Python package](https://github.com/tanglef/chaoseverywhere/workflows/Python%20package/badge.svg?branch=master)

## Overview

```diff
This module deals with the links between the Mandlebrot set and the logistic map. 
Several animations are implemented in order to fully get what are the objects manipulated.
```

## Structure
```diff
In script.py, you can find a short demonstration.

The report folder contains a jupyter notebook to display different elements like images of the fractals
and bifurcation diagram and lets you manipulate the objects with some interactions.

A beamer presentation will be stored in the beamer folder and a documentation will be made using the
sphinx package.

Tests functions are implemented in the Tests folder in order to assure good development of this package.

Hook actions were also installed in the github/workflows and trigger an action everyday at 5 am and at each push.

Every bit of the main code is in the chaoseverywherefolder. Animations are in the Animations folder
which is created on the fly. It also stores saved images.

Currently, we mainly work in the sketch folder that won't be present at the end of this project. 
```

## Install
```diff
Aside from python packages, ffmpeg as a software, should be installed on the computer and be allowed 
the write/read/execute access.
```
