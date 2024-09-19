import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.array([list]).reshape(3,3)
    mean_axis0, mean_axis1, mean_flat = np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix)
    var_axis0, var_axis1, var_flat = np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix)
    std_axis0, std_axis1, std_flat = np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix)
    max_axis0, max_axis1, max_flat = np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix)
    min_axis0, min_axis1, min_flat = np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix)
    sum_axis0, sum_axis1, sum_flat = np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix)

    calculations   = {
          'mean': [mean_axis0, mean_axis1, mean_flat],
          'variance': [var_axis0, var_axis1, var_flat],
          'standard deviation': [std_axis0, std_axis1, std_flat],
          'max': [max_axis0, max_axis1, max_flat],
          'min': [min_axis0, min_axis1, min_flat],
          'sum': [sum_axis0, sum_axis1, sum_flat]
        }



    return calculations
