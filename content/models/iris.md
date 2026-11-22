+++
title = "Iris"
description = "Look at this fops spin around in three dimensions. Isn't that dandy?"
+++

<div>
<a id="part-1"></a>
<a id="part-2"></a>

{% <rendering id="page" z={1000} y={300} animate={false}> %}

<!-- side 1 -->
<div class="rect opaque" style="
    --a-x: -300;
    --a-y: -200;
    --a-z: 0;
    --b-x: 300;
    --b-y: -200;
    --b-z: 0;
    --c-x: -300;
    --c-y: 1000;
    --c-z: 0;
">

This is [Iris](https://ink.horse/refs/iris), wow so cool! Look at the fops spin in three dimensions. Isn't that dandy?

<a href="#part-2">next</a>

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
    --a-z: 0;
    --b-x: -300;
    --b-y: -200;
    --b-z: 0;
    --c-x: 300;
    --c-y: 1000;
    --c-z: 0;
">

welcome to side two!

{% <rendering id="iris2" z={200} y={300} animate={true}> %}
{{ load_data(path="/models/iris.divs") }}
{% </rendering> %}

that's crazy, it's iris again!

<a href="#part-1">go back</a>

</div>

{% </rendering> %}

</div>

<style>
#page {
    height: 100cqmin;
}

@keyframes rotate-to-part-2 {
    from {
        --cam-yaw: 0;
    }
    to {
        --cam-yaw: 180;
    }
}

@keyframes zoom-out-in-part-1 {
    0%, 100% {
        --cam-z: 1000;
    }
    50% {
        --cam-z: 2000;
    }
}

@keyframes rotate-to-part-1 {
    from {
        --cam-yaw: 180;
    }
    to {
        --cam-yaw: 0;
    }
}

@keyframes roll-to-part-1 {
    from {
        --cam-roll: 0;
    }
    to {
        --cam-roll: 360;
    }
}


#part-2:target ~ #page {
    & > .camera-projection > .camera-roll > .camera-pitch > .camera-yaw {
        animation: rotate-to-part-2 3s forwards ease-in-out;
    }
}

#part-1:target ~ #page {
    & > .camera-projection {
        animation: zoom-out-in-part-1 3s forwards ease-in-out;
    }

    & > .camera-projection > .camera-roll {
        animation: roll-to-part-1 3s forwards ease-in-out;
    }

    & > .camera-projection > .camera-roll > .camera-pitch > .camera-yaw {
        animation: rotate-to-part-1 3s forwards ease-in-out;
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