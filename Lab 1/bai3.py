so_tien_gui = 10000
lai_suat = 0.06
#So tien sau 5 nam
amount_after_5_years = so_tien_gui * ((1 + lai_suat)**5)
print(f"So tien se co sau 5 nam la : {amount_after_5_years:.2f} dollars ")
#So tien sau 10 nam
amount_after_10_years = so_tien_gui * ((1 + lai_suat)**10)
print(f"So tien se co sau 10 nam la : {amount_after_10_years:.2f} dollars ")
#Ti le tang truong sau 5 nam
growth_rate = (amount_after_10_years - amount_after_5_years) / (amount_after_5_years)
print(f"Ti le tang truong sau 5 nam la : {growth_rate} % ")