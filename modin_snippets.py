import modin.pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 100, size=(2**10, 2**8)))