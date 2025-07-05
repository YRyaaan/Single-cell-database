import anndata
import pandas as pd
import scanpy as sc

data = anndata.read_h5ad("D:/GRADE3/RESEARCH_singlecell/data整合/data/9_human_bonemarrow/human_bonemarrow.h5ad")

#scRNA-seq表达情况矩阵
scRNA_matrix = data.X
print(scRNA_matrix)

#scRNA-seq dim的行列名
scRNA_row = data.obs_names.tolist()
print(scRNA_row)
scRNA_col = data.var_names.tolist()
print(scRNA_col)

#scATAC-seq peaks表达情况矩阵
atac_mask = data.var['modality'] == 'ATAC'
scATAC_matrix = data[:, atac_mask].X
print(scATAC_matrix)

#scATAC-seq dim的行列名
scATAC_row = data[:, atac_mask].obs_names.tolist()
print(scATAC_row)
scATAC_col = data[:, atac_mask].var_names.tolist()
print(scATAC_col)

