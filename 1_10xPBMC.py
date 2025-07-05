import anndata
import pandas as pd
import scanpy as sc

data = anndata.read_h5ad("D:/GRADE3/RESEARCH_singlecell/data整合/data/1_10xPBMC/paired_full_features.h5ad")

#scRNA-seq表达情况矩阵
scRNA_matrix = data.X
print(scRNA_matrix)

#scRNA-seq dim的行列名
scRNA_row = data.obs_names.tolist()
print(scRNA_row)
scRNA_col = data.var_names.tolist()
print(scRNA_col)

atac_features = data.var_names[data.var['modality'] == 'Peaks']
#scATAC-seq peaks表达情况矩阵
atac_matrix = data[:, atac_features].X
print(atac_matrix)
#scATAC-seq dim的行列名
scATAC_row = data[:, atac_features].obs_names.tolist()
print(scATAC_row)
scATAC_col = data[:, atac_features].var_names.tolist()
print(scATAC_col)
