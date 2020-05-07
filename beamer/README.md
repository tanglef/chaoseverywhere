# Guide for the beamer presentation

This presentation includes an animation made using the `animate` package. However, it is known that its using can be problematic. Please follow the instructions.

## Generate the animation

The `generate_animation_data.py` file will create a folder in the current directory (*ie* `./beamer`) in order to store the images produced. These images are a requirement to run the animation in the beamer.

So, please, run this file **before** compiling the beamer presentation.

:warning: This file calls the FFMPEG software, it must be installed and accesible in the command prompt as dicted in the installation section of the documentation. The following command must work:

```console
$ ffmpeg -version
```

if not, please refer to the installation section in the documentation of chaoseverywhere. :warning:

## Reader

In order to visualize this presentation, one can face multiple situations:

1. if you're using Windows, then we advise you to download Acrobat Reader,
2. if you're using Linux, please use a visualizer supported by the [animate package](http://ctan.unsw.edu.au/macros/latex/contrib/animate/animate.pdf).

## Fail-safe

If, for any reason, you are not able to either generate or use a pdf reader that is supported by the `animate` package, you can still compile and open the outputed pdf.

The only change you will notice, is that:

- if you aren't able to produce the images (*ie* run the Python file), a message indicating to click on a button will appear,
- if you aren't able to read the animation, you will still be able to click on the button by yourself.

This button is a fail-safe that leads to the Youtube video of the animation. You will be able to watch the animation, only not in the pdf.
