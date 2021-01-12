import numpy as np
#"time" windowize data in preparation for LSTM/RNN modeling 

def windowize_data(data, n_prev):
    n_pred = len(data) - n_prev
    y = data[n_prev:]
    indices = np.arange(n_prev) + np.arange(n_pred)[:, None]
    x = data[indices, None]
    return x, y

if __name__ == '__main__':
    pass