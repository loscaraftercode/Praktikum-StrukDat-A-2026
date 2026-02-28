ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
mahasiswa_unik = ukm_coding | ukm_robotik
print("yang mendaftar pada ukm coding adalah:", ukm_coding - ukm_robotik)
print("mahasiswa yang unik adalah", mahasiswa_unik)
print("Andi" in ukm_robotik)
