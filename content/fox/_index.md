+++
title = "minecraft fox"
description = "this is a minecraft fox"

[extra]
hide_reading_time = true

[extra.social_media_image]
path = "icon.png"
+++

{{ rendering(path="content/fox/model.divs") }}

<style>
.node.N\/A > .node.leg0, .node.N\/A > .node.leg3 {
    --node-rotation-x: 1;
    animation: walk 1s infinite ease-in-out;
}
.node.N\/A > .node.leg1, .node.N\/A > .node.leg2 {
    --node-rotation-x: 1;
    animation: walk 1s 0.5s infinite ease-in-out;
}

@keyframes walk {
    0%, 100% {
        --node-rotation-angle: 35deg;
    }

    50% {
        --node-rotation-angle: -35deg;
    }
}

.node.N\/A > .node.head {
    --node-rotation-x: 1;
    animation: head-bob 1s 0.25s infinite ease-in-out;
}

@keyframes head-bob {
    0%, 100% {
        --node-rotation-angle: 10deg;
    }

    50% {
        --node-rotation-angle: -10deg;
    }
}

.node.N\/A > .node.tail {
    --node-rotation-z: 1;
    animation: tail-swing 1s 0.25s infinite ease-in-out;
}

@keyframes tail-swing {
    0%, 100% {
        --node-rotation-angle: 10deg;
    }

    50% {
        --node-rotation-angle: -10deg;
    }
}
</style>