+++
title = "rendering in pure css (part 1)"
date = "2026-05-14"
description = "more linear algebra than you ever thought possible"

[extra]
hidden = true
+++

as you can tell by my website, I like minecraft horses. and ever since reading about [DOOM rendered entirely with css](https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/), I have been fixated on the idea of rendering minecraft horses using just css. 

it kind of makes sense. one of the browser's main jobs is rendering content. this content is more often than not declared by **html** and styled by **css**. javascript is also used for fancier things, using the [canvas](https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API) or [webgl](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API) apis, but using html and css has a lot of desirable properties. 

they are declarative languages, so there is not really internal state that you have to think about. simply producing a piece of html styled by a piece of css will draw the same pixels to the screen, *no matter how that code was produced*. 

also, working within the framework of html and css gives you access to the rich suite of interaction that browsers already, meaning that you can do incredibly *niche and cursed* things with them, as you will hopefully see.

I am not an expert on graphics, and this represents the result a lot of research I've done relearning linear algebra and the basics of graphics programming. jump down to the [references](#references) section to check out some of the resources I used for making this.

okay I've said enough. look at this demo, and if this doesn't scare you away, please read the rest of the post to learn how I did it.

## demo

{% rendering_part_1() %}
<div class="rect" style="
--a-x: -100;
--a-y: -100;
--a-z: 100;
--b-x: 100;
--b-y: -100;
--b-z: 100;
--c-x: -100;
--c-y: 100;
--c-z: 100;
background: radial-gradient(cyan 0%, magenta 100%);
">
    <div style="margin: 10px;">
        <h5>WELCOME TO MY HORSE</h5>
        <p>SLIDE THE SLIDERS TO SPIN THIS CUBE AND SEE ITS DELIGHTS</p>
    </div>
</div>
<div class="rect" style="
--a-x: 100;
--a-y: 100;
--a-z: 100;
--b-x: 100;
--b-y: -100;
--b-z: 100;
--c-x: 100;
--c-y: 100;
--c-z: -100;
background: url(/minecraft-grass.jpg);
background-size: 100%;
">
<iframe 
    src="/" 
    title="description" 
    width="800" 
    height="800"
    style="transform-origin: 0% 0%; transform: scale(25%, 25%);"
></iframe>
</div>        
<div class="rect" style="
--a-x: -100;
--a-y: -100;
--a-z: 100;
--b-x: 100;
--b-y: -100;
--b-z: 100;
--c-x: -100;
--c-y: -100;
--c-z: -100;
background: white;
">
<img src="/blog/horse-spin.gif" width="200" height="200"/>
</div>
<div class="rect" style="
--a-x: 100;
--a-y: -100;
--a-z: -100;
--b-x: -100;
--b-y: -100;
--b-z: -100;
--c-x: 100;
--c-y: 100;
--c-z: -100;
background: linear-gradient(
    #5BCEFA 0%, #5BCEFA 20%, 
    #F5A9B8 20%, #F5A9B8 40%, 
    #FFFFFF 40%, #FFFFFF 60%, 
    #F5A9B8 60%, #F5A9B8 80%, 
    #5BCEFA 80%, #5BCEFA 100%
);
"></div>
        <div class="rect" style="
--a-x: -100;
--a-y: -100;
--a-z: 100;
--b-x: -100;
--b-y: 100;
--b-z: 100;
--c-x: -100;
--c-y: -100;
--c-z: -100;
background: var(--background-color);
">
    <label for="animate" style="font-size: calc(2.5 * var(--font-size))">animate?</label>    
    <input type="checkbox" id="animate" name="animate" style="scale: 2.5;" />
</div>
<div class="rect" style="
--a-x: -100;
--a-y: 100;
--a-z: 100;
--b-x: 100;
--b-y: 100;
--b-z: 100;
--c-x: -100;
--c-y: 100;
--c-z: -100;
background: linear-gradient(
    #FFF433 25%, 
    #FFFFFF 25% 50%, 
    #9B59D0 50% 75%, 
    #2D2D2D 75%
);
"></div>
<script>
(() => {
    const animate = document.getElementById("animate");

    const scene = animate.parentElement.parentElement;
    let sceneStartingStyle = scene.getAttribute("style");

    animate.addEventListener("input", () => {
        if (animate.checked) {
            sceneStartingStyle = scene.getAttribute("style");
            const animation = `
                spinnies 10s infinite linear,
                uppies 3s infinite ease-in-out,
                rollies 7s infinite ease-in-out
            `;
            scene.setAttribute("style", `
                ${sceneStartingStyle}
                animation: ${animation};
            `);
        } else {
            scene.setAttribute("style", sceneStartingStyle);
        }
    });
})();
</script>
{% end %}

## how it works
to render a complex piece of geometry, we must render smaller polygons of that geometry, often triangles. in typical graphics programming, you compile lists of coordinates representing the polygons to be rendered, plus information about how those interact with lighting, how textures map to those triangles, shaders that run arbitrary transformations against those polygons, and a lot of other fancy stuff that graphics libraries do.

for this html/css-based rendering, it's a lot simpler but also a little more complicated. the browser is not set up to render arbitrary polygons in a 3d scene, so we have to implement some part of the graphics library ourselves in the language that the browser speaks. this means creating a physical manifestation of that triangle, in this case the humble div, and manipulating the shit out of it with css transforms until it looks just about right. I had to re-learn a bunch of linear algebra for this (and a bunch of $\LaTeX$ to take notes) so y'all better LISTEN UP.

there are three principal parts to this:
1. creating a triangle (this post)
2. transforming the triangle into 3d space
3. adding camera movement and perspective to the scene

### creating a triangle
```html
<div 
  class="tri" 
  style="
    --a-x: 0;
    --a-y: 0;
    --a-z: 0;
    --b-x: 1;
    --b-y: 0;
    --b-z: 0;
    --c-x: 0;
    --c-y: 1;
    --c-z: 0;
  "></div>
```

the div is our smallest unit of three-dimensional rendering. we use [css custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties), also known as variables, to set the coordinates of the triangle. custom properties have a really nice benefit of being animatable if they're defined with [the @property rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property), meaning you can have fun writing pure-css animations if you're so inclined.

the goal here is to take a rectangular div, clip it into a right triangle, and then transform it so that it has the correct angle. these divs are set with `position: absolute` so that they are positioned at the origin, which gives the top left corner and top side of the triangle a predictable position, making future transformations simpler.

the following css clips a rectangular div into a right triangle, with the upper-left portion preserved.

```css
.tri {
    /* position this div at the origin to start */
    /* transformations will ensure it ends up where we need it */
    position: absolute;
    
    /* clip rectangle to just the upper-left triangle */
    clip-path: polygon(0 0, 0 100%, 100% 0);
}
```

so now the div is a right triangle, but what about other triangle shapes? in order to achieve that, we'll have to skew the triangle until the angle matches. it's math time, little buddy, so lock in. look at this triangle:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="15.057 199.487 327.579 166.422" xmlns:bx="https://boxy-svg.com" style="max-width: 300px; background: white;">
  <defs>
    <bx:export>
      <bx:file format="svg" path="triangle.svg"></bx:file>
    </bx:export>
  </defs>
  <path style="fill: none; stroke: rgb(0, 0, 0); stroke-width: 4px;" d="M 53.713 314.736 L 258.62 316.04 L 292.788 238.799 L 53.713 314.736 Z"></path>
  <path style="fill: none; stroke: rgb(0, 0, 0);" d="M 221.506 314.925 C 231.822 291.938 250.459 284.009 269.423 288.732"></path>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="254.956" y="344.792">A</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="300.736" y="232.851">B</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="29.509" y="340.817">C</text>
</svg>

the triangles rendered here have conventional points $ABC$, from which the vectors $\overrightarrow{AB}$ and $\overrightarrow{AC}$ roughly orient it right-hand rule style. we will set point $A$ is at the origin (0, 0, 0), and set $\overrightarrow{AB}$, the top leg, along the x axis. the side leg, $\overrightarrow{AC}$, stretches out somewhere into the positive Y direction (which is down by the way!!). this is what the triangle above looks like aligned in this standardized way:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20.146 74.853 377.077 348.298" xmlns:bx="https://boxy-svg.com" style="max-width: 300px; background: white;">
  <defs>
    <bx:export>
      <bx:file format="svg" path="triangle.svg"></bx:file>
    </bx:export>
  </defs>
  <path style="fill: none; stroke: rgb(0, 0, 0); stroke-width: 4px;" d="M 64.331 272.593 L 258.62 238.799 L 301.239 312.431 L 64.331 272.593 Z" transform="matrix(0.5, -0.86602503, 0.86602503, 0.5, -153.62697656, 288.74901295)"></path>
  <path style="fill: none; stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%;" d="M 170.367 195.581 C 178.915 213.62 198.953 221.165 215.9 215.395" transform="matrix(0.5, -0.866025, 0.866025, 0.5, 0.803378, -5.485617)"></path>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="154.764" y="178.991">A</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="268.413" y="176.513">B</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="78.838" y="379.459">C</text>
  <path style="fill: none; stroke: rgb(0, 0, 0);" d="M -43.595 183.965 L 461.758 181.943" bx:d="M -43.595 183.965 U 461.758 181.943 1@e87613f6"></path>
  <path style="fill: none; stroke: rgb(0, 0, 0); stroke-width: 1; transform-box: fill-box; transform-origin: 50% 50%;" d="M -70.613 215.731 L 434.74 213.709" bx:d="M -70.613 215.731 U 434.74 213.709 1@859bc1de" transform="matrix(0, 1, -1, 0, -0.000016, 0.000001)"></path>
</svg>

and the initial triangle we will need to create, in order to transform it to that shape:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="-20.146 74.853 377.077 348.298" xmlns:bx="https://boxy-svg.com" style="max-width: 300px; background: white;">
  <defs>
    <bx:export>
      <bx:file format="svg" path="triangle.svg"></bx:file>
    </bx:export>
  </defs>
  <path style="fill: none; stroke: rgb(0, 0, 0); stroke-width: 4px; stroke-dasharray: 4;" d="M 64.331 272.593 L 258.62 238.799 L 301.239 312.431 L 64.331 272.593 Z" transform="matrix(0.5, -0.86602503, 0.86602503, 0.5, -153.62697656, 288.74901295)"></path>
  <path style="fill: none; stroke: rgb(0, 0, 0); transform-box: fill-box; transform-origin: 50% 50%;" d="M 170.367 195.581 C 178.915 213.62 198.953 221.165 215.9 215.395" transform="matrix(0.5, -0.866025, 0.866025, 0.5, 0.803378, -5.485617)"></path>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="154.764" y="178.991">A</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="268.413" y="176.513">B</text>
  <text style="white-space: pre; fill: rgb(51, 51, 51); font-family: Arial, sans-serif; font-size: 28px;" x="78.838" y="379.459">C</text>
  <path style="fill: none; stroke: rgb(0, 0, 0);" d="M -43.595 183.965 L 461.758 181.943" bx:d="M -43.595 183.965 U 461.758 181.943 1@e87613f6"></path>
  <path style="fill: none; stroke: rgb(0, 0, 0); stroke-width: 1; transform-box: fill-box; transform-origin: 50% 50%;" d="M -70.613 215.731 L 434.74 213.709" bx:d="M -70.613 215.731 U 434.74 213.709 1@859bc1de" transform="matrix(0, 1, -1, 0, -0.000016, 0.000001)"></path>
  <path style="fill: none; stroke: rgb(0, 0, 0); stroke-width: 4; transform-box: fill-box; transform-origin: 50% 50%;" d="M 93.175 322.454 L 252.338 231.082 L 294.957 304.713 L 93.175 322.454 Z" transform="matrix(0.5, -0.866025, 0.866025, 0.5, -1.099412, -19.64525)"></path>
  <path d="M 171.58 367.124 H 203.647 L 203.647 359.624 L 216.647 368.624 L 203.647 377.624 L 203.647 370.124 H 171.58 V 367.124 Z" bx:shape="arrow 171.58 359.624 45.067 18 3 13 0 1@54f76886" style="fill: rgb(216, 216, 216); stroke: rgb(0, 0, 0);" transform="matrix(-0.999975, 0.007109, -0.007109, -0.999975, 345.776093, 736.019531)"></path>
</svg>

the first problem to solve is: what size should the initial div be? the triangle will be skewed along the x axis, so the points A and vector $\overrightarrow{AB}$ will be preserved, since they lie on the axis, giving us $\|\overrightarrow{AB}\|$ as the width of the div. since the skew will not affect the height of the shape at all, we can figure out how much of $\overrightarrow{AC}$ will be in the Y direction, and that should be the height of the div.

to calculate "figure out how much of $\overrightarrow{AC}$ will be in the Y direction", we can use the the [orthogonal projection](https://en.wikipedia.org/wiki/Vector_projection) of $\overrightarrow{AC}$ from $\overrightarrow{AB}$. this works because we have defined $\overrightarrow{AB}$ to lie along the x axis, and $\overrightarrow{AC}$ to lie in the XY plane, so this orthogonal projection must lie along the Y axis. the formula for orthogonal projection is as follows:

{% katex() %}
\begin{align}
\operatorname{proj}_{\mathbf{b}} \mathbf{a} &= \bigg(\frac {\mathbf{a} \cdot \mathbf{b}} {\left\|\mathbf{b}\right\|^2}\bigg) \mathbf{b} \\
\operatorname{oproj}_{\mathbf{b}} \mathbf{a} &= \mathbf{a} - \operatorname{proj}_{\mathbf{b}} \mathbf{a} 
\end{align}
{% end %}

plugging in our vectors gives us our starting dimensions and a skew amount:

{% katex() %}
\begin{align}
\operatorname{width} &= \|\overrightarrow{AB}\| \\
\operatorname{height} &= \|\operatorname{oproj}_{\overrightarrow{AB}} \overrightarrow{AC}\| \\
&= \|\overrightarrow{AC} -\bigg(\frac{\overrightarrow{AC} \cdot \overrightarrow{AB}}{\|\overrightarrow{AB}\|^2}\bigg) \overrightarrow{AB}\| \\
\end{align}
{% end %}

and the css to do this:

```css
.tri {
    /* 
     * use AB and AC vectors to determine the height and width
     * of the containing rectangle
     */
    --delta-ab-x: calc(var(--b-x) - var(--a-x));
    --delta-ab-y: calc(var(--b-y) - var(--a-y));
    --delta-ab-z: calc(var(--b-z) - var(--a-z));

    --delta-ac-x: calc(var(--c-x) - var(--a-x));
    --delta-ac-y: calc(var(--c-y) - var(--a-y));
    --delta-ac-z: calc(var(--c-z) - var(--a-z));

    --hypot-ab: calc(hypot(var(--delta-ab-x), var(--delta-ab-y), var(--delta-ab-z)));

    /* projection of AC onto Y */
    --ac-dot-ab: calc(
        (var(--delta-ac-x) * var(--delta-ab-x)) +
        (var(--delta-ac-y) * var(--delta-ab-y)) +
        (var(--delta-ac-z) * var(--delta-ab-z))
    );
    --ac-project-ab: calc(var(--ac-dot-ab) / pow(var(--hypot-ab), 2));
    
    /* orthogonal projection of AC from Y */
    --tri-ac-x: calc(var(--delta-ac-x) - (var(--ac-project-ab) * var(--delta-ab-x)));
    --tri-ac-y: calc(var(--delta-ac-y) - (var(--ac-project-ab) * var(--delta-ab-y)));
    --tri-ac-z: calc(var(--delta-ac-z) - (var(--ac-project-ab) * var(--delta-ab-z)));
    --tri-height: calc(hypot(var(--tri-ac-x), var(--tri-ac-y), var(--tri-ac-z)));

    /* width and height of the initial right triangle */
    width: calc(var(--hypot-ab) * 1px);
    height: calc(var(--tri-height) * 1px);
}
```

and how that looks rendered:

{% rendering_part_1() %}
<div 
class="tri" 
style="
    --a-x: 0;
    --a-y: 0;
    --a-z: 0;
    --b-x: 75;
    --b-y: 0;
    --b-z: 0;
    --c-x: 0;
    --c-y: 150;
    --c-z: 0;
    background: orange;
"></div>
{% end %}

the next thing we need is how much to skew the div along the x axis. the skew value is the amount that the $\overrightarrow{AC}$ must shift in the x axis, that is, in the direction of $\overrightarrow{AB}$, over the course of its height. see the [shear affine transformation](https://en.wikipedia.org/wiki/Affine_transformation#Image_transformation) here for more details. the transformation to do the skewing is thus:

{% katex() %}
\begin{align}
\operatorname{skew} &= \|\operatorname{proj}_{\overrightarrow{AB}} \overrightarrow{AC}\| \\
&= \|\bigg(\frac{\overrightarrow{AC} \cdot \overrightarrow{AB}}{\|\overrightarrow{AB}\|^2}\bigg) \overrightarrow{AB}\| \\
M_{skew} &= \begin{bmatrix} 
1 & \frac{skew}{height} & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
\end{align}
{% end %}

this ensures that at the full height of the div, it is fully skewed to the point it should be.

with this math, we can begin writing the basic css to give us a triangle-shaped div with the correct shape:

```css
.tri {
    /* calculate the skew matrix coefficient */
    --skew-ac-x: calc(var(--ac-project-ab) * var(--delta-ab-x));
    --skew-ac-y: calc(var(--ac-project-ab) * var(--delta-ab-y));
    --skew-ac-z: calc(var(--ac-project-ab) * var(--delta-ab-z));
    --skew-length: calc(hypot(var(--skew-ac-x), var(--skew-ac-y), var(--skew-ac-z)));
    --skew-coefficient: calc(var(--skew-length) / var(--tri-height));

    /* Z basis vector, formed from the normalized cross product of the X and Y basis vectors */
    transform-origin: 0% 0%;
    transform:
        matrix3d(
            1, 0, 0, 0,
            var(--skew-coefficient), 1, 0, 0,
            0, 0, 1, 0,
            0, 0, 0, 1
        );
    }

```

you might notice that the skew coefficient swapped around in the transformation matrix from how it was defined above: that's because the matrices in css are column-major, which from what I can understand is common in graphics programming. this just means that the visual representation ends up looking like the matrix is transposed. the more you know...


{% rendering_part_1() %}
<div 
class="tri" 
style="
    --a-x: 0;
    --a-y: 0;
    --a-z: 0;
    --b-x: 75;
    --b-y: 0;
    --b-z: 0;
    --c-x: -50;
    --c-y: 150;
    --c-z: 0;
    background: orange;
"></div>
{% end %}

with that all set up, we have step one done! there is a triangle, and it looks like the triange we want. the only problem is that it's stuck in the XY plane, staring at us, taunting us.

and that's part 1! there will be more coming in the future, covering the transformation of our triangles into three-dimensional space, camera rotation, perspective transformation, texturing (still figuring this one out), and animation.

those will be linked here when they're out!

## references
[scratchapixel - The Perspective and Orthographic Projection Matrix](https://www.scratchapixel.com/lessons/3d-basic-rendering/perspective-and-orthographic-projection-matrix/projection-matrix-introduction.html) - a great introduction to the concepts behind perspective transformation. I still don't fully _get it_ but this got me a little closer. it looks like there are a bunch of other great posts here about graphics programming basics, so I'm excited to dive deeper here as I work more on this project

[Wikipedia - Rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix#General_3D_rotations) - I kinda just stole the general 3d rotation matrix from here without thinking too hard about that. I hope that's okay.

[Niels Leenheer - CSS is DOOMed](https://nielsleenheer.com/articles/2026/css-is-doomed-rendering-doom-in-3d-with-css/) - obviously. this is what inspired my fascination with this whole things

 