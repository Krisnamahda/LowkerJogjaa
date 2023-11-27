import re  # Import modul re (Regular Expression) untuk pemrosesan string
from pprint import pprint

# Inisialisasi list kosong untuk menyimpan data pengguna
user_data = []
# Struktur data untuk pekerjaan dalam berbagai kategori
job_data = {
    "1": {
        "category_name": "Kesehatan",
        "jobs": {
            "1": {
                "title": "Dokter Umum",
                "education": "S1, Profesi",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "3.500.000",
                "location": "Kab. Sleman",
                "email": "hrd.klinikswa@gmail.com",
                "no_telp": "+6282135456784 ",
            },
            "2": {
                "title": "Perawat",
                "education": "D3, S1, Profesi",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "2.800.000",
                "location": "Kab. Sleman",
                "email": "hrd.klinikswa@gmail.com",
                "no_telp": "+6282135456784 ",
            },
            "3": {
                "title": "Teknisi Kefarmasian",
                "education": "D3, S1, Profesi",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "2.200.000",
                "location": "Kab. Sleman",
                "email": "hrd.klinikswa@gmail.com",
                "no_telp": "+6282135456784 ",
            },
        },
    },
    "2": {
        "category_name": "Pendidikan",
        "jobs": {
            "1": {
                "title": "Guru Privat kelas 3 SD",
                "education": "SMA/SMK, D3, S1",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Part Time",
                "salary": "1.500.000",
                "location": "Kab. Bantul",
                "email": "-",
                "no_telp": "+6281270241551",
            },
            "2": {
                "title": "Guru Bahasa Jepang",
                "education": "D3, S1",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "4.000.000",
                "location": "Kab. Bantul",
                "email": "hrd@minori.co.id ",
                "no_telp": "+6285703031899 ",
            },
            "3": {
                "title": "Guru Tata Kecantikan",
                "education": "D3, S1",
                "gender": "Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "2.500.000",
                "location": "Kota Yogyakarta",
                "email": "berbudi.hrd@berbudi.sch.id ",
                "no_telp": "+6289530271774  ",
            },
        },
    },
    "3": {
        "category_name": "Restaurant",
        "jobs": {
            "1": {
                "title": "Cook Helper (Hot Kitchen) - Pastry Chef - Crew Store (Minimarket)",
                "education": "SMA/SMK",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "2.700.000",
                "location": "Kota Yogyakarta",
                "email": "ptsaranadayainsani@gmail.com ",
                "no_telp": "+6289515527575",
            },
            "2": {
                "title": "Crew Outlet",
                "education": "SMA/SMK",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 Tahun",
                "employment_status": "Full Time, Part Time",
                "salary": "3.500.000",
                "location": "Kab. Sleman",
                "email": " maowyogya@gmail.com",
                "no_telp": " +6282136332282  ",
            },
            "3": {
                "title": "Head Barista - Barista",
                "education": "SMA/SMK",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "2.200.000",
                "location": "Kota Yogyakarta",
                "email": " jobs@champs.asia  ",
                "no_telp": "+6288980047209 ",
            },
        },
    },
    "4": {
        "category_name": "Teknologi Informasi",
        "jobs": {
            "1": {
                "title": "Web Developer",
                "education": "SMA/SMK, D3, S1",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "6.500.000",
                "location": "Kab. Sleman",
                "email": " karir.fayida@gmail.com  ",
                "no_telp": "-",
            },
            "2": {
                "title": "Staff IT Developer",
                "education": "SMA/SMK, D3, S1",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 30 tahun",
                "employment_status": "Full Time",
                "salary": "5.500.000",
                "location": "Kab. Gunung Kidul",
                "email": " alvina@atacorp.co ",
                "no_telp": "-",
            },
            "3": {
                "title": "Graphic Designer - Web Developer",
                "education": "SMA/SMK, D3, S1",
                "gender": "Pria",
                "age_limit": "Maks. 27 tahun",
                "employment_status": "Full Time",
                "salary": "6.000.000",
                "location": "Kota Yogyakarta",
                "email": " careersabilagroup@gmail.com  ",
                "no_telp": "+6285172142728  ",
            },
        },
    },
    "5": {
        "category_name": "Media & Hiburan",
        "jobs": {
            "1": {
                "title": "TikTok Creator",
                "education": "SMA/SMK",
                "gender": "Wanita",
                "age_limit": "Maks. 25 tahun",
                "employment_status": "Full Time",
                "salary": "2.500.000",
                "location": "Kota Yogyakarta",
                "email": " cvmaranatha12@gmail.com ",
                "no_telp": " +6285643578396",
            },
            "2": {
                "title": "Tiktok Content Creator & Host Live Streaming",
                "education": "SMA/SMK",
                "gender": "Wanita",
                "age_limit": "Maks. 35 tahun",
                "employment_status": "Full Time",
                "salary": "3.100.000",
                "location": "Kota Yogyakarta",
                "email": "-",
                "no_telp": " +628562599117",
            },
            "3": {
                "title": "Social Media Officer",
                "education": "D3, S1",
                "gender": "Pria/Wanita",
                "age_limit": "Maks. 28 tahun",
                "employment_status": "Full Time",
                "salary": "2.800.000",
                "location": "Kab. Gunung Kidul",
                "email": "hrd.sukionigiri@gmail.com",
                "no_telp": "-",
            },
        },
    },
}


# Fungsi untuk tampilan sign up
def signup():
    email = input("Masukkan email: ")
    username = input("Masukkan username: ")

    while True:
        password = input("Masukkan password: ")
        re_password = input("Masukkan ulang password: ")

        if password == re_password:
            break
        else:
            print("Password tidak cocok. Silakan coba lagi.")

    # Menyimpan data pengguna ke dalam list
    user_data.append({"username": username, "email": email, "password": password})
    print("Registrasi berhasil!")
    login()


# Fungsi untuk tampilan login
def login():
    print("Silakan login untuk melanjutkan:")
    username_input = input("Username: ")
    password_input = input("Password: ")

    # Verifikasi login sebagai admin
    if username_input == "admin" and password_input == "12345":
        print("Login sebagai admin berhasil")
        menu_admin()
        return

    # Verifikasi login dengan memeriksa keberadaan username dan password yang cocok
    for user in user_data:
        if user["username"] == username_input and user["password"] == password_input:
            print("Login berhasil!")
            job_board()
            return

    # Jika tidak ada user yang cocok
    print("Username atau password salah. Silakan coba lagi.")
    login()


def add_data(job_data):
    # Input data baru
    category_name = input("Masukkan kategori pekerjaan: ")
    title = input("Masukkan judul pekerjaan: ")
    education = input("Masukkan pendidikan: ")
    gender = input("Masukkan gender: ")
    age_limit = input("Masukkan batas usia: ")
    employment_status = input("Masukkan status kepegawaian: ")
    salary = input("Masukkan gaji: ")
    location = input("Masukkan lokasi: ")
    email = input("Masukkan email: ")
    phone_number = input("Masukkan nomor telepon: ")

    # Buat dictionary baru
    new_job = {
        "title": title,
        "education": education,
        "gender": gender,
        "age_limit": age_limit,
        "employment_status": employment_status,
        "salary": salary,
        "location": location,
        "email": email,
        "phone_number": phone_number,
    }

    # Tambahkan dictionary baru ke dictionary utama
    job_data[str(len(job_data) + 1)] = {
        "category_name": category_name,
        "jobs": {
            str(len(job_data[category_name]["jobs"]) + 1): new_job,
        },
    }

    print("Data berhasil ditambahkan!")
    pprint(job_data, width=1)
    back_to_main_menu()


def edit_data(job_data):
    # Input id pekerjaan
    id_job = input("Masukkan id pekerjaan yang ingin diedit: ")

    # Cek apakah id pekerjaan ada
    if id_job not in job_data:
        print("Id pekerjaan tidak ada!")
        back_to_main_menu()
        return

    # Input data yang ingin diedit
    field = input("Masukkan field yang ingin diubah: ")
    value = input("Masukkan nilai baru: ")

    # Edit data
    job_data[id_job][field] = value

    print("Data berhasil diedit!")
    pprint(job_data, width=1)
    back_to_main_menu()


def delete_data(job_data):
    # Input id pekerjaan
    id_job = input("Masukkan id pekerjaan yang ingin dihapus: ")

    # Cek apakah id pekerjaan ada
    if id_job not in job_data:
        print("Id pekerjaan tidak ada!")
        back_to_main_menu()
        return

    # Hapus data
    del job_data[id_job]

    print("Data berhasil dihapus!")
    pprint(job_data, width=1)
    back_to_main_menu()


def back_to_main_menu():
    input("Tekan Enter untuk kembali ke Main Menu...")


def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Create Data")
        print("2. Edit Data")
        print("3. Delete Data")
        print("4. Exit")

        choice = input("Pilih menu: ")
        if choice == "1":
            add_data(job_data)
        elif choice == "2":
            edit_data(job_data)
        elif choice == "3":
            delete_data(job_data)
        elif choice == "4":
            print("Keluar dari Menu Admin.")
            tampilan_awal()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Fungsi untuk tampilan job board
def job_board():
    while True:
        print("\n  === Job Board ===")
        print(" | 1. Job Category |")
        print(" | 2. Search Job   |")
        print(" | 3. Filter Job   |")
        print(" | 4. Logout       |")
        print(" ===================")

        choice = input("Pilih menu: ")
        if choice == "1":
            show_job_categories()
        elif choice == "2":
            search_job()
        elif choice == "3":
            filter_job()
        elif choice == "4":
            print("Anda telah logout.")
            tampilan_awal()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue  # Kembali ke awal loop jika pilihan tidak valid


# Fungsi untuk tampilan job category
def show_job_categories():
    print("\n === Job Category ===")
    print("1. Kesehatan")
    print("2. Pendidikan")
    print("3. Restaurant")
    print("4. Teknologi Informasi")
    print("5. Media & Hiburan")
    print("0. Back")

    category_choice = input("Pilih kategori pekerjaan (1-5): ")
    if category_choice == "0":
        return  # Kembali dari fungsi jika pengguna memilih "Back"
    show_jobs_by_category(category_choice)


# Fungsi untuk mencari lowongan pekerjaan
def search_job():
    keyword = input("Masukkan kata kunci pencarian: ")
    found_jobs = []

    # Lakukan pencarian pekerjaan berdasarkan kata kunci
    for category_key, category_data in job_data.items():
        if category_key.isdigit():
            for job_number, job_details in category_data["jobs"].items():
                if (
                    keyword.lower() in job_details["title"].lower()
                    or keyword.lower() in job_details["education"].lower()
                    or keyword.lower() in job_details["location"].lower()
                ):
                    found_jobs.append(
                        {
                            "category_name": category_data["category_name"],
                            "title": job_details["title"],
                            "education": job_details["education"],
                            "location": job_details["location"],
                            "category": category_key,
                            "job_number": job_number,
                        }
                    )

    if found_jobs:
        print("\n=== Hasil Pencarian ===")
        for index, job in enumerate(found_jobs, start=1):
            print(
                f"{index}. {job['title']} - {job['category_name']} - {job['location']} - {job['education']}"
            )
        print("0. Back")

        # Meminta pengguna untuk memilih nomor pekerjaan yang ingin dilihat persyaratannya
        selected_job_number = input("Pilih nomor pekerjaan: ")

        # Memastikan bahwa input pengguna valid
        try:
            selected_job_number = int(selected_job_number)
        except ValueError:
            print("Input tidak valid. Silakan masukkan nomor yang valid.")
            job_board()

        if selected_job_number == 0:
            job_board()
        # Menampilkan persyaratan pekerjaan yang dipilih
        elif 1 <= selected_job_number <= len(found_jobs):
            selected_job = found_jobs[selected_job_number - 1]
            show_job_requirements(selected_job["category"], selected_job["job_number"])
        else:
            print("Nomor pekerjaan tidak valid.")
            job_board()
    else:
        print("Tidak ada pekerjaan yang sesuai dengan kata kunci.")
        job_board()


def filter_job():
    # Pilihan pendidikan
    education_options = {
        "1": ["SLTA", "SMA", "SMK"],
        "2": ["D1", "D2", "D3"],
        "3": ["D4", "S1"],
        "4": ["S2"],
        "5": ["S3"],
    }

    # Pilihan lokasi
    location_options = {
        "1": "Kab. Bantul",
        "2": "Kab. Gunung Kidul",
        "3": "Kab. Kulon Progo",
        "4": "Kab. Sleman",
        "5": "Kota Yogyakarta",
    }

    print("\n=== Kriteria Pencarian ===")

    # Meminta pengguna untuk memasukkan kriteria pendidikan
    print("\n=== Pendidikan ===")
    for key, value in education_options.items():
        print(f"{key}. {', '.join(value)}")
    print("0. Back")
    education_option = input("Pilih tingkat pendidikan (1-5): ")
    if education_option == "0":
        job_board()
    if education_option not in education_options:
        print("Pilihan tingkat pendidikan tidak valid.")
        job_board()

    # Meminta pengguna untuk memasukkan kriteria gaji
    print("\n=== Gaji ===")
    min_salary = int(input("Masukkan gaji minimal (Contoh:2000000): "))
    max_salary = int(input("Masukkan gaji maksimal (Contoh:3000000): "))

    # Meminta pengguna untuk memasukkan kriteria lokasi
    print("\n=== Lokasi ===")
    for key, value in location_options.items():
        print(f"{key}. {value}")
    location_option = input("Pilih lokasi (1-5): ")
    if location_option not in location_options:
        print("Pilihan lokasi tidak valid.")
        job_board()

    # Melakukan penyaringan pekerjaan berdasarkan kriteria
    filtered_jobs = []
    for category_key, category_data in job_data.items():
        if category_key.isdigit():
            for job_number, job_details in category_data["jobs"].items():
                job_salary = int(
                    job_details["salary"].replace(".", "").replace(",", "")
                )

                # Memeriksa apakah tingkat pendidikan sesuai dengan pilihan pengguna
                education_levels = re.split(
                    r", | |/", job_details["education"]
                )  # Split berdasarkan koma dan spasi (", ") atau spasi tunggal (" ") atau garis miring ("/")
                if (
                    any(
                        education_level in education_options[education_option]
                        for education_level in education_levels
                    )
                    and min_salary <= job_salary <= max_salary
                    and job_details["location"] == location_options[location_option]
                ):
                    filtered_jobs.append(
                        {
                            "category_name": category_data["category_name"],
                            "title": job_details["title"],
                            "education": job_details["education"],
                            "location": job_details["location"],
                            "category": category_key,
                            "job_number": job_number,
                        }
                    )

    if filtered_jobs:
        print("\n=== Hasil Penyaringan ===")
        for index, job in enumerate(filtered_jobs, start=1):
            print(
                f"{index}. {job['title']} - {job['category_name']} - {job['location']} - {job['education']}"
            )

        # Meminta pengguna untuk memilih nomor pekerjaan yang ingin dilihat persyaratannya
        selected_job_number = input("Pilih nomor pekerjaan: ")

        # Memastikan bahwa input pengguna valid
        try:
            selected_job_number = int(selected_job_number)
        except ValueError:
            print("Input tidak valid. Silakan masukkan nomor yang valid.")
            job_board()

        # Menampilkan persyaratan pekerjaan yang dipilih
        if 1 <= selected_job_number <= len(filtered_jobs):
            selected_job = filtered_jobs[selected_job_number - 1]
            show_job_requirements(selected_job["category"], selected_job["job_number"])
        else:
            print("Nomor pekerjaan tidak valid.")
            job_board()
    else:
        print("Tidak ada pekerjaan yang sesuai dengan kriteria.")
        job_board()


# Fungsi untuk menampilkan persyaratan pekerjaan tertentu
def show_job_requirements(category, job_number):
    category_data = job_data.get(category)
    gender = input("Masukkan jenis kelamin (Pria/Wanita): ")
    age = int(input("Masukkan umur Anda: "))
    education = input("Masukkan tingkat pendidikan Anda: ")

    if category_data:
        job_details = category_data["jobs"].get(job_number)
        if job_details:
            print(f"\nPersyaratan untuk {job_details['title']}:")
            print(f"- Tingkat Pendidikan: {job_details['education']}")
            print(f"- Gender: {job_details['gender']}")
            print(f"- Umur: {job_details['age_limit']}")
            print(f"- Status Kerja: {job_details['employment_status']}")
            print(f"- Besaran Gaji: {job_details['salary']}")
            print(f"- Lokasi Kerja: {job_details['location']}")
            print(f"- Email: {job_details['email']}")
            print(f"- No. Telp: {job_details['no_telp']}")

            # Memeriksa apakah kandidat memenuhi syarat
            if (
                gender.lower() in job_details["gender"].lower()
                and age <= int(job_details["age_limit"].split()[1])
                and any(
                    edu.lower() in education.lower()
                    for edu in re.split(r", | |/", job_details["education"])
                )
            ):
                print("Anda memenuhi syarat pekerjaan!")
            else:
                print("Maaf, Anda tidak memenuhi syarat pekerjaan.")
        else:
            print("Nomor pekerjaan tidak valid.")
    else:
        print("Kategori tidak valid.")


# Fungsi untuk menampilkan pekerjaan dalam kategori tertentu
def show_jobs_by_category(category):
    category_data = job_data.get(category)

    if category_data:
        print(f"\n({category_data['category_name']})")
        for job_number, job_details in category_data["jobs"].items():
            print(f"{job_number}. {job_details['title']}")
        print("0. Back")
        job_number_choice = input("Pilih nomor pekerjaan: ")
        if job_number_choice == "0":
            show_job_categories()
        elif job_number_choice in category_data["jobs"]:
            show_job_requirements(category, job_number_choice)
    else:
        print("Kategori tidak valid.")


def tampilan_awal():
    print("============================================")
    print("|Selamat Datang di Info Lowongan Kerja Jogja|")
    print("============================================")
    print("|             1. Sign Up                    |")
    print("|             2. Login                      |")
    print("|             3. Exit                       |")
    print("=============================================")

    while True:
        choice = input("Pilih menu: ")
        if choice == "1":
            signup()
            break  # Keluar dari loop setelah signup
        elif choice == "2":
            login()
            break  # Keluar dari loop setelah login
        elif choice == "3":
            print("Terima kasih telah menggunakan aplikasi ini.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


tampilan_awal()
