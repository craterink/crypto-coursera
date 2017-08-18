from util.fs.read import read_file, read_lines_from_file
from util.num_rep.convert import hexstr2dec
from ManyTimePadSolver import ManyTimePadSolver

CIPHER_TEXTS_FILE = 'data-ct.txt'
TARGET_CIPHER = 'data-target-ct.txt'

# import data
cipher_texts = read_lines_from_file(CIPHER_TEXTS_FILE)
target_cipher_text = read_file(TARGET_CIPHER)

# convert data to decimal
convert_to_dec = hexstr2dec
cipher_texts = map(convert_to_dec, cipher_texts)
target_cipher_text = convert_to_dec(target_cipher_text)

# solve problem
solver = ManyTimePadSolver(cipher_texts)
solver.ascii_analyze()
