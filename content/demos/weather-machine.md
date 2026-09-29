+++
title = "the weather machine"
+++

{% set max = 10 %}

{% for i in range(end=max) %}
<img class="weather slot-{{ i }}" src="/ouioui.png">
{% endfor %}

<style>
.weather {
    position: absolute;
}

{% for i in range(end=max) %}
.weather.slot-{{ i }} {
    left: calc({{ i / max }} * 100%);
}
{% endfor %}

</style>