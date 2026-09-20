+++
title = "about"
description = "about the dog/horse"
+++
<main id="about">


# HELLO, I AM HORSE

my name is _flowbish_ and I am speaking to you through the medium of ~hypertext~. i am a _borzoi_, a russian breed of _sight hound_ with beautiful, flowing fur. i also like _horses_ because they're basically the same thing :3

![minecraft horse](/minecraft-horse.gif)

![minecraft pig](/minecraft-pig.gif)

{% <rendering class="inline"> %}
{{ load_data(path="models/borzoi.divs") }}
{% </rendering> %}

check out my [blog](/blog) where I write about stuff that I've done or where I've been

look at my [character references](/refs) to see my little animals. they're cool and cute and I have a lot of art of them!

{% <rendering class="inline"> %}
{{ load_data(path="models/salmon.divs") }}
{% </rendering> %}

{% <rendering class="inline"> %}
{{ load_data(path="models/skeleton-horse.divs") }}
{% </rendering> %}

look at my [cat](/photos/honey-crisp) and my [itemlabel plushies](/photos/item-label) and my cool [minecraft photos](/photos/minecraft)

ponder my [stuff](/stuff) including some 3d models rendered using only html and css!!! just like the horse that's rotating here, wow

## my hobbies

_knitting_

_sewing_

~brazilian jiu-jitsu~

_cooking_ 

_making this website I guess lol_

> but that's not all :3

{% <rendering id="about-horse"> %}
{{ load_data(path="models/horse.divs") }}
{% </rendering> %}

thanks for all your hard work, little guy

</main>

<style>
.container.inline {
    display: inline;
    width: 40%;

    .camera {
        --cam-z: 400;
        --cam-pitch: 35;
        animation: spin 5s linear infinite;
    }
}

@keyframes spin {
    from {
        --cam-yaw: 0;
    }

    to {
        --cam-yaw: 360;
    }
}
#about-horse {
    position: sticky;
    inset: 0;
    width: 100%;
    height: 100cqh;


    mix-blend-mode: darken; 
    pointer-events: none;
    
    .camera {
        --cam-y: 260;
        --cam-z: 500;
        --cam-pitch: 15;

        animation: spin 3s linear infinite;
    }
}
</style>