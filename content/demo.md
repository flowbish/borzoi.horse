+++
title = "Borzoi Looking Demo"

[extra]
hide_comments = true
+++

unfortunately the the grid I need to cover the screen to make the looking work interferes with clicking links. there's some cool javascript you can use to block specific pointer events but it's quite seamless enough to work for me, I think.

<div class="inner">
{% for i in range(end=11) %}
{% for j in range(end=11) %}
<div id="box-{{ i }}-{{ j }}"></div>
{% endfor %}
{% endfor %}
{{ <rendering path="/models/borzoi.divs" y={250} z={150} projection={1} /> }}
</div>

<style>
.inner {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;

    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;

    overflow: hidden;

    .container {
        position: absolute;
        width: 600px;
        height: 600px;
        right: -200px;
        bottom: 0px;

        pointer-events: none;

        .camera {
            transition: all 0.2s;
        }
    }

    .node.base {
        --node-translate-y: 200px;
        --node-translate-z: 100px;
    }
}

{% for i in range(end=11) %}
{% for j in range(end=11) %}
#box-{{ i }}-{{ j }} {
    opacity: 0;
    // background-color: rgb(calc(25 * {{ i }}), calc(25 * {{ j }}), 256);
}

#box-{{ i }}-{{ j }}:hover ~ .container {
    .camera-pitch {
        --cam-pitch: calc(12 * 6 - 6 * {{ i }});
    }

    .camera-yaw {
        --cam-yaw: calc(-90 + 9 * {{ j }});
    }
}
{% endfor %}
{% endfor %}
</style>