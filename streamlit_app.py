import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2C3E50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Definisikan fungsi uji Molisch
def uji_molisch(nama_sampel):
    st.write("### Uji Molisch")
    hasil_molisch = "Terbentuk :violet[Cincin Ungu] :green[(Uji Positif +)]" if nama_sampel.lower() in ["01", "02"] else "Tidak terbentuk :violet[Cincin Ungu] :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji Molisch untuk {nama_sampel} adalah: {hasil_molisch}")

    # Tambahkan uji positif
    if nama_sampel.lower() in ["01", "02"]:
        st.write("Dengan penambahan larutan a-naftol 5 tetes dan H2SO4 pekat 1 drop pada sampel akan menghasilkan :violet[Cincin Ungu] pada tabung reaksi. Uji ini merupakan uji umum untuk semua Senyawa Karbohidrat dan akan menghasilkan :green[Uji Positif +].")

    # Tambahkan uji negatif
    if nama_sampel.lower() not in ["01", "02"]:
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan merupakan Senyawa karbohidrat yang dimana pada uji ini umum untuk semua Senyawa Karbohidrat dan akan menghasilkan :green[Uji Positif +].")
    
    # Definisikan fungsi uji Seliwanoff
def uji_seliwanoff(nama_sampel):
    st.write("### Uji Seliwanoff")
    hasil_seliwanoff = ":red[Larutan Berwarna Merah], Sampel merupakan :blue-background[Fruktosa] :green[(Uji Positif +)]" if nama_sampel.lower() == "01" else "Larutan Tidak berwarna :red[(Uji Negatif -)]" 
    st.write(f"Hasil Uji Seliwanoff untuk {nama_sampel} adalah: {hasil_seliwanoff}")
    
    # Tambahkan uji positif
    if nama_sampel.lower() == "01":
        st.write("Dengan penambahan pereaksi seliwanoff pada sampel sebanyak 1 drop dan dipanaskan dalam penangas air, akan menghasilkan :red[Larutan berwarna merah]. Uji ini spesifik untuk mengidentifikasi sampel yang termasuk Karbohidrat jenis Monosakarida.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "01":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan termasuk Senyawa Karbohidrat Jenis Monosakarida")

# Definisikan fungsi uji Iodium
def uji_iodium(nama_sampel):
    st.write("### Uji Iodium")
    hasil_iodium = ":violet[Larutan berwarna Ungu Pekat] , Sampel merupakan :blue-background[Pati]. :green[(Uji Positif +)]" if nama_sampel.lower() == "02" else ":violet[Larutan tidak berwarna Ungu Pekat]. :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji Iodium untuk {nama_sampel} adalah: {hasil_iodium}")

    # Tambahkan uji positif
    if nama_sampel.lower() == "02":
        st.write("Dengan penambahan larutan I2 sebanyak 3 tetes pada sampel, akan menghasilkan :violet[Larutan berwarna ungu pekat]. Uji ini spesifik untuk mengidentifikasi sampel yang termasuk Senyawa Karbohidrat jenis Polisakarida.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "02":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan termasuk Senyawa Karbohidrat Jenis Polisakarida.")

# Definisikan fungsi uji NaHSO3
def uji_nahso3(nama_sampel):
    st.write("### Uji NaHSO3")
    hasil_nahso3 = "Terbentuk Emulsi Putih atau Menghasilkan Panas :fire:, Sampel merupakan :blue-background[Formaldehida]. :green[(Uji positif +)]" if nama_sampel.lower() == "05" else "Tidak terbentuk Emulsi Putih atau Menghasilkan Panas :fire:. :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji NaHSO3 untuk {nama_sampel} adalah: {hasil_nahso3}")

    # Tambahkan uji positif
    if nama_sampel.lower() == "05":
        st.write("Dengan menambahkan larutan NaHSO3 sebanyak 1 drop pada sampel, akan menghasilkan Emulsi Putih atau menghasikan Panas :fire:. Uji ini umum untuk semua sampel yang termasuk dalam Senyawa Aldehida.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "05":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel bukan merupakan Senyawa Golongan Aldehida")

# Definisikan fungsi uji Cerric nitrat
def uji_cerric_nitrat(nama_sampel):
    st.write("### Uji Cerric nitrat")
    hasil_cerric_nitrat = ":red[Larutan berwarna Merah cherry] :cherries:. Sampel merupakan Senyawa Alkohol :green[(Uji positif +)]" if nama_sampel.lower() in ["04", "06"] else ":red[Larutan Tidak berwarna Merah Cherry] :cherries:. Sampel bukan merupakan Senyawa Alkohol :red[(Uji negatif -)]"
    st.write(f"Hasil Uji Cerric nitrat untuk {nama_sampel} adalah: {hasil_cerric_nitrat}")
    # Tambahkan uji positif
    if nama_sampel.lower() in ["04", "06"]:
        st.write("Dengan penambahan pereaksi Cerric nitrat 5 tetes pada sampel, akan menghasilkan :red[Larutan berwarna Merah Cherry] :cherries:. Uji ini umum untuk semua sampel yang termasuk dalam Senyawa Alkohol")

    # Tambahkan uji negatif
    if nama_sampel.lower() not in ["04", "06"]:
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel bukan termasuk dalam Senyawa Alkohol")

# Definisikan fungsi uji Iod-Huble
def uji_iod_huble(nama_sampel):
    st.write("### Uji Iod-Huble")
    hasil_iod_huble = "Warna :orange[Larutan Iod_Huble(Jingga)] memudar. Sampel merupakan :blue-background[Heksana] :green[(Uji Positif +)]" if nama_sampel.lower() == "03" else "Warna :orange[Larutan Iod-Huble(Jingga)] tidak memudar. :red[(Uji Negatif -)]"
    st.write(f"Hasil Uji Iod-Huble untuk {nama_sampel} adalah: {hasil_iod_huble}")
    # Tambahkan uji positif
    if nama_sampel.lower() == "03":
        st.write("Dengan penambahan :orange[Larutan Iod-Huble] sebanyak 5 tetes ke dalam sampel, akan menghasilkan warna :orange[Larutan Iod-Huble(Jingga)] akan memudar, (biasanya menjadi tidak berwarna atau :orange[kuning seulas]). Uji ini sepsifik untuk mengidentifikasi Senyawa Hidrokarbon Jenuh")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "03":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel ini bukan merupakan Senyawa Hidrokarbon Jenuh")

# Definisikan fungsi uji Lucas
def uji_lucas(nama_sampel):
    st.write("### Uji Lucas")
    hasil_lucas = "Terbentuk Emulsi Putih, Sampel merupakan :blue-background[t butil alkohol] :green[(Uji positif +)]" if nama_sampel.lower() == "04" else "Tidak terbentuk Emulsi Putih :red[(Uji negatif -)]"
    st.write(f"Hasil Uji Lucas untuk {nama_sampel} adalah: {hasil_lucas}")
    # Tambahkan uji positif
    if nama_sampel.lower() == "04":
        st.write("Dengan penambahan pereaksi Lucas sebanyak 1 drop pada sampel, akan menghasilkan Emulsi Putih. Uji ini merupakan uji spesifik untuk mengidentifikasi suatu sampel yang merupakan Senyawa Alkohol Tersier atau Sekunder.")

    # Tambahkan uji negatif
    if nama_sampel.lower() != "04":
        st.write("Sampel menghasilkan :red[Uji Negatif -)] , karena sampel ini bukan merupakan Senyawa Alkohol Tersier atau Sekunder")

# Definisikan fungsi uji Iodoform
def uji_iodoform(nama_sampel):
    st.write("### Uji Iodoform")
    hasil_iodoform = ":orange[Larutan berwarna Kuning dengan endapan] :green[(Uji positif)]" if nama_sampel.lower() == "06" else ":orange[Larutan tidak berwarna kuning dan tidak ada endapan] :red[(Uji negatif -)]"
    st.write(f"Hasil Uji Iodoform untuk {nama_sampel} adalah: {hasil_iodoform}")
    # Tambahkan uji positif
    if nama_sampel.lower() =="06":
        st.write("Dengan penambahan 5 tetes larutan I2 dalam KI dan 1 drop larutan NaOH 10% pada sampel, akan menghasilkan :orange[Larutan berwarna Kuning dan terbentuk Endapan]. Uji ini spesifik untuk mengidentifikasi senyawa Alkohol Primer atau Sekunder yang memiliki Gugus Metil Keton.")

    # Tambahkan uji negatif
    if nama_sampel.lower()!= "06":
        st.write("Sampel menghasilkan :red[Uji Negatif -] , karena sampel bukan merupakan Senyawa Alkohol Primer atau Sekunder yang memiliki Gugus Metil Keton.")
   
   # Create a title for the landing page
st.header(":rainbow[Uji Senyawa Kimia]", divider ='gray')

# Create a sidebar with a selectbox for sample number and chemical test
with st.sidebar:
    st.header("Menu")
    nama_sampel = st.selectbox("Pilih nomor sampel", ["", "01", "02", "03", "04", "05", "06"])
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
    st.write("Silakan pilih nomor sampel dan uji kimia pada sidebar untuk melihat hasilnya.")