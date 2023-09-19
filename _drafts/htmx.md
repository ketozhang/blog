---
title: "HTMX"
layout: post
---
<script src="https://unpkg.com/htmx.org@1.9.5"></script>
<!-- have a button POST a click via AJAX -->
<button hx-get="/blog/2023/09/06/htmx/" hx-swap="outerHTML">
  Click Me
</button>