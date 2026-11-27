+++
title = "peepy"
description = "this is a peepy"

[extra]
hide_reading_time = true
icon = "image.png"
+++

{{ <rendering id="peepy" path="/models/peepy.divs" yaw={135} pitch={15} z={300} y={150} /> }}

{{ <rendering.controls id="peepy" z={400} />}}

use the controls above to rotate peepy. gaze at it with wonder.

## Update: Item Label has replied


{% <rendering id="itemlabel-reply" z={1600}> %}
<div class="node base">
    <div class="rect" style="
    --a-x: 0;
    --a-y: 0;
    --a-z: 0;
    --b-x: 1067;
    --b-y: 0;
    --b-z: 0;
    --c-x: 0;
    --c-y: 373;
    --c-z: 0;
    --texture-image: url({{ section.path }}/itemlabel-reply.png);
    ">
    </div>
</div>
{% </rendering> %}

<style>
#itemlabel-reply {
    .node {
        --node-translate-x: -530px;
        --node-translate-y: -150px;
    }
    .camera-yaw {
        animation: spinnies 20s -10s linear infinite;
    }
}
</style>