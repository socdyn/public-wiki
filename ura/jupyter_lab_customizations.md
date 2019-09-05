


### To show all jupyter output, in a cell near the top of each notebook, execute this code: ###

```python
# Print all output (implicitly print results that are not assigned to a name)
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
```

----

### Open Jupyter Lab in Chrome app mode ###
from: http://christopherroach.com/articles/jupyterlab-desktop-app/

Open `~/.jupyter/jupyter_notebook_config.py`. If the file does not exist, first run the Terminal command:
`jupyter lab --generate-config`

Add this line to `~/.jupyter/jupyter_notebook_config.py`  
`c.LabApp.browser = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --app=%s'`  

To reopen a closed app mode window:
Look up to port and token from the jupyter server window and then use Terminal to:
`/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --app=http://localhost:8888/?token=<token>`



----



### Jupyter lab extensions to consider: ###

#### recommended ####
@jupyter-widgets/jupyterlab-manager
The JupyterLab extension providing Jupyter widgets.

@jupyterlab/toc
Table of Contents extension for JupyterLab

qgrid
An Interactive Grid for Sorting and Filtering DataFrames in Jupyter Notebook

#### conditionally useful for some people ###
jupyterlab_templates
A JupyterLab extension.

jupyterlab_vim
Code cell vim bindings

@jupyterlab/celltags
Extension for adding descriptive tags to notebook cells (Beta)

@jupyterlab/git
A JupyterLab extension for version control using git

jupyterlab-jupytext
A JupyterLab extension for Jupytext

nbdime-jupyterlab
A JupyterLab extension for showing Notebook diffs.

