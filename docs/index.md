---
title: Latest Posts
timetoread: False
---
<style>
.grid-item {
    border: 1px solid #eee;
    padding: 2em;
    display: inline-block;
    width: 19em;
    height: 19em;
    vertical-align: top;
}
</style>

{% for page in navigation.recent_pages() %}
<div class="grid-item">
<a href="{{ page.url }}">
  <figure >
    <img src="{{ page.meta.image }}"  width="240" loading="lazy"/>
    <figcaption>{{page.title}}</figcaption>
  </figure>
</a>
</div>
{% endfor %}