+++
title = "fox business card"
description = "fox business card"

[extra]
hide_reading_time = true
icon = "fox-business-card.png"
+++

{% <rendering animate={true} > %}
{{ load_data(path="models/business-card.divs") }}
{% </rendering> %}

<style>
.container {
    height: 800px;
}
.node.base {
    --node-scale: 2;
    --node-translate-y: 200px;
}
</style>