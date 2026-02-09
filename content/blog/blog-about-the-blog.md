+++
title = "blog about the blog"
date = "2026-02-08"
description = "this post describes how I used zola to create this webby site"
+++

hey so I made this website and whenever someone makes a website using an obscure technology, especially an obscure static site generate, it's all but required to make a post about it and why they chose to use it and why they would recommend everyone else use it. unfortunately, in my case, I'm not sure I can actually do that.

![the zola logo](/blog/Zola-logo-black.svg)

I made this website using [zola](https://www.getzola.org/), a static site generator not unlike the myriad other options available for generating a presentable pile of html and css from a series of markdown files and assets. in theory, these things should be pretty easy to pick up, download a theme, type words into your keyboard, and spit out a website. in practice, getting your interpreter versions and package versions and whatever other versions to line up and actually work and run inside of a github action (because of course you're hosting your site on github because who wants to maintain shit) is a nightmare.

![minecraft sheep head](/blog/SuckyBlowfish_21490068.png)

that's kinda where zola comes in. it's written in rust and is a single, statically-linked binary that just does the thing it does. you can't plugins, it just does it. and it kinda does it well. it's fast and lightweight and just worked when I set it up to run in github actions. it supports themes and has a somewhat usable scripting language built into the templating language and mostly acts like a hackathon project that had a couple weeks cleaning it up and that's all I really needed.

what's been kinda sucky is the documentation is a little lacking. I've had to look at the source code on a few occasions to confirm that some thing worked a specific way, which tbh is a reason to use open source projects written in a language you know. also, themes just did not seem to work for me. I tried a handful and they all seemed to require to you have config options set, but also didn't work once I set them, so I ended up just copying a lot of stuff from the [terminus theme source](https://github.com/ebkalderon/terminus) and just making up my own styles. I'm kind of thankful for that though, because otherwise I'd have just a boring nice looking website rather than this piece of shit /pos.

i think it's been really fun that every bit of the html and css and stuff that has ended up on this site has been filtered through my hands or at least through my selective use of copy and paste. I'm not sure I can really recommend zola if you're looking for a truly plug and play system with a robust community theme repository, but I've enjoyed playing with it and building something that it truly mine.

check out the [repository for this webby site](https://github.com/flowbish/borzoi.horse) to see how the sausage is made and also check out my [gallery of minecraft photos](/minecraft)!