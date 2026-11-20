+++
title = "Iris"
description = "Look at this fops spin around in three dimensions. Isn't that dandy?"
+++

This is [Iris](https://ink.horse/), wow so cool! Look at the fops spin in three dimensions. Isn't that dandy?


{% <rendering id="iris" z={200} y={300} animate={true}> %}
{{ load_data(path="/models/iris.divs") }}
{% </rendering> %}

<div class="theme-selector">
    <p>Also this looks better with the dark themes:</p>
    <button onclick="set_theme('nether')"><img src="/minecraft-netherrack.jpg" alt="select netherrack theme"></button>
    <button onclick="set_theme('sculk')"><img src="/minecraft-sculk.jpg" alt="select sculk theme"></button>
</div>

Find the model [here](/iris.glb). Maybe I'll add shading to this whole thing later. Don't forget to like and subscribe!!
