+++
title = "zoetrope demo"
+++

{% set frames = 6 %}
{% set open_percent = 0.1 %}
{% set animation_time_seconds = 6.0 %}

<div zoetrope>
{% <rendering> %}
{% for i in range(end=frames) %}
{{ load_data(path="models/horse.divs") }}
{% endfor %}
<div class="node ground" style="
    transform:
        translate3d(
        calc(1cqw + var(--node-translate-x)),
        calc(-1cqw + var(--node-translate-y)),
        calc(1cqw + var(--node-translate-z))
        )
        rotate3d(0, -0, 0, calc(-2 * acos(1)))
        rotate3d(var(--node-rotation-x), var(--node-rotation-y), var(--node-rotation-z), var(--node-rotation-angle))
        scale3d(calc(1 * var(--node-scale)), calc(1 * var(--node-scale)), calc(1 * var(--node-scale)));
    ">
    <div class="node ground-inner" style="
    transform:
        translate3d(
        calc(1cqw + var(--node-translate-x)),
        calc(-1cqw + var(--node-translate-y)),
        calc(1cqw + var(--node-translate-z))
        )
        rotate3d(0, -0, 0, calc(-2 * acos(1)))
        rotate3d(var(--node-rotation-x), var(--node-rotation-y), var(--node-rotation-z), var(--node-rotation-angle))
        scale3d(calc(1 * var(--node-scale)), calc(1 * var(--node-scale)), calc(1 * var(--node-scale)));
    ">
    <div class="rect" style="
        --a-x: -100;
        --a-y: -100;
        --a-z: 0;
        --b-x: 100;
        --b-y: -100;
        --b-z: 0;
        --c-x: -100;
        --c-y: 100;
        --c-z: 0;
        ">
    </div>
    </div>
</div>
{% </rendering> %}
</div>

<style>
@keyframes ground-spin {
    0% {
        --node-rotation-angle: 0deg;
    }
    100% {
        --node-rotation-angle: 360deg;
    }
}

@keyframes head_bob {
    0%, 50%, 100% {
        --node-rotation-angle: 0deg;
    }

    25%, 75% {
        --node-rotation-angle: 25deg;
    }
}

@keyframes legs_move {
    0%, 50%, 100% {
        --node-rotation-angle: -35deg;
    }

    25%, 75% {
        --node-rotation-angle: 35deg;
    }
}

@keyframes body_bounce {
    0%, 100% {
        --node-translate-y: -10px;
    }

    50% {
        --node-translate-y: 10px;
    }
}

div[zoetrope] {
    .camera {
        --cam-z: 1200;
        --cam-pitch: 15;
        --cam-projection: 0.8;
    }

    {% for i in range(end=frames) %}
    {% set animation_delay = animation_time_seconds / frames * i %}
    .node.base:nth-of-type({{ i + 1 }}) {
        --node-rotation-y: 1;
        --node-rotation-angle: {{ (360.0 * i / frames) }}deg;
        
        animation: body_bounce steps({{ frames }}, jump-end) infinite {{ animation_time_seconds }}s -{{ animation_delay }}s;

        & > .node {
            --node-rotation-y: 1;
            --node-rotation-angle: 90deg;
            --node-translate-z: 300px;
            --node-translate-x: 80px;
        }

        .node.Body > .node.Neck {
            --node-rotation-x: 1;
            animation: head_bob steps({{ frames }}, jump-end) infinite {{ animation_time_seconds }}s -{{ animation_delay }}s;
        }

        .node.Body > .node.LegFR, .node.Body > .node.LegBL {
            --node-rotation-x: 1;
            animation: legs_move steps({{ frames }}, jump-end) infinite {{ animation_time_seconds }}s -{{ animation_delay }}s;
        }

        .node.Body > .node.LegFL, .node.Body > .node.LegBR {
            --node-rotation-x: 1;
            animation: legs_move steps({{ frames }}, jump-end) infinite {{ animation_time_seconds }}s -{{ animation_delay + animation_time_seconds / 4 }}s;
        }
    }
    {% endfor %}

    .node.ground {
        --node-rotation-x: 1;
        --node-rotation-angle: 90deg;
        --node-scale: 5;
        --node-translate-y: 30px;

        .node.ground-inner {
            --node-rotation-z: 1;
            animation: ground-spin steps({{ frames * 2 }}, jump-end) infinite {{ animation_time_seconds }}s;
        }

        .rect {
            background-image: url("/minecraft-dirt.jpg");
            border-radius: 100px;
            background-clip: border-box;
        }
    }
}
</style>