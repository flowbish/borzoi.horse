+++
title = "Iris"
description = "Look at this fops spin around in three dimensions. Isn't that dandy?"
+++

<div>

<div id="part-1" class="invisible" popover="manual"></div>
<div id="part-2" class="invisible" popover="manual"></div>
<div id="part-3" class="invisible" popover="manual"></div>

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

<button commandfor="part-2" command="toggle-popover">next</button>
<button commandfor="part-3" command="toggle-popover">side 3</button>

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

<!-- side 2 -->
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

<button commandfor="part-3" command="toggle-popover">side 3</button>
<button commandfor="part-1" command="toggle-popover">go back</button>

</div>

<!-- side 3 -->
<div class="rect opaque" style="
    --a-x: -300;
    --a-y: -1200;
    --a-z: 0;
    --b-x: 300;
    --b-y: -1200;
    --b-z: 0;
    --c-x: -300;
    --c-y: -400;
    --c-z: 0;
">

oh god a third side???

anyway, check out this funny soundcloud meme:

<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay; encrypted-media" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/soundcloud%253Atracks%253A267505379&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/lucy-bscale" title="BscalE" target="_blank" style="color: #cccccc; text-decoration: none;">BscalE</a> · <a href="https://soundcloud.com/lucy-bscale/rappers-endorse-japanese-cartoons" title="Rappers Endorse Japanese Cartoons (shaliek reupload)" target="_blank" style="color: #cccccc; text-decoration: none;">Rappers Endorse Japanese Cartoons (shaliek reupload)</a></div>

{% <rendering id="iris3" z={200} y={300} animate={true}> %}
{{ load_data(path="/models/iris.divs") }}
{% </rendering> %}

didn't even know that could happen

<button commandfor="part-3" command="toggle-popover">go back</button>

</div>


{% </rendering> %}

</div>

<style>
#page {
    height: 100cqmin;
}

#page .camera {
    transition: 
        --cam-yaw 3s ease-in-out,
        --cam-roll 3s ease-in-out,
        --cam-pitch 3s ease-in-out,
        --cam-y 3s ease-in-out;
}

#part-1:popover-open ~ #part-2:popover-open ~ #part-3:not(:popover-open) ~ #page,
#part-1:not(:popover-open) ~ #part-2:not(:popover-open) ~ #part-3:not(:popover-open) ~ #page {
    & > .camera-projection > .camera-roll > .camera-pitch > .camera-yaw {
        --cam-yaw: 0;
    }
}

#part-1:not(:popover-open) ~ #part-2:popover-open ~ #part-3:not(:popover-open) ~ #page, 
#part-1:popover-open ~ #part-2:not(:popover-open) ~ #part-3:not(:popover-open) ~ #page {
    & > .camera-projection > .camera-roll > .camera-pitch > .camera-yaw {
        --cam-yaw: 180;
    }
}

#part-3:popover-open ~ #page {
    & > .camera-projection {
        --cam-y: 1200;
    }

    & > .camera-projection > .camera-roll > .camera-pitch > .camera-yaw {
        --cam-yaw: 0;
    }
}

#iris, #iris2, #iris3 {
    height: 300px;
}

#iris {
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

#iris3 {
    filter: hue-rotate(90deg)
        drop-shadow(1px 1px black)
        drop-shadow(1px -1px black)
        drop-shadow(-1px 1px black)
        drop-shadow(-1px -1px black);
}

.invisible:popover-open {
    display: none !important;
}
</style>