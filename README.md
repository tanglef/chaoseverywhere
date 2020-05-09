<p align="center">
  <strong> CHAOSEVERYWHERE </strong> <br>
<img src="./doc/_static/logo1_f.svg" style="vertical-align:middle" width="500" height='200' class='center' alt='logo'>
</p>

![Python package](https://github.com/tanglef/chaoseverywhere/workflows/Python%20package/badge.svg?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/54f7902ce179418982696c32613b98e7)](https://app.codacy.com/manual/tanglef/chaoseverywhere?utm_source=github.com&utm_medium=referral&utm_content=tanglef/chaoseverywhere&utm_campaign=Badge_Grade_Dashboard)
[![Documentation Status](https://readthedocs.org/projects/chaoseverywhere/badge/?version=latest)](https://chaoseverywhere.readthedocs.io/en/latest/?badge=latest)

## Overview

This module deals with the links between the Mandlebrot set and the logistic map.
Several animations are implemented in order to fully get what the objects manipulated are.

## Install

Aside from python packages in the requirements.txt file in the source directory, ffmpeg as a software, should be installed on the computer and be allowed the write/read/execute access. In order to install this package, one must run in its command prompt the following line.

```{bash}
$ pip install git+https://github.com/tanglef/chaoseverywhere
```

For those who whish to run the report, additional packages are need, they are listed in the `requirements_report.txt` file in the `.\report` directory and are only an additional layer, the main `requirements.txt` file is mandatory.

## Documentation

The documentation of this package is available [here](https://chaoseverywhere.readthedocs.io/en/latest/). You can find a gallery to learn using this package with examples. The code of these examples is located in the `.\examples` directory. One may run the `plot_mandelbrot_bw.py` file to verify the installation.

## Structure

The `.\report` folder contains a jupyter notebook to display different elements like images of the fractals
and the bifurcation diagram and lets you manipulate the objects with some interactions.

A beamer presentation will be stored in the `.\beamer` folder alongside the necessay style file to run the file and a documentation will be made using the sphinx package in the `.\doc` directory.

*Tests functions* are implemented in the `.\chaoseverywhere\tests` folder in order to assure the good development of this package. We also used a continuous integration hook action disposed in the `./github/workflows` folder which triggers an action everyday at `5`a.m and at each push.

Every bit of the main code is in the `.\chaoseverywhere` folder.
