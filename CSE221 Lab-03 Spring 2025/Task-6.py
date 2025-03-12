import sys

def build_postorder(seq_inorder, seq_preorder, index_inorder_map, in_bam, in_dan, index):
    if in_bam > in_dan:
        return []
    
    first = seq_preorder[index[0]]
    index[0] += 1
    root_idx = index_inorder_map[first]
    bam_postorder = build_postorder(seq_inorder,seq_preorder,index_inorder_map, in_bam, root_idx - 1, index)
    dan_postorder = build_postorder(seq_inorder,seq_preorder,index_inorder_map, root_idx + 1, in_dan, index)
    
    return bam_postorder + dan_postorder + [first]

input_data = sys.stdin.read().splitlines()
n = int(input_data[0])
inorder_str = input_data[1].split()
preorder_str = input_data[2].split()
seq_inorder = []
seq_preorder = []
for i in range(n):
    seq_inorder.append(int(inorder_str[i]))
for i in range(n):
    seq_preorder.append(int(preorder_str[i]))
index_inorder_map = {}
for i in range(n):
    index_inorder_map[seq_inorder[i]] = i
index = [0]
postorder = build_postorder(seq_inorder, seq_preorder, index_inorder_map, 0, n - 1, index)
output_str = ""
for i in range(n):
    output_str += str(postorder[i]) + " "
sys.stdout.write(output_str.strip() + "\n")
