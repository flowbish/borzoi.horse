+++
title = "rendering test"
+++

{% <rendering id="test" z={1000} y={200}> %}
<div id="rotate" class="rect" style="
--a-x: 0;
--a-y: 0;
--a-z: 0;
--b-x: 0;
--b-y: 0;
--b-z: 0;
--c-x: 0;
--c-y: 0;
--c-z: 0;
--texture-image: url(/wide-texture.jpg);
--texture-width: 500;
--texture-height: 500;
--texture-a-s: 0;
--texture-a-t: 0;
--texture-b-s: 1;
--texture-b-t: 0;
--texture-c-s: 0;
--texture-c-t: 1;
">
</div>
{{ load_data(path="/models/axes.divs") }}
{% </rendering> %}

{{ <rendering.controls id="test" /> }}

<div class="controls" id="rotate-controls">
    <label>angle</label>
    <input type="range" class="angle" name="angle" min="-180" max="180" />
    <label>texture width</label>
    <input type="range" class="texture-width" name="texture-width" min="0" max="100" />
    <label>texture height</label>
    <input type="range" class="texture-height" name="texture-height" min="0" max="100" />
    <input type="button" value="reset" class="reset" name="reset" />
</div>

<script>
(() => {
    const controls = document.getElementById("rotate-controls");

    let angle = controls.getElementsByClassName("angle")[0];
    angle.value = 0;

    let texture_width = controls.getElementsByClassName("texture-width")[0];
    texture_width.value = 0;

    let texture_height = controls.getElementsByClassName("texture-height")[0];
    texture_height.value = 100;

    const div = document.getElementById("rotate");
    let update_div = () => {
        const radians = parseFloat(angle.value) / 180 * Math.PI;
        const radians_a = radians + Math.PI / 4;
        const radians_b = radians + 3 * Math.PI / 4;
        const radians_c = radians - Math.PI / 4;
        const len = 141;

        div.style.setProperty('--a-x', `${-len * Math.cos(radians_a)}`);
        div.style.setProperty('--a-y', `${-len * Math.sin(radians_a)}`);

        div.style.setProperty('--c-x', `${-len * Math.cos(radians_b)}`);
        div.style.setProperty('--c-y', `${-len * Math.sin(radians_b)}`);

        div.style.setProperty('--b-x', `${-len * Math.cos(radians_c)}`);
        div.style.setProperty('--b-y', `${-len * Math.sin(radians_c)}`);

        const width = parseFloat(texture_width.value) / 100;
        div.style.setProperty('--texture-a-t', `${width}`);
        div.style.setProperty('--texture-b-t', `${width}`);

        const height = parseFloat(texture_height.value) / 100;
        div.style.setProperty('--texture-c-t', `${height}`);
    };

    angle.addEventListener("input", update_div);
    texture_width.addEventListener("input", update_div);
    texture_height.addEventListener("input", update_div);
    update_div();

    let reset = controls.getElementsByClassName("reset")[0];
    reset.addEventListener("click", () => {
        angle.value = 0;
        texture_width.value = 0;
        texture_height.value = 100;
        update_div();
    });
})();
</script>