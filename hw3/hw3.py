from scipy.linalg import eigh
import numpy as np
import matplotlib.pyplot as plt

def load_and_center_dataset(filename):
    # Your implementation goes here!
    x = np.load(filename)
    x = x - np.mean(x, axis = 0)
    return x
    pass

def get_covariance(dataset):
    # Your implementation goes here!
    x = dataset
    np.dot(x, np, transpose(x))
    for (int i = 0; i < ) {
        
    }
    return x
    return x
    pass

def get_eig(S, m):
    # Your implementation goes here!

    pass

def get_eig_prop(S, prop):
    # Your implementation goes here!
    pass

def project_image(image, U):
    # Your implementation goes here!
    pass

def display_image(orig, proj):
    # Your implementation goes here!
    pass
