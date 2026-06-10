+++
title = "Bœuf"
description = """
> hewwo :3 i'm a soft and fluffy borzoi (russian sighthound)
"""
template = "fursona_page.html"

[extra]
icon = "boeuf-nb-pride.png"
hide_reading_time = true
+++

## About the dog

{{ palette(path="refs/boeuf/palette.toml") }}

> ℹ️ **pronouns**: it/its

> 🐕 **bœuf** is a **borzoi** (russian sighthound), a breed of dog similar to a **greyhound** but with long, flowing fur on the top of its body to protect it in the harsh cold

> 🥩 the name is french for **"beef"**, and pronounced somewhere between "beef" and "buff"

> here is what it looks like, in three dimensions!

{{ rendering(path="/borzoi/model.divs", projection=100, yaw=-135, y=250, pitch=16, z=500, animated_spin=true) }}

> check out some pictures of **THIS DOG** below. feel free to save them if you like!!


## Gallery

{{ gallery(manifest="/refs/boeuf/gallery.toml") }}