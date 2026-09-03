+++
title = "polaroid"
description = "this is a minecraft-style polaroid?"

[extra]
hide_reading_time = true
+++

the divs for this model were generated with triangles instead of rectangles so it has 2x the number of divs as it really should. for some reason though, the model generated from blockbench doesn't have the same rectangle adjacent-triangle ordering as the minecraft models, so it doesn't produce rectangles cleanly. this is something to fix with [gltf-to-divs](https://github.com/flowbish/gltf-to-divs/).

this causes occasional screen tearing, probably from too many divs.

<div style="background-color: red">
{{ <rendering path="content/polaroid/model.divs" y={400} animate={true} /> }}
</div>