import numpy as np

"""Created a function calculate and an input list is given to the function..."""
def calculate(in_list):
    mean = []
    variance = []
    standard_deviation = []
    maximum = []
    minimum = []
    sum_total = []

    """Converted the input array to a numpy array"""
    arr = np.array(in_list)
    """Reshape the numpy array into a 3x3 matrix in try block. In except block raise a value error if the total number of elements in a list is not equal to 9."""
    try:
        arr = np.reshape(arr, (3, 3))
    except:
        raise ValueError("List must contain nine numbers.")

    """After calculation store the values in the corresponding lists created above.."""
    mean.append(np.mean(arr, axis=0).tolist())
    mean.append(np.mean(arr, axis=1).tolist())
    mean.append(np.mean(arr).tolist())

    variance.append(np.var(arr, axis=0).tolist())
    variance.append(np.var(arr, axis=1).tolist())
    variance.append(np.var(arr).tolist())

    standard_deviation.append(np.std(arr, axis=0).tolist())
    standard_deviation.append(np.std(arr, axis=1).tolist())
    standard_deviation.append(np.std(arr).tolist())

    maximum.append(np.max(arr, axis=0).tolist())
    maximum.append(np.max(arr, axis=1).tolist())
    maximum.append(np.max(arr).tolist())

    minimum.append(np.min(arr, axis=0).tolist())
    minimum.append(np.min(arr, axis=1).tolist())
    minimum.append(np.min(arr).tolist())

    sum_total.append(np.sum(arr, axis=0).tolist())
    sum_total.append(np.sum(arr, axis=1).tolist())
    sum_total.append(np.sum(arr).tolist())

    """Created a dictionary and use the lists as items.value in the dictionary. The calculate function will return the dictionary..."""

    calculation_dict = {
        "mean": mean,
        "variance": variance,
        "standard deviation": standard_deviation,
        "max": maximum,
        "min": minimum,
        "sum": sum_total
    }
    return calculation_dict
