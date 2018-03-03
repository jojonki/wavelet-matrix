from wavelet_matrix import WaveletMatrix

data = [4, 7, 6, 5, 3, 2, 1, 0, 1, 4, 1, 7]
print('data', data)
wm = WaveletMatrix(data)
print(wm.get_data())
print('access(1)', wm.access(1))
print('access(2)', wm.access(2))
print('access(6)', wm.access(6))
print('rank(4, 10)', wm.rank(4, 10))
print('rank(1, 10)', wm.rank(1, 10))
