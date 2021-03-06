class WaveletMatrix:
    def __init__(self, data=None):
        self.th_list = [None] # no threshold at first row
        if data:
            self.data = self.get_data(data)

    def get_data(self, data=None):
        if data is None:
            return self.data

        self.bin_size = len(bin(max(data))) - 2 # ignore '0b' prefix, e.g., 0b111
        self.fmt = '{0:0' + str(self.bin_size) + 'b}'

        bin_data = [self.fmt.format(d) for d in data]
        bin_data_list = []
        wav_mat = []

        for i in range(self.bin_size):
            bin_data_list.append([int(b[i]) for b in bin_data])

        wav_mat.append(bin_data_list[0])
        indices = range(len(data))
        for i in range(0, self.bin_size - 1):
            pfx_ind, sfx_ind = [], []
            pfx, sfx = [], []
            for c, b in enumerate(wav_mat[i]):
                if b == 0:
                    pfx_ind.append(c)
                    pfx.append(bin_data_list[i+1][indices[c]])
                else:
                    sfx_ind.append(c)
                    sfx.append(bin_data_list[i+1][indices[c]])

            self.th_list.append(len(pfx))
            indices = pfx_ind + sfx_ind
            wav_mat.append(pfx + sfx)

        self.data = wav_mat
        return self.data

    def access(self, index):
        d = self.data
        assert index >= 0 and index < len(d[0])

        idx = index
        mem = []
        for i in range(self.bin_size):
            b = d[i][idx]
            mem.append(b)
            if i < self.bin_size - 1: # update idx
                idx = d[i][:idx].count(b)
                if b == 1:
                    idx += self.th_list[i + 1]
        ans = int(''.join([str(b) for b in mem]), 2)
        return ans

    def rank(self, n, index):
        d = self.data
        assert index >= 0 and index < len(d[0])

        n_b = self.fmt.format(n) # ex) '100'
        beg, end = 0, index
        ct = None
        for i in range(self.bin_size):
            v = int(n_b[i])
            ct = d[i][beg:end].count(v)
            if i < self.bin_size - 1: # update idx
                if v == 0:
                    beg = 0
                else:
                    beg = self.th_list[i + 1]
                end = beg + ct

        return ct
