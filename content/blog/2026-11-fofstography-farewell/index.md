+++
title = "Farewell to the Foftography 2025 Minecraft Server"
date = "2026-11-24"
description = "Here's are few pictures of this world before it goes away for good"

[extra]
icon = "cover.png"
+++

{% set manifest = "blog/2026-11-fofstography-farewell/gallery.toml" %}

This server was set up in the winter of 2025 by [Iris](https://ink.horse/refs/iris/). The idea was to have a server with the [Exposure](https://modrinth.com/mod/exposure) that adds cameras, film, development, and printing, and have regular photo contests with different themes. As things go, there were only ever a few photo contests, but this really kicked off a lot of things, such as the concept for this website and my real-life exploration into film photography.

{{ <gallery.embed manifest fragment="diamond-armor-horse" />}}

I was very much into Minecraft when I created this site, and this image was actually the first header on the site: the horse in diamond armor, clipped out from this picture, that would flip horizontally when you moused over it. Now instead I load 92KB of html on every page to display roughly the same thing.

{{ <embed.light src="/logo.png" description="the original logo" /> }}

This website was created originally to show off my [Minecraft photos](/photos/minecraft) and then kind of evolved from there, as a place to design and write and show my real photos too.

All of my recent film photography stuff such as [these photos of bridges](../2026-11-portland-bridges/) and [lomo purple](../2026-10-lomochrome-purple/) were directly inspired by this server and mod. I love being places, finding spots where the sun hits just right, where your subject is lit and the background feels right and there's interest and intrigue.

As for the Minecraft server, however, here are a few highlights:

{{ <gallery.embed manifest fragment="horse-house-warning" />}}

This is my horse house. It was a house, but I filled it with so many horses that it's actually quite dangerous inside, in that it is quite difficult to leave. It is quite a party in there though.

{{ <gallery.embed manifest fragment="burger" />}}

This is Stephen's definitely-not-five-guys burger shop. You could select the ingredients you wanted on the burger and it would build it for you. I set up a redstone clone inside the shop at some point so that it would make me infinite burgers, and I don't think I had to gather any new food since.

{{ <gallery.embed manifest fragment="spawn-house" />}}

As often happens, the spawn ended up on a pretty desolate beach island with nothing much to do. Most people ran off to somewhere cool to start mining and crafting, leaving only the most barebones house here for shelter.

And finally, some of the early photos I took on the server, in _the photo cube_:

<a href="/photos/minecraft">
{% <rendering id="photo-cube" y={200} animate={true}> %}
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
--texture-image: url({{ page.path }}/cube/side-1.png);
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
--texture-image: url({{ page.path }}/cube/side-2.png);
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
--texture-image: url({{ page.path }}/cube/side-3.png);
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
--texture-image: url({{ page.path }}/cube/side-4.png);
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
--texture-image: url({{ page.path }}/cube/side-5.png);
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
--texture-image: url({{ page.path }}/cube/side-6.png);
"></div>
{% </rendering> %}
</a>


See more in the gallery below!

## Gallery

{{ <gallery manifest /> }}