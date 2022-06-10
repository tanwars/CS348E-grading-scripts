
def ref_get_state_slice_t_idx(t):
    # t in range(0, P)
    # return the *indices* in x that represents (q,dq) at frame t, shape(8,)
    # TODO: student code starts here
    return np.arange(t*slice_length, t*slice_length + state_slice_length)

def ref_get_control_slice_t_idx(t):
    # t in range(0, P)
    # return the *indices* in x that represents a at frame t, shape(4,)
    # TODO: student code starts here
    return np.arange((t+1)*slice_length - control_slice_length, (t+1)*slice_length)

def ref1_dyn_constr_jac_structure_t(t):
    # m=len(s_t) constraints (m=8)
    # N=len(x) variables
    # return a binary m-by-N matrix with 1 elements meaning jacobian
    # of constraint dyn_constr_f_t(x, t) can have non-zero element there
    # and 0 elements meaning jacobian is always zero there
    # TODO: student code starts here
    m = len(ref_get_state_slice_t_idx(t + 1))
    jac_structure = np.zeros((m, N))     # m-by-N
    jac_structure[:, ref_get_state_slice_t_idx(t)] = 1.0    # broadcast
    jac_structure[:, ref_get_state_slice_t_idx(t + 1)] = np.identity(m)   # block assign
    jac_structure[:, ref_get_control_slice_t_idx(t)] = 1.0      # broadcast
    # end student code
    return jac_structure

def ref2_dyn_constr_jac_structure_t(t):
    # m=len(s_t) constraints (m=8)
    # N=len(x) variables
    # return a binary m-by-N matrix with 1 elements meaning jacobian
    # of constraint dyn_constr_f_t(x, t) can have non-zero element there
    # and 0 elements meaning jacobian is always zero there
    # TODO: student code starts here
    m = len(ref_get_state_slice_t_idx(t + 1))
    jac_structure = np.zeros((m, N))     # m-by-N
    jac_structure[:, ref_get_state_slice_t_idx(t)] = 1.0    # broadcast
    jac_structure[:, ref_get_state_slice_t_idx(t + 1)] = 1.0   # block assign
    jac_structure[:, ref_get_control_slice_t_idx(t)] = 1.0      # broadcast
    # end student code
    return jac_structure

def ref_grf_constr_jac_structure_t(t):
    # m=1 constraint
    # N=len(x) variables
    # return a binary 1-by-N matrix with 1 elements meaning jacobian
    # of constraint grf_constr_f_t(x, t) can have non-zero element there
    # and 0 elements meaning jacobian is always zero there
    # TODO: student code starts here
    m = 1
    jac_structure = np.zeros((m, N))     # 1-by-n
    jac_structure[:, ref_get_state_slice_t_idx(t)] = 1.0    # broadcast
    jac_structure[:, ref_get_state_slice_t_idx(t + 1)] = 1.0    # broadcast
    return jac_structure

def ref_t4_dyn_constr_jac_structure_t(t):
    # m=len(s_t) constraints (m=8)
    # N=len(x) variables
    # return a binary m-by-N matrix with 1 elements meaning jacobian
    # of constraint dyn_constr_f_t(x, t) can have non-zero element there
    # and 0 elements meaning jacobian is always zero there
    # TODO: student code starts here
    m = len(ref_get_state_slice_t_idx(t + 1))
    jac_structure = np.zeros((m, N))     # m-by-N
    jac_structure[:, ref_get_state_slice_t_idx(t)] = 1.0    # broadcast
    jac_structure[:, ref_get_state_slice_t_idx(t + 1)] = 1.0   # broadcast
    jac_structure[:, ref_get_control_slice_t_idx(t)] = 1.0      # broadcast
    jac_structure[:, ref_get_control_slice_t_idx(t + 1)] = 1.0  # broadcast
    # end student code
    return jac_structure


print("*"*80)
print('Testing state slice')
print("*"*80)
sum = 0
for t in range(P):
    sum += np.linalg.norm(ref_get_state_slice_t_idx(t) - get_state_slice_t_idx(t))
print(sum)
if sum==0:
    print('PASS!!!')
else:
    print('FAIL!!!')

print("*"*80)
print('Testing control slice')
print("*"*80)
sum = 0
for t in range(P):
    sum += np.linalg.norm(ref_get_control_slice_t_idx(t) - get_control_slice_t_idx(t))
print(sum)
if sum==0:
    print('PASS!!!')
else:
    print('FAIL!!!')

print("*"*80)
print('Testing jacobian ref1')
print("*"*80)
sum = 0
for t in range(P-1):
    sum += np.linalg.norm(ref1_dyn_constr_jac_structure_t(t) - dyn_constr_jac_structure_t(t))
print(sum)
if sum==0:
    print('PASS!!!')
else:
    print('FAIL!!!')

print("*"*80)
print('Testing jacobian ref2')
print("*"*80)
sum = 0
for t in range(P-1):
    sum += np.linalg.norm(ref2_dyn_constr_jac_structure_t(t) - dyn_constr_jac_structure_t(t))
print(sum)
if sum==0:
    print('PASS!!!')
else:
    print('FAIL!!!')

print("*"*80)
print('Testing grf jacobian')
print("*"*80)
sum = 0
for t in range(P-1):
    sum += np.linalg.norm(ref_grf_constr_jac_structure_t(t) - grf_constr_jac_structure_t(t))
print(sum)
if sum==0:
    print('PASS!!!')
else:
    print('FAIL!!!')

print("*"*80)
print('Testing dyn jacobian task 4')
print("*"*80)
sum = 0
for t in range(P-1):
    sum += np.linalg.norm(ref_t4_dyn_constr_jac_structure_t(t) - dyn_constr_jac_structure_t(t))
print(sum)
if sum==0:
    print('PASS!!!')
else:
    print('FAIL!!!')