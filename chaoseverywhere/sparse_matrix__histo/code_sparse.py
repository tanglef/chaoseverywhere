import matplotlib.pyplot as plt
import scipy.sparse as sparse

def sparse_matrix(wi, leng, den):
    """This fucntion creates a sparse matrix.
    It uses random number to place the values (different of 0).

    : param wi : the width of the matrix
    : type wi : integer
    : param leng : the length of the matrix
    : type leng : integer
    : param den : density of number different of 0 in the matrix
    : type den : float
    : return : The representation of a sparse matrix
    : rtype : image
    """
    sp_mat = sparse.random(wi, leng, den)
    plt.spy(sp_mat, markersize=1, mfc='purple', marker='p', mec='red')