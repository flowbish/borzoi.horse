+++
title = "Iris"
description = "Look at this fops spin around in three dimensions. Isn't that dandy?"
+++

{% <rendering id="page" z={1200} y={300} animate={false}> %}

<!-- side 1 -->
<div class="rect opaque" style="
    --a-x: -300;
    --a-y: -200;
    --a-z: 300;
    --b-x: 300;
    --b-y: -200;
    --b-z: 300;
    --c-x: -300;
    --c-y: 1000;
    --c-z: 300;
">

This is [Iris](https://ink.horse/refs/iris), wow so cool! Look at the fops spin in three dimensions. Isn't that dandy?

<a href="#page">next</a>

{% <rendering id="iris" z={200} y={300} animate={true}> %}
{{ load_data(path="/models/iris.divs") }}
{% </rendering> %}

<div class="theme-selector">
    <p>Also this looks better with the dark themes:</p>
    <button onclick="set_theme('nether')"><img src="/minecraft-netherrack.jpg" alt="select netherrack theme"></button>
    <button onclick="set_theme('sculk')"><img src="/minecraft-sculk.jpg" alt="select sculk theme"></button>
</div>

Find the model [here](/iris.glb). It was made by [mega-KOT](https://mega-kot.newgrounds.com/). Maybe I'll add shading to this whole thing later. Don't forget to like and subscribe!!

</div>

<!-- side 1 -->
<div class="rect opaque" style="
    --a-x: 300;
    --a-y: -200;
    --a-z: 300;
    --b-x: 300;
    --b-y: -200;
    --b-z: -300;
    --c-x: 300;
    --c-y: 1000;
    --c-z: 300;
">

welcome to side two!

{% <rendering id="iris2" z={200} y={300} animate={true}> %}
{{ load_data(path="/models/iris.divs") }}
{% </rendering> %}

that's crazy, it's iris again!

<a href="#unpage">go back</a>

</div>

{% </rendering> %}

<style>
#page {
    height: 100cqmin;
}

@keyframes rotate-to-part-2 {
    from {
        --cam-yaw: 0;
    }
    to {
        --cam-yaw: 90;
    }
}

#page:target {
    & > .camera-projection > .camera-roll > .camera-pitch > .camera-yaw {
        animation: rotate-to-part-2 3s forwards ease-in-out;
        --cam-yaw: 90;
    }
}

#iris, #iris2 {
    height: 300px;
    filter:
        drop-shadow(1px 1px black)
        drop-shadow(1px -1px black)
        drop-shadow(-1px 1px black)
        drop-shadow(-1px -1px black);
}

#iris2 {
    filter: invert(1.0)
        drop-shadow(1px 1px black)
        drop-shadow(1px -1px black)
        drop-shadow(-1px 1px black)
        drop-shadow(-1px -1px black);

}
</style>