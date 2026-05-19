+++
title = "rendering in pure css (part 2)"
date = "2026-05-14"
description = "let's render geometry in pure css: part 2: transforming in three dimensions"

[extra]
hidden = true
+++

# Demo 1

{% rendering_part_2() %}
<div class="rect" style="
--a-x: -100;
--a-y: -100;
--a-z: 100;
--b-x: 100;
--b-y: -100;
--b-z: 100;
--c-x: -100;
--c-y: 100;
--c-z: 100;
--texture-image: url(/texture.jpg);
--texture-a-s: 0.25;
--texture-a-t: 0.25;
--texture-b-s: 0.75;
--texture-b-t: 0.25;
--texture-c-s: 0.25;
--texture-c-t: 0.75;
">
</div>
<div class="rect" style="
--a-x: 100;
--a-y: -100;
--a-z: 100;
--b-x: 100;
--b-y: -100;
--b-z: -100;
--c-x: 100;
--c-y: 100;
--c-z: 100;
--texture-image: url(/texture.jpg);
--texture-a-s: 0.75;
--texture-a-t: 0.25;
--texture-b-s: 1;
--texture-b-t: 0.25;
--texture-c-s: 0.75;
--texture-c-t: 0.75;
">
</div>        
<div class="rect" style="
--a-x: -100;
--a-y: -100;
--a-z: -100;
--b-x: 100;
--b-y: -100;
--b-z: -100;
--c-x: -100;
--c-y: -100;
--c-z: 100;
--texture-image: url(/texture.jpg);
--texture-a-s: 0.25;
--texture-a-t: 0;
--texture-b-s: 0.75;
--texture-b-t: 0;
--texture-c-s: 0.25;
--texture-c-t: 0.25;
">
</div>
<div class="rect" style="
--a-x: 100;
--a-y: -100;
--a-z: -100;
--b-x: -100;
--b-y: -100;
--b-z: -100;
--c-x: 100;
--c-y: 100;
--c-z: -100;
--texture-image: url(/texture.jpg);
--texture-a-s: 0.75;
--texture-a-t: 0.75;
--texture-b-s: 0.25;
--texture-b-t: 0.75;
--texture-c-s: 0.75;
--texture-c-t: 0.25;
"></div>
<div class="rect" style="
--a-x: -100;
--a-y: -100;
--a-z: -100;
--b-x: -100;
--b-y: -100;
--b-z: 100;
--c-x: -100;
--c-y: 100;
--c-z: -100;
--texture-image: url(/texture.jpg);
--texture-a-s: 0;
--texture-a-t: 0.25;
--texture-b-s: 0.25;
--texture-b-t: 0.25;
--texture-c-s: 0;
--texture-c-t: 0.75;
"></div>
<div class="rect" style="
--a-x: -100;
--a-y: 100;
--a-z: 100;
--b-x: 100;
--b-y: 100;
--b-z: 100;
--c-x: -100;
--c-y: 100;
--c-z: -100;
--texture-image: url(/texture.jpg);
--texture-a-s: 0.25;
--texture-a-t: 0.75;
--texture-b-s: 0.75;
--texture-b-t: 0.75;
--texture-c-s: 0.25;
--texture-c-t: 1;
"></div>
{% end %}

# Demo 2
a
{% rendering_part_2() %}    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 0;
  --b-y: 100;
  --b-z: 0;
  --c-x: -38;
  --c-y: 92;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.5;
  --texture-b-t: 1.0;
  --texture-c-s: 0.3086582838174551;
  --texture-c-t: 0.9619397662556434;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -38;
  --b-y: 92;
  --b-z: 0;
  --c-x: -71;
  --c-y: 71;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.3086582838174551;
  --texture-b-t: 0.9619397662556434;
  --texture-c-s: 0.14644660940672627;
  --texture-c-t: 0.8535533905932737;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -71;
  --b-y: 71;
  --b-z: 0;
  --c-x: -92;
  --c-y: 38;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.14644660940672627;
  --texture-b-t: 0.8535533905932737;
  --texture-c-s: 0.03806023374435663;
  --texture-c-t: 0.6913417161825449;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -92;
  --b-y: 38;
  --b-z: 0;
  --c-x: -100;
  --c-y: 0;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.03806023374435663;
  --texture-b-t: 0.6913417161825449;
  --texture-c-s: 0.0;
  --texture-c-t: 0.5;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -100;
  --b-y: 0;
  --b-z: 0;
  --c-x: -92;
  --c-y: -38;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.0;
  --texture-b-t: 0.5;
  --texture-c-s: 0.03806023374435663;
  --texture-c-t: 0.30865828381745514;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -92;
  --b-y: -38;
  --b-z: 0;
  --c-x: -71;
  --c-y: -71;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.03806023374435663;
  --texture-b-t: 0.30865828381745514;
  --texture-c-s: 0.1464466094067262;
  --texture-c-t: 0.14644660940672627;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -71;
  --b-y: -71;
  --b-z: 0;
  --c-x: -38;
  --c-y: -92;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.1464466094067262;
  --texture-b-t: 0.14644660940672627;
  --texture-c-s: 0.3086582838174551;
  --texture-c-t: 0.03806023374435663;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: -38;
  --b-y: -92;
  --b-z: 0;
  --c-x: 0;
  --c-y: -100;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.3086582838174551;
  --texture-b-t: 0.03806023374435663;
  --texture-c-s: 0.49999999999999994;
  --texture-c-t: 0.0;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 0;
  --b-y: -100;
  --b-z: 0;
  --c-x: 38;
  --c-y: -92;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.49999999999999994;
  --texture-b-t: 0.0;
  --texture-c-s: 0.6913417161825448;
  --texture-c-t: 0.038060233744356575;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 38;
  --b-y: -92;
  --b-z: 0;
  --c-x: 71;
  --c-y: -71;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.6913417161825448;
  --texture-b-t: 0.038060233744356575;
  --texture-c-s: 0.8535533905932737;
  --texture-c-t: 0.14644660940672616;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 71;
  --b-y: -71;
  --b-z: 0;
  --c-x: 92;
  --c-y: -38;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.8535533905932737;
  --texture-b-t: 0.14644660940672616;
  --texture-c-s: 0.9619397662556433;
  --texture-c-t: 0.30865828381745486;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 92;
  --b-y: -38;
  --b-z: 0;
  --c-x: 100;
  --c-y: 0;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.9619397662556433;
  --texture-b-t: 0.30865828381745486;
  --texture-c-s: 1.0;
  --texture-c-t: 0.4999999999999999;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 100;
  --b-y: 0;
  --b-z: 0;
  --c-x: 92;
  --c-y: 38;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 1.0;
  --texture-b-t: 0.4999999999999999;
  --texture-c-s: 0.9619397662556433;
  --texture-c-t: 0.691341716182545;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 92;
  --b-y: 38;
  --b-z: 0;
  --c-x: 71;
  --c-y: 71;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.9619397662556433;
  --texture-b-t: 0.691341716182545;
  --texture-c-s: 0.8535533905932738;
  --texture-c-t: 0.8535533905932737;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 71;
  --b-y: 71;
  --b-z: 0;
  --c-x: 38;
  --c-y: 92;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.8535533905932738;
  --texture-b-t: 0.8535533905932737;
  --texture-c-s: 0.6913417161825453;
  --texture-c-t: 0.9619397662556433;
"></div>
    

<div class="tri" style="
  --a-x: 0;
  --a-y: 0;
  --a-z: 0;
  --b-x: 38;
  --b-y: 92;
  --b-z: 0;
  --c-x: 0;
  --c-y: 100;
  --c-z: 0;
  --texture-image: url(/texture.jpg);
  --texture-a-s: 0.5;
  --texture-a-t: 0.5;
  --texture-b-s: 0.6913417161825453;
  --texture-b-t: 0.9619397662556433;
  --texture-c-s: 0.5000000000000001;
  --texture-c-t: 1.0;
"></div>

{% end %}