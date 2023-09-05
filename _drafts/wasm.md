---
title: "Embedding Python and WebAssembly into your website"
layout: post
python: true
tags: python wasm webassembly
---

<!-- ## Using `<iframe/>`
```html
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html"
  width="100%"
  height="300px"
></iframe>
```
<iframe
  src="https://jupyterlite.github.io/demo/repl/index.html?kernel=python&theme=JupyterLab Dark"
  width="100%"
  height="300px"
></iframe> -->

## Using `<script/>` with Javascript

```html
```
<script type="text/javascript">
  async function main() {
    pyodide = await loadPython();
    console.log(
      pyodide.runPython(`
        import matplotlib
        matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")
        import matplotlib.pyplot as plt
        import numpy as np
        plt.plot(np.arange(100), np.arange(100)**2)
        plt.title("1")
        plt.show()
      `)
    );
  };
  main();
</script>

<script type="text/javascript">
  async function main() {
    pyodide = await loadPython();
    console.log(
      pyodide.runPython(`
        import matplotlib
        matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")
        import matplotlib.pyplot as plt
        import numpy as np
        plt.plot(np.arange(100), np.arange(100)**2)
        plt.title("2")
        plt.show()
      `)
    );
  };
  main();
</script>