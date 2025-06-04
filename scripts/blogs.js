const content = document.body.innerHTML;
const template = `
<div id="layout">
  <section id="sidebar">
    <ul id="navigation">
      <li>
        <a href="ref-"><a href="/#blogs">go back</a></a>
      </li>
    </ul>
  </section>

  <section id="main">
    <div id="about" class="blog">
      ${content}
    </div>
  </section>

  <div id="background-image"></div>

  <script src="/scripts/blogs.js"></script>
</div>
`;

document.body.innerHTML = template;
