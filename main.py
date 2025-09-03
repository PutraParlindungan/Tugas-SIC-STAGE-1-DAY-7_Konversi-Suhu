from utils import konversi_suhu

def main():
    print('=== KONVERSI SUHU ===')

    while True:
        try:
            nilai_input = float(input('Masukan nilai suhu: '))
            break
        except:
            print('Error: Masukan nilai suhu harus berupa angka valid, silakan masukan lagi')

    
    while True:
        dari_input = input('Dari satuan (C/F/K/R): ').upper()
        if dari_input in ['C', 'F', 'K', 'R']:
            break
        else:
            print('Error: Dari satuan tidak valid, pilih antara (C/F/K/R)')

    while True:
        ke_input = input('Ke satuan (C/F/K/R): ').upper()
        if ke_input in ['C', 'F', 'K', 'R']:
            break
        else:
            print('Error: Ke satuan tidak valid, pilih antara (C/F/K/R)')

    hasil_konversi = konversi_suhu(nilai_input, dari_input, ke_input)

    print(f"Hasil: {hasil_konversi}")


main()