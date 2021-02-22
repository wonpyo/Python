
#%% Define Jupyter-like code cells within Python code using a #%% comment
list(range(0,10,2))

# %%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

# %%
