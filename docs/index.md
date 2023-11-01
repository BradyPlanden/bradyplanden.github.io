---
title: Latest Posts
timetoread: False
---
<style>
.grid-item {
    border: 2px solid #eee;
    padding: 2em;
    display: inline-block;
    width: 18em;
    height: 20em;
    vertical-align: middle;
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