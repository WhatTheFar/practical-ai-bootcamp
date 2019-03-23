# Practical AI Bootcamp

## Reference

### Online course

[Machine Learning — Andrew Ng, Stanford University](https://www.youtube.com/playlist?list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN)

## Troubleshooting

#### For macOS, matplotlib problem

**Universal solution**
Use the following code in order to import matplotlib

```python
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
```

or just simply set a environment variable before run the code

```
MPLBACKED=TkAgg
```

**Alternative solution for anaconda user**

The default python provided in (Ana)conda is not a framework build. However,
a framework build can easily be installed, both in the main environment and in conda envs: install python.app (`conda install python.app`) and use pythonw rather than python

**For pycharm user**

Just run the code in PyCharm :P
