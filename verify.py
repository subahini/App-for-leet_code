import json,contextlib,io
lessons=json.load(open('dist/lessons.json'))
ns={}
for l in lessons:
 with contextlib.redirect_stdout(io.StringIO()):exec(l['code'],ns)
assert ns['array_sum']([-1,3])==2
assert ns['has_pair']([1,2],3)
assert ns['has_duplicate']([1,1]) and not ns['has_duplicate']([])
assert ns['two_sum']([3,3],6)==[0,1]
assert ns['pair_sorted']([1,3,5],6)==[0,2]
a=[2,1,2];assert ns['remove_value'](a,2)==1 and a[0]==1
assert ns['max_window_sum']([-5,-2,-3],2)==-5
assert ns['min_length']([2,3,1,2,4,3],7)==2
assert ns['prefixes']([2,4,6])==[0,2,6,12]
assert ns['count_sum']([1,-1,0],0)==3
assert ns['search']([],2)==-1 and ns['search']([1,2,2,4],2)==1
assert ns['max_subarray']([-5,-2,-8])==-2
assert ns['merge']([[2,5],[1,3]])==[[1,5]]
assert ns['warmer']([73,74,75,71,69,72,76,73])==[1,1,4,2,1,1,0,0]
a=[[1,2],[3,4]];ns['rotate'](a);assert a==[[3,1],[4,2]]
assert ns['can_jump']([2,3,1,1,4]) and not ns['can_jump']([3,2,1,0,4])
assert ns['split_limit']([7,2,5,10,8],2)==18
print('18 Python examples compile; algorithm checks passed.')
