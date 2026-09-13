+++
title = "Borzoi Looking Demo"

[extra]
hide_comments = true
+++

<div class="inner">
{% for i in range(end=21) %}
{% for j in range(end=21) %}
<div id="box-{{ i }}-{{ j }}"></div>
{% endfor %}
{% endfor %}
{{ <rendering path="content/borzoi/model.divs" y={400} projection={3} /> }}
</div>

<style>
.inner {
    position: relative;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr 1fr;
    height: 500px;

    .container {
        position: absolute;
        height: 800px;
        left: 0;
        top: 0;

        pointer-events: none;

        .camera-yaw {
            --cam-yaw: 180;
        }
    }
}

{% for i in range(end=21) %}
{% for j in range(end=21) %}
#box-{{ i }}-{{ j }} {
    // background-color: rgb(calc(25 * {{ i }}), calc(25 * {{ j }}), 256);
}

#box-{{ i }}-{{ j }}:hover ~ .container {
    .camera-pitch {
        --cam-pitch: calc(-3 * 11 + 3 * {{ i }});
    }

    .camera-yaw {
        --cam-yaw: calc(180 + 3 * 11 - 3* {{ j }});
    }
}
{% endfor %}
{% endfor %}
</style>