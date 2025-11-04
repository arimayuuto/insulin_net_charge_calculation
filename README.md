# insulin_net_charge_calculation

Source : AWS RE/START Python Practice - Working with the String Sequence and Numeric Weight of Insulin in Python

-----

## 📄 Tujuan: Analisis Muatan Bersih (Net Charge) Insulin Manusia

### 🧬 Deskripsi Proyek

Proyek ini melakukan **analisis sekuens protein** untuk menghitung **muatan bersih (net charge)** dari berbagai bagian **insulin manusia** pada pH tertentu. Muatan bersih adalah properti biokimia penting yang memengaruhi struktur, fungsi, dan interaksi protein.

Proyek ini menggunakan sekuens preproinsulin manusia dan nilai pKR untuk asam amino bermuatan.

### 🛠️ Struktur File

Proyek ini terdiri dari dua komponen utama:

1.  **`7_net-charge.py`**: Skrip Python yang berisi logika pembersihan sekuens, pemisahan rantai insulin, pendefinisian nilai pKR, dan perhitungan muatan bersih.
2.  **`insulin.xlsx - Sheet1.csv`** (Atau file data sekuens yang digunakan): Berisi sekuens protein mentah dan/atau data pendukung (seperti nilai pKR dan hasil perhitungan) yang digunakan dalam skrip.

### ⚙️ Cara Menggunakan Skrip (`7_net-charge.py`)

#### 1\. Persyaratan

Pastikan Anda telah menginstal Python dan pustaka/library yang diperlukan.

  * **Python 3.13.7**
  * **`re`** (Regular Expression, sudah termasuk dalam instalasi standar Python)

#### 2\. Menjalankan Skrip

Skrip ini diasumsikan membaca sekuens dari file teks yang bernama **`preproinsulin-seq.txt`** dan memiliki nilai pKR yang ditentukan di dalamnya (seperti yang terlihat pada *snippet*).

Untuk menjalankan analisis, cukup eksekusi file Python dari *terminal* atau *command prompt*:

```bash
python 7_net-charge.py
```

#### 3\. Output Skrip

Skrip akan mencetak:

  * Sekuens **preproinsulin** yang telah dibersihkan.
  * Jumlah total karakter dalam sekuens tersebut.
  * Sekuens untuk masing-masing bagian **lsInsulin**, **bInsulin**, **cInsulin**, **aInsulin**, dan **insulin** (bInsulin + aInsulin).
  * **Muatan bersih** (net charge) untuk setiap bagian insulin pada pH yang berbeda.

### 📊 Detail Sekuens & Perhitungan

Berikut adalah detail utama yang digunakan dalam analisis (berdasarkan file data dan skrip):

#### 1\. Sekuens Insulin

Skrip memecah sekuens preproinsulin (110 karakter) menjadi bagian-bagian berikut:

| Variabel | Sekuens (Contoh) | Rentang Karakter | Panjang | Catatan |
| :--- | :--- | :--- | :--- | :--- |
| **`lsInsulin`** | `malwmrllpllallalwgpdpaaa` | 1 - 24 | 24 | Peptide Sinyal |
| **`bInsulin`** | `fvnqhlcgshlvealylvcgergffytpkt` | 25 - 54 | 30 | Rantai B |
| **`cInsulin`** | `rreaedlqvgqvelgggpgagslqplalegslqkr` | 55 - 89 | 35 | Peptide Penghubung (C-Peptide) |
| **`aInsulin`** | `giveqcctsicslyqlenycn` | 90 - 110 | 21 | Rantai A |
| **`insulin`** | *bInsulin + aInsulin* | N/A | 51 | Insulin Matang |

#### 2\. Nilai pKR

Nilai pKR (konstanta disosiasi) yang digunakan untuk asam amino bermuatan:

| Asam Amino | Kode (Satu Huruf) | pKR |
| :--- | :--- | :--- |
| Tirosin | **Y** | 10.07 |
| Sistein | **C** | 8.18 |
| Lisin | **K** | 10.53 |
| Histidin | **H** | 6.00 |
| Arginin | **R** | 12.48 |
| Asam Aspartat | **D** | 3.65 |
| Asam Glutamat | **E** | 4.25 |

#### 3\. Metodologi Perhitungan

Muatan bersih (Net Charge) dihitung menggunakan **persamaan Henderson-Hasselbalch** untuk setiap gugus yang dapat terionisasi.

  * **Untuk gugus bermuatan positif (Lysine, Arginine, Histidine):**
    $$Charge = \sum \frac{10^{pKR}}{10^{pKR} + 10^{pH}}$$
  * **Untuk gugus bermuatan negatif (Aspartate, Glutamate):**
    $$Charge = \sum \frac{-10^{pH}}{10^{pKR} + 10^{pH}}$$

> **Catatan:** Skrip harus mengimplementasikan fungsi yang menghitung muatan bersih untuk setiap segmen pada rentang nilai pH yang berbeda (misalnya, dari pH 0 hingga 14) menggunakan rumus di atas dan jumlah residu bermuatan dalam setiap sekuens.

-----
