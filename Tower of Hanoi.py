#########################################################################################
#                              1 Simulate Binary System                                 #
#########################################################################################

# Input the layer(level) of the tower.
try:
    layer = int(input('Input layers (1~10):'))
except ValueError:
    print('Please input a valid number.')

# Translate number of layers into a binary string.
def layer_f(l):
    layer_to_bin_str = []
    while l > 0:
        layer_to_bin_str.append(1)
        l -= 1
    return layer_to_bin_str
layer_to_bin_str = layer_f(layer)

# Default status of the disks, set to 0b00000...(digits = layers).
def ini_bin_str_f(l):
    ini_b_str = []
    while l > 0:
        ini_b_str.append(0)
        l -= 1
    return ini_b_str

# Function for translate binary number into a string, for comparison.
def bin_num_to_bin_str(b_num):
    div = 0b10                                  # Base of binary system.
    bin_str = ini_bin_str_f(layer)
    ite = 0                                     # Digit need to be translated.
    while b_num > 0:
        bin_str[ite] = b_num % div
        b_num = b_num // div
        ite += 1
    return bin_str

# translate layer number to comparable number(0d or 0b type, here 0d type).
def layer_to_digit(l):
    digit = 0
    for i in range(l):
        digit = 2 ** i
        digit += digit
    return digit - 1

# Main function: binary number to string and compare, binary number ++, iterate...
def compare_layters_and_move():
    bin_num = 0
    while bin_num < layer_to_digit(layer):
        for i in range(len(layer_to_bin_str)):
            if bin_num_to_bin_str(bin_num + 1)[i] - bin_num_to_bin_str(bin_num)[i] > 0:
                print ('Move layer {layer}'.format(layer = i+1))
        bin_num += 1
    else:
        print ('Done!')

show_step = compare_layters_and_move()

#########################################################################################
#                                 2 Recursive way                                       #
#########################################################################################
try:
    level = int(input('Input levels of ToH (1~10):'))
except ValueError:
    print('Please input a valid number.')

def toh_func (n_level):
    if 0 == n_level:
        return
    toh_func(n_level-1)
    move_func(n_level)
    toh_func(n_level-1)

def move_func(n_level):
    print('Move layer {}'.format(n_level))

show_result = toh_func(level)
