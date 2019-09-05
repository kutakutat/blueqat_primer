from blueqat import Circuit

def hadamard_gate_1qbit(shot_num):
    print("\n1 量子ビットにアダマールゲートを適用")
    print("--H--M")
    print(Circuit(1).h[0].m[:].run(shots = shot_num))

def hadamard_gate_2qbit(shot_num):
    print("--H--M")
    print("--H--M")
    print("\n2 量子ビットにアダマールゲートを独立に適用")
    print(Circuit(2).h[0,1].m[:].run(shots = shot_num))

def entanglment_2qbit(shot_num):
    print("\n2 量子ビットの量子もつれ")
    print("--H--*--M")
    print("--H--X--M")
    print(Circuit(2).h[0].cx[0,1].m[:].run(shots = shot_num))

def plus_2qbit(shot_num):
    print("\n2量子ビットの足し算(使用するのは4量子ビット)")
    print("--H--*-----*--M")
    print("--H-----*--*--M")
    print("-----X--X-----M")
    print("-----------X--M")
    print(Circuit(4).h[0,1].cx[0,2].cx[1,2].ccx[0,1,3].m[:].run(shots = shot_num))


def simple_grover_2qbit(shot_num):
    print("\n2量子ビットの grover アルゴリズム")
    print("--H-----*-----H--X-----*-----X--H--M")
    print("--H--H--X--H--H--X--H--X--H--X--H--M")
    print(Circuit(2).h[0,1].h[1].cx[0,1].h[1].h[0,1].x[0,1].h[1].cx[0,1].h[1].x[0,1].h[0,1].m[:].run(shots=shot_num))


def grover_2qbit(shot_num, mark_bit):
    print("\n2量子ビットの grover アルゴリズム")
    amp_inverse = Circuit(2).h[:].x[:].cz[0,1].x[:].h[:].m[:]
    if str(mark_bit == "00"):
        print((Circuit(2).h[:].s[:].cz[0,1].s[:] + amp_inverse).run(shots=shot_num))
    if str(mark_bit == "01"):
        print((Circuit(2).h[:].s[1].cz[0,1].s[1] + amp_inverse).run(shots=shot_num))
    if str(mark_bit == "10"):
        print((Circuit(2).h[:].s[0].cz[0,1].s[0] + amp_inverse).run(shots=shot_num))
    if str(mark_bit == "11"):
        print((Circuit(2).h[:].cz[0,1] + amp_inverse).run(shots=shot_num))

def simple_grover_3qbit(shot_num):
    print("\n3量子ビットの grover アルゴリズム")
    mark_111 = Circuit(3).h[2].ccx[0,1,2].h[2]
    amp_inverse = Circuit(3).h[:].x[:].h[2].ccx[0,1,2].h[2].x[:].h[:]
    u = mark_111 + amp_inverse
    print((Circuit(3).h[:] + u + u).m[:].run(shots=shot_num))
