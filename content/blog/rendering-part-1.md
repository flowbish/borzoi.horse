+++
title = "rendering in pure css (part 1)"
date = "2026-05-14"
description = "more linear algebra than you ever thought possible"

[extra]
hidden = true
+++

as you can tell by my website, I like minecraft horses. and ever since reading about [DOOM rendered entirely with css](https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/), I have been fixated on the idea of rendering minecraft horses using just css. 

on the surface, it makes sense. one of the browser's main jobs is rendering content. often this content is declared by html and styled by css. for fancier things, javascript is used to draw more complicated geometry directly. but using html and css has a lot of desirable properties. they are declarative languages, so there is not really internal state that you have to think about. simply producing a piece of html styled by a piece of css will draw the same pixels to the screen, no matter how it was produced. also, working within the confines of html and css give you access to the rich suite of interaction that browsers already, meaning that you can do incredibly niche and cursed things with them, as you will hopefully see.

## how it works

to render a complex piece of geometry, we must render smaller polygons of that geometry, typically triangles. in practice, for this css rendering, this means creating a physical manifestation of that triangle, in my case the humble div, and manipulating the shit out of it with css transforms until it looks just about right. I had to re-learn a bunch of linear algebra for this (and a bunch of $\LaTeX$ to take notes) so y'all better LISTEN UP.

$$ \begin{align}
T_a &= \begin{bmatrix} 0 \\\\ 0 \\\\ 0 \end{bmatrix} \\\\
T_b &= \begin{bmatrix} |\overrightarrow{AB}| \\\\ 0 \\\\ 0 \end{bmatrix} \\\\
T_c &= \begin{bmatrix} 0 \\\\ |\overrightarrow{AC} - (\frac{\overrightarrow{AC} \cdot \overrightarrow{AB}}{|\overrightarrow{AB}|^2}) \overrightarrow{AB}| \\\\ 0 \end{bmatrix}
\end{align} $$

{{ rendering_part_1() }}