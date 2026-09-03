+++
title = "stuff ?"

[extra]
nav_title = "stuff ?"
+++

# My Stuff

## minecraft guys

`click to visit their page and learn more (maybe)`

<style>
.content {
    .guys {
        display: flex;
        width: 100%;
        flex-wrap: wrap;
    }

    .container {
        width: 200px;
        height: 200px;

        .camera {
            transition: --cam-yaw 0.1s;
        }

        display: flow-start;
    }

    .container:hover .camera {
        --cam-yaw: 45 !important;
    }
}
</style>

<div class="guys">
<a href="/squid/">
{{ <rendering path="/squid/model.divs" projection={100} yaw={-135} pitch={16} y={100} z={500} /> }}
</a>
<a href="/fox/">
{{ <rendering path="/fox/model.divs" projection={100} yaw={-135} y={250} pitch={16} z={500} /> }}
</a>
<a href="/horse/">
{{ <rendering path="/horse/model.divs" projection={100} yaw={-135} y={250} pitch={16} z={500} /> }}
</a>
<a href="/skeleton-horse/">

{{ <rendering path="/skeleton-horse/model.divs" projection={100} yaw={-135} y={250} pitch={16} z={500} /> }}

</a>
<a href="/salmon/">
{{ <rendering path="/salmon/model.divs" projection={100} yaw={-135} y={250} pitch={16} z={500} /> }}
</a>
<a href="/borzoi/">
{{ <rendering path="/borzoi/model.divs" projection={100} yaw={-135} y={250} pitch={16} z={500} /> }}
</a>
</div>

## the octogon

<style>
.rotatable {
    animation-name: rotate;
    animation-duration: 4s;
    animation-iteration-count: infinite;
    animation-timing-function: linear;
    animation-play-state: paused;
}

.rotatable:hover {
    animation-play-state: running;
}

@keyframes rotate {
0% {
    transform: rotate(0);
}
100% {
    transform: rotate(360deg);
}
}
</style>
<img class="rotatable" src="the-octogon.png" alt="a octagonal cat" />