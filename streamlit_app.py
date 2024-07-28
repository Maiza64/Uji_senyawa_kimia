import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E67E22;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Definisikan fungsi uji Molisch
def uji_molisch(nama_sampel):
    st.write("### Uji Molisch")
    hasil_molisch = "Terbentuk :violet-bakcground[Cincin Ungu] :green-background[(Uji Positif +)]" if nama_sampel.lower() in ["Fruktosa", "Pati"] else "Tidak terbentuk :violet-background[Cincin Ungu] :red-background[(Uji Negatif -)]"
    st.write(f"Hasil Uji Molisch untuk {nama_sampel} adalah: {hasil_molisch}")

    # Tambahkan uji positif
    if nama_sampel.lower() in ["Fruktosa", "Pati"]:
        st.write("Dengan penambahan larutan a-naftol 5 tetes dan H2SO4 pekat 1 drop pada sampel akan menghasilkan :violet[Cincin Ungu] pada tabung reaksi. Uji ini merupakan uji umum untuk semua Senyawa Karbohidrat dan akan menghasilkan :green[Uji Positif +].")

    # Tambahkan uji negatif
    if nama_sampel.lower() not in ["Fruktosa", "Pati"]:
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan merupakan Senyawa karbohidrat yang dimana pada uji ini umum untuk semua Senyawa Karbohidrat dan akan menghasilkan :green[Uji Positif +]. Lanjutkan pengujian kimia pada sampel Formaldehida, Heksana, t butil alkohol, dan Etanol menggunakan uji NaHSO3 untuk mengetahui senyawanya.")
    
    # Definisikan fungsi uji Seliwanoff
def uji_seliwanoff(nama_sampel):
    st.write("### Uji Seliwanoff")
    hasil_seliwanoff = ":red[Larutan Berwarna Merah], :green[(Uji Positif +)]" if nama_sampel.lower() == "Fruktosa" else "Larutan Tidak berwarna :red[(Uji Negatif -)]" 
    st.write(f"Hasil Uji Seliwanoff untuk {nama_sampel} adalah: {hasil_seliwanoff}")
    
    # Tambahkan uji positif
    if nama_sampel.lower() == "Fruktosa":
        st.write("Dengan penambahan pereaksi seliwanoff pada sampel sebanyak 1 drop dan dipanaskan dalam penangas air, akan menghasilkan :red[Larutan berwarna merah]. Uji ini spesifik untuk mengidentifikasi sampel yang termasuk Karbohidrat jenis Monosakarida.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "Fruktosa":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan termasuk Senyawa Karbohidrat Jenis Monosakarida. Lanjutkan pengujian kimia pada sampel Pati menggunakan uji Iodium untuk mengetahui senyawanya.")

# Definisikan fungsi uji Iodium
def uji_iodium(nama_sampel):
    st.write("### Uji Iodium")
    hasil_iodium = ":violet[Larutan berwarna Ungu Pekat] , :green[(Uji Positif +)]" if nama_sampel.lower() == "pati" else ":violet[Larutan tidak berwarna Ungu Pekat]. :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji Iodium untuk {nama_sampel} adalah: {hasil_iodium}")

    # Tambahkan uji positif
    if nama_sampel.lower() == "Pati":
        st.write("Dengan penambahan larutan I2 sebanyak 3 tetes pada sampel, akan menghasilkan :violet[Larutan berwarna ungu pekat]. Uji ini spesifik untuk mengidentifikasi sampel yang termasuk Senyawa Karbohidrat jenis Polisakarida.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "Pati":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan termasuk Senyawa Karbohidrat Jenis Polisakarida.")

# Definisikan fungsi uji NaHSO3
def uji_nahso3(nama_sampel):
    st.write("### Uji NaHSO3")
    hasil_nahso3 = "Terbentuk Emulsi Putih atau Menghasilkan Panas :fire:, :green[(Uji positif +)]" if nama_sampel.lower() == "Formaldehida" else "Tidak terbentuk Emulsi Putih atau Menghasilkan Panas :fire:. :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji NaHSO3 untuk {nama_sampel} adalah: {hasil_nahso3}")

    # Tambahkan uji positif
    if nama_sampel.lower() == "Formaldehida":
        st.write("Dengan menambahkan larutan NaHSO3 sebanyak 1 drop pada sampel, akan menghasilkan Emulsi Putih atau menghasikan Panas :fire:. Uji ini umum untuk semua sampel yang termasuk dalam Senyawa Aldehida.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "Formaldehida":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel bukan merupakan Senyawa Golongan Aldehida. Lanjutkan pengujian kimia pada sampel Heksana, t butil alkohol, dan Etanol menggunakan uji Cerric nitrat untuk mengetahui senyawanya.")

# Definisikan fungsi uji Cerric nitrat
def uji_cerric_nitrat(nama_sampel):
    st.write("### Uji Cerric nitrat")
    hasil_cerric_nitrat = ":red[Larutan berwarna Merah cherry] :cherries:. Sampel merupakan Senyawa Alkohol :green[(Uji positif +)]" if nama_sampel.lower() in ["t butil alkohol", "Etanol"] else ":red[Larutan Tidak berwarna Merah Cherry] :cherries:. Sampel bukan merupakan Senyawa Alkohol :red[(Uji negatif -)]"
    st.write(f"Hasil Uji Cerric nitrat untuk {nama_sampel} adalah: {hasil_cerric_nitrat}")
    # Tambahkan uji positif
    if nama_sampel.lower() in ["t butil alkohol", "Etanol"]:
        st.write("Dengan penambahan pereaksi Cerric nitrat 5 tetes pada sampel, akan menghasilkan :red[Larutan berwarna Merah Cherry] :cherries:. Uji ini umum untuk semua sampel yang termasuk dalam Senyawa Alkohol")

    # Tambahkan uji negatif
    if nama_sampel.lower() not in ["t butil alkohol", "Etanol"]:
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel bukan termasuk dalam Senyawa Alkohol. Lanjutkan pengujian kimia pada sampel Heksana mengguanakan uji Iod-Huble untuk mengetahui senyawanya.")

# Definisikan fungsi uji Iod-Huble
def uji_iod_huble(nama_sampel):
    st.write("### Uji Iod-Huble")
    hasil_iod_huble = "Warna :orange[Larutan Iod_Huble(Jingga)] memudar, :green[(Uji Positif +)]" if nama_sampel.lower() == "Heksana" else "Warna :orange[Larutan Iod-Huble(Jingga)] tidak memudar. :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji Iod-Huble untuk {nama_sampel} adalah: {hasil_iod_huble}")
    # Tambahkan uji positif
    if nama_sampel.lower() == "Heksana":
        st.write("Dengan penambahan :orange[Larutan Iod-Huble] sebanyak 5 tetes ke dalam sampel, akan menghasilkan warna :orange[Larutan Iod-Huble(Jingga)] akan memudar, (biasanya menjadi tidak berwarna atau :orange[kuning seulas]). Uji ini sepsifik untuk mengidentifikasi Senyawa Hidrokarbon Jenuh")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "Heksana":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan merupakan Senyawa Hidrokarbon Jenuh")

# Definisikan fungsi uji Lucas
def uji_lucas(nama_sampel):
    st.write("### Uji Lucas")
    hasil_lucas = "Terbentuk Emulsi Putih, :green[(Uji positif +)]" if nama_sampel.lower() == "t butil alkohol" else "Tidak terbentuk Emulsi Putih :red[(Uji negatif -)]"
    st.write(f"Hasil Uji Lucas untuk {nama_sampel} adalah: {hasil_lucas}")
    # Tambahkan uji positif
    if nama_sampel.lower() == "t butil alkohol":
        st.write("Dengan penambahan pereaksi Lucas sebanyak 1 drop pada sampel, akan menghasilkan Emulsi Putih. Uji ini merupakan uji spesifik untuk mengidentifikasi suatu sampel yang merupakan Senyawa Alkohol Tersier atau Sekunder.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "t butil alkohol":
        st.write("Sampel menghasilkan :red[Uji Negatif -)] , karena sampel ini bukan merupakan Senyawa Alkohol Tersier atau Sekunder. Lanjutkan pengujian kimia pada sampel Etanol menggunakan uji Iodoform untuk mengetahui senyawanya.")

# Definisikan fungsi uji Iodoform
def uji_iodoform(nama_sampel):
    st.write("### Uji Iodoform")
    hasil_iodoform = ":orange[Larutan berwarna Kuning dengan endapan], :green[(Uji positif)]" if nama_sampel.lower() == "Etanol" else ":orange[Larutan tidak berwarna kuning dan tidak ada endapan] :red[(Uji negatif -)]"
    st.write(f"Hasil Uji Iodoform untuk {nama_sampel} adalah: {hasil_iodoform}")
    # Tambahkan uji positif
    if nama_sampel.lower() =="Etanol":
        st.write("Dengan penambahan 5 tetes larutan I2 dalam KI dan 1 drop larutan NaOH 10% pada sampel, akan menghasilkan :orange[Larutan berwarna Kuning dan terbentuk Endapan]. Uji ini spesifik untuk mengidentifikasi senyawa Alkohol Primer atau Sekunder yang memiliki Gugus Metil Keton.")

    # Tambahkan uji negatif
    if nama_sampel.lower()!= "Etanol":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel bukan merupakan Senyawa Alkohol Primer atau Sekunder yang memiliki Gugus Metil Keton.")
   
   # Create a title for the landing page
st.title(":rainbow[Uji Senyawa Kimia]")
st.header("", divider= "gray")

# Create a sidebar with a selectbox for sample and chemical test
with st.sidebar:
    st.header("Menu")
    nama_sampel = st.selectbox("Pilih sampel", ["", "Fruktosa", "Pati", "Formaldehida", "t butil alkohol", "Heksana", "Etanol"])
    uji_kimia = st.selectbox("Pilih uji kimia", ["", "Uji Molisch", "Uji Seliwanoff", "Uji Iodium", "Uji NaHSO3", "Uji Cerric nitrat", "Uji Lucas", "Uji Iod-Huble", "Uji Iodoform"])

# Check if sample number and chemical test are selected
if nama_sampel!= "" and uji_kimia!= "":
    # Call the corresponding function based on the selected chemical test
    if uji_kimia == "Uji Molisch":
        uji_molisch(nama_sampel)
    elif uji_kimia == "Uji Seliwanoff":
        uji_seliwanoff(nama_sampel)
    elif uji_kimia == "Uji Iodium":
        uji_iodium(nama_sampel)
    elif uji_kimia == "Uji NaHSO3":
        uji_nahso3(nama_sampel)
    elif uji_kimia == "Uji Cerric nitrat":
        uji_cerric_nitrat(nama_sampel)
    elif uji_kimia == "Uji Lucas":
        uji_lucas(nama_sampel)
    elif uji_kimia == "Uji Iod-Huble":
        uji_iod_huble(nama_sampel)
    elif uji_kimia == "Uji Iodoform":
        uji_iodoform(nama_sampel)
else:
    # Display a message if no sample number or chemical test is selected
    st.subheader("Pengujian Senyawa Kimia")
    st.write("adalah serangkaian prosedur yang digunakan untuk mengidentifikasi, dan menganalisis sifat fisik, kimia, dan biologis dari suatu senyawa atau campuran kimia.")
    st.write("Tujuan utama dari pengujian ini adalah untuk memahami karakteristik senyawa tersebut dalam berbagai kondisi ")
    st.write("Silakan pilih sampel dan uji kimia pada sidebar untuk melihat hasilnya.")
