#01 : A
#02 : B
#03 : B
#05 : B
#06 : A
#07 : A
#08 : B
#09 : A
#10 : D

# class TaiKhoan:
#     def __init__(self, stk, ten, so_du):
#         self.stk = stk            
#         self.ten = ten            
#         self.so_du = so_du        

#     def rut_tien(self, so_tien):
#         if so_tien > self.so_du:
#             print("Số dư không đủ để rút tiền.")
#         else:
#             self.so_du -= so_tien
#             print(f"Đã rút {so_tien} đồng.")

#     def nap_tien(self, so_tien):
#         self.so_du += so_tien
#         print(f"Đã nạp {so_tien} đồng. ")

#     def lay_so_du(self):
#         return self.so_du

# class TaiKhoanTietKiem(TaiKhoan):
#     def __init__(self, stk, ten, so_du, lai_suat):
#         super().__init__(stk, ten, so_du)  
#         self.lai_suat = lai_suat  
                  
#     def hien_thi_thong_tin(self):
#         return f"Số tài khoản: {self.stk}, Tên chủ tài khoản: {self.ten}, Số dư: {self.so_du}, Lãi suất: {self.lai_suat}%"


# tai_khoan = TaiKhoan("123456789", "Le KHoi", 10000000)
# tai_khoan.nap_tien(500000)
# tai_khoan.rut_tien(200000)
# print("Số dư tài khoản chính:", tai_khoan_chinh.lay_so_du())

# tai_khoan_tiet_kiem = TaiKhoanTietKiem("987654321", "Tran Thi B", 2000000, 5.0)
# tai_khoan_tiet_kiem.nap_tien(1000000)
# print(tai_khoan_tiet_kiem.hien_thi_thong_tin())
