Dear SDL researchers  - 

We use the Anaconda Python distribution in the lab. We use other languages too, but a lot of work gets done in Python and R. To be ready to contribute, install Python and R:

#### Install the packages specified below:

##### [1] Download and install the Python 3.7 version of Anaconda
[https://www.anaconda.com/distribution/](https://www.anaconda.com/distribution/)

`conda config --add channels conda-forge` 

Once this is installed, follow your platform specific directions at [https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/](https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/)
to install:

`conda install regex plotnine seaborn jupyterlab networkx pip bokeh plotly chartify`  
then  
`pip install sklearn`  

##### [2] If you are working on Scenario A, install GIS tools. 

Try to install [https://libspatialindex.github.io/](https://libspatialindex.github.io/).  
 
- On macOS, install https://brew.sh/ and then `brew install spatialindex`  
- On Windows, try the binaries linked on the github page and use google  
- If you use linux, you know what to do.  

Once libspatial is installed, try  
`pip install geopandas Fiona Shapely Rtree`


##### [3] If you want to create agent based models compatible with the other DARPA collaborators, install DWORP  
[https://github.com/ACI-ESP/dworp](https://github.com/ACI-ESP/dworp)

See the examples folder for examples of simple ABMs. 

##### [4] Install R
For non-python data analysis Install R from https://cran.r-project.org/  

[https://www.rstudio.com/](https://www.rstudio.com/) is a popular R frontend.  


#### General Anaconda install instructions can be found at: (thanks @alexruch) 

Mac - [https://medium.com/@GalarnykMichael/install-python-on-mac-anaconda-ccd9f2014072
](https://medium.com/@GalarnykMichael/install-python-on-mac-anaconda-ccd9f2014072)  

Windows - [https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444](https://medium.com/@GalarnykMichael/install-python-on-windows-anaconda-c63c7c3d1444)


