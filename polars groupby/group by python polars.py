import polars as pl

# Membuat DataFrame dengan data penjualan
df = pl.DataFrame({
    "kategori_produk": ["Elektronik", "Pakaian", "Elektronik", "Pakaian", "Elektronik"],
    "jumlah_transaksi": [5, 10, 4, 7, 6],
    "total_penjualan": [100, 200, 150, 300, 250]
})

# Menampilkan DataFrame
print("DataFrame:")
print(df)

# Melakukan operasi groupby untuk menghitung total penjualan dan jumlah transaksi per kategori
grouped_df = df.group_by("kategori_produk").agg(
    pl.col("total_penjualan").sum().alias("total_penjualan_per_kategori"),
    pl.col("jumlah_transaksi").sum().alias("total_transaksi_per_kategori"),
    pl.col("total_penjualan").mean().alias("rata_rata_penjualan_per_transaksi")
)

# Menampilkan hasil
print("\nHasil GroupBy:")
print(grouped_df)
