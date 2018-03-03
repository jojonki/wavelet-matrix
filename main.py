from wave_matrix import WaveMatrix

data = [4, 7, 6, 5, 3, 2, 1, 0, 1, 4, 1, 7]
print('data', data)
wm = WaveMatrix()
wav_mat = wm.get_data(data)
print(wav_mat)
print('access 6', wm.access(6))
print('access 1', wm.access(1))
print('access 2', wm.access(2))
print('rank (4, 10)', wm.rank(4, 10))
print('rank (1, 10)', wm.rank(1, 10))
