import polars as pl

# Membuat DataFrame
df = pl.DataFrame({
    "kategori": ["Elektronik", "Pakaian", "Elektronik", "Pakaian", "Elektronik"],
    "penjualan": [100, 200, 150, 300, 250]
})

# Menambahkan kolom 'kategori_penjualan' berdasarkan kondisi
df = df.with_columns([
    pl.when(pl.col("penjualan") < 150).then(pl.lit("Rendah"))
    .when((pl.col("penjualan") > 150) & (pl.col("penjualan") <= 250)).then(pl.lit("Sedang"))
    .otherwise(pl.lit("Tinggi"))
    .alias("kategori_penjualan")
    ]
)

print(df)
