+++
title = "Wisp"
description = "Look at this dragon spin around in three dimensions. Isn't that dandy?"
+++

This is [Wisp](https://www.reveriewisp.com/), wow so cool! Look at the dragon spin in three dimensions. Isn't that dandy?

{% <rendering id="wisp" z={1000} y={400} animate={true}> %}
{{ load_data(path="/models/wisp.divs") }}
{% </rendering> %}

<style>
#wisp {
    filter:
        drop-shadow(1px 1px black)
        drop-shadow(1px -1px black)
        drop-shadow(-1px 1px black)
        drop-shadow(-1px -1px black);
}
</style>

Find the model [here](/wisp.gltf). Maybe I'll add shading to this whole thing later. Don't forget to like and subscribe!!
