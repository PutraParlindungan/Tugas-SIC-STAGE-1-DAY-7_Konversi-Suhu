def konversi_suhu(nilai, dari, ke):
    
    dari = dari.upper()
    ke = ke.upper()
    satuan = ['C', 'F', 'K', 'R']

    if dari not in satuan or ke not in satuan:
        print('Error: satuan tidak valid. Pilih antara C/F/K/R')
    
    if dari == 'K' and nilai < 0:
        print('Error: Kelvin tidak bisa negatif')
    
    # jila satuan dari dan ke nya sama
    if dari == ke:
        if dari == 'C':
            return f"{nilai}°{dari} = {nilai}°{ke}"
        if dari == 'F':
            return f"{nilai}°{dari} = {nilai}°{ke}"
        if dari == 'K':
            return f"{nilai}°{dari} = {nilai}°{ke}"
        if dari == 'R':
            return f"{nilai}°{dari} = {nilai}°{ke}"
        
    # jika satuan dari dan ke nya beda
    if dari == 'C':
        if ke == 'F':
            hasil = (nilai * 9/5) + 32
        elif ke == 'K':
            hasil = nilai + 273.15
        elif ke == 'R':
            hasil = nilai * 4/5
    
    if dari == 'F':
        if ke == 'C':
            hasil = (nilai - 32) * 5/9
        elif ke == 'K':
            hasil = ((nilai - 32) * 5/9) + 273.15
        elif ke == 'R':
            hasil = (nilai - 32) * 4/9
    
    if dari == 'K':
        if ke == 'C':
            hasil = nilai + 273.15
        elif ke == 'F':
            hasil = ((nilai - 273.15) * 9/5) + 32
        elif ke == 'R':
            hasil = (nilai - 273.15) * 4/5

    if dari == 'R':
        if ke == 'C':
            hasil = nilai * 5/4
        elif ke == 'F':
            hasil = (nilai * 9/4) + 32
        elif ke == 'K':
            hasil = (nilai * 5/4) + 273.15
        
    
    return f"{nilai}°{dari} = {hasil}°{ke}"