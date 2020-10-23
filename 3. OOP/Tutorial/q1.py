class O: pass

class A(O): pass
class B(O): pass
class C(O): pass

class D(A,B): pass
class E(C,A): pass

class F(D,E,B): pass

print(F.mro())


# # A and C have foo()
# L_O = [O, obj]

# L_A = [A] + merge(L(O), [O])
# L_A = [A, O, obj]

# L_B = [B] + merge(L(O), [O])
# L_B = [B, O, obj]

# L_C = [C] + merge(L(O), [O])
# L_C = [C, O, obj]

# L_D = [D] + merge(L(A), L(B), [A, B])
# L_D = [D] + merge([A, O, obj], [B, O, obj], [A, B])
# L_D = [D] + [A] + merge([O, obj], [B, O, obj], [B])
# L_D = [D, A] + [B] + merge([O, obj], [O, obj], [])
# L_D = [D, A, B, O, obj]

# L_E = [E] + merge(L(C), L(A), [C, A])
# L_E = [E] + merge([C, O, obj], [A, O, obj], [C, A])
# L_E = [E] + [C] + merge([O, obj], [A, O, obj], [A])
# L_E = [E, C] + [A] + merge([O, obj], [O, obj], [])
# L_E = [E, C, A, O, obj]

# L_F = [F] + merge(L(D), L(B), L(E), [D, B, E])
# L_F = [F] + merge([D, A, B, O, obj], [B, O, obj], [E, C, A, O, obj], [D, B, E])
# L_F = [F] + [D] + merge([A, B, O, obj], [B, O, obj], [E, C, A, O, obj], [B, E])
# # error:

# L_F_DEB = [F] + merge(L(D), L(E), L(B), [D, E, B])
# L_F_DEB = [F] + merge([D, A, B, O, obj], [E, C, A, O, obj], [B, O, obj], [D, E, B])
# L_F_DEB = [F] + [D] + merge([A, B, O, obj], [E, C, A, O, obj], [B, O, obj], [E, B])
# L_F_DEB = [F] + [D] + [E] + merge([A, B, O, obj], [C, A, O, obj], [B, O, obj], [B])
# L_F_DEB = [F] + [D] + [E] + [C] + merge([A, B, O, obj], [A, O, obj], [B, O, obj], [B])
# L_F_DEB = [F] + [D] + [E] + [C] + [A] + merge([B, O, obj], [O, obj], [B, O, obj], [B])
# L_F_DEB = [F] + [D] + [E] + [C] + [A] + [B] + merge([O, obj], [O, obj], [O, obj], [])
# L_F_DEB = [F, D, E, C, A, B, O, obj]

# # b): C's foo() will be called
