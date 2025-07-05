import mudata as md

data = md.read_h5mu("D:/GRADE3/RESEARCH_singlecell\data整合/data/11_mouse_gastrulation/mouse_gastrulation.h5mu")

#scRNA-seq表达情况矩阵
scRNA_matrix = data["rna"].X
print(scRNA_matrix)

#scRNA-seq dim的行列名
scRNA_row = data["rna"].obs_names.tolist()
print(scRNA_row)
scRNA_col = data["rna"].var_names.tolist()
print(scRNA_col)

#scATAC-seq表达情况矩阵
scATAC_matrix = data["atac"].X
print(scATAC_matrix)

#scATAC-seq dim的行列名
scATAC_row = data["atac"].obs_names.tolist()
print(scATAC_row)
scATAC_col = data["atac"].var_names.tolist()
print(scATAC_col)
