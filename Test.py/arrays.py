import numpy as np
# %%
import numpy as np

# %%
arr_2d = np.array([[0, 5, 10], [15, 20, 25], [30, 35, 40]])

# %%
np.eye(3)
# %%
np.zeros(3)
# %%
# Cuarto nivel, 2 elementos en ancho por 2 de alto
# por 2 de profundidad por 2 más, 16 en total
arr_4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
                   [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])
arr_4d
# %%
arr_5d =np.arange(243).reshape(3,3,3,3,3)
# %%
arr_5d
# %%
