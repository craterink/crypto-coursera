import itertools


def __mesh_map(fn, iterable, comb_length):
    combos_iter = itertools.combinations(iterable, comb_length)
    return map(fn, combos_iter)


def _mesh_map(fn, iterable, comb_lengths):
        mapped_dict = {comb_length: __mesh_map(fn, iterable, comb_length)
                       for comb_length in comb_lengths}
        return mapped_dict


def mesh_map(fn, iterable, comb_length=2, all_comb_lengths=False):
    if all_comb_lengths:
        return _mesh_map(fn, iterable, range(1, iterable.size(), 1))
    else:
        return _mesh_map(fn, iterable, [comb_length])[2]

