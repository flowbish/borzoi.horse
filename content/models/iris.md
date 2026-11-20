+++
title = "Iris"
description = "Look at this fops spin around in three dimensions. Isn't that dandy?"
+++

This is [Iris](https://ink.horse/refs/iris), wow so cool! Look at the fops spin in three dimensions. Isn't that dandy?

<div id="iriscontainer">
{% <rendering id="iris" z={200} y={300} animate={true}> %}
{{ load_data(path="/models/iris.divs") }}
{% </rendering> %}
</div>

<style>
#iriscontainer {
  width: 100%;
  height: 50%;
  position: absolute;
  animation: bounce linear 17s infinite alternate;
  #iris {
    width: 400px;
    animation: toRight linear 6.8s infinite alternate;
  }
}

@keyframes bounce {
  0% {
    transform: translateY(-100%);
  }
  48% {
  }
  50% {
    transform: translateY(100%);
  }
  52% {
  }
  100% {
    transform: translateY(-100%);
  }
}

@keyframes toRight {

  0% {
    transform: translateX(-100%);

  }

  100% {
    transform: translateX(100%);
  }
}
</style>

<div class="theme-selector">
    <p>Also this looks better with the dark themes:</p>
    <button onclick="set_theme('nether')"><img src="/minecraft-netherrack.jpg" alt="select netherrack theme"></button>
    <button onclick="set_theme('sculk')"><img src="/minecraft-sculk.jpg" alt="select sculk theme"></button>
</div>

Find the model [here](/iris.glb). It was made by [mega-KOT](https://mega-kot.newgrounds.com/). Maybe I'll add shading to this whole thing later. Don't forget to like and subscribe!!
