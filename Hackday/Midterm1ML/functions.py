import math
def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    n = len(x)
    m = len(x[0])
    res = 1
    for i in range(min(n, m)):
        if (x[i][i] != 0):
            res *= x[i][i]
    return res
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    
    x.sort()
    y.sort()
    
    n = len(x)
    m = len(y)
    
    if (n != m):
        return False
    
    for i in range(n):
        if (x[i] != y[i]):
            return False
    
    return True


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    n = len(x)
    mx = 0
    for i in range(n - 1):
        if (x[i] == 0):
            mx = max(mx, x[i + 1])    
    return mx
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """    
    x = img.shape[0]
    y = img.shape[1]    
    res = [[0 for i in range(y)] for j in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(3):
                res[i][j] += img[i][j][k] * coefs[k]
    return res
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    n = len(x)
    cnt = 0
    a = []
    b = []
    for i in range(n):
        if (len(a) == 0 or x[i] != a[-1]):
            a.append(x[i])
            b.append(1)
            ++ cnt
        else:
            b[-1] += 1
    print(a, b)
    pass

def distance(x, y):
    res = 0;
    for i in range(len(x)):
        res += pow(x[i] - y[i], 2)
    return math.sqrt(res)

def pairwise_distance(x, y):
    """Return pairwise object distance.
    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    dist = [[1 for i in range(len(y))] for j in range(len(x))]
    n = len(x)
    m = len(y)
    for i in range(n):
        for j in range(m):
            dist[i][j] = distance(x[i], y[j])
    return dist
    pass
