+++
title = "sign my guestbook"
description = "let the world know you came"

hidden = true
+++

# Guestbook

since it's not SOCIAL media, I can't really know who's coming by and reading this stuff unless you fill out the form below and press go.

these messages are hand-approved by me before they are published, so it make take some time before you see them appear here.

<div class="post">
    <form class="guestbook" action="https://guestbook.borzoi.horse" method="POST" enctype="application/x-www-form-urlencoded">
        <label for="name">name</label>
        <input type="text" id="name" name="name" />
        <label for="email">email (will not be published)</label>
        <input type="email" id="email" name="email" />
        <label for="message">message</label>
        <textarea id="message" name="message" rows=4></textarea>
        <input type="text" value="true" name="legit" hidden="true" />
        <input type="text" value="{{ get_url(path="/guestbook/success") }}" name="success" hidden="true" />
        <input type="text" value="{{ get_url(path="/guestbook/failure") }}" name="failure" hidden="true" />
        <label for="submit">submit</label> <input type="submit" id="submit" />
    </form>
</div>

<style>
.guestbook {
    display: grid;
    grid-template-columns: 1fr 3fr;
    gap: 10px;
}
</style>

## see entries below!

{% set guestbook_data = load_data(path=section.path ~ "/guestbook.toml", format="toml") %}
{% for entry in guestbook_data.entries %}
<div class="post">
    <h3>{{ entry.name }}</h2>
    <time datetime="{{ entry.date }}">{{ entry.date | date(format="%Y-%m-%d %H:%m") }}</time>
    <p>{{ entry.message }}</p>
</div>
{% endfor %}
